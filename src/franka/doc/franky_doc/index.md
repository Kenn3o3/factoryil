<div id="top">

<div id="titlearea">

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><div id="projectname">
franky<span id="projectnumber"> 1.1.3</span>
</div>
<div id="projectbrief">
A High-Level Motion API for Franka
</div></td>
</tr>
</tbody>
</table>

</div>

<div id="main-nav">

</div>

</div>

<div id="MSearchSelectWindow" onmouseover="return searchBox.OnSearchSelectShow()" onmouseout="return searchBox.OnSearchSelectHide()" onkeydown="return searchBox.OnSearchSelectKey(event)">

</div>

<div id="MSearchResultsWindow">

<div id="MSearchResults">

<div class="SRPage">

<div id="SRIndex">

<div id="SRResults">

</div>

<div id="Loading" class="SRStatus">

Loading...

</div>

<div id="Searching" class="SRStatus">

Searching...

</div>

<div id="NoMatches" class="SRStatus">

No Matches

</div>

</div>

</div>

</div>

</div>

<div>

<div class="header">

<div class="headertitle">

<div class="title">

franky

</div>

</div>

</div>

<div class="contents">

<div class="textblock">

<span id="md__2home_2runner_2work_2franky_2franky_2_r_e_a_d_m_e" class="anchor"></span>

<div data-align="center">

