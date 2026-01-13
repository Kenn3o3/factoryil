> 说明：`franky` 是一个高层控制库（Python/C++），它的核心卖点是**你不用自己写 1kHz 的严格实时控制逻辑**：你给它高层目标（位置/速度），它在实时线程里用 **Ruckig** 做实时轨迹规划，并允许随时 preempt/replan；同时也把 libfranka 的很多能力（比如 gripper、阻抗相关设置等）暴露到 Python。  
> 它支持四种阻抗控制模式：**关节位置/关节速度/笛卡尔位置/笛卡尔速度**。

---

## 0. 先确认你要的 libfranka 版本（非常关键）

`franky` 会用到 `libfranka`，而 **libfranka 必须与机器人 Robot System Version 兼容**。README 里也提到，如果你看到 server/library mismatch（比如 `server version: 5, library version: 9`），本质就是版本不匹配，需要换对应版本的 wheels。

你现在机器人是 **Control 5.8.2**，通常对应 `libfranka` 在 `0.15.x ~ 0.17.x` 区间（你已经验证 `0.17.0` 可连上并 `readOnce()` 成功），因此 franky 这边建议选：
- **直接用默认 pip 安装（README 提到默认 libfranka 0.16.0）**，或
- **安装 `libfranka 0.17.0` 对应的 franky wheels**（README 明确列出支持 `0.17.0`）。

---

## 1. 前置条件（franky README 的三步）

franky 的 README 把 setup 总结成三步：

1) **确认你在 real-time kernel 上**  
2) **给执行用户 real-time 权限**  
3) **pip 安装 franky（或从源码编译）**

### 1.1 检查是否是 PREEMPT_RT 内核

```bash
uname -a
```

你应该看到类似（重点是 `PREEMPT_RT`）：

```text
... SMP PREEMPT_RT ...
```

如果没有 `PREEMPT_RT`，README 提到你可以**从源码构建实时内核**或（Ubuntu 上）通过 **Ubuntu Pro** 启用。

> 你当前已经是 `6.8.0-rt8 ... PREEMPT_RT` 且 `/sys/kernel/realtime=1`，这一步你已满足。

### 1.2 给用户实时权限（realtime 组 + limits.conf）

README 给的标准做法如下（你也已经做过）：

```bash
sudo addgroup realtime
sudo usermod -a -G realtime $(whoami)
```

在 `/etc/security/limits.conf` 增加：

```text
@realtime soft rtprio 99
@realtime soft priority 99
@realtime soft memlock 102400
@realtime hard rtprio 99
@realtime hard priority 99
@realtime hard memlock 102400
```

登出再登录后验证：

```bash
groups
ulimit -r
ulimit -l
```

---

## 2. 安装方式

```bash
conda create -n franka_arm python=3.10 -y
conda activate franka_arm
python -m pip install -U pip
```

```bash 
wget https://github.com/TimSchneider42/franky/releases/latest/download/libfranka_0-17-0_wheels.zip #can change 0-17-0
unzip libfranka_0-17-0_wheels.zip

pip install numpy
pip install --no-index --find-links=./dist franky-control
```

---

## 3. 运行前准备：Desk 里解刹车 + 启用 FCI

- 在网页界面**Unlock brakes**
- **Enable FCI**
- 然后再跑代码

---

## 4. 最小运行示例（Python）

保存成 `demo.py`：

```python
from franky import Robot, CartesianMotion, Affine, ReferenceType

robot = Robot("172.16.0.2")  # 改成你的 FCI IP
robot.relative_dynamics_factor = 0.05  # 建议从很小开始

motion = CartesianMotion(
    Affine([0.2, 0.0, 0.0]),
    ReferenceType.Relative
)

robot.move(motion)
print("Done.")
```

运行：

```bash
python demo.py
```

Status: It worked 