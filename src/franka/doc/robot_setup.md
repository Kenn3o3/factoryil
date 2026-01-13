# Franka（libfranka）在 Ubuntu 22.04（Jammy）上的安装与实时内核（PREEMPT_RT）配置指南

> 适用对象：希望在 Linux 上用 **libfranka** 进行 Franka 机器人实时控制（例如阻抗控制/力控/数据采集）的同学。  
> 本文面向“和我类似的电脑系统”的复现：**Ubuntu 22.04.x LTS / x86_64 / 直连千兆网口 / 需要 PREEMPT_RT 实时内核**。  
>
> **测试通过环境（示例）**  
> - OS：Ubuntu 22.04.5 LTS（jammy）  
> - Kernel：`6.8.0-rt8`（`PREEMPT_RT`）  
> - Robot：Franka Research Robot（Desk 可访问）  
> - Robot System（示例）：Control `5.8.2`，FCI feature installed（示例：FCI `1.0.0`）  
> - PC ↔ Robot：1GbE（1000BASE-T）直连（推荐）

---

## 目录

- [1. 背景与要点](#1-背景与要点)
- [2. 先确认：你需要哪个 libfranka 版本？](#2-先确认你需要哪个-libfranka-版本)
- [3. 网络配置（必须先通）](#3-网络配置必须先通)
- [4. 配置 PREEMPT_RT 实时内核（Ubuntu 22.04 手动打补丁方案）](#4-配置-preempt_rt-实时内核ubuntu-2204-手动打补丁方案)
  - [4.1 安装构建依赖](#41-安装构建依赖)
  - [4.2 下载内核与 RT 补丁](#42-下载内核与-rt-补丁)
  - [4.3（可选但推荐）验证文件完整性（GPG）](#43可选但推荐验证文件完整性gpg)
  - [4.4 编译内核并生成 deb 包](#44-编译内核并生成-deb-包)
  - [4.5 安装新内核并重启验证](#45-安装新内核并重启验证)
- [5. 允许用户进程设置实时权限（realtime 组 + limits.conf）](#5-允许用户进程设置实时权限realtime-组--limitsconf)
- [6. 安装 libfranka（两种方法）](#6-安装-libfranka两种方法)
  - [方法 A：安装官方发布的 Debian 包（推荐，若版本匹配且有对应 jammy 包）](#方法-a安装官方发布的-debian-包推荐若版本匹配且有对应-jammy-包)
  - [方法 B：从源代码构建并打包成 deb（当你需要特定版本或仓库包不匹配时）](#方法-b从源代码构建并打包成-deb当你需要特定版本或仓库包不匹配时)
    - [B.1 清理旧的 libfranka（避免混装）](#b1-清理旧的-libfranka避免混装)
    - [B.2 安装构建依赖](#b2-安装构建依赖)
    - [B.3 安装 pinocchio（推荐两条路：按 libfranka README 的“Advanced”或用 robotpkg）](#b3-安装-pinocchio推荐两条路按-libfranka-readme-的advanced或用-robotpkg)
    - [B.4 解决 fmt 版本问题（常见坑：Jammy 默认是 libfmt8）](#b4-解决-fmt-版本问题常见坑jammy-默认是-libfmt8)
    - [B.5 构建 libfranka 指定版本并生成 deb](#b5-构建-libfranka-指定版本并生成-deb)
    - [B.6 验证安装](#b6-验证安装)
- [7. 冒烟测试：用最小 C++ 程序连上机器人](#7-冒烟测试用最小-c-程序连上机器人)
- [8. 常见问题 / 排错清单](#8-常见问题--排错清单)
- [9. 下一步：为模仿学习做数据采集系统（建议框架）](#9-下一步为模仿学习做数据采集系统建议框架)
- [10. 参考资料（原始链接）](#10-参考资料原始链接)

---

## 1. 背景与要点

- **libfranka** 是 Franka 研究机器人底层实时控制的 C++ 库（低层控制、实时通信等）。
- 想用 libfranka 做实时控制（例如阻抗控制），工作站 PC 上的控制程序必须在 **PREEMPT_RT** 内核下以 **实时优先级** 运行。
- `franka_ros` 只有在你想用 **ROS 平台控制机器人**时才需要；纯 C++/Python 直接调用 libfranka 不必装 `franka_ros`。

---

## 2. 先确认：你需要哪个 libfranka 版本？

最重要的一步：**libfranka 版本必须和机器人 Robot System Version 兼容**。  
否则可能出现：
- 能 ping 通、甚至 `readOnce()` 也能读到，但进入控制（control loop）时失败
- 协议/服务器版本不匹配导致异常

示例兼容表（请以官方“Robot System Version Compatibility”为准）：

| libfranka Version | Robot System Version |
|---|---|
| `>= 0.18.0` | `>= 5.9.0` |
| `>= 0.15.0 < 0.18.0` | `>= 5.7.2 < 5.9.0` |

**示例**：如果你的 Control 是 `5.8.2`，则通常选择 `0.15.x ~ 0.17.x`，例如 `0.17.0`。

---

## 3. 网络配置（必须先通）

### 3.1 推荐拓扑

- PC 用 **独立的千兆有线网口**直连到机器人（或通过同一交换机）
- 不建议把实时控制流量走 Wi‑Fi/VPN/虚拟网卡

### 3.2 检查网卡、IP 和链路速率

```bash
ip -br addr
ip route
sudo ethtool <你的有线网卡名> | egrep "Speed|Duplex|Link detected"
```

你希望看到类似：
- `Speed: 1000Mb/s`
- `Duplex: Full`
- `Link detected: yes`

### 3.3 Ping 机器人

把 PC 有线网卡配置到机器人同网段，例如机器人是 `172.16.0.2/24`，PC 可以设成 `172.16.0.3/24`：

```bash
ping -c 5 172.16.0.2
```

---

## 4. 配置 PREEMPT_RT 实时内核（Ubuntu 22.04 手动打补丁方案）

> 说明：FCI Linux 安装文档中提到：Ubuntu 22.04 推荐使用 Ubuntu Pro 实时内核；如果不使用 Ubuntu Pro，也可以按其他版本方式继续（已在 **内核 6.8.0** 下测试），并应用 **PREEMPT_RT** 补丁。

### 4.1 安装构建依赖

```bash
sudo apt-get update
sudo apt-get install -y \
  build-essential bc curl debhelper dpkg-dev devscripts fakeroot \
  libssl-dev libelf-dev bison flex cpio kmod rsync libncurses-dev
```

### 4.2 下载内核与 RT 补丁

以 Ubuntu 22.04（示例：6.8 + rt8）为例：

```bash
mkdir -p ~/rt_kernel_build && cd ~/rt_kernel_build

# Linux kernel source + signature
curl -fLO https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.8.tar.xz
curl -fLO https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.8.tar.sign

# RT patch + signature
curl -fLO https://www.kernel.org/pub/linux/kernel/projects/rt/6.8/older/patch-6.8-rt8.patch.xz
curl -fLO https://www.kernel.org/pub/linux/kernel/projects/rt/6.8/older/patch-6.8-rt8.patch.sign

# 解压
xz -d *.xz
```

> 你也可以用 `uname -r` 查看当前内核，尽量选择“匹配或最接近”的 RT patch 版本。

### 4.3（可选但推荐）验证文件完整性（GPG）

```bash
# 验证 kernel tar
gpg2 --verify linux-*.tar.sign

# 验证 RT patch
gpg2 --verify patch-*.patch.sign patch-*.patch
```

如果提示 `Can't check signature: No public key`，按输出中的 key id 去拉取公钥，例如：

```bash
gpg2 --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys <KEY_ID>
```

> 注意：不同内核/补丁的 key id 可能不同，要以你本机 gpg 输出为准。

### 4.4 编译内核并生成 deb 包

```bash
cd ~/rt_kernel_build
tar xf linux-*.tar
cd linux-*/

# 应用 RT patch
patch -p1 < ../patch-*.patch

# 拷贝当前内核配置作为默认配置
cp -v /boot/config-$(uname -r) .config

# 去掉调试信息（节省空间）
scripts/config --disable DEBUG_INFO
scripts/config --disable DEBUG_INFO_DWARF_TOOLCHAIN_DEFAULT
scripts/config --disable DEBUG_KERNEL

# 禁用系统范围受信密钥环
scripts/config --disable SYSTEM_TRUSTED_KEYS
scripts/config --disable SYSTEM_REVOCATION_LIST

# 激活完全可抢占内核（实时）
scripts/config --disable PREEMPT_NONE
scripts/config --disable PREEMPT_VOLUNTARY
scripts/config --disable PREEMPT
scripts/config --enable PREEMPT_RT

make olddefconfig
```

开始编译并打包：

```bash
# 官方文档示例是 deb-pkg，但从 tarball 构建时可能会遇到 “requires git repository”
# 推荐直接用 bindeb-pkg（只做二进制包，适合我们这种 tarball + patch）
make -j"$(nproc)" bindeb-pkg
```

> 常见坑：如果你运行 `make deb-pkg` 报错 `creating source package requires git repository`，就改用 `bindeb-pkg`。

### 4.5 安装新内核并重启验证

回到上级目录，会生成类似 `linux-image-6.8.0-rt8_*.deb`、`linux-headers-6.8.0-rt8_*.deb`：

```bash
cd ~/rt_kernel_build
ls -1 *.deb | egrep 'linux-(image|headers).*rt'

# 安装 headers 和 image（不要装 -dbg）
sudo dpkg -i linux-headers-6.8.0-rt8_*_amd64.deb \
             linux-image-6.8.0-rt8_*_amd64.deb

sudo update-grub
sudo reboot
```

重启后在 GRUB 里选择 `6.8.0-rt8` 之类的内核项启动。

验证：

```bash
uname -a
cat /sys/kernel/realtime
```

你希望看到：
- `uname -a` 输出包含 `PREEMPT_RT`
- `/sys/kernel/realtime` 输出为 `1`

---

## 5. 允许用户进程设置实时权限（realtime 组 + limits.conf）

```bash
sudo addgroup realtime
sudo usermod -a -G realtime $(whoami)
```

编辑 `/etc/security/limits.conf`（推荐追加到文件末尾）：

```bash
sudo cp /etc/security/limits.conf /etc/security/limits.conf.bak.$(date +%F_%H%M%S)

sudo tee -a /etc/security/limits.conf >/dev/null <<'EOF'

# Franka realtime permissions
@realtime soft rtprio 99
@realtime soft priority 99
@realtime soft memlock 102400
@realtime hard rtprio 99
@realtime hard priority 99
@realtime hard memlock 102400
EOF
```

**注销并重新登录**（或直接重启）后生效。

验证：

```bash
groups | grep realtime
ulimit -r
ulimit -l
```

期望：
- `ulimit -r` 为 `99`
- `ulimit -l` 为 `102400`

---

## 6. 安装 libfranka（两种方法）

### 方法 A：安装官方发布的 Debian 包（推荐，若版本匹配且有对应 jammy 包）

libfranka 官方 README 提供了 “Installation from Debian Package（Recommended）” 流程：下载 `.deb` + `.sha256`，校验后 `dpkg -i` 安装。

示例（把版本与 codename 改成你需要的）：

```bash
LIBFRANKA_VER="0.19.0"
UBUNTU_CODENAME="$(lsb_release -cs)"   # focal/jammy/noble

wget "https://github.com/frankarobotics/libfranka/releases/download/${LIBFRANKA_VER}/libfranka_${LIBFRANKA_VER}_${UBUNTU_CODENAME}_amd64.deb"
wget "https://github.com/frankarobotics/libfranka/releases/download/${LIBFRANKA_VER}/libfranka_${LIBFRANKA_VER}_${UBUNTU_CODENAME}_amd64.deb.sha256"

sha256sum -c "libfranka_${LIBFRANKA_VER}_${UBUNTU_CODENAME}_amd64.deb.sha256"
sudo dpkg -i "libfranka_${LIBFRANKA_VER}_${UBUNTU_CODENAME}_amd64.deb"
```

> 提醒：尽量不要用 `wget --no-check-certificate`，这会跳过 TLS 证书校验，有安全风险。优先修复本机 CA 证书（如安装/更新 `ca-certificates`）。

如果 `dpkg -i` 提示缺依赖：

```bash
sudo apt-get -f install
```

### 方法 B：从源代码构建并打包成 deb（当你需要特定版本或仓库包不匹配时）

当出现以下情况，建议用方法 B：
- 你需要一个特定 tag（例如 `0.17.0`）但没有现成 jammy deb
- 你需要和 Robot System Version 严格匹配的版本
- 你需要自己控制依赖（pinocchio、fmt 等）

#### B.1 清理旧的 libfranka（避免混装）

```bash
sudo apt-get purge -y libfranka || true
sudo apt-get autoremove -y --purge || true
sudo ldconfig

dpkg -l | grep libfranka || echo "OK: libfranka removed"
```

（可选，若你之前手动复制/安装过库文件）：

```bash
sudo rm -f /usr/lib/x86_64-linux-gnu/libfranka.so* /usr/lib/libfranka.so* 2>/dev/null || true
sudo ldconfig
```

#### B.2 安装构建依赖

根据 libfranka README 的 “Building from Source” 基本依赖：

```bash
sudo apt-get update
sudo apt-get install -y \
  build-essential \
  cmake \
  git \
  wget \
  libeigen3-dev \
  libpoco-dev \
  libfmt-dev \
  pybind11-dev
```

> Jammy 默认 CMake 一般满足（README 要求 CMake >= 3.22）。  
> 若你在 Ubuntu 20.04 需要升级 CMake，README 给了 kitware apt 的方法（Jammy 通常不需要）。

#### B.3 安装 pinocchio（推荐两条路：按 libfranka README 的“Advanced”或用 robotpkg）

- **推荐/最稳**：完全按 libfranka README 的 **“Building from Source (Advanced)”**，它会按顺序把依赖（Boost、TinyXML2、urdfdom、assimp、pinocchio 等）从源代码编译并做静态链接。  
  优点：最少系统依赖坑。缺点：非常耗时。

- **更快（但更“系统工程”）**：用 **robotpkg** 安装 pinocchio（示例：装到 `/opt/openrobots`），并在 CMake 时设置 `CMAKE_PREFIX_PATH=/opt/openrobots`。

robotpkg 示例流程（供参考）：

```bash
sudo apt-get install -y lsb-release ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings

curl -fsSL http://robotpkg.openrobots.org/packages/debian/robotpkg.asc \
  | sudo tee /etc/apt/keyrings/robotpkg.asc > /dev/null

echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/robotpkg.asc] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -cs) robotpkg" \
  | sudo tee /etc/apt/sources.list.d/robotpkg.list > /dev/null

sudo apt-get update

# 找 pinocchio 包名（不同机器可能不同）
apt-cache search robotpkg | grep -i pinocchio

# 安装其中一个存在的包
sudo apt-get install -y robotpkg-pinocchio || sudo apt-get install -y robotpkg-py38-pinocchio
```

确认 `pinocchioConfig.cmake` 存在：

```bash
sudo find /opt/openrobots -name 'pinocchioConfig.cmake' -o -name 'pinocchio-config.cmake'
```

让系统运行时能找到 `/opt/openrobots/lib` 下的动态库：

```bash
echo "/opt/openrobots/lib" | sudo tee /etc/ld.so.conf.d/openrobots.conf >/dev/null
sudo ldconfig
ldconfig -p | grep pinocchio || true
```

#### B.4 解决 fmt 版本问题（常见坑：Jammy 默认是 libfmt8）

一些版本/构建组合下，你可能会遇到 `libfranka.so` 需要 `libfmt.so.9`，但 Ubuntu 22.04 仓库只有 `libfmt8` 的情况。

如果你 `ldd` 看到 `libfmt.so.9 => not found`，一种可复现的解决方式是在 `/usr/local` 安装 fmt 9（shared library）：

```bash
sudo apt-get update
sudo apt-get install -y build-essential cmake git

cd /tmp
rm -rf fmt
git clone --depth 1 --branch 9.1.0 https://github.com/fmtlib/fmt.git

cmake -S fmt -B fmt/build \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS=ON \
  -DFMT_DOC=OFF \
  -DFMT_TEST=OFF

cmake --build fmt/build -j"$(nproc)"
sudo cmake --install fmt/build

# 确保 /usr/local/lib 在 linker cache 里
echo "/usr/local/lib" | sudo tee /etc/ld.so.conf.d/local.conf >/dev/null
sudo ldconfig

ldconfig -p | grep -E 'libfmt\.so\.9' || echo "ERROR: libfmt.so.9 not found in cache"
```

> 说明：这属于“系统依赖管理”的取舍。更稳的方式依然是走 libfranka README 的 Advanced（依赖全从源编译静态链接），但代价是耗时。

#### B.5 构建 libfranka 指定版本并生成 deb

以 `0.17.0` 为例：

```bash
mkdir -p ~/franka && cd ~/franka
rm -rf libfranka

git clone --recurse-submodules https://github.com/frankarobotics/libfranka.git
cd libfranka
git checkout 0.17.0
git submodule update --init --recursive

rm -rf build
mkdir build && cd build

cmake -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_TESTS=OFF \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_PREFIX_PATH=/opt/openrobots \
      ..

cmake --build . -j"$(nproc)"

# 生成 deb 包（便于卸载/迁移/复现）
cpack -G DEB

# 安装
sudo dpkg -i ./*.deb
sudo ldconfig
```

> 如果你没用 robotpkg（没有 `/opt/openrobots`），就不要加 `-DCMAKE_PREFIX_PATH=/opt/openrobots`；或改成你的 pinocchio 安装路径。  
> 如果 CMake 报 “找不到 pinocchioConfig.cmake”，说明你需要设置 `CMAKE_PREFIX_PATH` 或 `pinocchio_DIR`。

#### B.6 验证安装

```bash
dpkg -l | grep libfranka

# 文件位置可能是 /usr/lib 或 /usr/lib/x86_64-linux-gnu（取决于打包/发行版 multiarch）
ls -l /usr/lib/libfranka.so 2>/dev/null || true
ls -l /usr/lib/x86_64-linux-gnu/libfranka.so 2>/dev/null || true

ls /usr/include/franka/ | head

# 检查动态库依赖是否缺失
ldd /usr/lib/x86_64-linux-gnu/libfranka.so | egrep 'not found|fmt|pinocchio' || true
```

---

## 7. 冒烟测试：用最小 C++ 程序连上机器人

在任意工作目录创建 `check_franka.cpp`：

```cpp
#include <franka/exception.h>
#include <franka/robot.h>
#include <iostream>

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <robot-ip>\n";
    return 1;
  }
  try {
    franka::Robot robot(argv[1]);
    auto state = robot.readOnce();
    std::cout << "Connected. RobotState.time(ms since robot start) = "
              << state.time.toMSec() << "\n";
    return 0;
  } catch (const franka::Exception& e) {
    std::cerr << "libfranka exception:\n" << e.what() << "\n";
    return 2;
  }
}
```

编译并运行（将 `<ROBOT_IP>` 替换成机器人 IP，比如 `172.16.0.2`）：

```bash
g++ -O2 -std=c++17 check_franka.cpp -lfranka -o check_franka
./check_franka <ROBOT_IP>
```

期望输出类似：

```text
Connected. RobotState.time(ms since robot start) = 1496746
```

---

## 8. 常见问题 / 排错清单

### 8.1 没进 RT 内核（/sys/kernel/realtime 不存在或不是 1）

```bash
uname -a
cat /sys/kernel/realtime 2>/dev/null || echo "no /sys/kernel/realtime"
```

- `uname -a` 必须包含 `PREEMPT_RT`
- `/sys/kernel/realtime` 必须是 `1`  
否则：检查 GRUB 是否选对内核项、是否安装了 `linux-image-*-rt*`。

### 8.2 `ulimit -r` 还是 0

- 确认自己在 `realtime` 组中：

```bash
groups | grep realtime
```

- 修改 `/etc/security/limits.conf` 后必须 **注销再登录**（或重启）
- 仍不生效：检查 PAM 是否启用了 limits（一般 Ubuntu 默认是启用的）

### 8.3 构建内核时报 `make deb-pkg` 需要 git repo

现象：

```text
error: creating source package requires git repository
```

解决：用

```bash
make -j"$(nproc)" bindeb-pkg
```

### 8.4 CMake 找不到 pinocchio

现象：

```text
Could not find pinocchioConfig.cmake
```

解决思路：
- 找到 pinocchio 的 cmake config 位置（例如 `/opt/openrobots/lib/cmake/pinocchio/pinocchioConfig.cmake`）
- 在 cmake 时指定其中一种：
  - `-DCMAKE_PREFIX_PATH=/opt/openrobots`
  - 或 `-Dpinocchio_DIR=/opt/openrobots/lib/cmake/pinocchio`

### 8.5 `ldd libfranka.so` 显示 pinocchio / fmt “not found”

- pinocchio 缺失：把 `/opt/openrobots/lib` 加入 linker cache：

```bash
echo "/opt/openrobots/lib" | sudo tee /etc/ld.so.conf.d/openrobots.conf >/dev/null
sudo ldconfig
```

- fmt 缺失：如果需要 `libfmt.so.9`，Jammy 仓库通常没有 `libfmt9` 包，可能需要自己安装 fmt 9（见上文 B.4），或用其它方式让 libfranka 链到系统 `libfmt.so.8`（这通常意味着要确保构建时使用的是系统 fmt8）。

### 8.6 不要在实时控制链路上走 VPN

你可以用 VPN/子网路由访问 Desk 网页做配置，但**实时控制程序**最好跑在 PC 与机器人直连的千兆网段上。

---

## 9. 下一步：为模仿学习做数据采集系统（建议框架）

> 这部分不是 libfranka 安装必需，但对你最终目标（两相机 + 机器人位姿 + GelSight）有帮助。

### 9.1 场景一：两相机 + 机器人位姿（同步时间帧）

建议做法：
- 用一个“采集主进程/主时钟”统一发时间戳（例如 `CLOCK_MONOTONIC`）
- 每个相机帧写入：
  - `t_capture`（相机驱动给的时间戳或你接收时刻）
  - `frame_id`
- 机器人状态写入：
  - `t_robot_read`（你调用 `readOnce()`/控制回调的时间）
  - `RobotState.time`（机器人内部时间字段，可作为辅助对齐信号）
- 最终离线对齐方式：
  - 最近邻对齐（每个相机帧找最近的机器人状态）
  - 或按固定采样率插值机器人状态到相机时间轴

### 9.2 场景二：两相机 + GelSight + 机器人位姿（不同频率）

- GelSight 通常频率低于相机/机器人（你也观察到了）。
- 是否要“同一时间帧”取决于训练数据格式：
  - 如果模型输入需要同时刻多模态：用时间戳做对齐，允许缺帧/插值
  - 如果模型允许异步：用各自时间戳，训练时做时间窗口融合

提高 GelSight 频率的一般方向（经验项）：
- 降分辨率、裁剪 ROI
- 调整曝光/帧率设置（如果驱动允许）
- 优化图像处理链路（避免 Python 单线程瓶颈，改 C++/多线程/用 GPU）
- 确保 USB 带宽充足（USB3、独占控制器、禁用省电）

### 9.3 控制接口（阻抗控制 / VR / 手柄）

- 阻抗控制通常要在实时线程里跑控制律（1kHz 级），VR/手柄输入属于低频“目标更新”：
  - **高频实时线程**：读取 RobotState、计算并输出控制（torque/pose 等）
  - **低频非实时线程**：读取 VR 输入、更新目标位姿/力参数，并用锁/无锁队列传给实时线程

---

## 10. 参考资料（原始链接）

- libfranka GitHub（README、Releases、安装说明）：
  - `https://github.com/frankarobotics/libfranka`
- FCI 文档（Linux 安装、实时内核、realtime 权限设置）：
  - `https://franka.cn/FCI/installation_linux.html`

---