![](https://raw.githubusercontent.com/timschneider42/franky/master/doc/logo.svg?sanitize=true)

### High-Level Control Library for Franka Robots with Python and C++ Support

</div>

<div data-align="center">

</div>

[![CI](https://github.com/timschneider42/franky/workflows/CI/badge.svg)](https://github.com/timschneider42/franky/actions)

[![Publish](https://github.com/timschneider42/franky/workflows/Publish/badge.svg)](https://github.com/timschneider42/franky/actions)

[![Issues](https://img.shields.io/github/issues/timschneider42/franky.svg)](https://github.com/timschneider42/franky/issues)

[![Releases](https://img.shields.io/github/v/release/timschneider42/franky.svg?include_prereleases&sort=semver)](https://github.com/timschneider42/franky/releases)

[![LGPL](https://img.shields.io/badge/license-LGPL-green.svg)](https://github.com/timschneider42/franky/blob/master/LICENSE)

franky is a high-level control library for Franka robots, offering Python and C++ support. By providing a high-level control interface, franky eliminates the need for strict real-time programming at 1 kHz, making control from non-real-time environments, such as Python programs, feasible. Instead of relying on low-level control commands, franky expects high-level position or velocity targets and uses [Ruckig](https://github.com/pantor/ruckig) to plan time-optimal trajectories in real-time.

Although Python does not provide real-time guarantees, franky strives to maintain as much real-time control as possible. Motions can be preempted at any moment, prompting franky to re-plan trajectories on the fly. To handle unforeseen situations—such as unexpected contact with the environment — franky includes a reaction system that allows for updating motion commands dynamically. Furthermore, most non-real-time functionality of [libfranka](https://frankarobotics.github.io/docs/libfranka/docs/index.md), such as Gripper control is made directly available in Python.

Check out the tutorial and the [examples](https://github.com/TimSchneider42/franky/tree/master/examples) for an introduction. The full documentation can be found at [https://timschneider42.github.io/franky/](index.md).

## 🚀 Features

  - **Control your Franka robot directly from Python in just a few lines\!** No more endless hours setting up ROS, juggling packages, or untangling dependencies. Just `pip install` — no ROS at all.
  - **[Four control modes](index.md#motion-types)**: Cartesian position, Cartesian velocity, Joint position, Joint velocity franky uses [Ruckig](https://github.com/pantor/ruckig) to generate smooth, time-optimal trajectories while respecting velocity, acceleration, and jerk limits.
  - **[Real-time control from Python and C++](index.md#real-time-motions)** Need to change the target while the robot’s moving? No problem. franky replans trajectories on the fly so that you can preempt motions anytime.
  - **Reactive behavior** Robots don’t always go according to plan. franky lets you define reactions to unexpected events—like contact with the environment — so you can change course in real-time.
  - **Motion and reaction callbacks** Want to monitor what’s happening under the hood? Add callbacks to your motions and reactions. They won’t block the control thread and are super handy for debugging or logging.
  - **Things are moving too fast? Tune the robot's dynamics to your needs** Adjust max velocity, acceleration, and jerk to match your setup or task. Fine control for smooth, safe operation.
  - **Full Python access to the libfranka API** Want to tweak impedance, read the robot state, set force thresholds, or mess with the Jacobian? Go for it. If libfranka supports it, chances are franky does, too.

## 📖 Python Quickstart Guide

Real-time kernel already installed and real-time permissions granted? Just install franky via

<div class="fragment">

<div class="line">

pip install franky-control

</div>

</div>

Otherwise, follow the [setup instructions](index.md#setup) first.

Now we are already ready to go\! Unlock the brakes in the web interface, activate FCI, and start coding:

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> \*

</div>

<div class="line">

</div>

<div class="line">

robot = Robot(<span class="stringliteral">"10.90.90.1"</span>) <span class="comment">\# Replace this with your robot's IP</span>

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Let's start slow (this lets the robot use a maximum of 5% of its velocity, acceleration, and jerk limits)</span>

</div>

<div class="line">

robot.relative\_dynamics\_factor = 0.05

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Move the robot 20cm along the relative X-axis of its end-effector</span>

</div>

<div class="line">

motion = CartesianMotion(Affine(\[0.2, 0.0, 0.0\]), ReferenceType.Relative)

</div>

<div class="line">

robot.move(motion)

</div>

</div>

If you are seeing server version mismatch errors, such as

<div class="fragment">

<div class="line">

franky.IncompatibleVersionException: libfranka: Incompatible library version (server version: 5, library version: 9)

</div>

</div>

then your Franka robot is either not on the most recent firmware version, or you are using the older Franka Panda model. In any case, it's no big deal; just check [here](https://frankarobotics.github.io/docs/compatibility.md) which libfranka version you need and follow our instructions to install the appropriate franky wheels.

## <span id="setup" class="anchor"></span> ⚙️ Setup

To install franky, you have to follow three steps:

1.  Ensure that you are using a real-time kernel
2.  Ensure that the executing user has permission to run real-time applications
3.  Install franky via pip or build it from source

### Installing a real-time kernel

In order for Franky to function properly, it requires the underlying OS to use a real-time kernel. Otherwise, you might see `communication_constrains_violation` errors.

To check whether your system is currently using a real-time kernel, type `uname -a`. You should see something like this:

<div class="fragment">

<div class="line">

$ uname -a

</div>

<div class="line">

Linux \[PCNAME\] 5.15.0-1056-realtime \#63-Ubuntu SMP PREEMPT\_RT ...

</div>

</div>

If it does not say PREEMPT\_RT, you are not currently running a real-time kernel.

There are multiple ways of installing a real-time kernel. You can [build it from source](https://frankarobotics.github.io/docs/libfranka/docs/real_time_kernel.md) or, if you are using Ubuntu, it can be [enabled through Ubuntu Pro](https://ubuntu.com/real-time).

### Allowing the executing user to run real-time applications

First, create a group `realtime` and add your user (or whoever is running franky) to this group:

<div class="fragment">

<div class="line">

sudo addgroup realtime

</div>

<div class="line">

sudo usermod -a -G realtime $(whoami)

</div>

</div>

Afterward, add the following limits to the real-time group in /etc/security/limits.conf:

<div class="fragment">

<div class="line">

@realtime soft rtprio 99

</div>

<div class="line">

@realtime soft priority 99

</div>

<div class="line">

@realtime soft memlock 102400

</div>

<div class="line">

@realtime hard rtprio 99

</div>

<div class="line">

@realtime hard priority 99

</div>

<div class="line">

@realtime hard memlock 102400

</div>

</div>

Log out and log in again to let the changes take effect.

To verify that the changes were applied, check if your user is in the `realtime` group:

<div class="fragment">

<div class="line">

$ groups

</div>

<div class="line">

... realtime

</div>

</div>

If real-time is not listed in your groups, try rebooting.

### Installing franky

To start using franky with Python and libfranka *0.16.0*, just install it via

<div class="fragment">

<div class="line">

pip install franky-control

</div>

</div>

We also provide wheels for libfranka versions *0.7.1*, *0.8.0*, *0.9.2*, *0.12.1*, *0.13.3*, *0.14.2*, *0.17.0*, and *0.18.0*. They can be installed via

<div class="fragment">

<div class="line">

VERSION=0-9-2

</div>

<div class="line">

wget https://github.com/TimSchneider42/franky/releases/latest/download/libfranka\_${VERSION}\_wheels.zip

</div>

<div class="line">

unzip libfranka\_${VERSION}\_wheels.zip

</div>

<div class="line">

pip install numpy

</div>

<div class="line">

pip install --no-index --find-links=./dist franky-control

</div>

</div>

### Using Docker

To use franky within Docker we provide a [Dockerfile](https://timschneider42.github.io/franky/docker/run/Dockerfile) and accompanying [docker-compose](https://timschneider42.github.io/franky/docker-compose.yml) file.

<div class="fragment">

<div class="line">

git clone --recurse-submodules https://github.com/timschneider42/franky.git

</div>

<div class="line">

cd franky/

</div>

<div class="line">

docker compose build franky-run

</div>

</div>

To use another version of libfranka than the default (0.16.0), add a build argument:

<div class="fragment">

<div class="line">

docker compose build franky-run --build-arg LIBFRANKA\_VERSION=0.9.2

</div>

</div>

To run the container:

<div class="fragment">

<div class="line">

docker compose run franky-run bash

</div>

</div>

The container requires access to the host machine's network *and* elevated user rights to allow the Docker user to set RT capabilities of the processes run from within it.

### Can I use CUDA jointly with franky?

Yes. However, you need to set `IGNORE_PREEMPT_RT_PRESENCE=1` during the installation and all subsequent updates of the CUDA drivers on the real-time kernel.

First, make sure that you have rebooted your system after installing the real-time kernel. Then, add `IGNORE_PREEMPT_RT_PRESENCE=1` to `/etc/environment`, call `export IGNORE_PREEMPT_RT_PRESENCE=1` to also set it in the current session, and follow the instructions of Nvidia to install CUDA on your system.

If you are on Ubuntu, you can also use [this](https://timschneider42.github.io/franky/tools/install_cuda_realtime.bash) script to install CUDA on your real-time system:

<div class="fragment">

<div class="line">

\# Download the script

</div>

<div class="line">

wget https://raw.githubusercontent.com/timschneider42/franky/master/tools/install\_cuda\_realtime.bash

</div>

<div class="line">

</div>

<div class="line">

\# Inspect the script to ensure it does what you expect

</div>

<div class="line">

</div>

<div class="line">

\# Make it executable

</div>

<div class="line">

chmod +x install\_cuda\_realtime.bash

</div>

<div class="line">

</div>

<div class="line">

\# Execute the script

</div>

<div class="line">

./install\_cuda\_realtime.bash

</div>

</div>

Alternatively, if you are a cowboy and do not care about security, you can also use this one-liner to directly call the script without checking it:

<div class="fragment">

<div class="line">

bash \<(wget -qO- https://raw.githubusercontent.com/timschneider42/franky/master/tools/install\_cuda\_realtime.bash)

</div>

</div>

### Is your robot connected to a different machine?

No problem\! There are two projects which let you run franky remotely via RPC with minimal effort: [franky-remote](https://github.com/kvasios/franky-remote) and [net\_franky](https://github.com/yblei/net_franky).

Please note that I’m not involved in the development of these projects, so I cannot take any liability for its use. If you decide to use it, please ensure that you credit the developers of these projects for their work.

### Building franky

franky is based on [libfranka](https://github.com/frankarobotics/libfranka), [Eigen](https://eigen.tuxfamily.org) for transformation calculations and [pybind11](https://github.com/pybind/pybind11) for the Python bindings. As the Franka is sensitive to acceleration discontinuities, it requires jerk-constrained motion generation, for which franky uses the [Ruckig](https://ruckig.com) community version for Online Trajectory Generation (OTG).

After installing the dependencies (the exact versions can be found here), you can build and install franky via

<div class="fragment">

<div class="line">

git clone --recurse-submodules git@github.com:timschneider42/franky.git

</div>

<div class="line">

cd franky

</div>

<div class="line">

mkdir -p build

</div>

<div class="line">

cd build

</div>

<div class="line">

cmake -DCMAKE\_BUILD\_TYPE=Release ..

</div>

<div class="line">

make

</div>

<div class="line">

make install

</div>

</div>

To use franky, you can also include it as a subproject in your parent CMake via `add_subdirectory(franky)` and then `target_link_libraries(<target> franky)`.

If you need only the Python module, you can install franky via

<div class="fragment">

<div class="line">

pip install .

</div>

</div>

Make sure that the built library `_franky.cpython-3**-****-linux-gnu.so` is in the Python path, e.g. by adjusting `PYTHONPATH` accordingly.

#### Building franky with Docker

For building franky and its wheels, we provide another Docker container that can also be launched using docker-compose:

<div class="fragment">

<div class="line">

docker compose build franky-build

</div>

<div class="line">

docker compose run --rm franky-build run-tests \# To run the tests

</div>

<div class="line">

docker compose run --rm franky-build build-wheels \# To build wheels for all supported python versions

</div>

</div>

## 📚 Tutorial

franky comes with both a C++ and Python API that differ only regarding real-time capability. We will introduce both languages next to each other. In your C++ project, just include `include <franky.hpp>` and link the library. For Python, just `import franky`. As a first example, only four lines of code are needed for simple robotic motions.

<div class="fragment">

<div class="line">

\++

</div>

<div class="line">

<span class="preprocessor">\#include \<[franky.hpp](franky_8hpp.md)\></span>

</div>

<div class="line">

<span class="keyword">using namespace </span>[franky](namespacefranky.md);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Connect to the robot with the FCI IP address</span>

</div>

<div class="line">

[Robot](classfranky_1_1_robot.md) robot(<span class="stringliteral">"10.90.90.1"</span>);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Reduce velocity and acceleration of the robot</span>

</div>

<div class="line">

robot.setRelativeDynamicsFactor(0.05);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Move the end-effector 20cm in positive x-direction</span>

</div>

<div class="line">

<span class="keyword">auto</span> motion = std::make\_shared\<CartesianMotion\>([RobotPose](classfranky_1_1_robot_pose.md)([Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)({0.2, 0.0, 0.0}), 0.0), ReferenceType::Relative);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Finally move the robot</span>

</div>

<div class="line">

robot.move(motion);

</div>

<div id="aclassfranky_1_1_robot_html" class="ttc">

<div class="ttname">

[franky::Robot](classfranky_1_1_robot.md)

</div>

<div class="ttdoc">

A class representing a Franka robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:47

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html" class="ttc">

<div class="ttname">

[franky::RobotPose](classfranky_1_1_robot_pose.md)

</div>

<div class="ttdoc">

Cartesian pose of a robot.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:19

</div>

</div>

<div id="afranky_8hpp_html" class="ttc">

<div class="ttname">

[franky.hpp](franky_8hpp.md)

</div>

</div>

<div id="anamespacefranky_html" class="ttc">

<div class="ttname">

[franky](namespacefranky.md)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:8

</div>

</div>

<div id="anamespacefranky_html_afab9faf133666ada543b15236a8c4b5f" class="ttc">

<div class="ttname">

[franky::Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)

</div>

<div class="ttdeci">

Eigen::Affine3d Affine

</div>

<div class="ttdef">

**Definition** types.hpp:15

</div>

</div>

</div>

The corresponding program in Python is

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> Affine, CartesianMotion, Robot, ReferenceType

</div>

<div class="line">

</div>

<div class="line">

robot = Robot(<span class="stringliteral">"10.90.90.1"</span>)

</div>

<div class="line">

robot.relative\_dynamics\_factor = 0.05

</div>

<div class="line">

</div>

<div class="line">

motion = CartesianMotion(Affine(\[0.2, 0.0, 0.0\]), ReferenceType.Relative)

</div>

<div class="line">

robot.move(motion)

</div>

</div>

Before executing any code, make sure that you have enabled the Franka Control Interface (FCI) in the Franka UI web interface.

Furthermore, we will introduce methods for geometric calculations, for moving the robot according to different motion types, how to implement real-time reactions and changing waypoints in real time, as well as controlling the gripper.

### 🧮 Geometry

`franky.Affine` is a python wrapper for [Eigen::Affine3d](https://eigen.tuxfamily.org/dox/group__TutorialGeometry.md). It is used for Cartesian poses, frames and transformation. franky adds its own constructor, which takes a position and a quaternion as inputs:

<div class="fragment">

<div class="line">

<span class="keyword">import</span> math

</div>

<div class="line">

<span class="keyword">from</span> scipy.spatial.transform <span class="keyword">import</span> Rotation

</div>

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> Affine

</div>

<div class="line">

</div>

<div class="line">

z\_translation = Affine(\[0.0, 0.0, 0.5\])

</div>

<div class="line">

</div>

<div class="line">

quat = Rotation.from\_euler(<span class="stringliteral">"xyz"</span>, \[0, 0, math.pi / 2\]).as\_quat()

</div>

<div class="line">

z\_rotation = Affine(\[0.0, 0.0, 0.0\], quat)

</div>

<div class="line">

</div>

<div class="line">

combined\_transformation = z\_translation \* z\_rotation

</div>

</div>

In all cases, distances are in \[m\] and rotations in \[rad\].

### 🤖 Robot

franky exposes most of the libfanka API for Python. Moreover, we added methods to adapt the dynamic limits of the robot for all motions.

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> \*

</div>

<div class="line">

</div>

<div class="line">

robot = Robot(<span class="stringliteral">"10.90.90.1"</span>)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Recover from errors</span>

</div>

<div class="line">

robot.recover\_from\_errors()

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Set velocity, acceleration, and jerk to 5% of the maximum</span>

</div>

<div class="line">

robot.relative\_dynamics\_factor = 0.05

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Alternatively, you can define each constraint individually</span>

</div>

<div class="line">

robot.relative\_dynamics\_factor = RelativeDynamicsFactor(

</div>

<div class="line">

velocity=0.1, acceleration=0.05, jerk=0.1

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Or, for more fine-grained access, set individual limits</span>

</div>

<div class="line">

robot.translation\_velocity\_limit.set(3.0)

</div>

<div class="line">

robot.rotation\_velocity\_limit.set(2.5)

</div>

<div class="line">

robot.elbow\_velocity\_limit.set(2.62)

</div>

<div class="line">

robot.translation\_acceleration\_limit.set(9.0)

</div>

<div class="line">

robot.rotation\_acceleration\_limit.set(17.0)

</div>

<div class="line">

robot.elbow\_acceleration\_limit.set(10.0)

</div>

<div class="line">

robot.translation\_jerk\_limit.set(4500.0)

</div>

<div class="line">

robot.rotation\_jerk\_limit.set(8500.0)

</div>

<div class="line">

robot.elbow\_jerk\_limit.set(5000.0)

</div>

<div class="line">

robot.joint\_velocity\_limit.set(\[2.62, 2.62, 2.62, 2.62, 5.26, 4.18, 5.26\])

</div>

<div class="line">

robot.joint\_acceleration\_limit.set(\[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0\])

</div>

<div class="line">

robot.joint\_jerk\_limit.set(\[5000.0, 5000.0, 5000.0, 5000.0, 5000.0, 5000.0, 5000.0\])

</div>

<div class="line">

<span class="comment">\# By default, these limits are set to their respective maxima (the values shown here)</span>

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Get the max of each limit (as provided by Franka) with the max function, e.g.:</span>

</div>

<div class="line">

print(robot.joint\_jerk\_limit.max)

</div>

</div>

#### Robot State

The robot state can be retrieved by accessing the following properties:

  - `state`: Object of type `franky.RobotState`, which extends the libfranka [franka::RobotState](https://frankarobotics.github.io/libfranka/0.15.3/structfranka_1_1RobotState.md) structure by additional state elements.
  - `current_cartesian_state`: Object of type `franky.CartesianState`, which contains the end-effector pose and velocity obtained from [franka::RobotState::O\_T\_EE](https://frankarobotics.github.io/libfranka/0.15.3/structfranka_1_1RobotState.md#a193781d47722b32925e0ea7ac415f442) and [franka::RobotState::O\_dP\_EE\_c](https://frankarobotics.github.io/libfranka/0.15.3/structfranka_1_1RobotState.md#a4be112bd1a9a7d777a67aea4a18a8dcc).
  - `current_joint_state`: Object of type `franky.JointState`, which contains the joint positions and velocities obtained from [franka::RobotState::q](https://frankarobotics.github.io/libfranka/0.15.3/structfranka_1_1RobotState.md#ade3335d1ac2f6c44741a916d565f7091) and [franka::RobotState::dq](https://frankarobotics.github.io/libfranka/0.15.3/structfranka_1_1RobotState.md#a706045af1b176049e9e56df755325bd2).

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> \*

</div>

<div class="line">

</div>

<div class="line">

robot = Robot(<span class="stringliteral">"10.90.90.1"</span>)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Get the current state as \`franky.RobotState\`. See the documentation for a list of fields.</span>

</div>

<div class="line">

state = robot.state

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Get the robot's cartesian state</span>

</div>

<div class="line">

cartesian\_state = robot.current\_cartesian\_state

</div>

<div class="line">

robot\_pose = cartesian\_state.pose <span class="comment">\# Contains end-effector pose and elbow position</span>

</div>

<div class="line">

ee\_pose = robot\_pose.end\_effector\_pose

</div>

<div class="line">

elbow\_pos = robot\_pose.elbow\_state

</div>

<div class="line">

robot\_velocity = cartesian\_state.velocity <span class="comment">\# Contains end-effector twist and elbow velocity</span>

</div>

<div class="line">

ee\_twist = robot\_velocity.end\_effector\_twist

</div>

<div class="line">

elbow\_vel = robot\_velocity.elbow\_velocity

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Get the robot's joint state</span>

</div>

<div class="line">

joint\_state = robot.current\_joint\_state

</div>

<div class="line">

joint\_pos = joint\_state.position

</div>

<div class="line">

joint\_vel = joint\_state.velocity

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Use the robot model to compute kinematics</span>

</div>

<div class="line">

q = \[-0.3, 0.1, 0.3, -1.4, 0.1, 1.8, 0.7\]

</div>

<div class="line">

f\_t\_ee = Affine()

</div>

<div class="line">

ee\_t\_k = Affine()

</div>

<div class="line">

ee\_pose\_kin = robot.model.pose(Frame.EndEffector, q, f\_t\_ee, ee\_t\_k)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Get the Jacobian of the current robot state</span>

</div>

<div class="line">

jacobian = robot.model.body\_jacobian(Frame.EndEffector, state)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Alternatively, just get the URDF as a string and do the kinematics computation yourself (only</span>

</div>

<div class="line">

<span class="comment">\# for libfranka \>= 0.15.0)</span>

</div>

<div class="line">

urdf\_model = robot.model\_urdf

</div>

</div>

For a full list of state-related features, check the [Robot](classfranky_1_1_robot.md) and [Model](classfranky_1_1_model.md) sections of the documentation.

### <span id="motion-types" class="anchor"></span> 🏃‍♂️ Motion Types

franky currently supports four different impedance control modes: **joint position control**, **joint velocity control**, **cartesian position control**, and **cartesian velocity control**. Each of these control modes is invoked by passing the robot an appropriate *Motion* object.

In the following, we provide a brief example for each motion type implemented by franky in Python. The C++ interface is generally analogous, though some variable and method names are different because we follow [PEP 8](https://peps.python.org/pep-0008/) naming conventions in Python and [Google naming conventions](https://google.github.io/styleguide/cppguide.md) in C++.

All units are in $m$, $\\frac{m}{s}$, $\\textit{rad}$, or $\\frac{\\textit{rad}}{s}$.

#### Joint Position Control

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> \*

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# A point-to-point motion in the joint space</span>

</div>

<div class="line">

m\_jp1 = JointMotion(\[-0.3, 0.1, 0.3, -1.4, 0.1, 1.8, 0.7\])

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# A motion in joint space with multiple waypoints. The robot will stop at each of these</span>

</div>

<div class="line">

<span class="comment">\# waypoints. If you want the robot to move continuously, you have to specify a target velocity</span>

</div>

<div class="line">

<span class="comment">\# at every waypoint as shown in the example following this one.</span>

</div>

<div class="line">

m\_jp2 = JointWaypointMotion(

</div>

<div class="line">

\[

</div>

<div class="line">

JointWaypoint(\[-0.3, 0.1, 0.3, -1.4, 0.1, 1.8, 0.7\]),

</div>

<div class="line">

JointWaypoint(\[0.0, 0.3, 0.3, -1.5, -0.2, 1.5, 0.8\]),

</div>

<div class="line">

JointWaypoint(\[0.1, 0.4, 0.3, -1.4, -0.3, 1.7, 0.9\]),

</div>

<div class="line">

\]

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Intermediate waypoints also permit specifying target velocities. The default target velocity</span>

</div>

<div class="line">

<span class="comment">\# is 0, meaning that the robot will stop at every waypoint.</span>

</div>

<div class="line">

m\_jp3 = JointWaypointMotion(

</div>

<div class="line">

\[

</div>

<div class="line">

JointWaypoint(\[-0.3, 0.1, 0.3, -1.4, 0.1, 1.8, 0.7\]),

</div>

<div class="line">

JointWaypoint(

</div>

<div class="line">

JointState(

</div>

<div class="line">

position=\[0.0, 0.3, 0.3, -1.5, -0.2, 1.5, 0.8\],

</div>

<div class="line">

velocity=\[0.1, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0\],

</div>

<div class="line">

)

</div>

<div class="line">

),

</div>

<div class="line">

JointWaypoint(\[0.1, 0.4, 0.3, -1.4, -0.3, 1.7, 0.9\]),

</div>

<div class="line">

\]

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Stop the robot in joint position control mode. The difference between JointStopMotion to other</span>

</div>

<div class="line">

<span class="comment">\# stop-motions, such as CartesianStopMotion, is that JointStopMotion stops the robot in joint</span>

</div>

<div class="line">

<span class="comment">\# position control mode while CartesianStopMotion stops it in cartesian pose control mode. The</span>

</div>

<div class="line">

<span class="comment">\# difference becomes relevant when asynchronous move commands are being sent or reactions are</span>

</div>

<div class="line">

<span class="comment">\# being used(see below).</span>

</div>

<div class="line">

m\_jp4 = JointStopMotion()

</div>

</div>

#### Joint Velocity Control

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> \*

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Accelerate to the given joint velocity and hold it. After 1000ms, stop the robot again.</span>

</div>

<div class="line">

m\_jv1 = JointVelocityMotion(

</div>

<div class="line">

\[0.1, 0.3, -0.1, 0.0, 0.1, -0.2, 0.4\], duration=Duration(1000)

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Joint velocity motions also support waypoints. Unlike in joint position control, a joint</span>

</div>

<div class="line">

<span class="comment">\# velocity waypoint is a target velocity to be reached. This particular example first</span>

</div>

<div class="line">

<span class="comment">\# accelerates the joints, holds the velocity for 1s, then reverses direction for 2s, reverses</span>

</div>

<div class="line">

<span class="comment">\# direction again for 1s, and finally stops. It is important not to forget to stop the robot</span>

</div>

<div class="line">

<span class="comment">\# at the end of such a sequence, as it will otherwise throw an error.</span>

</div>

<div class="line">

m\_jv2 = JointVelocityWaypointMotion(

</div>

<div class="line">

\[

</div>

<div class="line">

JointVelocityWaypoint(

</div>

<div class="line">

\[0.1, 0.3, -0.1, 0.0, 0.1, -0.2, 0.4\], hold\_target\_duration=Duration(1000)

</div>

<div class="line">

),

</div>

<div class="line">

JointVelocityWaypoint(

</div>

<div class="line">

\[-0.1, -0.3, 0.1, -0.0, -0.1, 0.2, -0.4\],

</div>

<div class="line">

hold\_target\_duration=Duration(2000),

</div>

<div class="line">

),

</div>

<div class="line">

JointVelocityWaypoint(

</div>

<div class="line">

\[0.1, 0.3, -0.1, 0.0, 0.1, -0.2, 0.4\], hold\_target\_duration=Duration(1000)

</div>

<div class="line">

),

</div>

<div class="line">

JointVelocityWaypoint(\[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0\]),

</div>

<div class="line">

\]

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Stop the robot in joint velocity control mode.</span>

</div>

<div class="line">

m\_jv3 = JointVelocityStopMotion()

</div>

</div>

#### Cartesian Position Control

<div class="fragment">

<div class="line">

<span class="keyword">import</span> math

</div>

<div class="line">

<span class="keyword">from</span> scipy.spatial.transform <span class="keyword">import</span> Rotation

</div>

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> \*

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Move to the given target pose</span>

</div>

<div class="line">

quat = Rotation.from\_euler(<span class="stringliteral">"xyz"</span>, \[0, 0, math.pi / 2\]).as\_quat()

</div>

<div class="line">

m\_cp1 = CartesianMotion(Affine(\[0.4, -0.2, 0.3\], quat))

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# With target elbow angle (otherwise, the Franka firmware will choose by itself)</span>

</div>

<div class="line">

m\_cp2 = CartesianMotion(

</div>

<div class="line">

RobotPose(Affine(\[0.4, -0.2, 0.3\], quat), elbow\_state=ElbowState(0.3))

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# A linear motion in Cartesian space relative to the initial position</span>

</div>

<div class="line">

<span class="comment">\# (Note that this motion is relative both in position and orientation. Hence, when the robot's</span>

</div>

<div class="line">

<span class="comment">\# end-effector is oriented differently, it will move in a different direction)</span>

</div>

<div class="line">

m\_cp3 = CartesianMotion(Affine(\[0.2, 0.0, 0.0\]), ReferenceType.Relative)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Generalization of CartesianMotion that allows for multiple waypoints. The robot will stop at</span>

</div>

<div class="line">

<span class="comment">\# each of these waypoints. If you want the robot to move continuously, you have to specify a</span>

</div>

<div class="line">

<span class="comment">\# target velocity at every waypoint as shown in the example following this one.</span>

</div>

<div class="line">

m\_cp4 = CartesianWaypointMotion(

</div>

<div class="line">

\[

</div>

<div class="line">

CartesianWaypoint(

</div>

<div class="line">

RobotPose(Affine(\[0.4, -0.2, 0.3\], quat), elbow\_state=ElbowState(0.3))

</div>

<div class="line">

),

</div>

<div class="line">

<span class="comment">\# The following waypoint is relative to the prior one and 50% slower</span>

</div>

<div class="line">

CartesianWaypoint(

</div>

<div class="line">

Affine(\[0.2, 0.0, 0.0\]),

</div>

<div class="line">

ReferenceType.Relative,

</div>

<div class="line">

RelativeDynamicsFactor(0.5, 1.0, 1.0),

</div>

<div class="line">

),

</div>

<div class="line">

\]

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Cartesian waypoints permit specifying target velocities</span>

</div>

<div class="line">

m\_cp5 = CartesianWaypointMotion(

</div>

<div class="line">

\[

</div>

<div class="line">

CartesianWaypoint(Affine(\[0.5, -0.2, 0.3\], quat)),

</div>

<div class="line">

CartesianWaypoint(

</div>

<div class="line">

CartesianState(

</div>

<div class="line">

pose=Affine(\[0.4, -0.1, 0.3\], quat), velocity=Twist(\[-0.01, 0.01, 0.0\])

</div>

<div class="line">

)

</div>

<div class="line">

),

</div>

<div class="line">

CartesianWaypoint(Affine(\[0.3, 0.0, 0.3\], quat)),

</div>

<div class="line">

\]

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Stop the robot in Cartesian position control mode.</span>

</div>

<div class="line">

m\_cp6 = CartesianStopMotion()

</div>

</div>

#### Cartesian Velocity Control

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> \*

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# A Cartesian velocity motion with linear (first argument) and angular (second argument)</span>

</div>

<div class="line">

<span class="comment">\# components</span>

</div>

<div class="line">

m\_cv1 = CartesianVelocityMotion(Twist(\[0.2, -0.1, 0.1\], \[0.1, -0.1, 0.2\]))

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# With target elbow velocity</span>

</div>

<div class="line">

m\_cv2 = CartesianVelocityMotion(

</div>

<div class="line">

RobotVelocity(Twist(\[0.2, -0.1, 0.1\], \[0.1, -0.1, 0.2\]), elbow\_velocity=-0.2)

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Cartesian velocity motions also support multiple waypoints. Unlike in Cartesian position</span>

</div>

<div class="line">

<span class="comment">\# control, a Cartesian velocity waypoint is a target velocity to be reached. This particular</span>

</div>

<div class="line">

<span class="comment">\# example first accelerates the end-effector, holds the velocity for 1s, then reverses</span>

</div>

<div class="line">

<span class="comment">\# direction for 2s, reverses direction again for 1s, and finally stops. It is important not to</span>

</div>

<div class="line">

<span class="comment">\# forget to stop the robot at the end of such a sequence, as it will otherwise throw an error.</span>

</div>

<div class="line">

m\_cv4 = CartesianVelocityWaypointMotion(

</div>

<div class="line">

\[

</div>

<div class="line">

CartesianVelocityWaypoint(

</div>

<div class="line">

Twist(\[0.2, -0.1, 0.1\], \[0.1, -0.1, 0.2\]),

</div>

<div class="line">

hold\_target\_duration=Duration(1000),

</div>

<div class="line">

),

</div>

<div class="line">

CartesianVelocityWaypoint(

</div>

<div class="line">

Twist(\[-0.2, 0.1, -0.1\], \[-0.1, 0.1, -0.2\]),

</div>

<div class="line">

hold\_target\_duration=Duration(2000),

</div>

<div class="line">

),

</div>

<div class="line">

CartesianVelocityWaypoint(

</div>

<div class="line">

Twist(\[0.2, -0.1, 0.1\], \[0.1, -0.1, 0.2\]),

</div>

<div class="line">

hold\_target\_duration=Duration(1000),

</div>

<div class="line">

),

</div>

<div class="line">

CartesianVelocityWaypoint(Twist()),

</div>

<div class="line">

\]

</div>

<div class="line">

)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Stop the robot in Cartesian velocity control mode.</span>

</div>

<div class="line">

m\_cv6 = CartesianVelocityStopMotion()

</div>

</div>

#### Relative Dynamics Factors

Every motion and waypoint type allows for adapting the dynamics (velocity, acceleration, and jerk) by setting the respective `relative_dynamics_factor` parameter. This parameter can also be set for the robot globally, as shown below, or in the `robot.move` command. Crucially, relative dynamics factors on different layers (robot, move command, and motion) do not override each other but rather get multiplied. Hence, a relative dynamics factor on a motion can only reduce the dynamics of the robot and never increase them.

There is one exception to this rule, and that is if any layer sets the relative dynamics factor to `RelativeDynamicsFactor.MAX_DYNAMICS`. This will cause the motion to be executed with maximum velocity, acceleration, and jerk limits, independently of the relative dynamics factors of the other layers. This feature should only be used to abruptly stop the robot in case of an unexpected environment contact, as executing Other motions with it are likely to lead to a discontinuity error and might be dangerous.

#### Executing Motions

The real robot can be moved by applying a motion to the robot using `move`:

<div class="fragment">

<div class="line">

<span class="comment">\# Before moving the robot, set an appropriate dynamics factor. We start small:</span>

</div>

<div class="line">

robot.relative\_dynamics\_factor = 0.05

</div>

<div class="line">

<span class="comment">\# or alternatively, to control the scaling of velocity, acceleration, and jerk limits</span>

</div>

<div class="line">

<span class="comment">\# separately:</span>

</div>

<div class="line">

robot.relative\_dynamics\_factor = RelativeDynamicsFactor(0.05, 0.1, 0.15)

</div>

<div class="line">

<span class="comment">\# If these values are set too high, you will see discontinuity errors</span>

</div>

<div class="line">

</div>

<div class="line">

robot.move(m\_jp1)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# We can also set a relative dynamics factor in the move command. It will be multiplied by</span>

</div>

<div class="line">

<span class="comment">\# the other relative dynamics factors (robot and motion if present).</span>

</div>

<div class="line">

robot.move(m\_jp2, relative\_dynamics\_factor=0.8)

</div>

</div>

#### Motion Callbacks

All motions support callbacks, which will be invoked in every control step at 1kHz. Callbacks can be attached as follows:

<div class="fragment">

<div class="line">

<span class="keyword">def </span>cb(

</div>

<div class="line">

robot\_state: RobotState,

</div>

<div class="line">

time\_step: Duration,

</div>

<div class="line">

rel\_time: Duration,

</div>

<div class="line">

abs\_time: Duration,

</div>

<div class="line">

control\_signal: JointPositions,

</div>

<div class="line">

):

</div>

<div class="line">

print(f<span class="stringliteral">"At time {abs\_time}, the target joint positions were {control\_signal.q}"</span>)

</div>

<div class="line">

</div>

<div class="line">

</div>

<div class="line">

m\_jp1.register\_callback(cb)

</div>

<div class="line">

robot.move(m\_jp1)

</div>

</div>

Note that in Python, these callbacks are not executed in the control thread since they would otherwise block it. Instead, they are put in a queue and executed by another thread. While this scheme ensures that the control thread can always run, it cannot prevent the queue from growing indefinitely when the callbacks take more time to execute than it takes for new callbacks to be queued. Hence, callbacks might be executed significantly after they were queued if they take a long time to execute.

### ⚡ Real-Time Reactions

By adding reactions to the motion data, the robot can react to unforeseen events. In the Python API, you can define conditions by using a comparison between a robot's value and a given threshold. If the threshold is exceeded, the reaction fires.

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> CartesianMotion, Affine, ReferenceType, Measure, Reaction

</div>

<div class="line">

</div>

<div class="line">

motion = CartesianMotion(Affine(\[0.0, 0.0, 0.1\]), ReferenceType.Relative) <span class="comment">\# Move down 10cm</span>

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# It is important that the reaction motion uses the same control mode as the original motion.</span>

</div>

<div class="line">

<span class="comment">\# Hence, we cannot register a JointMotion as a reaction motion to a CartesianMotion.</span>

</div>

<div class="line">

<span class="comment">\# Move up by 1cm</span>

</div>

<div class="line">

reaction\_motion = CartesianMotion(Affine(\[0.0, 0.0, -0.01\]), ReferenceType.Relative)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Trigger reaction if the Z force is greater than 30N</span>

</div>

<div class="line">

reaction = Reaction(Measure.FORCE\_Z \> 5.0, reaction\_motion)

</div>

<div class="line">

motion.add\_reaction(reaction)

</div>

<div class="line">

</div>

<div class="line">

robot.move(motion)

</div>

</div>

Possible values to measure are

  - `Measure.FORCE_X,` `Measure.FORCE_Y,` `Measure.FORCE_Z`: Force in X, Y and Z direction
  - `Measure.REL_TIME`: Time in seconds since the current motion started
  - `Measure.ABS_TIME`: Time in seconds since the initial motion started

The difference between `Measure.REL_TIME` and `Measure.ABS_TIME` is that `Measure.REL_TIME` is reset to zero whenever a new motion starts (either by calling `Robot.move` or as a result of a triggered `Reaction`). `Measure.ABS_TIME`, on the other hand, is only reset to zero when a motion terminates regularly without being interrupted and the robot stops moving. Hence, `Measure.ABS_TIME` measures the total time in which the robot has moved without interruption.

`Measure` values support all classical arithmetic operations, like addition, subtraction, multiplication, division, and exponentiation (both as base and exponent).

<div class="fragment">

<div class="line">

normal\_force = (Measure.FORCE\_X \*\* 2 + Measure.FORCE\_Y \*\* 2 + Measure.FORCE\_Z \*\* 2) \*\* 0.5

</div>

</div>

With arithmetic comparisons, conditions can be generated.

<div class="fragment">

<div class="line">

normal\_force\_within\_bounds = normal\_force \< 30.0

</div>

<div class="line">

time\_up = Measure.ABS\_TIME \> 10.0

</div>

</div>

Conditions support negation, conjunction (and), and disjunction (or):

<div class="fragment">

<div class="line">

abort = \~normal\_force\_within\_bounds | time\_up

</div>

<div class="line">

fast\_abort = \~normal\_force\_within\_bounds | time\_up

</div>

</div>

To check whether a reaction has fired, a callback can be attached:

<div class="fragment">

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> RobotState

</div>

<div class="line">

</div>

<div class="line">

</div>

<div class="line">

<span class="keyword">def </span>reaction\_callback(robot\_state: RobotState, rel\_time: float, abs\_time: float):

</div>

<div class="line">

print(f<span class="stringliteral">"Reaction fired at {abs\_time}."</span>)

</div>

<div class="line">

</div>

<div class="line">

</div>

<div class="line">

reaction.register\_callback(reaction\_callback)

</div>

</div>

Similar to the motion callbacks, in Python, reaction callbacks are not executed in real-time but in a regular thread with lower priority to ensure that the control thread does not get blocked. Thus, the callbacks might fire substantially after the reaction has fired, depending on the time it takes to execute them.

In C++, you can additionally use lambdas to define more complex behaviours:

<div class="fragment">

<div class="line">

\++

</div>

<div class="line">

<span class="keyword">auto</span> motion = [CartesianMotion](classfranky_1_1_cartesian_motion.md)(

</div>

<div class="line">

[RobotPose](classfranky_1_1_robot_pose.md)([Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)({0.0, 0.0, 0.2}), 0.0), ReferenceType::Relative);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Stop motion if force is over 10N</span>

</div>

<div class="line">

<span class="keyword">auto</span> stop\_motion = [StopMotion\<franka::CartesianPose\>](classfranky_1_1_stop_motion.md)()

</div>

<div class="line">

</div>

<div class="line">

motion

</div>

<div class="line">

.addReaction(

</div>

<div class="line">

[Reaction](classfranky_1_1_reaction.md)(

</div>

<div class="line">

[Measure](classfranky_1_1_measure.md)::ForceZ() \> 10.0, <span class="comment">// \[N\],</span>

</div>

<div class="line">

stop\_motion))

</div>

<div class="line">

.addReaction(

</div>

<div class="line">

[Reaction](classfranky_1_1_reaction.md)(

</div>

<div class="line">

[Condition](classfranky_1_1_condition.md)(

</div>

<div class="line">

\[\](const franka::[RobotState](structfranky_1_1_robot_state.md)& state, <span class="keywordtype">double</span> rel\_time, <span class="keywordtype">double</span> abs\_time) {

</div>

<div class="line">

<span class="comment">// Lambda condition</span>

</div>

<div class="line">

<span class="keywordflow">return</span> state.current\_errors.self\_collision\_avoidance\_violation;

</div>

<div class="line">

}),

</div>

<div class="line">

\[\](<span class="keyword">const</span> franka::RobotState& state, <span class="keywordtype">double</span> rel\_time, <span class="keywordtype">double</span> abs\_time) {

</div>

<div class="line">

<span class="comment">// Lambda reaction motion generator</span>

</div>

<div class="line">

<span class="comment">// (we are just returning a stop motion, but there could be arbitrary</span>

</div>

<div class="line">

<span class="comment">// logic here for generating reaction motions)</span>

</div>

<div class="line">

<span class="keywordflow">return</span> [StopMotion\<franka::CartesianPose\>](classfranky_1_1_stop_motion.md)();

</div>

<div class="line">

})

</div>

<div class="line">

));

</div>

<div class="line">

</div>

<div class="line">

robot.move(motion)

</div>

<div id="aclassfranky_1_1_cartesian_motion_html" class="ttc">

<div class="ttname">

[franky::CartesianMotion](classfranky_1_1_cartesian_motion.md)

</div>

<div class="ttdoc">

Cartesian motion with a single target.

</div>

<div class="ttdef">

**Definition** cartesian\_motion.hpp:11

</div>

</div>

<div id="aclassfranky_1_1_condition_html" class="ttc">

<div class="ttname">

[franky::Condition](classfranky_1_1_condition.md)

</div>

<div class="ttdoc">

A condition on the robot state.

</div>

<div class="ttdef">

**Definition** condition.hpp:16

</div>

</div>

<div id="aclassfranky_1_1_measure_html" class="ttc">

<div class="ttname">

[franky::Measure](classfranky_1_1_measure.md)

</div>

<div class="ttdoc">

A measure on the robot state.

</div>

<div class="ttdef">

**Definition** measure.hpp:20

</div>

</div>

<div id="aclassfranky_1_1_reaction_html" class="ttc">

<div class="ttname">

[franky::Reaction](classfranky_1_1_reaction.md)

</div>

<div class="ttdoc">

A reaction that can be attached to a motion.

</div>

<div class="ttdef">

**Definition** reaction.hpp:27

</div>

</div>

<div id="aclassfranky_1_1_stop_motion_html" class="ttc">

<div class="ttname">

[franky::StopMotion](classfranky_1_1_stop_motion.md)

</div>

<div class="ttdef">

**Definition** stop\_motion.hpp:12

</div>

</div>

<div id="astructfranky_1_1_robot_state_html" class="ttc">

<div class="ttname">

[franky::RobotState](structfranky_1_1_robot_state.md)

</div>

<div class="ttdoc">

Full state of the robot.

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:23

</div>

</div>

</div>

### <span id="real-time-motions" class="anchor"></span> ⏱️ Real-Time Motions

By setting the `asynchronous` parameter of `Robot.move` to `True`, the function does not block until the motion finishes. Instead, it returns immediately and, thus, allows the main thread to set new motions asynchronously.

<div class="fragment">

<div class="line">

<span class="keyword">import</span> time

</div>

<div class="line">

<span class="keyword">from</span> franky <span class="keyword">import</span> Affine, CartesianMotion, Robot, ReferenceType

</div>

<div class="line">

</div>

<div class="line">

robot = Robot(<span class="stringliteral">"10.90.90.1"</span>)

</div>

<div class="line">

robot.relative\_dynamics\_factor = 0.05

</div>

<div class="line">

</div>

<div class="line">

motion1 = CartesianMotion(Affine(\[0.2, 0.0, 0.0\]), ReferenceType.Relative)

</div>

<div class="line">

robot.move(motion1, asynchronous=<span class="keyword">True</span>)

</div>

<div class="line">

</div>

<div class="line">

time.sleep(0.5)

</div>

<div class="line">

<span class="comment">\# Note that, similar to reactions, when preempting active motions with new motions, the</span>

</div>

<div class="line">

<span class="comment">\# control mode cannot change. Hence, we cannot use, e.g., a JointMotion here.</span>

</div>

<div class="line">

motion2 = CartesianMotion(Affine(\[0.2, 0.0, 0.0\]), ReferenceType.Relative)

</div>

<div class="line">

robot.move(motion2, asynchronous=<span class="keyword">True</span>)

</div>

</div>

By calling `Robot.join_motion`, the main thread can be synchronized with the motion thread, as it will block until the robot finishes its motion.

<div class="fragment">

<div class="line">

robot.join\_motion()

</div>

</div>

Note that when exceptions occur during the asynchronous execution of a motion, they will not be thrown immediately. Instead, the control thread stores the exception and terminates. The next time `Robot.join_motion` or `Robot.move` is called, they will throw the stored exception in the main thread. Hence, after an asynchronous motion has finished, make sure to call `Robot.join_motion` to ensure being notified of any exceptions that occurred during the motion.

### <span id="gripper" class="anchor"></span> 👌 Gripper

In the `franky::Gripper` class, the default gripper force and gripper speed can be set. Then, in addition to the libfranka commands, the following helper methods can be used:

<div class="fragment">

<div class="line">

\++

</div>

<div class="line">

<span class="preprocessor">\#include \<[franky.hpp](franky_8hpp.md)\></span>

</div>

<div class="line">

<span class="preprocessor">\#include \<chrono\></span>

</div>

<div class="line">

<span class="preprocessor">\#include \<future\></span>

</div>

<div class="line">

</div>

<div class="line">

<span class="keyword">auto</span> gripper = [franky::Gripper](classfranky_1_1_gripper.md)(<span class="stringliteral">"10.90.90.1"</span>);

</div>

<div class="line">

</div>

<div class="line">

<span class="keywordtype">double</span> speed = 0.02; <span class="comment">// \[m/s\]</span>

</div>

<div class="line">

<span class="keywordtype">double</span> force = 20.0; <span class="comment">// \[N\]</span>

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Move the fingers to a specific width (5cm)</span>

</div>

<div class="line">

<span class="keywordtype">bool</span> success = gripper.move(0.05, speed);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Grasp an object of unknown width</span>

</div>

<div class="line">

success &= gripper.grasp(0.0, speed, force, epsilon\_outer=1.0);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Get the width of the grasped object</span>

</div>

<div class="line">

<span class="keywordtype">double</span> width = gripper.width();

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Release the object</span>

</div>

<div class="line">

gripper.open(speed);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// There are also asynchronous versions of the methods</span>

</div>

<div class="line">

std::future\<bool\> success\_future = gripper.moveAsync(0.05, speed);

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">// Wait for 1s</span>

</div>

<div class="line">

<span class="keywordflow">if</span> (\!success\_future.wait\_for(std::chrono::seconds(1)) == std::future\_status::ready) {

</div>

<div class="line">

<span class="comment">// Get the result</span>

</div>

<div class="line">

std::cout \<\< <span class="stringliteral">"Success: "</span> \<\< success\_future.get() \<\< std::endl;

</div>

<div class="line">

} <span class="keywordflow">else</span> {

</div>

<div class="line">

gripper.stop();

</div>

<div class="line">

success\_future.wait();

</div>

<div class="line">

std::cout \<\< <span class="stringliteral">"Gripper motion timed out."</span> \<\< std::endl;

</div>

<div class="line">

}

</div>

<div id="aclassfranky_1_1_gripper_html" class="ttc">

<div class="ttname">

[franky::Gripper](classfranky_1_1_gripper.md)

</div>

<div class="ttdoc">

A wrapper around the franka::Gripper class that adds asynchronous functionality.

</div>

<div class="ttdef">

**Definition** gripper.hpp:21

</div>

</div>

</div>

The Python API follows the C++ API closely:

<div class="fragment">

<div class="line">

<span class="keyword">import</span> franky

</div>

<div class="line">

</div>

<div class="line">

gripper = [franky.Gripper](classfranky_1_1_gripper.md)(<span class="stringliteral">"10.90.90.1"</span>)

</div>

<div class="line">

</div>

<div class="line">

speed = 0.02 <span class="comment">\# \[m/s\]</span>

</div>

<div class="line">

force = 20.0 <span class="comment">\# \[N\]</span>

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Move the fingers to a specific width (5cm)</span>

</div>

<div class="line">

success = gripper.move(0.05, speed)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Grasp an object of unknown width</span>

</div>

<div class="line">

success &= gripper.grasp(0.0, speed, force, epsilon\_outer=1.0)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Get the width of the grasped object</span>

</div>

<div class="line">

width = gripper.width

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Release the object</span>

</div>

<div class="line">

gripper.open(speed)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# There are also asynchronous versions of the methods</span>

</div>

<div class="line">

success\_future = gripper.move\_async(0.05, speed)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Wait for 1s</span>

</div>

<div class="line">

<span class="keywordflow">if</span> success\_future.wait(1):

</div>

<div class="line">

print(f<span class="stringliteral">"Success: {success\_future.get()}"</span>)

</div>

<div class="line">

<span class="keywordflow">else</span>:

</div>

<div class="line">

gripper.stop()

</div>

<div class="line">

success\_future.wait()

</div>

<div class="line">

print(<span class="stringliteral">"Gripper motion timed out."</span>)

</div>

</div>

### Accessing the Web Interface API

For Franka robots, control happens via the Franka Control Interface (FCI), which has to be enabled through the Franka UI in the robot's web interface. The Franka UI also provides methods for locking and unlocking the brakes, setting the execution mode, and executing the safety self-test. However, sometimes you may want to access these methods programmatically, e.g., for automatically unlocking the brakes before starting a motion, or automatically executing the self-test after 24h of continuous execution.

For that reason, franky provides a `RobotWebSession` class that allows you to access the web interface API of the robot. Note that directly accessing the web interface API is not officially supported and documented by Franka. Hence, use this feature at your own risk.

A typical automated workflow could look like this:

<div class="fragment">

<div class="line">

<span class="keyword">import</span> franky

</div>

<div class="line">

</div>

<div class="line">

<span class="keyword">with</span> franky.RobotWebSession(<span class="stringliteral">"10.90.90.1"</span>, <span class="stringliteral">"username"</span>, <span class="stringliteral">"password"</span>) <span class="keyword">as</span> robot\_web\_session:

</div>

<div class="line">

<span class="comment">\# First take control</span>

</div>

<div class="line">

<span class="keywordflow">try</span>:

</div>

<div class="line">

<span class="comment">\# Try taking control. The session currently holding control has to release it in order</span>

</div>

<div class="line">

<span class="comment">\# for this session to gain control. In the web interface, a notification will show</span>

</div>

<div class="line">

<span class="comment">\# prompting the user to release control. If the other session is another</span>

</div>

<div class="line">

<span class="comment">\# franky.RobotWebSession, then the \`release\_control\` method can be called on the other</span>

</div>

<div class="line">

<span class="comment">\# session to release control.</span>

</div>

<div class="line">

robot\_web\_session.take\_control(wait\_timeout=10.0)

</div>

<div class="line">

<span class="keywordflow">except</span> franky.TakeControlTimeoutError:

</div>

<div class="line">

<span class="comment">\# If nothing happens for 10s, we try to take control forcefully. This is particularly</span>

</div>

<div class="line">

<span class="comment">\# useful if the session holding control is dead. Taking control by force requires the</span>

</div>

<div class="line">

<span class="comment">\# user to manually push the blue button close to the robot's wrist.</span>

</div>

<div class="line">

robot\_web\_session.take\_control(wait\_timeout=30.0, force=<span class="keyword">True</span>)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Unlock the brakes</span>

</div>

<div class="line">

robot\_web\_session.unlock\_brakes()

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Enable the FCI</span>

</div>

<div class="line">

robot\_web\_session.enable\_fci()

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Create a franky.Robot instance and do whatever you want</span>

</div>

<div class="line">

...

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Disable the FCI</span>

</div>

<div class="line">

robot\_web\_session.disable\_fci()

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Lock brakes</span>

</div>

<div class="line">

robot\_web\_session.lock\_brakes()

</div>

</div>

In case you are running the robot for longer than 24h you will have noticed that you have to do a safety self-test every 24h. `RobotWebSession` allows to automate this task as well:

<div class="fragment">

<div class="line">

<span class="keyword">import</span> time

</div>

<div class="line">

<span class="keyword">import</span> franky

</div>

<div class="line">

</div>

<div class="line">

<span class="keyword">with</span> franky.RobotWebSession(<span class="stringliteral">"10.90.90.1"</span>, <span class="stringliteral">"username"</span>, <span class="stringliteral">"password"</span>) <span class="keyword">as</span> robot\_web\_session:

</div>

<div class="line">

<span class="comment">\# Execute self-test if the time until self-test is less than 5 minutes.</span>

</div>

<div class="line">

<span class="keywordflow">if</span> robot\_web\_session.get\_system\_status()\[<span class="stringliteral">"safety"</span>\]\[<span class="stringliteral">"timeToTd2"</span>\] \< 300:

</div>

<div class="line">

robot\_web\_session.disable\_fci()

</div>

<div class="line">

robot\_web\_session.lock\_brakes()

</div>

<div class="line">

time.sleep(1.0)

</div>

<div class="line">

</div>

<div class="line">

robot\_web\_session.execute\_self\_test()

</div>

<div class="line">

</div>

<div class="line">

robot\_web\_session.unlock\_brakes()

</div>

<div class="line">

robot\_web\_session.enable\_fci()

</div>

<div class="line">

time.sleep(1.0)

</div>

<div class="line">

</div>

<div class="line">

<span class="comment">\# Recreate your franky.Robot instance as the FCI has been disabled and re-enabled</span>

</div>

<div class="line">

...

</div>

</div>

`robot_web_session.get_system_status()` contains more information than just the time until self-test, such as the current execution mode, whether the brakes are locked, whether the FCI is enabled, and more.

If you want to call other API functions, you can use the `RobotWebSession.send_api_request` and `RobotWebSession.send_control_api_request` methods. See [robot\_web\_session.py](https://timschneider42.github.io/franky/franky/robot_web_session.py) for an example of how to use these methods.

## 🛠️ Development

franky is currently tested against the following versions

  - libfranka 0.7.1, 0.8.0, 0.9.2, 0.10.0, 0.11.0, 0.12.1, 0.13.3, 0.14.2, 0.15.3, 0.16.1, 0.17.0, 0.18.0
  - Eigen 3.4.0
  - Pybind11 2.13.6
  - POCO 1.12.5p2
  - Pinocchio 3.4.0
  - Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
  - Catch2 2.13.8 (for testing only)

## 📜 License

For non-commercial applications, this software is licensed under the LGPL v3.0. If you want to use franky within commercial applications or under a different license, please contact us for individual agreements.

## 🔍 Differences to frankx

franky started originally as a fork of [frankx](https://github.com/pantor/frankx), though both codebase and functionality differ substantially from frankx by now. Aside from bug fixes and general performance improvements, franky provides the following new features/improvements:

  - Motions can be updated asynchronously.
  - Reactions allow for the registration of callbacks instead of just printing to stdout when fired.
  - Motions allow for the registration of callbacks for profiling.
  - The robot state is also available during control.
  - A larger part of the libfranka API is exposed to python (e.g., `setCollisionBehavior`, `setJoinImpedance`, and `setCartesianImpedance`).
  - Cartesian motion generation handles boundaries in Euler angles properly.
  - There is a new joint motion type that supports waypoints.
  - The signature of \`Affine\` changed. `Affine` does not handle elbow positions anymore. Instead, a new class `RobotPose` stores both the end-effector pose and optionally the elbow position.
  - The `MotionData` class does not exist anymore. Instead, reactions and other settings moved to `Motion`.
  - The \`Measure\` class allows for arithmetic operations.
  - Exceptions caused by libfranka are raised properly instead of being printed to stdout.
  - We provide wheels for both Franka Research 3 and the older Franka Panda
  - franky supports joint velocity control and cartesian velocity control
  - The dynamics limits are not hard-coded anymore but can be set for each robot instance.

## Contributing

If you wish to contribute to this project, you are welcome to create a pull request. Please run the [pre-commit](https://pre-commit.com/) hooks before submitting your pull request. To install the pre-commit hooks, run:

1.  [Install pre-commit](https://pre-commit.com/#install)
2.  Install the Git hooks by running `pre-commit install` or, alternatively, run `pre-commit run --all-files` manually.

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
