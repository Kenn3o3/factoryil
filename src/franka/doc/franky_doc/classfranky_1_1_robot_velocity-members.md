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
  - [RobotVelocity](classfranky_1_1_robot_velocity.md)

</div>

</div>

<div class="header">

<div class="headertitle">

<div class="title">

franky::RobotVelocity Member List

</div>

</div>

</div>

<div class="contents">

This is the complete list of members for [franky::RobotVelocity](classfranky_1_1_robot_velocity.md), including all inherited members.

|                                                                                                                                                                                                                                              |                                                              |                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------ |
| [as\_franka\_velocity](classfranky_1_1_robot_velocity.md#a03b492d4eb5585514405f78a88a1b6e0)(const std::optional\< ElbowState \> \&elbow\_state=std::nullopt, FlipDirection default\_elbow\_flip\_direction=FlipDirection::kNegative) const | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) |                                      |
| [changeEndEffectorFrame](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95)(const Eigen::Vector3d \&offset\_world\_frame) const                                                                                          | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">inline</span>   |
| [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)() const                                                                                                                                             | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">inline</span>   |
| [end\_effector\_twist](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b)() const                                                                                                                                        | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">inline</span>   |
| [operator\<\<](classfranky_1_1_robot_velocity.md#a5650119c96c36dfba8aaf863df12e0aa)                                                                                                                                                        | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">friend</span>   |
| [RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)()                                                                                                                                                     | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) |                                      |
| [RobotVelocity](classfranky_1_1_robot_velocity.md#a05c422e3c640b24a825f0ed2d400fe7b)(const RobotVelocity \&robot\_velocity)                                                                                                                | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) |                                      |
| [RobotVelocity](classfranky_1_1_robot_velocity.md#ad798edda4f3a7d09c2cd28be6d06f4a8)(const Twist \&end\_effector\_twist, std::optional\< double \> elbow\_velocity=std::nullopt)                                                           | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) |                                      |
| [RobotVelocity](classfranky_1_1_robot_velocity.md#aea7c0239f9b0a3f9d16e0c4fe0d52762)(const Vector7d \&vector\_repr, bool ignore\_elbow=false)                                                                                              | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">explicit</span> |
| [RobotVelocity](classfranky_1_1_robot_velocity.md#ab57c629481b8cc757b19dce33c55e405)(const Vector6d \&vector\_repr, std::optional\< double \> elbow\_velocity=std::nullopt)                                                                | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">explicit</span> |
| [RobotVelocity](classfranky_1_1_robot_velocity.md#ab487401f026209fcd265a36500e09ca7)(franka::CartesianVelocities franka\_velocity)                                                                                                         | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">explicit</span> |
| [transform](classfranky_1_1_robot_velocity.md#a7e10894668e53f945a34939cc828716e)(const Affine \&affine) const                                                                                                                              | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">inline</span>   |
| [transform](classfranky_1_1_robot_velocity.md#a4e2cbc0ba39425815403cffcffdb6545)(const RotationMatrixType \&rotation) const                                                                                                                | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">inline</span>   |
| [vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c)() const                                                                                                                                                | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) |                                      |
| [withElbowVelocity](classfranky_1_1_robot_velocity.md#aa53f2a9297f426cb327ee4172bd3ccd1)(const std::optional\< double \> elbow\_velocity) const                                                                                            | [franky::RobotVelocity](classfranky_1_1_robot_velocity.md) | <span class="mlabel">inline</span>   |

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
