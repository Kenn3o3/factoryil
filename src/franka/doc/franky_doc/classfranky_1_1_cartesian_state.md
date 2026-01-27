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
  - [CartesianState](classfranky_1_1_cartesian_state.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_cartesian_state.md#pub-methods) | [Friends](classfranky_1_1_cartesian_state.md#friends) | [List of all members](classfranky_1_1_cartesian_state-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::CartesianState Class Reference

</div>

</div>

</div>

<div class="contents">

`#include <cartesian_state.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[CartesianState](classfranky_1_1_cartesian_state.md#a7764a37806a5bb6cd2539f520ee2333c) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotPose](classfranky_1_1_robot_pose.md) &[pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b))

 

 

[CartesianState](classfranky_1_1_cartesian_state.md#a5bd6839fb4e69757aa4525b913adfc79) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotPose](classfranky_1_1_robot_pose.md) &[pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotVelocity](classfranky_1_1_robot_velocity.md) &[velocity](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f))

 

 

[CartesianState](classfranky_1_1_cartesian_state.md#aae23bc79979e802bb6242d7c720dad4a) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [CartesianState](classfranky_1_1_cartesian_state.md) &)=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

 

[CartesianState](classfranky_1_1_cartesian_state.md#aafe4a81eeddb9212361603d79b3bb0bd) ()=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[CartesianState](classfranky_1_1_cartesian_state.md) 

[transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform the frame of the state by applying the given affine transform.  

 

[CartesianState](classfranky_1_1_cartesian_state.md) 

[changeEndEffectorFrame](classfranky_1_1_cartesian_state.md#a95522df649508eed67ac81cf21ca1b08) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Change the end effector frame of the state by the given affine transform.  

 

[RobotPose](classfranky_1_1_robot_pose.md) 

[pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[RobotVelocity](classfranky_1_1_robot_velocity.md) 

[velocity](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

## <span id="friends"></span> Friends

std::ostream & 

[operator\<\<](classfranky_1_1_cartesian_state.md#a4889934eab07f3d4fac6c8c9ea9d3009) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [CartesianState](classfranky_1_1_cartesian_state.md) &[cartesian\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

## Constructor & Destructor Documentation

<span id="a7764a37806a5bb6cd2539f520ee2333c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#a7764a37806a5bb6cd2539f520ee2333c)</span>CartesianState() <span class="overload">\[1/4\]</span>

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
<td>franky::CartesianState::CartesianState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> &amp; </td>
<td><em>pose</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a5bd6839fb4e69757aa4525b913adfc79"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#a5bd6839fb4e69757aa4525b913adfc79)</span>CartesianState() <span class="overload">\[2/4\]</span>

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
<td>franky::CartesianState::CartesianState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> &amp; </td>
<td><em>pose</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> &amp; </td>
<td><em>velocity</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

  - Parameters
    
    |          |                                   |
    | -------- | --------------------------------- |
    | pose     | The pose of the end effector.     |
    | velocity | The velocity of the end effector. |
    

</div>

</div>

<span id="aae23bc79979e802bb6242d7c720dad4a"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#aae23bc79979e802bb6242d7c720dad4a)</span>CartesianState() <span class="overload">\[3/4\]</span>

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
<td>franky::CartesianState::CartesianState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_cartesian_state.md" class="el">CartesianState</a> &amp; </td>
<td></td>
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

<span id="aafe4a81eeddb9212361603d79b3bb0bd"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#aafe4a81eeddb9212361603d79b3bb0bd)</span>CartesianState() <span class="overload">\[4/4\]</span>

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
<td>franky::CartesianState::CartesianState</td>
<td>(</td>
<td></td>
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

## Member Function Documentation

<span id="a95522df649508eed67ac81cf21ca1b08"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#a95522df649508eed67ac81cf21ca1b08)</span>changeEndEffectorFrame()

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
<td><a href="classfranky_1_1_cartesian_state.md" class="el">CartesianState</a> franky::CartesianState::changeEndEffectorFrame</td>
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

Change the end effector frame of the state by the given affine transform.

  - Parameters
    
    |           |                                                                        |
    | --------- | ---------------------------------------------------------------------- |
    | transform | The pose of the new end-effector in the frame of the old end-effector. |
    

<!-- end list -->

  - Returns  
    The state with a new end-effector frame.

</div>

</div>

<span id="a5e8e2c8161dc22d18a01a0c28897792b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)</span>pose()

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
<td><a href="classfranky_1_1_robot_pose.md" class="el">RobotPose</a> franky::CartesianState::pose</td>
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

</div>

</div>

<span id="a9f7b644b3920e5816554b8855854a1aa"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)</span>transformWith()

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
<td><a href="classfranky_1_1_cartesian_state.md" class="el">CartesianState</a> franky::CartesianState::transformWith</td>
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

Transform the frame of the state by applying the given affine transform.

  - Parameters
    
    |           |                              |
    | --------- | ---------------------------- |
    | transform | The transformation to apply. |
    

<!-- end list -->

  - Returns  
    The state after the transformation.

</div>

</div>

<span id="ac212d0fc0f7b8f05baa3da6389bcf52f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f)</span>velocity()

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
<td><a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> franky::CartesianState::velocity</td>
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

</div>

</div>

## Friends And Related Symbol Documentation

<span id="a4889934eab07f3d4fac6c8c9ea9d3009"></span>

## <span class="permalink">[◆ ](classfranky_1_1_cartesian_state.md#a4889934eab07f3d4fac6c8c9ea9d3009)</span>operator\<\<

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_cartesian_state.md" class="el">CartesianState</a> &amp; </td>
<td><em>cartesian_state</em> </td>
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

The documentation for this class was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/[cartesian\_state.hpp](cartesian__state_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
