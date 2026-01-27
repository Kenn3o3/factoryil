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
  - [Model](classfranky_1_1_model.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_model.md#pub-methods) | [List of all members](classfranky_1_1_model-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Model Class Reference

</div>

</div>

</div>

<div class="contents">

A wrapper around franka::Model that uses Eigen types. [More...](classfranky_1_1_model.md#details)

`#include <model.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[Model](classfranky_1_1_model.md#a23b131d60fb32cc5ab57c7975cd0fb28) (franka::Model model)

 

 

[Model](classfranky_1_1_model.md#a0e0f5759222c436e411fee99f1cc2d93) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Model](classfranky_1_1_model.md) &)=[delete](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[Model](classfranky_1_1_model.md) & 

[operator=](classfranky_1_1_model.md#a5b3f54790270c3d9118a9595abfbcc8f) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Model](classfranky_1_1_model.md) &)=[delete](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

 

[Model](classfranky_1_1_model.md#a277027b0b51b1f536a224c270eb12d82) ([Model](classfranky_1_1_model.md) &&[other](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [noexcept](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[Model](classfranky_1_1_model.md) & 

[operator=](classfranky_1_1_model.md#a6b540e314ea304166c0d5249b92bbf03) ([Model](classfranky_1_1_model.md) &&[other](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [noexcept](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[pose](classfranky_1_1_model.md#a09d525af34503e95214f7bd07e616e64) (franka::Frame [frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) \&state) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the pose of a frame relative to the base frame.  

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[pose](classfranky_1_1_model.md#a0f6a1b55c860153af5bb7e8a4a18c00d) (franka::Frame [frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&F\_T\_EE, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&EE\_T\_K) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the pose of a frame relative to the base frame.  

 

[Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) 

[bodyJacobian](classfranky_1_1_model.md#a2473ad35c5b1cd9f89c80293ac84b434) (franka::Frame [frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) \&state) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the body Jacobian in base frame.  

 

[Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) 

[bodyJacobian](classfranky_1_1_model.md#a133d08b266c51a524c529b35bbe7cdfd) (franka::Frame [frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&F\_T\_EE, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&EE\_T\_K) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the body Jacobian in base frame.  

 

[Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) 

[zeroJacobian](classfranky_1_1_model.md#ad5c6a7ac820f5e4df98525e3a9acda81) (franka::Frame [frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) \&state) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the zero Jacobian in base frame.  

 

[Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) 

[zeroJacobian](classfranky_1_1_model.md#af6e1970e18d0fed9695a879027ae8985) (franka::Frame [frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&F\_T\_EE, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&EE\_T\_K) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the zero Jacobian in base frame.  

 

Eigen::Matrix\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 7, 7 \> 

[mass](classfranky_1_1_model.md#a2b68eeac2f6990175097787f948d4f5b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) \&state) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the mass matrix.  

 

Eigen::Matrix\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 7, 7 \> 

[mass](classfranky_1_1_model.md#a3f07f9c967ff893475a0f76f397cff14) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Matrix3d \&I\_total, [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) m\_total, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d \&F\_x\_Ctotal) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the mass matrix.  

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[coriolis](classfranky_1_1_model.md#ab71c9e3f23f6963568f2bb42397d1599) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) \&state) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the Coriolis force vector.  

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[coriolis](classfranky_1_1_model.md#a6a405f52d262f0dbc744190646e7cf17) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&dq, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Matrix3d \&I\_total, [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) m\_total, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d \&F\_x\_Ctotal) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the Coriolis force vector.  

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[gravity](classfranky_1_1_model.md#a72889aed517ceb27c48baf30b21b20e5) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) \&state, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &[gravity\_earth](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the gravity vector.  

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[gravity](classfranky_1_1_model.md#a5a4ecdb90b14481314169f6bab3574d7) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) \&state) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the gravity vector using default gravity direction (0, 0, -9.81).  

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[gravity](classfranky_1_1_model.md#aaac1089cb473128a821f079cc86804c9) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) m\_total, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d \&F\_x\_Ctotal, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &[gravity\_earth](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)={0., 0., -9.81}) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Calculates the gravity vector.  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

A wrapper around franka::Model that uses Eigen types.

This class exposes the same functionality as franka::Model, but uses Eigen types for inputs and outputs instead of std::array. All 2D arrays are returned as Eigen matrices.

</div>

## Constructor & Destructor Documentation

<span id="a23b131d60fb32cc5ab57c7975cd0fb28"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a23b131d60fb32cc5ab57c7975cd0fb28)</span>Model() <span class="overload">\[1/3\]</span>

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
<td>franky::Model::Model</td>
<td>(</td>
<td>franka::Model </td>
<td><em>model</em></td>
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
    
    |       |                                                |
    | ----- | ---------------------------------------------- |
    | model | The underlying franka::Model instance to wrap. |
    

</div>

</div>

<span id="a0e0f5759222c436e411fee99f1cc2d93"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a0e0f5759222c436e411fee99f1cc2d93)</span>Model() <span class="overload">\[2/3\]</span>

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
<td>franky::Model::Model</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_model.md" class="el">Model</a> &amp; </td>
<td></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">delete</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a277027b0b51b1f536a224c270eb12d82"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a277027b0b51b1f536a224c270eb12d82)</span>Model() <span class="overload">\[3/3\]</span>

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
<td>franky::Model::Model</td>
<td>(</td>
<td><a href="classfranky_1_1_model.md" class="el">Model</a> &amp;&amp; </td>
<td><em>other</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">noexcept</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

## Member Function Documentation

<span id="a2473ad35c5b1cd9f89c80293ac84b434"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a2473ad35c5b1cd9f89c80293ac84b434)</span>bodyJacobian() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                                |   |                                                                                                                   |          |
| ---------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | -------- |
| [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) franky::Model::bodyJacobian | ( | franka::Frame                                                                                                     | *frame*, |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *state*  |
|                                                                                                | ) |                                                                                                                   | const    |

</div>

<div class="memdoc">

Calculates the body Jacobian in base frame.

  - Parameters
    
    |       |                                               |
    | ----- | --------------------------------------------- |
    | frame | The frame for which the Jacobian is computed. |
    | state | The current robot state.                      |
    

<!-- end list -->

  - Returns  
    The 6x7 body Jacobian matrix.

</div>

</div>

<span id="a133d08b266c51a524c529b35bbe7cdfd"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a133d08b266c51a524c529b35bbe7cdfd)</span>bodyJacobian() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                                |   |                                                                                                                                      |             |
| ---------------------------------------------------------------------------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) franky::Model::bodyJacobian | ( | franka::Frame                                                                                                                        | *frame*,    |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) & | *q*,        |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &   | *F\_T\_EE*, |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &   | *EE\_T\_K*  |
|                                                                                                | ) |                                                                                                                                      | const       |

</div>

<div class="memdoc">

Calculates the body Jacobian in base frame.

  - Parameters
    
    |          |                                                                                                  |
    | -------- | ------------------------------------------------------------------------------------------------ |
    | frame    | The frame for which the Jacobian is computed.                                                    |
    | q        | [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") joint angles \[rad\]. |
    | F\_T\_EE | Transformation from flange to end-effector frame.                                                |
    | EE\_T\_K | Transformation from end-effector frame to stiffness frame.                                       |
    

<!-- end list -->

  - Returns  
    The 6x7 body Jacobian matrix.

</div>

</div>

<span id="ab71c9e3f23f6963568f2bb42397d1599"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#ab71c9e3f23f6963568f2bb42397d1599)</span>coriolis() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                            |   |                                                                                                                   |         |   |       |
| ------------------------------------------------------------------------------------------ | - | ----------------------------------------------------------------------------------------------------------------- | ------- | - | ----- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::Model::coriolis | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *state* | ) | const |

</div>

<div class="memdoc">

Calculates the Coriolis force vector.

  - Parameters
    
    |       |                          |
    | ----- | ------------------------ |
    | state | The current robot state. |
    

<!-- end list -->

  - Returns  
    The Coriolis vector \[Nm\].

</div>

</div>

<span id="a6a405f52d262f0dbc744190646e7cf17"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a6a405f52d262f0dbc744190646e7cf17)</span>coriolis() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                            |   |                                                                                                                                      |                |
| ------------------------------------------------------------------------------------------ | - | ------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::Model::coriolis | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) & | *q*,           |
|                                                                                            |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) & | *dq*,          |
|                                                                                            |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Matrix3d &                                                    | *I\_total*,    |
|                                                                                            |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)                                                                     | *m\_total*,    |
|                                                                                            |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &                                                    | *F\_x\_Ctotal* |
|                                                                                            | ) |                                                                                                                                      | const          |

</div>

<div class="memdoc">

Calculates the Coriolis force vector.

  - Parameters
    
    |              |                                                                                                        |
    | ------------ | ------------------------------------------------------------------------------------------------------ |
    | q            | [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") joint angles \[rad\].       |
    | dq           | [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") joint velocities \[rad/s\]. |
    | I\_total     | Combined load and robot inertia \[kg·m²\].                                                             |
    | m\_total     | Combined mass of robot and load \[kg\].                                                                |
    | F\_x\_Ctotal | Center of mass relative to flange frame \[m\].                                                         |
    

<!-- end list -->

  - Returns  
    The Coriolis vector \[Nm\].

</div>

</div>

<span id="a5a4ecdb90b14481314169f6bab3574d7"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a5a4ecdb90b14481314169f6bab3574d7)</span>gravity() <span class="overload">\[1/3\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                           |   |                                                                                                                   |         |   |       |
| ----------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | ------- | - | ----- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::Model::gravity | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *state* | ) | const |

</div>

<div class="memdoc">

Calculates the gravity vector using default gravity direction (0, 0, -9.81).

  - Parameters
    
    |       |                          |
    | ----- | ------------------------ |
    | state | The current robot state. |
    

<!-- end list -->

  - Returns  
    The gravity vector \[Nm\].

</div>

</div>

<span id="a72889aed517ceb27c48baf30b21b20e5"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a72889aed517ceb27c48baf30b21b20e5)</span>gravity() <span class="overload">\[2/3\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                           |   |                                                                                                                   |                  |
| ----------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | ---------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::Model::gravity | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *state*,         |
|                                                                                           |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &                                 | *gravity\_earth* |
|                                                                                           | ) |                                                                                                                   | const            |

</div>

<div class="memdoc">

Calculates the gravity vector.

  - Parameters
    
    |                |                                        |
    | -------------- | -------------------------------------- |
    | state          | The current robot state.               |
    | gravity\_earth | Gravity vector in base frame \[m/s²\]. |
    

<!-- end list -->

  - Returns  
    The gravity vector \[Nm\].

</div>

</div>

<span id="aaac1089cb473128a821f079cc86804c9"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#aaac1089cb473128a821f079cc86804c9)</span>gravity() <span class="overload">\[3/3\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                           |   |                                                                                                                                      |                                      |
| ----------------------------------------------------------------------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::Model::gravity | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) & | *q*,                                 |
|                                                                                           |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)                                                                     | *m\_total*,                          |
|                                                                                           |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &                                                    | *F\_x\_Ctotal*,                      |
|                                                                                           |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &                                                    | *gravity\_earth* = `{0., 0., -9.81}` |
|                                                                                           | ) |                                                                                                                                      | const                                |

</div>

<div class="memdoc">

Calculates the gravity vector.

  - Parameters
    
    |                |                                                                                                  |
    | -------------- | ------------------------------------------------------------------------------------------------ |
    | q              | [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") joint angles \[rad\]. |
    | m\_total       | Combined mass of robot and load \[kg\].                                                          |
    | F\_x\_Ctotal   | Center of mass relative to flange frame \[m\].                                                   |
    | gravity\_earth | Gravity vector in base frame \[m/s²\], default is (0, 0, -9.81).                                 |
    

<!-- end list -->

  - Returns  
    The gravity vector \[Nm\].

</div>

</div>

<span id="a2b68eeac2f6990175097787f948d4f5b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a2b68eeac2f6990175097787f948d4f5b)</span>mass() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                                               |   |                                                                                                                   |         |   |       |
| ------------------------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | ------- | - | ----- |
| Eigen::Matrix\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 7, 7 \> franky::Model::mass | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *state* | ) | const |

</div>

<div class="memdoc">

Calculates the mass matrix.

  - Parameters
    
    |       |                          |
    | ----- | ------------------------ |
    | state | The current robot state. |
    

<!-- end list -->

  - Returns  
    The 7x7 mass matrix.

</div>

</div>

<span id="a3f07f9c967ff893475a0f76f397cff14"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a3f07f9c967ff893475a0f76f397cff14)</span>mass() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                                               |   |                                                                                                                                      |                |
| ------------------------------------------------------------------------------------------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| Eigen::Matrix\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 7, 7 \> franky::Model::mass | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) & | *q*,           |
|                                                                                                               |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Matrix3d &                                                    | *I\_total*,    |
|                                                                                                               |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)                                                                     | *m\_total*,    |
|                                                                                                               |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &                                                    | *F\_x\_Ctotal* |
|                                                                                                               | ) |                                                                                                                                      | const          |

</div>

<div class="memdoc">

Calculates the mass matrix.

  - Parameters
    
    |              |                                                                                                  |
    | ------------ | ------------------------------------------------------------------------------------------------ |
    | q            | [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") joint angles \[rad\]. |
    | I\_total     | Combined load and robot inertia \[kg·m²\].                                                       |
    | m\_total     | Combined mass of robot and load \[kg\].                                                          |
    | F\_x\_Ctotal | Center of mass relative to flange frame \[m\].                                                   |
    

<!-- end list -->

  - Returns  
    The 7x7 mass matrix.

</div>

</div>

<span id="a5b3f54790270c3d9118a9595abfbcc8f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a5b3f54790270c3d9118a9595abfbcc8f)</span>operator=() <span class="overload">\[1/2\]</span>

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
<td><a href="classfranky_1_1_model.md" class="el">Model</a> &amp; franky::Model::operator=</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_model.md" class="el">Model</a> &amp; </td>
<td></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">delete</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a6b540e314ea304166c0d5249b92bbf03"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a6b540e314ea304166c0d5249b92bbf03)</span>operator=() <span class="overload">\[2/2\]</span>

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
<td><a href="classfranky_1_1_model.md" class="el">Model</a> &amp; franky::Model::operator=</td>
<td>(</td>
<td><a href="classfranky_1_1_model.md" class="el">Model</a> &amp;&amp; </td>
<td><em>other</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">noexcept</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a09d525af34503e95214f7bd07e616e64"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a09d525af34503e95214f7bd07e616e64)</span>pose() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                      |   |                                                                                                                   |          |
| ------------------------------------------------------------------------------------ | - | ----------------------------------------------------------------------------------------------------------------- | -------- |
| [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) franky::Model::pose | ( | franka::Frame                                                                                                     | *frame*, |
|                                                                                      |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *state*  |
|                                                                                      | ) |                                                                                                                   | const    |

</div>

<div class="memdoc">

Calculates the pose of a frame relative to the base frame.

  - Parameters
    
    |       |                                          |
    | ----- | ---------------------------------------- |
    | frame | The frame whose pose should be returned. |
    | state | The current robot state.                 |
    

<!-- end list -->

  - Returns  
    The pose as an affine transformation matrix.

</div>

</div>

<span id="a0f6a1b55c860153af5bb7e8a4a18c00d"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#a0f6a1b55c860153af5bb7e8a4a18c00d)</span>pose() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                      |   |                                                                                                                                      |             |
| ------------------------------------------------------------------------------------ | - | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) franky::Model::pose | ( | franka::Frame                                                                                                                        | *frame*,    |
|                                                                                      |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) & | *q*,        |
|                                                                                      |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &   | *F\_T\_EE*, |
|                                                                                      |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &   | *EE\_T\_K*  |
|                                                                                      | ) |                                                                                                                                      | const       |

</div>

<div class="memdoc">

Calculates the pose of a frame relative to the base frame.

  - Parameters
    
    |          |                                                                                                  |
    | -------- | ------------------------------------------------------------------------------------------------ |
    | frame    | The frame whose pose should be returned.                                                         |
    | q        | [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") joint angles \[rad\]. |
    | F\_T\_EE | Transformation from flange to end-effector frame.                                                |
    | EE\_T\_K | Transformation from end-effector frame to stiffness frame.                                       |
    

<!-- end list -->

  - Returns  
    The pose as an affine transformation matrix.

</div>

</div>

<span id="ad5c6a7ac820f5e4df98525e3a9acda81"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#ad5c6a7ac820f5e4df98525e3a9acda81)</span>zeroJacobian() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                                |   |                                                                                                                   |          |
| ---------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | -------- |
| [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) franky::Model::zeroJacobian | ( | franka::Frame                                                                                                     | *frame*, |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *state*  |
|                                                                                                | ) |                                                                                                                   | const    |

</div>

<div class="memdoc">

Calculates the zero Jacobian in base frame.

  - Parameters
    
    |       |                                               |
    | ----- | --------------------------------------------- |
    | frame | The frame for which the Jacobian is computed. |
    | state | The current robot state.                      |
    

<!-- end list -->

  - Returns  
    The 6x7 zero Jacobian matrix.

</div>

</div>

<span id="af6e1970e18d0fed9695a879027ae8985"></span>

## <span class="permalink">[◆ ](classfranky_1_1_model.md#af6e1970e18d0fed9695a879027ae8985)</span>zeroJacobian() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                                |   |                                                                                                                                      |             |
| ---------------------------------------------------------------------------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) franky::Model::zeroJacobian | ( | franka::Frame                                                                                                                        | *frame*,    |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) & | *q*,        |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &   | *F\_T\_EE*, |
|                                                                                                |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &   | *EE\_T\_K*  |
|                                                                                                | ) |                                                                                                                                      | const       |

</div>

<div class="memdoc">

Calculates the zero Jacobian in base frame.

  - Parameters
    
    |          |                                                                                                  |
    | -------- | ------------------------------------------------------------------------------------------------ |
    | frame    | The frame for which the Jacobian is computed.                                                    |
    | q        | [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") joint angles \[rad\]. |
    | F\_T\_EE | Transformation from flange to end-effector frame.                                                |
    | EE\_T\_K | Transformation from end-effector frame to stiffness frame.                                       |
    

<!-- end list -->

  - Returns  
    The 6x7 zero Jacobian matrix.

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/[model.hpp](model_8hpp_source.md)
  - /home/runner/work/franky/franky/src/[model.cpp](model_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
