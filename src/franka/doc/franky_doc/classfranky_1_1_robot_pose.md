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

<div class="summary">

[Public Member Functions](classfranky_1_1_robot_pose.md#pub-methods) | [Friends](classfranky_1_1_robot_pose.md#friends) | [List of all members](classfranky_1_1_robot_pose-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::RobotPose Class Reference

</div>

</div>

</div>

<div class="contents">

Cartesian pose of a robot. [More...](classfranky_1_1_robot_pose.md#details)

`#include <robot_pose.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197) ()

 

 

[RobotPose](classfranky_1_1_robot_pose.md#a33ec908498b031c97c384e220f5fa6db) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotPose](classfranky_1_1_robot_pose.md) &[robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

 

[RobotPose](classfranky_1_1_robot_pose.md#a17e04d7a6e94322631124be162fd2020) ([Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd), std::optional\< [ElbowState](classfranky_1_1_elbow_state.md) \> [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)=std::nullopt)

 

 

[RobotPose](classfranky_1_1_robot_pose.md#ad1789082d7c0a7af4579baf77348d5ac) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d), [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ignore\_elbow](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=[false](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) [flip\_direction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=[FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3))

 

 

[RobotPose](classfranky_1_1_robot_pose.md#a2b39f85fbbc2c1f9388ea0dc89fbf375) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d), std::optional\< [ElbowState](classfranky_1_1_elbow_state.md) \> [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)=std::nullopt)

 

 

[RobotPose](classfranky_1_1_robot_pose.md#a7de9a07b5668acf85bca2bf127cde4e1) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::CartesianPose &[franka\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the vector representation of the pose, which consists of the end effector position and orientation (as rotation vector) and the elbow position. Does not contain the flip component of the elbow state.  

 

franka::CartesianPose 

[as\_franka\_pose](classfranky_1_1_robot_pose.md#a87b43342db37db66af0b1411af496dd2) ([FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) [default\_elbow\_flip\_direction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=[FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Convert this pose to a franka pose.  

 

[RobotPose](classfranky_1_1_robot_pose.md) 

[leftTransform](classfranky_1_1_robot_pose.md#adc234649707e63232c54d9e392db25c6) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform this pose with a given affine transformation from the left side.  

 

[RobotPose](classfranky_1_1_robot_pose.md) 

[rightTransform](classfranky_1_1_robot_pose.md#afdbee35c5bf294ed93a139cc6280a076) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform this pose with a given affine transformation from the right side.  

 

[RobotPose](classfranky_1_1_robot_pose.md) 

[changeEndEffectorFrame](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Change the frame of the end effector by applying a transformation from the right side. This is equivalent to calling rightTransform(transform).  

 

[RobotPose](classfranky_1_1_robot_pose.md) 

[withElbowState](classfranky_1_1_robot_pose.md#a79b9d1d5960fe44eebda0d309c868e1a) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ElbowState](classfranky_1_1_elbow_state.md) \> [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the pose with a new elbow state.  

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the end effector pose.  

 

std::optional\< [ElbowState](classfranky_1_1_elbow_state.md) \> 

[elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the elbow state.  

 

## <span id="friends"></span> Friends

std::ostream & 

[operator\<\<](classfranky_1_1_robot_pose.md#abd7aca5ba4c84f9ad7257f1de3b94cb0) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotPose](classfranky_1_1_robot_pose.md) &[robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Cartesian pose of a robot.

This class encapsulates the cartesian pose of a robot, which comprises the end effector pose and the elbow position.

</div>

## Constructor & Destructor Documentation

<span id="a2dbca2efd3922f5b8a0954e778dcd197"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)</span>RobotPose() <span class="overload">\[1/6\]</span>

<div class="memitem">

<div class="memproto">

|                              |   |  |   |  |
| ---------------------------- | - |  | - |  |
| franky::RobotPose::RobotPose | ( |  | ) |  |

</div>

<div class="memdoc">

</div>

</div>

<span id="a33ec908498b031c97c384e220f5fa6db"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a33ec908498b031c97c384e220f5fa6db)</span>RobotPose() <span class="overload">\[2/6\]</span>

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td>franky::RobotPose::RobotPose</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> &amp; </td>
<td><em>robot_pose</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">default</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a17e04d7a6e94322631124be162fd2020"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a17e04d7a6e94322631124be162fd2020)</span>RobotPose() <span class="overload">\[3/6\]</span>

<div class="memitem">

<div class="memproto">

|                              |   |                                                                   |                                 |
| ---------------------------- | - | ----------------------------------------------------------------- | ------------------------------- |
| franky::RobotPose::RobotPose | ( | [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)  | *end\_effector\_pose*,          |
|                              |   | std::optional\< [ElbowState](classfranky_1_1_elbow_state.md) \> | *elbow\_state* = `std::nullopt` |
|                              | ) |                                                                   |                                 |

</div>

<div class="memdoc">

  - Parameters
    
    |                     |                                   |
    | ------------------- | --------------------------------- |
    | end\_effector\_pose | The pose of the end effector.     |
    | elbow\_state        | The state of the elbow. Optional. |
    

</div>

</div>

<span id="ad1789082d7c0a7af4579baf77348d5ac"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#ad1789082d7c0a7af4579baf77348d5ac)</span>RobotPose() <span class="overload">\[4/6\]</span>

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td>franky::RobotPose::RobotPose</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &amp; </td>
<td><em>vector_repr</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> </td>
<td><em>ignore_elbow</em> = <code>false</code>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b" class="el">FlipDirection</a> </td>
<td><em>flip_direction</em> = <code>FlipDirection::kNegative</code> </td>
</tr>
<tr class="even">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">explicit</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

  - Parameters
    
    |                 |                                                                             |
    | --------------- | --------------------------------------------------------------------------- |
    | vector\_repr    | The vector representation of the pose.                                      |
    | ignore\_elbow   | Whether to ignore the elbow state. Default is false.                        |
    | flip\_direction | The flip direction to use if the elbow is not ignored. Default is negative. |
    

</div>

</div>

<span id="a2b39f85fbbc2c1f9388ea0dc89fbf375"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a2b39f85fbbc2c1f9388ea0dc89fbf375)</span>RobotPose() <span class="overload">\[5/6\]</span>

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td>franky::RobotPose::RobotPose</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb" class="el">Vector6d</a> &amp; </td>
<td><em>vector_repr</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::optional&lt; <a href="classfranky_1_1_elbow_state.md" class="el">ElbowState</a> &gt; </td>
<td><em>elbow_state</em> = <code>std::nullopt</code> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">explicit</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

  - Parameters
    
    |              |                                        |
    | ------------ | -------------------------------------- |
    | vector\_repr | The vector representation of the pose. |
    | elbow\_state | The state of the elbow. Optional.      |
    

</div>

</div>

<span id="a7de9a07b5668acf85bca2bf127cde4e1"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a7de9a07b5668acf85bca2bf127cde4e1)</span>RobotPose() <span class="overload">\[6/6\]</span>

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td>franky::RobotPose::RobotPose</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> franka::CartesianPose &amp; </td>
<td><em>franka_pose</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">explicit</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

  - Parameters
    
    |              |                  |
    | ------------ | ---------------- |
    | franka\_pose | The franka pose. |
    

</div>

</div>

## Member Function Documentation

<span id="a87b43342db37db66af0b1411af496dd2"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a87b43342db37db66af0b1411af496dd2)</span>as\_franka\_pose()

<div class="memitem">

<div class="memproto">

|                                                           |   |                                                                         |                                                                |   |       |
| --------------------------------------------------------- | - | ----------------------------------------------------------------------- | -------------------------------------------------------------- | - | ----- |
| franka::CartesianPose franky::RobotPose::as\_franka\_pose | ( | [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) | *default\_elbow\_flip\_direction* = `FlipDirection::kNegative` | ) | const |

</div>

<div class="memdoc">

Convert this pose to a franka pose.

  - Parameters
    
    |                                 |                                                                           |
    | ------------------------------- | ------------------------------------------------------------------------- |
    | default\_elbow\_flip\_direction | The default flip direction to use if the elbow flip direction is not set. |
    

<!-- end list -->

  - Returns  
    The franka pose.

</div>

</div>

<span id="a132eef8bd15ba00132fb64ed441382ba"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba)</span>changeEndEffectorFrame()

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td><a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> franky::RobotPose::changeEndEffectorFrame</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> &amp; </td>
<td><em>transform</em></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Change the frame of the end effector by applying a transformation from the right side. This is equivalent to calling rightTransform(transform).

  - Parameters
    
    |           |                         |
    | --------- | ----------------------- |
    | transform | The transform to apply. |
    

<!-- end list -->

  - Returns  
    The robot pose with the new end effector frame.

</div>

</div>

<span id="aca6a0cfec885c9aa09800603b2487a55"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)</span>elbow\_state()

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td>std::optional&lt; <a href="classfranky_1_1_elbow_state.md" class="el">ElbowState</a> &gt; franky::RobotPose::elbow_state</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Get the elbow state.

  - Returns  
    The elbow state.

</div>

</div>

<span id="abe83d0dc121a5e1312ac4f2acdbd9fbd"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd)</span>end\_effector\_pose()

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td><a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> franky::RobotPose::end_effector_pose</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Get the end effector pose.

  - Returns  
    The end effector pose.

</div>

</div>

<span id="adc234649707e63232c54d9e392db25c6"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#adc234649707e63232c54d9e392db25c6)</span>leftTransform()

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td><a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> franky::RobotPose::leftTransform</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> &amp; </td>
<td><em>transform</em></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Transform this pose with a given affine transformation from the left side.

  - Parameters
    
    |           |                         |
    | --------- | ----------------------- |
    | transform | The transform to apply. |
    

<!-- end list -->

  - Returns  
    The transformed robot pose.

</div>

</div>

<span id="afdbee35c5bf294ed93a139cc6280a076"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#afdbee35c5bf294ed93a139cc6280a076)</span>rightTransform()

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td><a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> franky::RobotPose::rightTransform</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> &amp; </td>
<td><em>transform</em></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Transform this pose with a given affine transformation from the right side.

  - Parameters
    
    |           |                         |
    | --------- | ----------------------- |
    | transform | The transform to apply. |
    

<!-- end list -->

  - Returns  
    The transformed robot pose.

</div>

</div>

<span id="a49bde12b0fbe8a2cc7e95c923b170c8d"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d)</span>vector\_repr()

<div class="memitem">

<div class="memproto">

|                                                                                                    |   |  |   |       |
| -------------------------------------------------------------------------------------------------- | - |  | - | ----- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotPose::vector\_repr | ( |  | ) | const |

</div>

<div class="memdoc">

Get the vector representation of the pose, which consists of the end effector position and orientation (as rotation vector) and the elbow position. Does not contain the flip component of the elbow state.

  - Returns  
    The vector representation of the pose.

</div>

</div>

<span id="a79b9d1d5960fe44eebda0d309c868e1a"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#a79b9d1d5960fe44eebda0d309c868e1a)</span>withElbowState()

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td><a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> franky::RobotPose::withElbowState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="classfranky_1_1_elbow_state.md" class="el">ElbowState</a> &gt; </td>
<td><em>elbow_state</em></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Get the pose with a new elbow state.

  - Parameters
    
    |              |                      |
    | ------------ | -------------------- |
    | elbow\_state | The new elbow state. |
    

<!-- end list -->

  - Returns  
    The pose with the new elbow state.

</div>

</div>

## Friends And Related Symbol Documentation

<span id="abd7aca5ba4c84f9ad7257f1de3b94cb0"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_pose.md#abd7aca5ba4c84f9ad7257f1de3b94cb0)</span>operator\<\<

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td>std::ostream &amp; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">operator</a>&lt;&lt;</td>
<td>(</td>
<td>std::ostream &amp; </td>
<td><em>os</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> &amp; </td>
<td><em>robot_pose</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">friend</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/[robot\_pose.hpp](robot__pose_8hpp_source.md)
  - /home/runner/work/franky/franky/src/[robot\_pose.cpp](robot__pose_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
