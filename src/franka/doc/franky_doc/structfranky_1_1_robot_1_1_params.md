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

<div id="nav-path" class="navpath">

  - [franky](namespacefranky.md)
  - [Robot](classfranky_1_1_robot.md)
  - [Params](structfranky_1_1_robot_1_1_params.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Attributes](structfranky_1_1_robot_1_1_params.md#pub-attribs) | [List of all members](structfranky_1_1_robot_1_1_params-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Robot::Params Struct Reference

</div>

</div>

</div>

<div class="contents">

Global parameters for the robot. [More...](structfranky_1_1_robot_1_1_params.md#details)

`#include <robot.hpp>`

## <span id="pub-attribs"></span> Public Attributes

</div>

[RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) 

[relative\_dynamics\_factor](structfranky_1_1_robot_1_1_params.md#a232bd0323512dd23a1e6003c906eb328) {1.0}

 

Relative dynamics factor for the robot.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[default\_torque\_threshold](structfranky_1_1_robot_1_1_params.md#ac52be6b32e29563c8bb6576679bcbfa5) {20.0}

 

Default torque threshold for collision behavior.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[default\_force\_threshold](structfranky_1_1_robot_1_1_params.md#a2535f117ddde7fd4294eeb952d4746bd) {30.0}

 

Default force threshold for collision behavior.  

 

franka::ControllerMode 

[controller\_mode](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083) {franka::ControllerMode::kJointImpedance}

 

Default controller mode for the robot.  

 

franka::RealtimeConfig 

[realtime\_config](structfranky_1_1_robot_1_1_params.md#a7c8199f22e083645746aa47020c97d56) {franka::RealtimeConfig::kEnforce}

 

Default realtime configuration for the robot.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_q\_process\_var](structfranky_1_1_robot_1_1_params.md#ae6c5c63f100b88ae3fc1ae3dcd50c44e) = 0.0001

 

Kalman parameter: process noise variance of the position.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_dq\_process\_var](structfranky_1_1_robot_1_1_params.md#a1e9c37c50668090f408db94e12e54bc9) = 0.001

 

Kalman parameter: process noise variance of the velocity.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_ddq\_process\_var](structfranky_1_1_robot_1_1_params.md#acd2d77ccd361a615b18b0a89fa0b2dd0) = 0.1

 

Kalman parameter: process noise variance of the acceleration.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_control\_process\_var](structfranky_1_1_robot_1_1_params.md#a62b242c8c50ac828af9ac497b3cba801) = 1

 

Kalman parameter: process noise variance of the control signal.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_q\_obs\_var](structfranky_1_1_robot_1_1_params.md#a304e57064f927eb2c00757a1d86d2e08) = 0.01

 

Kalman parameter: observation noise variance of measured joint positions.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_dq\_obs\_var](structfranky_1_1_robot_1_1_params.md#a2bccca1dff1d1cd4c4d7d1f0cae03f7b) = 0.1

 

Kalman parameter: observation noise variance of measured joint velocities.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_q\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#a78a7c309785935bab49cdb24b5a750a8) = 0.0001

 

Kalman parameter: observation noise variance of desired joint positions.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_dq\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#a51f8d9dbacca9c18de1b2429bea65dae) = 0.0001

 

Kalman parameter: observation noise variance of desired joint velocities.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_ddq\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#abeaee212f2cac08ce47158dc44bb6b71) = 0.0001

 

Kalman parameter: observation noise variance of desired joint accelerations.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[kalman\_control\_adaptation\_rate](structfranky_1_1_robot_1_1_params.md#a28da04d85b05bdc0483931fdb5ee9665) = 0.1

 

Kalman parameter: rate of adaptation of the robot state to the desired robot state.  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Global parameters for the robot.

</div>

## Member Data Documentation

<span id="a598cc77f3116a601bac482ddc4c74083"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083)</span>controller\_mode

<div class="memitem">

<div class="memproto">

|                                                                                                          |
| -------------------------------------------------------------------------------------------------------- |
| franka::ControllerMode franky::Robot::Params::controller\_mode {franka::ControllerMode::kJointImpedance} |

</div>

<div class="memdoc">

Default controller mode for the robot.

See libfranka documentation for details.

</div>

</div>

<span id="a2535f117ddde7fd4294eeb952d4746bd"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a2535f117ddde7fd4294eeb952d4746bd)</span>default\_force\_threshold

<div class="memitem">

<div class="memproto">

|                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::default\_force\_threshold {30.0} |

</div>

<div class="memdoc">

Default force threshold for collision behavior.

</div>

</div>

<span id="ac52be6b32e29563c8bb6576679bcbfa5"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#ac52be6b32e29563c8bb6576679bcbfa5)</span>default\_torque\_threshold

<div class="memitem">

<div class="memproto">

|                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::default\_torque\_threshold {20.0} |

</div>

<div class="memdoc">

Default torque threshold for collision behavior.

</div>

</div>

<span id="a28da04d85b05bdc0483931fdb5ee9665"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a28da04d85b05bdc0483931fdb5ee9665)</span>kalman\_control\_adaptation\_rate

<div class="memitem">

<div class="memproto">

|                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_control\_adaptation\_rate = 0.1 |

</div>

<div class="memdoc">

Kalman parameter: rate of adaptation of the robot state to the desired robot state.

</div>

</div>

<span id="a62b242c8c50ac828af9ac497b3cba801"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a62b242c8c50ac828af9ac497b3cba801)</span>kalman\_control\_process\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_control\_process\_var = 1 |

</div>

<div class="memdoc">

Kalman parameter: process noise variance of the control signal.

</div>

</div>

<span id="abeaee212f2cac08ce47158dc44bb6b71"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#abeaee212f2cac08ce47158dc44bb6b71)</span>kalman\_ddq\_d\_obs\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_ddq\_d\_obs\_var = 0.0001 |

</div>

<div class="memdoc">

Kalman parameter: observation noise variance of desired joint accelerations.

</div>

</div>

<span id="acd2d77ccd361a615b18b0a89fa0b2dd0"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#acd2d77ccd361a615b18b0a89fa0b2dd0)</span>kalman\_ddq\_process\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_ddq\_process\_var = 0.1 |

</div>

<div class="memdoc">

Kalman parameter: process noise variance of the acceleration.

</div>

</div>

<span id="a51f8d9dbacca9c18de1b2429bea65dae"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a51f8d9dbacca9c18de1b2429bea65dae)</span>kalman\_dq\_d\_obs\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_dq\_d\_obs\_var = 0.0001 |

</div>

<div class="memdoc">

Kalman parameter: observation noise variance of desired joint velocities.

</div>

</div>

<span id="a2bccca1dff1d1cd4c4d7d1f0cae03f7b"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a2bccca1dff1d1cd4c4d7d1f0cae03f7b)</span>kalman\_dq\_obs\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_dq\_obs\_var = 0.1 |

</div>

<div class="memdoc">

Kalman parameter: observation noise variance of measured joint velocities.

</div>

</div>

<span id="a1e9c37c50668090f408db94e12e54bc9"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a1e9c37c50668090f408db94e12e54bc9)</span>kalman\_dq\_process\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_dq\_process\_var = 0.001 |

