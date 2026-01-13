### 0.1 你现在的 EquiBot 在代码里到底做了什么（精确对齐到文件与张量形状）

**核心结论：你这份 EquiBot 代码已经天然支持“把触觉作为 *world‑invariant 的标量条件*”注入，并且不会破坏等变性。**原因是 `VecConditionalUnet1D` 通过 `scalar_cond` 做 FiLM 式调制（标量调制向量通道），这在群作用下是安全的。

---

#### (A) 等变视觉编码器：`SIM3Vec4Latent`（`vision/sim3_encoder.py`）

- 输入点云：`pcl` 形状 **`[B, T=Ho, N, 3]`**。
- 内部 canonicalization（这是 EquiBot 的 SIM(3) 部分）：
  - `centroid = mean(pcl)`  
  - `scale = mean(||pcl - centroid||) / target_norm`
  - 用 `(pcl - centroid)/scale` 做归一化再送入 VN PointNet。
- 输出字典（关键字段）：
  - `so3`: **旋转等变**向量特征，形状 **`[B*Ho, c_dim, 3]`**
  - `inv`: 标量不变量特征（但你当前 EquiBot 的主干并没有显式用它）
  - `center`: **`[B*Ho, 1, 3]`**（代码里是 `z_center = centroid.permute(0,2,1)`）
  - `scale`: **`[B*Ho]`**

> 注意：你“不想要 canonicalization”指的是你旧 DRIFT-DP 里把动作/状态表达进初始夹爪帧（GFC）。  
> EquiBot 这里的 centroid/scale canonicalization 只用于 SIM(3) 归一化点云特征，不等价于你旧方法的动作坐标系重写。

---

#### (B) 状态/动作的“向量/标量分解”（`agents/equibot_policy.py`）

以 FactoryIL 里常用 **`dof=7`** 为例：

- **状态**（`eef_pose_w`）被分成：
  - 位置向量：`S_t^(x) ∈ R^3`
  - 方向向量：`S_t^(d)` 两个列向量（6D rot）
  - 标量：`S_t^(s)`（gripper）
- 代码 `EquiBotPolicy._convert_state_to_vec`：
  - `z_pos`: **`[B, Ho, num_eef, 3]`**
  - `z_dir`: **`[B, Ho, 2*num_eef, 3]`**
  - `z_scalar`: **`[B, Ho, num_eef]`**

- **动作**（`action`，dof=7）被分成：
  - 两个 3D 向量通道（平移 + 角速度/轴角）：`A_t^(v) ∈ R^{2*num_eef × 3}`
  - 标量通道（gripper）：`A_t^(s) ∈ R^{num_eef}`
- 代码 `EquiBotPolicy._convert_action_to_vec` 输出：
  - `vec_eef_action`: **`[B, 2*num_eef, 3, Hp]`**（注意 permute 后的排列）
  - `vec_gripper_action`: **`[B, num_eef, Hp]`**

---

#### (C) 等变扩散骨干：`VecConditionalUnet1D`（`utils/equivariant_diffusion/conditional_unet1d.py`）

你当前等变 diffusion backbone 的关键接口是：

- `sample`: noisy vector action，形状 **`[B, Hp, C_a, 3]`**（forward 内部会 rearrange）
- `scalar_sample`: noisy scalar action（gripper），形状 **`[B, Hp, num_eef]`**
- `cond`: **向量条件**，形状 **`[B, Ho*obs_dim, 3]`**
- `scalar_cond`: **标量条件**，形状 **`[B, Ho*num_eef]`**（目前只有 gripper state）

**scalar_cond 如何被用？**  
在 `VecConditionalUnet1D.forward()`：

1. 先得到 diffusion step embedding：`scalar_feature = diffusion_step_encoder(timestep)`  
2. 然后 `scalar_feature = cat([scalar_feature, scalar_cond])`
3. 这个 `scalar_feature` 进入每个 residual block 的 FiLM（准确说是 `VecLNA(... s_in=scalar_cond_dim)` + `VecLinear(... s_out=...)`）对向量通道做尺度/偏置调制。

> 这意味着：**只要你把触觉编码成 “world‑invariant 的标量向量”，拼进 `scalar_cond`，不会破坏 SO(3)/SIM(3) 等变性。**

---

