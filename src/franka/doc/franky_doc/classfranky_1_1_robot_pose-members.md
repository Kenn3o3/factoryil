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
  - [RobotPose](classfranky_1_1_robot_pose.md)

</div>

</div>

<div class="header">

<div class="headertitle">

<div class="title">

franky::RobotPose Member List

</div>

</div>

</div>

<div class="contents">

This is the complete list of members for [franky::RobotPose](classfranky_1_1_robot_pose.md), including all inherited members.

|                                                                                                                                                                                                 |                                                      |                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------ |
| [as\_franka\_pose](classfranky_1_1_robot_pose.md#a87b43342db37db66af0b1411af496dd2)(FlipDirection default\_elbow\_flip\_direction=FlipDirection::kNegative) const                             | [franky::RobotPose](classfranky_1_1_robot_pose.md) |                                      |
| [changeEndEffectorFrame](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba)(const Affine \&transform) const                                                                     | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">inline</span>   |
| [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)() const                                                                                                       | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">inline</span>   |
| [end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd)() const                                                                                                | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">inline</span>   |
| [leftTransform](classfranky_1_1_robot_pose.md#adc234649707e63232c54d9e392db25c6)(const Affine \&transform) const                                                                              | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">inline</span>   |
| [operator\<\<](classfranky_1_1_robot_pose.md#abd7aca5ba4c84f9ad7257f1de3b94cb0)                                                                                                               | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">friend</span>   |
| [rightTransform](classfranky_1_1_robot_pose.md#afdbee35c5bf294ed93a139cc6280a076)(const Affine \&transform) const                                                                             | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">inline</span>   |
| [RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)()                                                                                                                | [franky::RobotPose](classfranky_1_1_robot_pose.md) |                                      |
| [RobotPose](classfranky_1_1_robot_pose.md#a33ec908498b031c97c384e220f5fa6db)(const RobotPose \&robot\_pose)                                                                                   | [franky::RobotPose](classfranky_1_1_robot_pose.md) |                                      |
| [RobotPose](classfranky_1_1_robot_pose.md#a17e04d7a6e94322631124be162fd2020)(Affine end\_effector\_pose, std::optional\< ElbowState \> elbow\_state=std::nullopt)                             | [franky::RobotPose](classfranky_1_1_robot_pose.md) |                                      |
| [RobotPose](classfranky_1_1_robot_pose.md#ad1789082d7c0a7af4579baf77348d5ac)(const Vector7d \&vector\_repr, bool ignore\_elbow=false, FlipDirection flip\_direction=FlipDirection::kNegative) | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">explicit</span> |
| [RobotPose](classfranky_1_1_robot_pose.md#a2b39f85fbbc2c1f9388ea0dc89fbf375)(const Vector6d \&vector\_repr, std::optional\< ElbowState \> elbow\_state=std::nullopt)                          | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">explicit</span> |
| [RobotPose](classfranky_1_1_robot_pose.md#a7de9a07b5668acf85bca2bf127cde4e1)(const franka::CartesianPose \&franka\_pose)                                                                      | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">explicit</span> |
| [vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d)() const                                                                                                       | [franky::RobotPose](classfranky_1_1_robot_pose.md) |                                      |
| [withElbowState](classfranky_1_1_robot_pose.md#a79b9d1d5960fe44eebda0d309c868e1a)(const std::optional\< ElbowState \> elbow\_state) const                                                     | [franky::RobotPose](classfranky_1_1_robot_pose.md) | <span class="mlabel">inline</span>   |

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
