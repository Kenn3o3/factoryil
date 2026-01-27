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

<div class="summary">

[Public Member Functions](classfranky_1_1_robot_velocity.md#pub-methods) | [Friends](classfranky_1_1_robot_velocity.md#friends) | [List of all members](classfranky_1_1_robot_velocity-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::RobotVelocity Class Reference

</div>

</div>

</div>

<div class="contents">

Cartesian velocity of a robot. [More...](classfranky_1_1_robot_velocity.md#details)

`#include <robot_velocity.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310) ()

 

 

[RobotVelocity](classfranky_1_1_robot_velocity.md#a05c422e3c640b24a825f0ed2d400fe7b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotVelocity](classfranky_1_1_robot_velocity.md) &[robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

 

[RobotVelocity](classfranky_1_1_robot_velocity.md#ad798edda4f3a7d09c2cd28be6d06f4a8) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Twist](classfranky_1_1_twist.md) &[end\_effector\_twist](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b), std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)=std::nullopt)

 

 

[RobotVelocity](classfranky_1_1_robot_velocity.md#aea7c0239f9b0a3f9d16e0c4fe0d52762) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c), [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ignore\_elbow](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=[false](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

 

[RobotVelocity](classfranky_1_1_robot_velocity.md#ab57c629481b8cc757b19dce33c55e405) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c), std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)=std::nullopt)

 

 

[RobotVelocity](classfranky_1_1_robot_velocity.md#ab487401f026209fcd265a36500e09ca7) (franka::CartesianVelocities [franka\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the vector representation of the velocity. It consists of the linear and angular velocity of the end effector and the joint velocity of the elbow.  

 

franka::CartesianVelocities 

[as\_franka\_velocity](classfranky_1_1_robot_velocity.md#a03b492d4eb5585514405f78a88a1b6e0) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ElbowState](classfranky_1_1_elbow_state.md) \> \&elbow\_state=std::nullopt, [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) [default\_elbow\_flip\_direction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=[FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the franka velocity.  

 

[RobotVelocity](classfranky_1_1_robot_velocity.md) 

[transform](classfranky_1_1_robot_velocity.md#a7e10894668e53f945a34939cc828716e) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform the frame of the velocity by applying the given affine transform.  

 

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

[RobotVelocity](classfranky_1_1_robot_velocity.md) 

[transform](classfranky_1_1_robot_velocity.md#a4e2cbc0ba39425815403cffcffdb6545) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform the frame of the velocity by applying the given rotation.  

 

[RobotVelocity](classfranky_1_1_robot_velocity.md) 

[changeEndEffectorFrame](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &[offset\_world\_frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Change the end-effector frame by adding the given offset to the current end-effector frame. Note that the offset must be given in world coordinates.  

 

[RobotVelocity](classfranky_1_1_robot_velocity.md) 

[withElbowVelocity](classfranky_1_1_robot_velocity.md#aa53f2a9297f426cb327ee4172bd3ccd1) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the velocity with a new elbow velocity.  

 

[Twist](classfranky_1_1_twist.md) 

[end\_effector\_twist](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the end effector twist.  

 

std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the elbow velocity.  

 

## <span id="friends"></span> Friends

std::ostream & 

[operator\<\<](classfranky_1_1_robot_velocity.md#a5650119c96c36dfba8aaf863df12e0aa) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotVelocity](classfranky_1_1_robot_velocity.md) &[robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Cartesian velocity of a robot.

This class encapsulates the cartesian velocity of a robot, which comproses the end effector twist and the elbow velocity.

</div>

## Constructor & Destructor Documentation

<span id="afe5611a93ddbac86a054f5c9dd7c2310"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)</span>RobotVelocity() <span class="overload">\[1/6\]</span>

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
<td>franky::RobotVelocity::RobotVelocity</td>
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

<span id="a05c422e3c640b24a825f0ed2d400fe7b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#a05c422e3c640b24a825f0ed2d400fe7b)</span>RobotVelocity() <span class="overload">\[2/6\]</span>

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
<td>franky::RobotVelocity::RobotVelocity</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> &amp; </td>
<td><em>robot_velocity</em></td>
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

<span id="ad798edda4f3a7d09c2cd28be6d06f4a8"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#ad798edda4f3a7d09c2cd28be6d06f4a8)</span>RobotVelocity() <span class="overload">\[3/6\]</span>

<div class="memitem">

<div class="memproto">

|                                      |   |                                                                                                       |                                    |
| ------------------------------------ | - | ----------------------------------------------------------------------------------------------------- | ---------------------------------- |
| franky::RobotVelocity::RobotVelocity | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Twist](classfranky_1_1_twist.md) & | *end\_effector\_twist*,            |
|                                      |   | std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>                   | *elbow\_velocity* = `std::nullopt` |
|                                      | ) |                                                                                                       |                                    |

</div>

<div class="memdoc">

  - Parameters
    
    |                      |                                       |
    | -------------------- | ------------------------------------- |
    | end\_effector\_twist | The twist of the end effector.        |
    | elbow\_velocity      | The velocity of the elbow (optional). |
    

</div>

</div>

<span id="aea7c0239f9b0a3f9d16e0c4fe0d52762"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#aea7c0239f9b0a3f9d16e0c4fe0d52762)</span>RobotVelocity() <span class="overload">\[4/6\]</span>

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
<td>franky::RobotVelocity::RobotVelocity</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &amp; </td>
<td><em>vector_repr</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> </td>
<td><em>ignore_elbow</em> = <code>false</code> </td>
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
    
    |               |                                                         |
    | ------------- | ------------------------------------------------------- |
    | vector\_repr  | The vector representation of the velocity.              |
    | ignore\_elbow | Whether to ignore the elbow velocity. Default is false. |
    

</div>

</div>

<span id="ab57c629481b8cc757b19dce33c55e405"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#ab57c629481b8cc757b19dce33c55e405)</span>RobotVelocity() <span class="overload">\[5/6\]</span>

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
<td>franky::RobotVelocity::RobotVelocity</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb" class="el">Vector6d</a> &amp; </td>
<td><em>vector_repr</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::optional&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> &gt; </td>
<td><em>elbow_velocity</em> = <code>std::nullopt</code> </td>
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
    
    |                 |                                            |
    | --------------- | ------------------------------------------ |
    | vector\_repr    | The vector representation of the velocity. |
    | elbow\_velocity | The velocity of the elbow (optional).      |
    

</div>

</div>

<span id="ab487401f026209fcd265a36500e09ca7"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#ab487401f026209fcd265a36500e09ca7)</span>RobotVelocity() <span class="overload">\[6/6\]</span>

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
<td>franky::RobotVelocity::RobotVelocity</td>
<td>(</td>
<td>franka::CartesianVelocities </td>
<td><em>franka_velocity</em></td>
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
    
    |                  |                      |
    | ---------------- | -------------------- |
    | franka\_velocity | The franka velocity. |
    

</div>

</div>

## Member Function Documentation

<span id="a03b492d4eb5585514405f78a88a1b6e0"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#a03b492d4eb5585514405f78a88a1b6e0)</span>as\_franka\_velocity()

<div class="memitem">

<div class="memproto">

|                                                                         |   |                                                                                                                                     |                                                                |
| ----------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| franka::CartesianVelocities franky::RobotVelocity::as\_franka\_velocity | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ElbowState](classfranky_1_1_elbow_state.md) \> & | *elbow\_state* = `std::nullopt`,                               |
|                                                                         |   | [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b)                                                             | *default\_elbow\_flip\_direction* = `FlipDirection::kNegative` |
|                                                                         | ) |                                                                                                                                     | const                                                          |

</div>

<div class="memdoc">

Get the franka velocity.

  - Parameters
    
    |                                 |                                                                                                                                                                                                                        |
    | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | elbow\_state                    | The elbow state to use. Note, that franka::CartesianVelocities contains the elbow state and not the elbow velocity, contrary to [RobotVelocity](classfranky_1_1_robot_velocity.md "Cartesian velocity of a robot."). |
    | default\_elbow\_flip\_direction | The default flip direction of the elbow if it is not set.                                                                                                                                                              |
    

<!-- end list -->

  - Returns  
    The franka velocity.

</div>

</div>

<span id="ab7fe3ffb8b3a627027d6441d57223c95"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95)</span>changeEndEffectorFrame()

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
<td><a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> franky::RobotVelocity::changeEndEffectorFrame</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> Eigen::Vector3d &amp; </td>
<td><em>offset_world_frame</em></td>
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

Change the end-effector frame by adding the given offset to the current end-effector frame. Note that the offset must be given in world coordinates.

  - Parameters
    
    |                      |                                                      |
    | -------------------- | ---------------------------------------------------- |
    | offset\_world\_frame | The offset to add to the current end-effector frame. |
    

<!-- end list -->

  - Returns  
    The velocity of the new end-effector frame.

</div>

</div>

<span id="ac7f635a3ee546c5fb8c0d6ffbd3e0467"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)</span>elbow\_velocity()

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
<td>std::optional&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> &gt; franky::RobotVelocity::elbow_velocity</td>
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

Get the elbow velocity.

  - Returns  
    The elbow velocity.

</div>

</div>

<span id="addf40a07374fd18d74d84c7027291b2b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b)</span>end\_effector\_twist()

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
<td><a href="classfranky_1_1_twist.md" class="el">Twist</a> franky::RobotVelocity::end_effector_twist</td>
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

Get the end effector twist.

  - Returns  
    The end effector twist.

</div>

</div>

<span id="a7e10894668e53f945a34939cc828716e"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#a7e10894668e53f945a34939cc828716e)</span>transform() <span class="overload">\[1/2\]</span>

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
<td><a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> franky::RobotVelocity::transform</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> &amp; </td>
<td><em>affine</em></td>
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

Transform the frame of the velocity by applying the given affine transform.

  - Parameters
    
    |        |                      |
    | ------ | -------------------- |
    | affine | The affine to apply. |
    

<!-- end list -->

  - Returns  
    The velocity after the transformation.

</div>

</div>

<span id="a4e2cbc0ba39425815403cffcffdb6545"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#a4e2cbc0ba39425815403cffcffdb6545)</span>transform() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

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
<td><a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> franky::RobotVelocity::transform</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">RotationMatrixType</a> &amp; </td>
<td><em>rotation</em></td>
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

Transform the frame of the velocity by applying the given rotation.

  - Parameters
    
    |          |                        |
    | -------- | ---------------------- |
    | rotation | The rotation to apply. |
    

<!-- end list -->

  - Returns  
    The velocity after the transformation.

</div>

</div>

<span id="ab5457d7739425402e41821a66d7ab32c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c)</span>vector\_repr()

<div class="memitem">

<div class="memproto">

|                                                                                                        |   |  |   |       |
| ------------------------------------------------------------------------------------------------------ | - |  | - | ----- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotVelocity::vector\_repr | ( |  | ) | const |

</div>

<div class="memdoc">

Get the vector representation of the velocity. It consists of the linear and angular velocity of the end effector and the joint velocity of the elbow.

  - Returns  
    The vector representation of the velocity.

</div>

</div>

<span id="aa53f2a9297f426cb327ee4172bd3ccd1"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#aa53f2a9297f426cb327ee4172bd3ccd1)</span>withElbowVelocity()

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
<td><a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> franky::RobotVelocity::withElbowVelocity</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> &gt; </td>
<td><em>elbow_velocity</em></td>
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

Get the velocity with a new elbow velocity.

  - Parameters
    
    |                 |                         |
    | --------------- | ----------------------- |
    | elbow\_velocity | The new elbow velocity. |
    

<!-- end list -->

  - Returns  
    The velocity with the new elbow velocity.

</div>

</div>

## Friends And Related Symbol Documentation

<span id="a5650119c96c36dfba8aaf863df12e0aa"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_velocity.md#a5650119c96c36dfba8aaf863df12e0aa)</span>operator\<\<

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_velocity.md" class="el">RobotVelocity</a> &amp; </td>
<td><em>robot_velocity</em> </td>
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

  - /home/runner/work/franky/franky/include/franky/[robot\_velocity.hpp](robot__velocity_8hpp_source.md)
  - /home/runner/work/franky/franky/src/[robot\_velocity.cpp](robot__velocity_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