#### (D) 训练目标：标准 DDPM 噪声预测（`agents/equibot_agent.py`）

你现在的训练就是：

- 随机采样 `k`  
- 加噪 `A^k = add_noise(A, ε, k)`  
- 预测 `ε̂ = εθ(A^k, k, cond)`  
- 损失 `MSE(ε̂, ε)`（dof=7 用 vec/sca 加权）

---

### 0.2 EquiTac 给你的关键启示（与你想要的“tactile invariant fusion + anti-shortcut”高度相关）

EquiTac 的三个关键点可以直接抽象成你的 ECCV 方法“触觉处理原则”：

1. **RGB tactile 不是几何载体**：直接用 RGB 会受内部光照影响，旋转不一致 → 会造成策略学到“颜色 shortcut”。  
2. **normal map 才是几何一致的 carrier**：  
   $$
   N(u) = (n_x(u), n_y(u), n_z(u)),\quad \|N(u)\|=1
   $$
   其中 $(n_x,n_y)$ 是 SO(2) 的向量载体，$n_z$ 是不变量载体。  
3. **结构上给触觉一个必须负责的“学习路径/目标”**：EquiTac 用 residual correction 强迫触觉被用到；你这里不想做两阶段，就需要 **auxiliary objectives + contact-aware data regime** 达到同等效果。

---

## 1) 你要写 ECCV 的新方法：一个具体可落地的端到端提案  
### 方法名建议：**EquiBot‑TIC**（Tactile Invariant Conditioning for Equivariant Diffusion Policy）

下面给你一个**严格满足你新约束**的 proposal：

- **不做 gripper-frame canonicalization**（不把动作/状态重写到初始夹爪帧）
- **触觉只作为 world‑invariant 标量条件注入 EquiBot**（scalar_cond）
- **端到端训练**（触觉 encoder 与 diffusion policy 同时训练）
- **显式 anti-shortcut**（不靠“盲目 sensor dropout”，而是：normal field + 自监督等变/不变损失 + 接触阶段视觉退化 + 可选 residual‑in‑noise）

---

## 2) 数学定义（可直接放 Method/Preliminaries）

### 2.1 观测与动作

令时间 $t$ 的观测为  
$$
O_t = (X_t, S_t, I_t),
$$
其中：