</div>

<div class="memdoc">

Kalman parameter: process noise variance of the velocity.

</div>

</div>

<span id="a78a7c309785935bab49cdb24b5a750a8"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a78a7c309785935bab49cdb24b5a750a8)</span>kalman\_q\_d\_obs\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_q\_d\_obs\_var = 0.0001 |

</div>

<div class="memdoc">

Kalman parameter: observation noise variance of desired joint positions.

</div>

</div>

<span id="a304e57064f927eb2c00757a1d86d2e08"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a304e57064f927eb2c00757a1d86d2e08)</span>kalman\_q\_obs\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_q\_obs\_var = 0.01 |

</div>

<div class="memdoc">

Kalman parameter: observation noise variance of measured joint positions.

</div>

</div>

<span id="ae6c5c63f100b88ae3fc1ae3dcd50c44e"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#ae6c5c63f100b88ae3fc1ae3dcd50c44e)</span>kalman\_q\_process\_var

<div class="memitem">

<div class="memproto">

|                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Robot::Params::kalman\_q\_process\_var = 0.0001 |

</div>

<div class="memdoc">

Kalman parameter: process noise variance of the position.

</div>

</div>

<span id="a7c8199f22e083645746aa47020c97d56"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a7c8199f22e083645746aa47020c97d56)</span>realtime\_config

<div class="memitem">

<div class="memproto">

|                                                                                                   |
| ------------------------------------------------------------------------------------------------- |
| franka::RealtimeConfig franky::Robot::Params::realtime\_config {franka::RealtimeConfig::kEnforce} |

</div>

<div class="memdoc">

Default realtime configuration for the robot.

See libfranka documentation for details.

</div>

</div>

<span id="a232bd0323512dd23a1e6003c906eb328"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_1_1_params.md#a232bd0323512dd23a1e6003c906eb328)</span>relative\_dynamics\_factor

<div class="memitem">

<div class="memproto">

|                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------- |
| [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) franky::Robot::Params::relative\_dynamics\_factor {1.0} |

</div>

<div class="memdoc">

Relative dynamics factor for the robot.

The maximum velocity, acceleration and jerk of the robot are scaled by the factors specified here.

</div>

</div>

-----

The documentation for this struct was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/[robot.hpp](robot_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