- $X_t \in \mathbb{R}^{N\times 3}$：世界/环境坐标系点云（EquiBot 的输入）
- $S_t=(S_t^{(v)}, S_t^{(s)})$：机器人 proprioception，拆成  
  - 向量载体 $S_t^{(v)}\in \mathbb{R}^{C_s\times 3}$（例如位置、方向列向量）
  - 标量载体 $S_t^{(s)}\in \mathbb{R}^{C_s'}$（例如 gripper）
- $I_t=\{I_t^L,I_t^R\}$，每个触觉 RGB 图像 $I_t^\cdot \in [0,1]^{3\times H\times W}$，定义在夹爪局部帧。

动作序列（预测 horizon $H_p$）为  
$$
A_{t:t+H_p-1} = \{a_t,\dots,a_{t+H_p-1}\},
$$
并按 EquiBot 的 vector/scalar 形式表示：
$$
a_t = (a_t^{(v)}, a_t^{(s)}),
$$
其中 $a_t^{(v)}\in\mathbb{R}^{C_a\times 3}$，$a_t^{(s)}\in\mathbb{R}^{C_a'}$。  
在 `dof=7, num_eef=1` 的实现里：$C_a=2$（平移与旋转两个 3D 向量），$C_a'=1$（夹爪标量）。

---

### 2.2 世界等变性（你关心的是“不破坏 EquiBot 等变”）

令 $g=(R,t,s)\in SIM(3)$ 作用在世界量上：
$$
g\cdot x = sRx + t,\quad x\in\mathbb{R}^3.
$$
则
$$
g\cdot X_t = \{g\cdot x \mid x\in X_t\},\quad
g\cdot S_t^{(v)} = sR S_t^{(v)},\quad
g\cdot a_t^{(v)} = sR a_t^{(v)}.
$$
标量量不变：$g\cdot S_t^{(s)}=S_t^{(s)}$，$g\cdot a_t^{(s)}=a_t^{(s)}$。

**关键：触觉是 world‑invariant**
$$
g\cdot I_t = I_t
$$
因为 $I_t$ 是夹爪局部传感器读数，世界坐标系刚体变换不改变其像素值（在“群作用”意义下）。

---

## 3) 端到端触觉模块（贴 EquiTac 的处理方式，但输出为 world‑invariant 条件）

### 3.1 RGB → Normal field（Normal Reconstructor）

引入可学习重建器 $f_\psi$：
$$
N_t = f_\psi(I_t)\in \mathbb{R}^{3\times H\times W},\quad \|N_t(u)\|_2=1.
$$
其中 $u$ 为像素坐标。实现上你可以输出未归一化 $\tilde N_t$，然后
$$
N_t(u)=\frac{\tilde N_t(u)}{\|\tilde N_t(u)\|_2+\epsilon}.
$$

> 训练 $f_\psi$ 的监督来源（两条路）  
> - **(real) EquiTac 同款校准球**：sphere press → GT normal  
> - **(sim) 直接拿仿真接触几何/height map**：若能拿 height map，$N$ 可用可微梯度算子得到（不需要学习）

---

### 3.2 定义 SO(2) 向量场旋转算子（用于自监督/等变约束）

定义平面旋转矩阵
$$
R_\theta=
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}.
$$
令 $\mathcal{R}_\theta$ 对 normal field 的作用为（**空间旋转 + 分量旋转**）：
$$
(\mathcal{R}_\theta N)(u)=
\begin{bmatrix}
R_\theta & 0\\
0 & 1
\end{bmatrix}
N(R_{-\theta}u),
$$
其中 $N(R_{-\theta}u)$ 由双线性采样实现。

分解：
$$
N_{xy}\in\mathbb{R}^{2\times H\times W},\quad N_{z}\in\mathbb{R}^{1\times H\times W}.
$$
则
$$
\mathcal{R}_\theta N_{xy} = R_\theta N_{xy}(R_{-\theta}u),\quad
\mathcal{R}_\theta N_z = N_z(R_{-\theta}u).
$$

---

### 3.3 SO(2)‑equivariant tactile encoder → **group pooling 得到 world‑invariant embedding**

我们构造触觉 encoder $h_\phi$ 输出两类量：

1) **invariant embedding**（给 EquiBot 用）  
$$
e_t = h_\phi^{inv}(N_t)\in\mathbb{R}^{D}.
$$
要求对 in-hand SO(2) 旋转不变：
$$
e_t(\mathcal{R}_\theta N) = e_t(N).
$$

2) （可选）**equivariant orientation head**（只用于反 shortcut 的 aux loss）  
$$
y_t = h_\phi^{eq}(N_t)\in\mathbb{R}^2,
$$
并满足
$$
y(\mathcal{R}_\theta N)=R_{2\theta}y(N).
$$
我们用 EquiTac 的 **double-angle** 表示把 $\pi$ 对称合并：
$$
y_t=(\cos 2\alpha_t,\ \sin 2\alpha_t).
$$

**实现方式（贴 EquiTac）：**
- 用 ESCNN 的 C8-equivariant CNN 处理 $N_{xy}$（把它当成 vector field carrier）
- $N_z$ 走普通 CNN
- 最后做 **group pooling**（对 8 个离散角平均/最大），再做空间 pooling 得到 $e_t$

> 这一步非常关键：  
> 你可以在触觉 branch 内部利用 SO(2) 结构提高样本效率；  
> 但输出给 EquiBot 时通过 group pooling 变成 invariant 标量 embedding，从而保持世界等变。

---

### 3.4 触觉时序摘要（你旧 DRIFT 的 static/dynamic 思路保留，但不 canonicalize）

给定观测窗口 $H_o$，得到每一帧 embedding：
$$
\{e_{t-H_o+1},\dots,e_t\}.
$$
定义：
- 静态摘要：$\bar e_t=\frac1{H_o}\sum_{i=0}^{H_o-1}e_{t-i}$
- 动态差分：$\Delta e_t = e_t - e_{t-H_o+1}$

拼成最终触觉条件向量：
$$
c_t^{tac} = \Big[\mathrm{vec}(e_{t-H_o+1:t});\ \bar e_t;\ \Delta e_t\Big]\in\mathbb{R}^{D_{tac}},
\quad D_{tac}=(H_o+2)D.
$$

此外定义一个**接触强度标量**（用于 gating/数据增强）：
$$
\omega_t = \mathrm{mean}_u\big(1 - N_{z,t}(u)\big)\in\mathbb{R},
$$
直觉：没接触时 $n_z\approx 1$，压下去/倾斜时 $n_z$ 下降。

---

## 4) 把触觉无缝注入 EquiBot（关键是：只走 scalar_cond）

### 4.1 条件构造

EquiBot 原本的条件是：
- 向量条件：`obs_cond_vec ∈ R^{B×(H_o·obs_dim)×3}`
- 标量条件：`obs_cond_scalar = flatten(z_scalar) ∈ R^{B×(H_o·num_eef)}`

我们改成：
$$
\texttt{obs\_cond\_scalar} =
\big[\ \mathrm{vec}(S^{(s)}_{t-H_o+1:t})\ ;\ c_t^{tac}\ ;\ \omega_t\ \big].
$$

> 这一步在你的代码里就是：  
> `obs_cond_scalar = torch.cat([z_scalar_flat, c_tac, omega], dim=-1)`  
> 然后传给 `VecConditionalUnet1D(... scalar_cond=obs_cond_scalar)`。

---

### 4.2 等变性为何仍成立（你可以写成一个 Proposition）

令整体条件 $C_t=(X_{t-H_o+1:t}, S_{t-H_o+1:t}, c_t^{tac})$。  
其中 $c_t^{tac}$ 对世界变换 $g\in SIM(3)$ 不变。

如果你的噪声预测网络 $\epsilon_\theta$ 对世界变换满足：
$$
\epsilon_\theta(g\!\cdot\!A^k,\ g\!\cdot\!X,\ g\!\cdot\!S,\ c^{tac},\ k)
=
g\!\cdot\!\epsilon_\theta(A^k, X,S,c^{tac},k),
$$
且 DDPM prior $p(A^K)$ 是各向同性高斯（SO(3) 不变），则按照 EquiBot 论文里的 Proposition 1（马尔可夫链逐步等变 ⇒ 末端分布等变），得到最终策略分布：
$$
p_\theta(A^0\mid X,S,c^{tac})
=
p_\theta(g\!\cdot\!A^0 \mid g\!\cdot\!X,\ g\!\cdot\!S,\ c^{tac}).
$$
也就是说：**触觉作为 invariant scalar condition 不会破坏世界等变性。**

---

## 5) Anti‑shortcut：端到端但“结构上让触觉必须学到有用东西”的训练目标

你的核心痛点是：仅把触觉 concat 进去，扩散损失仍可能被视觉 shortcut 主导，从而触觉被忽略。  
我们给你一个**端到端**但很“EquiTac 风格”的组合损失：

### 5.1 主损失：扩散噪声预测

与现有 EquiBot 完全一致。以 epsilon prediction 为例（向量/标量都可）：
$$
\mathcal{L}_{DP}
=
\mathbb{E}_{k,\epsilon}
\left[
\left\|
\epsilon_\theta(O,\ A^k,\ k)-\epsilon
\right\|_2^2
\right],
$$
其中 $A^k = \sqrt{\bar\alpha_k}A^0 + \sqrt{1-\bar\alpha_k}\epsilon$。

---

### 5.2 触觉自监督 1：**equivariance consistency（不需要任何物体姿态标签）**

采样 $\theta\sim U(-\pi,\pi)$，构造 $N_\theta=\mathcal{R}_\theta N$。

对 orientation head：
$$
\mathcal{L}_{eq}
=
\mathbb{E}_{\theta}
\left\|
y(N_\theta) - R_{2\theta}y(N)
\right\|_2^2.
$$
再加单位范数：
$$
\mathcal{L}_{unit}
=
\left(\|y(N)\|_2-1\right)^2.
$$

> 这套 loss 的优点：  
> - 完全不需要真实 in-hand 角度标签  
> - 强制网络学到“旋转结构化的触觉表示”，减少颜色 shortcut

---

### 5.3 触觉自监督 2：**invariant embedding 对旋转的对比学习（防止 embedding 塌缩）**

对 invariant embedding $e$：
- 正样本对：$(e(N), e(N_\theta))$
- 负样本：同 batch 其他样本/其他时间步

InfoNCE：
$$
\mathcal{L}_{inv}
=
-\log
\frac{\exp(\langle \hat e,\hat e_\theta\rangle/\tau)}
{\sum_j \exp(\langle \hat e,\hat e_j\rangle/\tau)},
\quad \hat e = \frac{e}{\|e\|}.
$$

---

### 5.4 训练数据层面的 anti‑shortcut：**接触阶段的“局部点云退化”**

用 $\omega_t$（触觉接触强度）控制增强强度。令末端位置 $p_t$（从 `eef_pose_w` 的前三维取），对每个点 $x\in X_t$ 计算距离：
$$
d(x)=\|x-p_t\|.
$$
定义保留概率（例）：
$$
P(\text{keep}\mid x) = 1 - \omega_t\cdot \sigma\!\left(\frac{r-d(x)}{\delta}\right),
$$
其中 $r$ 是夹爪附近半径，$\delta$ 控制过渡带。

实现上你可以：
- 对近距离点随机丢弃/替换为远点
- 或对近距离点加大噪声

**直觉**：接触时最关键的几何细节恰好在夹爪附近，而视觉/点云在真实系统里也最容易被遮挡/反光污染；你在训练中模拟这一 regime，会强迫策略利用触觉条件降低 $\mathcal{L}_{DP}$。

---

### 5.5 总损失（端到端）

$$
\mathcal{L}
=
\mathcal{L}_{DP}
+\lambda_{eq}\mathcal{L}_{eq}
+\lambda_{unit}\mathcal{L}_{unit}
+\lambda_{inv}\mathcal{L}_{inv}.
$$

你可以从一个非常稳的初始权重开始：
- $\lambda_{eq}=0.1$
- $\lambda_{unit}=0.01$
- $\lambda_{inv}=0.05$

---

## 6) 训练/推理算法（可直接写成 ECCV Algorithm）

### Algorithm 1：单步训练（batch 内端到端）

1. 取 batch：$(X_{1:H_o}, S_{1:H_o}, I_{1:H_o}, A_{1:H_p})$
2. 用 EquiBot encoder 得到向量条件 $c^{vec}$
3. 用 tactile branch 得到 $c^{tac}$ 和 $\omega$
4. 形成标量条件 $c^{sca}=[S^{(s)};c^{tac};\omega]$
5. 随机采样 diffusion step $k$ 与噪声 $\epsilon$，构造 noisy actions $A^k$
6. 预测 $\hat\epsilon=\epsilon_\theta(A^k,k,c^{vec},c^{sca})$
7. 计算 $\mathcal{L}_{DP}$
8. 采样 $\theta$，构造 $N_\theta$，计算 $\mathcal{L}_{eq},\mathcal{L}_{unit},\mathcal{L}_{inv}$
9. 总损失 $\mathcal{L}$ 反传更新全部参数（encoder + tactile + unet）

推理时与 EquiBot 相同，只是每一步额外算 $c^{tac}$ 并拼进 `scalar_cond`。

---

## 7) 你仓库里的 **concrete code proposal**（逐文件，改动最小且可跑）

下面按你提供的代码结构给出“最少侵入”的实现方案。

---

### 7.1 数据与 config

#### (1) `equibot.yaml`：让 BaseDataset 在 pc 模式也读 tactile 图

```yaml
data:
  dataset:
    obs_mode: "pc"
    rgb_keys: ["rgb_tactile_left", "rgb_tactile_right"]
    cache_rgb: true
```

并增加 tactile 模块超参：

```yaml
model:
  use_tactile: true
  tactile_keys: ["rgb_tactile_left", "rgb_tactile_right"]
  tactile:
    H: 128
    W: 128
    emb_dim: 128        # D
    use_normal_map: true
    so2_groups: 8       # C8
    loss:
      lambda_eq: 0.1
      lambda_unit: 0.01
      lambda_inv: 0.05
```

---

#### (2) `BaseDataset._init_cache()`：pc 模式也缓存 rgb（否则每次 np.load 会很慢）

你现在的 `_init_cache()` 只在 `obs_mode == "rgb"` 时缓存 rgb。建议改成：

```python
# dataset.py::_init_cache
keys_to_keep = ["eef_pose_w", "action"]
if self.obs_mode.startswith("pc"):
    keys_to_keep.append("pc")

# NEW: if rgb_keys exists, cache them even in pc mode
if len(self.rgb_keys) > 0 and self.cache_rgb:
    keys_to_keep.extend(self.rgb_keys)
```

并在写入 cache 时加：

```python
if len(self.rgb_keys) > 0 and self.cache_rgb:
    for k in self.rgb_keys:
        if k in data.files:
            self.cache[fn][k] = data[k]
```

---

### 7.2 FactoryIL rollout：pc‑mode 也把 tactile 传给 policy

你现在 `ILPolicyAgent.act()` 在 `obs_mode.startswith("pc")` 时不会构造 `agent_obs["rgb"]`。  
建议改成：**无论 pc 还是 rgb 模式，只要 policy 需要 rgb_keys，就都传**。

在 `factoryil/agents/il_agents.py` 里：

- 保留 `rgb_hist` 的维护逻辑（目前只有 `obs_mode=="rgb"` 才进）
- 改为：只要 `obs_i` 里有 `"rgb"` 且 `self.rgb_keys` 非空/可推断，就把它存起来
- 构造 `agent_obs` 时，即使 pc 模式，也加：

```python
if len(self.rgb_keys) > 0:
    rgb_dict = {}
    for k in self.rgb_keys:
        if len(st.rgb_hist.get(k, [])) == 0:
            continue
        seq = _ensure_len(st.rgb_hist[k], int(self.obs_horizon))
        rgb_dict[k] = np.stack(seq, axis=0)  # [Ho,H,W,3] uint8
    agent_obs["rgb"] = rgb_dict
```

---

### 7.3 新增 tactile 模块文件（建议放 `policies/tactile/`）

你可以加两个文件：

#### (1) `policies/tactile/normal_reconstructor.py`

- 输入：`[B,Ho,3,H,W]`
- 输出：`[B,Ho,3,H,W]`，单位法向

MVP 可以先用一个小 U‑Net / ResNet‑like CNN；如果有 height map 则更简单。

#### (2) `policies/tactile/tactile_encoder.py`

- 输入：左右 normal maps
- 输出：
  - `e_seq`: `[B,Ho,D]`
  - `y_seq`: `[B,Ho,2]`（double-angle，可选）
  - `omega_seq`: `[B,Ho,1]`（接触强度，可从 $1-n_z$ 算）

---

### 7.4 `EquiBotPolicy`：把 tactile encoder 加进 nets + EMA，并拼进 scalar_cond

#### (1) `__init__` 里

关键是把 `scalar_cond_dim` 增大：

```python
# equibot_policy.py::EquiBotPolicy.__init__
self.use_tactile = bool(getattr(cfg.model, "use_tactile", False))
self.tactile_cond_dim = 0
if self.use_tactile:
    self.tactile_keys = list(cfg.model.tactile_keys)
    self.tactile_emb_dim = int(cfg.model.tactile.emb_dim)
    Ho = cfg.model.obs_horizon
    # (Ho + 2) * D  (+1 for omega if you want)
    self.tactile_cond_dim = (Ho + 2) * self.tactile_emb_dim + 1

    self.tactile_encoder = TactileEncoder(cfg.model.tactile)
else:
    self.tactile_encoder = None

scalar_cond_dim = (0 if self.dof == 3 else self.num_eef * self.obs_horizon) + self.tactile_cond_dim

self.noise_pred_net = VecConditionalUnet1D(
    input_dim=self.action_dim,
    cond_dim=self.obs_dim * self.obs_horizon,
    scalar_cond_dim=scalar_cond_dim,
    scalar_input_dim=num_scalar_dims,
    diffusion_step_embed_dim=self.obs_dim * self.obs_horizon,
    cond_predict_scale=True,
)
```

并把 tactile encoder 放进 EMA：

```python
self.nets = nn.ModuleDict({
    "encoder": self.encoder,
    "tactile_encoder": self.tactile_encoder,
    "noise_pred_net": self.noise_pred_net,
})
self.ema = EMAModel(model=copy.deepcopy(self.nets), power=0.75)
```

> 注意：如果 `tactile_encoder=None`，你要在 ModuleDict 里避免放 None（否则报错）。可以用 `nn.Identity()` 占位，或只在 use_tactile 时加入键。

---

#### (2) `forward()` 里从 `obs["rgb"]` 取触觉并拼 `obs_cond_scalar`

在 `equibot_policy.py::forward` 里，构造 `obs_cond_scalar` 后加：

```python
obs_cond_scalar = z_scalar.reshape(B, -1) if z_scalar is not None else None

if self.use_tactile:
    rgb = obs.get("rgb", None)
    assert rgb is not None, "use_tactile=True but obs has no rgb dict"

    tl = rgb["rgb_tactile_left"].float() / 255.0   # [B,Ho,H,W,3]
    tr = rgb["rgb_tactile_right"].float() / 255.0

    tl = tl.permute(0,1,4,2,3).contiguous()        # [B,Ho,3,H,W]
    tr = tr.permute(0,1,4,2,3).contiguous()

    # Use EMA tactile encoder at inference for stability
    tac_out = ema_nets["tactile_encoder"](tl, tr)  # returns dict
    c_tac = tac_out["cond"]                         # [B, tactile_cond_dim]
    if obs_cond_scalar is None:
        obs_cond_scalar = c_tac
    else:
        obs_cond_scalar = torch.cat([obs_cond_scalar, c_tac], dim=-1)
```

---

### 7.5 `EquiBotAgent.update()`：端到端训练损失加上 tactile aux losses

在 `equibot_agent.py::update` 里：

1) 从 batch 取触觉：
```python
rgb = batch.get("rgb", None)
```

2) 计算 tactile cond（用当前网络，不用 EMA）：
```python
if self.actor.use_tactile:
    tl = rgb["rgb_tactile_left"].float()/255.0   # [B,Ho,H,W,3]
    tr = rgb["rgb_tactile_right"].float()/255.0
    tl = tl.permute(0,1,4,2,3).contiguous()
    tr = tr.permute(0,1,4,2,3).contiguous()
    tac_out = self.actor.tactile_encoder_handle(tl, tr)
    obs_cond_scalar = torch.cat([obs_cond_scalar, tac_out["cond"]], dim=-1)
```

3) 维持原 diffusion loss `loss_dp`。

4) 加入 aux loss（建议在 `tactile_encoder` 里返回你需要的中间量，比如 `y`, `y_theta`，或在 update 里做旋转增强）：
```python
loss = loss_dp
if self.actor.use_tactile and self.cfg.model.tactile.loss.lambda_eq > 0:
    loss = loss + lambda_eq * tac_out["loss_eq"] + lambda_inv * tac_out["loss_inv"] + ...
```

5) `loss.backward()` 更新全部参数，即端到端。

---

## 8) 你 ECCV 论文可以怎么写贡献点（把代码与数学闭环）

你现在这套 proposal 的“paper 贡献”可以非常清晰：

1) **Tactile‑as‑Invariant Conditioning**：  
   证明/论证：把触觉嵌入作为 `scalar_cond` 注入 EquiBot 的等变 diffusion step，不破坏 $SIM(3)$ 等变性（给出上面的等变条件与 Proposition）。

2) **EquiTac‑style Normal Field Carrier**：  
   RGB→normal field，分解成 $(n_x,n_y)$（SO(2) 向量载体）与 $n_z$（不变量载体），作为触觉几何一致表示。

3) **Self‑supervised tactile equivariance/invariance losses**：  
   不用物体姿态标签，通过 $\mathcal{R}_\theta$ 旋转增强实现：
   - 等变一致性（orientation head）
   - 不变对比学习（embedding head）
   这些 loss 让触觉分支学到“结构化的触觉状态”，显著缓解 shortcut-learning。

4) **Contact‑aware visual degradation**：  
   用触觉接触强度 $\omega$ 控制点云局部退化，使训练分布更贴近真实接触遮挡 regime，从数据层面迫使策略用触觉。

---

如果你愿意，我可以在你下一条消息里按你偏好的写作风格，把以上内容直接改写成 **ECCV 论文的 Method 章节草稿**（含符号表、命题、证明草图、算法框、实现细节表格、以及与 EquiBot/EquiTac 的对齐叙述），并同时给出一个“最小改动的 patch 清单”（逐文件 diff 级别）。

Other chats:

https://gemini.google.com/u/1/app/1c701d4c76103f2f?pageId=none
https://poe.com/chat/2ub0ia5h613jglgj9l