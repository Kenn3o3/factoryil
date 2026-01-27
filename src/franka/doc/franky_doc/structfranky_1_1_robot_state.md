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
  - [RobotState](structfranky_1_1_robot_state.md)

</div>

</div>

<div class="header">

<div class="summary">

[Static Public Member Functions](structfranky_1_1_robot_state.md#pub-static-methods) | [Public Attributes](structfranky_1_1_robot_state.md#pub-attribs) | [List of all members](structfranky_1_1_robot_state-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::RobotState Struct Reference

</div>

</div>

</div>

<div class="contents">

Full state of the robot. [More...](structfranky_1_1_robot_state.md#details)

`#include <robot_state.hpp>`

## <span id="pub-static-methods"></span> Static Public Member Functions

</div>

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) 

[from\_franka](structfranky_1_1_robot_state.md#a2c4c90f4eac5e22551d97102452f8055) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::RobotState &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), std::optional\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \> [q\_est](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6)=std::nullopt, std::optional\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \> [dq\_est](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e)=std::nullopt, std::optional\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \> [ddq\_est](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c)=std::nullopt, std::optional\< [Twist](classfranky_1_1_twist.md) \> [O\_dP\_EE\_est](structfranky_1_1_robot_state.md#aa05402a790846ad287e136b0364359c6)=std::nullopt, std::optional\< [TwistAcceleration](classfranky_1_1_twist_acceleration.md) \> [O\_ddP\_EE\_est](structfranky_1_1_robot_state.md#a3a35fa21dfce2110e06f3b2476f9734e)=std::nullopt, std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> [delbow\_est](structfranky_1_1_robot_state.md#acd1c492bd7f6e10b9ecff6cc509d2f90)=std::nullopt, std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> [ddelbow\_est](structfranky_1_1_robot_state.md#ade3beb0d2a00728a316b43c1a6c15229)=std::nullopt)

 

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) 

[from\_franka](structfranky_1_1_robot_state.md#a6eef8a5ac902cc491f0f6122500e8429) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::RobotState &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) &[ee\_jacobian](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[q\_est](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[dq\_est](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[ddq\_est](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c))

 

## <span id="pub-attribs"></span> Public Attributes

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[O\_T\_EE](structfranky_1_1_robot_state.md#a0a9667e0d76a3901c0e9393a8b227c0a) {}

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[O\_T\_EE\_d](structfranky_1_1_robot_state.md#a9650368f3c772ed7d46f07f6412b3faf) {}

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[F\_T\_EE](structfranky_1_1_robot_state.md#aa2f851078b2a03f90c33a37bf13d07a1) {}

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[EE\_T\_K](structfranky_1_1_robot_state.md#a5bab6bd3d0b8e3781b80db887808be1e) {}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[m\_ee](structfranky_1_1_robot_state.md#aa5104cf1e290f362c032dd3099191bd8) {}

 

[IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) 

[I\_ee](structfranky_1_1_robot_state.md#a9646c969429e0853722837c950820f44) {}

 

Eigen::Vector3d 

[F\_x\_Cee](structfranky_1_1_robot_state.md#a32d78a9f6048cdce9f096e2a33b747f1) {}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[m\_load](structfranky_1_1_robot_state.md#ac7f17c8d7d1bb49658c872904caa8233) {}

 

[IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) 

[I\_load](structfranky_1_1_robot_state.md#ad8590b96b51241bea2620dcc482c0f9a) {}

 

Eigen::Vector3d 

[F\_x\_Cload](structfranky_1_1_robot_state.md#abbbebbf039f73e41d26193f5acebf536) {}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[m\_total](structfranky_1_1_robot_state.md#a8e8ddca4a286bfb33aa94bfbafc7666d) {}

 

[IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) 

[I\_total](structfranky_1_1_robot_state.md#a627a19dfeb245fe9929b5dba0de4516b) {}

 

Eigen::Vector3d 

[F\_x\_Ctotal](structfranky_1_1_robot_state.md#a3706cdbd18abaad5acae4b6420c6679c) {}

 

[ElbowState](classfranky_1_1_elbow_state.md) 

[elbow](structfranky_1_1_robot_state.md#aabafb74fb3a4c958ec20d1c944a58ef1) {}

 

[ElbowState](classfranky_1_1_elbow_state.md) 

[elbow\_d](structfranky_1_1_robot_state.md#aa7c69937e5e9837d62b490dcc8aa255f) {}

 

[ElbowState](classfranky_1_1_elbow_state.md) 

[elbow\_c](structfranky_1_1_robot_state.md#a69e433ddee972b5b751233b99a6643e9) {}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[delbow\_c](structfranky_1_1_robot_state.md#a3a38c0c7040b305f2d00c2388e0e451c) {}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[ddelbow\_c](structfranky_1_1_robot_state.md#ab6996c44d6d0b34e03cec086d6d16519) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[tau\_J](structfranky_1_1_robot_state.md#aa1d327630a6eedc9b3bbad3b5d7423b3) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[tau\_J\_d](structfranky_1_1_robot_state.md#a662a010406b9d9833673f5b84238abe7) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[dtau\_J](structfranky_1_1_robot_state.md#a7691ba4f68ee2c2c88138faa319156f5) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[q](structfranky_1_1_robot_state.md#adcba9f6e06d0161ee6ec2bb904e2f1cd) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[q\_d](structfranky_1_1_robot_state.md#aae25b9bee828132b2db5a669855bf16a) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[dq](structfranky_1_1_robot_state.md#ae63f90261417b37a6c731076ce4d5cc6) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[dq\_d](structfranky_1_1_robot_state.md#a3712f4da986dac8f09fa2af356a81fb9) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[ddq\_d](structfranky_1_1_robot_state.md#aadf8644c962475b364279719d4d4109f) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[joint\_contact](structfranky_1_1_robot_state.md#a2e51845f6d79feb2df6069812549c708) {}

 

[Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) 

[cartesian\_contact](structfranky_1_1_robot_state.md#a4ea218cbe444c02ba65c9e2f2d9fb9f0) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[joint\_collision](structfranky_1_1_robot_state.md#a72895f75e936aa0ff27597cac3875be3) {}

 

[Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) 

[cartesian\_collision](structfranky_1_1_robot_state.md#a7a4b2dc3fd3c5bd534b77c7ff2c44a6d) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[tau\_ext\_hat\_filtered](structfranky_1_1_robot_state.md#a255794f19c19cb60741ff2e1a3da3410) {}

 

[Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) 

[O\_F\_ext\_hat\_K](structfranky_1_1_robot_state.md#acac3a6e1b9e7f6e19c19aa5df3740b1c) {}

 

[Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) 

[K\_F\_ext\_hat\_K](structfranky_1_1_robot_state.md#a1d9419d22b2d3126f4c96b64740079e0) {}

 

[Twist](classfranky_1_1_twist.md) 

[O\_dP\_EE\_d](structfranky_1_1_robot_state.md#aa4d24e043152f36d3ad2c3d55e0a0eac) {}

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[O\_T\_EE\_c](structfranky_1_1_robot_state.md#aebb25f8a7c0e6b72f2a5f1829a97ea43) {}

 

[Twist](classfranky_1_1_twist.md) 

[O\_dP\_EE\_c](structfranky_1_1_robot_state.md#aa67ffe8b93078f07f4a3b36bb00650ad) {}

 

[TwistAcceleration](classfranky_1_1_twist_acceleration.md) 

[O\_ddP\_EE\_c](structfranky_1_1_robot_state.md#a3856ba38e33b30a04b7cca16509debde) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[theta](structfranky_1_1_robot_state.md#a87a42865d626b106dd186d3886489318) {}

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[dtheta](structfranky_1_1_robot_state.md#a80fbf260b9bbb1d9df330522b2f76568) {}

 

franka::Errors 

[current\_errors](structfranky_1_1_robot_state.md#af874b62c9e403d0c2e581aab20bebb4d) {}

 

franka::Errors 

[last\_motion\_errors](structfranky_1_1_robot_state.md#a01699ef2bcc0ac7126882755477c8cc4) {}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[control\_command\_success\_rate](structfranky_1_1_robot_state.md#a9f615eac9283d889c0b4dfe2a4ecc5c5) {}

 

franka::RobotMode 

[robot\_mode](structfranky_1_1_robot_state.md#ab2f6b32a306b39eed3170abe1b44a2d8) = franka::RobotMode::kUserStopped

 

franka::Duration 

[time](structfranky_1_1_robot_state.md#a9b00abaf922d5e0ce79ba8b9296840a6) {}

 

std::optional\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \> 

[q\_est](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6) {}

 

std::optional\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \> 

[dq\_est](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e) {}

 

std::optional\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \> 

[ddq\_est](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c) {}

 

std::optional\< [Twist](classfranky_1_1_twist.md) \> 

[O\_dP\_EE\_est](structfranky_1_1_robot_state.md#aa05402a790846ad287e136b0364359c6) {}

 

std::optional\< [TwistAcceleration](classfranky_1_1_twist_acceleration.md) \> 

[O\_ddP\_EE\_est](structfranky_1_1_robot_state.md#a3a35fa21dfce2110e06f3b2476f9734e) {}

 

std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[delbow\_est](structfranky_1_1_robot_state.md#acd1c492bd7f6e10b9ecff6cc509d2f90) {}

 

std::optional\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[ddelbow\_est](structfranky_1_1_robot_state.md#ade3beb0d2a00728a316b43c1a6c15229) {}

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Full state of the robot.

This class contains all fields of franka::RobotState and some additional fields. Each additional field ends in "\_est". Unlike franka::RobotState, all fields are converted to appropriate Eigen/franky types.

</div>

## Member Function Documentation

<span id="a6eef8a5ac902cc491f0f6122500e8429"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a6eef8a5ac902cc491f0f6122500e8429)</span>from\_franka() <span class="overload">\[1/2\]</span>

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
<td><a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> franky::RobotState::from_franka</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> franka::RobotState &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b" class="el">Jacobian</a> &amp; </td>
<td><em>ee_jacobian</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &amp; </td>
<td><em>q_est</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &amp; </td>
<td><em>dq_est</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &amp; </td>
<td><em>ddq_est</em> </td>
</tr>
<tr class="even">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">static</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a2c4c90f4eac5e22551d97102452f8055"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a2c4c90f4eac5e22551d97102452f8055)</span>from\_franka() <span class="overload">\[2/2\]</span>

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
<td><a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> franky::RobotState::from_franka</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> franka::RobotState &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::optional&lt; <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &gt; </td>
<td><em>q_est</em> = <code>std::nullopt</code>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>std::optional&lt; <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &gt; </td>
<td><em>dq_est</em> = <code>std::nullopt</code>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::optional&lt; <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &gt; </td>
<td><em>ddq_est</em> = <code>std::nullopt</code>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>std::optional&lt; <a href="classfranky_1_1_twist.md" class="el">Twist</a> &gt; </td>
<td><em>O_dP_EE_est</em> = <code>std::nullopt</code>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::optional&lt; <a href="classfranky_1_1_twist_acceleration.md" class="el">TwistAcceleration</a> &gt; </td>
<td><em>O_ddP_EE_est</em> = <code>std::nullopt</code>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>std::optional&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> &gt; </td>
<td><em>delbow_est</em> = <code>std::nullopt</code>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::optional&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> &gt; </td>
<td><em>ddelbow_est</em> = <code>std::nullopt</code> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">static</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

## Member Data Documentation

<span id="a7a4b2dc3fd3c5bd534b77c7ff2c44a6d"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a7a4b2dc3fd3c5bd534b77c7ff2c44a6d)</span>cartesian\_collision

<div class="memitem">

<div class="memproto">

|                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- |
| [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) franky::RobotState::cartesian\_collision {} |

</div>

<div class="memdoc">

Indicates which contact level is activated in which Cartesian dimension ![$(x,y,z,R,P,Y)$](https://timschneider42.github.io/franky/form_28.png). After contact disappears, the value stays the same until a reset command is sent.

  - See also  
    [Robot::setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373 "Set the collision behavior of the robot.") [for](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [setting](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [sensitivity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [values](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).
    Robot::automaticErrorRecovery [for](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [performing](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [a](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [reset](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [after](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [a](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [collision](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="a4ea218cbe444c02ba65c9e2f2d9fb9f0"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a4ea218cbe444c02ba65c9e2f2d9fb9f0)</span>cartesian\_contact

<div class="memitem">

<div class="memproto">

|                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) franky::RobotState::cartesian\_contact {} |

</div>

<div class="memdoc">

Indicates which contact level is activated in which Cartesian dimension ![$(x,y,z,R,P,Y)$](https://timschneider42.github.io/franky/form_28.png). After contact disappears, the value turns to zero.

  - See also  
    [Robot::setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373 "Set the collision behavior of the robot.") [for](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [setting](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [sensitivity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [values](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="a9f615eac9283d889c0b4dfe2a4ecc5c5"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a9f615eac9283d889c0b4dfe2a4ecc5c5)</span>control\_command\_success\_rate

<div class="memitem">

<div class="memproto">

|                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::RobotState::control\_command\_success\_rate {} |

</div>

<div class="memdoc">

Percentage of the last 100 control commands that were successfully received by the robot.

Shows a value of zero if no control or motion generator loop is currently running.

Range: ![$\[0, 1\]$](https://timschneider42.github.io/franky/form_42.png).

</div>

</div>

<span id="af874b62c9e403d0c2e581aab20bebb4d"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#af874b62c9e403d0c2e581aab20bebb4d)</span>current\_errors

<div class="memitem">

<div class="memproto">

|                                                       |
| ----------------------------------------------------- |
| franka::Errors franky::RobotState::current\_errors {} |

</div>

<div class="memdoc">

Current error state.

</div>

</div>

<span id="ab6996c44d6d0b34e03cec086d6d16519"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#ab6996c44d6d0b34e03cec086d6d16519)</span>ddelbow\_c

<div class="memitem">

<div class="memproto">

|                                                                                                    |
| -------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::RobotState::ddelbow\_c {} |

</div>

<div class="memdoc">

Commanded elbow acceleration of the 3rd joint in ![$\\frac{rad}{s^2}$](https://timschneider42.github.io/franky/form_14.png)

</div>

</div>

<span id="ade3beb0d2a00728a316b43c1a6c15229"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#ade3beb0d2a00728a316b43c1a6c15229)</span>ddelbow\_est

<div class="memitem">

<div class="memproto">

|                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- |
| std::optional\<[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\> franky::RobotState::ddelbow\_est {} |

</div>

<div class="memdoc">

Estimated elbow acceleration (acceleration of the third joint), computed by franky. Not provided by franka firmware. Unit: ![$\[\\frac{rad}{s^2}\]$](https://timschneider42.github.io/franky/form_27.png).

</div>

</div>

<span id="aadf8644c962475b364279719d4d4109f"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aadf8644c962475b364279719d4d4109f)</span>ddq\_d

<div class="memitem">

<div class="memproto">

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::ddq\_d {} |

</div>

<div class="memdoc">

![$\\ddot{q}\_d$](https://timschneider42.github.io/franky/form_26.png) Desired joint acceleration. Unit: ![$\[\\frac{rad}{s^2}\]$](https://timschneider42.github.io/franky/form_27.png)

</div>

</div>

<span id="aa3c4c83ad4b4a704665db984ebadd84c"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c)</span>ddq\_est

<div class="memitem">

<div class="memproto">

|                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------- |
| std::optional\<[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)\> franky::RobotState::ddq\_est {} |

</div>

<div class="memdoc">

Estimated joint acceleration computed by franky. This value does not come from the franka firmware. Unit: ![$\[\\frac{rad}{s^2}\]$](https://timschneider42.github.io/franky/form_27.png).

</div>

</div>

<span id="a3a38c0c7040b305f2d00c2388e0e451c"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a3a38c0c7040b305f2d00c2388e0e451c)</span>delbow\_c

<div class="memitem">

<div class="memproto">

|                                                                                                   |
| ------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::RobotState::delbow\_c {} |

</div>

<div class="memdoc">

Commanded velocity of the 3rd joint in ![$\\frac{rad}{s}$](https://timschneider42.github.io/franky/form_13.png)

</div>

</div>

<span id="acd1c492bd7f6e10b9ecff6cc509d2f90"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#acd1c492bd7f6e10b9ecff6cc509d2f90)</span>delbow\_est

<div class="memitem">

<div class="memproto">

|                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- |
| std::optional\<[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\> franky::RobotState::delbow\_est {} |

</div>

<div class="memdoc">

Estimated elbow velocity (velocity of the third joint), computed by franky. Not provided by franka firmware. Unit: ![$\[\\frac{rad}{s}\]$](https://timschneider42.github.io/franky/form_24.png).

</div>

</div>

<span id="ae63f90261417b37a6c731076ce4d5cc6"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#ae63f90261417b37a6c731076ce4d5cc6)</span>dq

<div class="memitem">

<div class="memproto">

|                                                                                              |
| -------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::dq {} |

</div>

<div class="memdoc">

![$\\dot{q}$](https://timschneider42.github.io/franky/form_23.png) Measured joint velocity. Unit: ![$\[\\frac{rad}{s}\]$](https://timschneider42.github.io/franky/form_24.png)

</div>

</div>

<span id="a3712f4da986dac8f09fa2af356a81fb9"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a3712f4da986dac8f09fa2af356a81fb9)</span>dq\_d

<div class="memitem">

<div class="memproto">

|                                                                                                 |
| ----------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::dq\_d {} |

</div>

<div class="memdoc">

![$\\dot{q}\_d$](https://timschneider42.github.io/franky/form_25.png) Desired joint velocity. Unit: ![$\[\\frac{rad}{s}\]$](https://timschneider42.github.io/franky/form_24.png)

</div>

</div>

<span id="aaea1aa7f342609aa0d8b4e917bf2c47e"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e)</span>dq\_est

<div class="memitem">

<div class="memproto">

|                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ |
| std::optional\<[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)\> franky::RobotState::dq\_est {} |

</div>

<div class="memdoc">

Estimated joint velocity computed by franky. This value does not come from the franka firmware. Unit: ![$\[\\frac{rad}{s}\]$](https://timschneider42.github.io/franky/form_24.png).

</div>

</div>

<span id="a7691ba4f68ee2c2c88138faa319156f5"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a7691ba4f68ee2c2c88138faa319156f5)</span>dtau\_J

<div class="memitem">

<div class="memproto">

|                                                                                                   |
| ------------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::dtau\_J {} |

</div>

<div class="memdoc">

![$\\dot{\\tau\_{J}}$](https://timschneider42.github.io/franky/form_18.png) Derivative of measured link-side joint torque sensor signals. Unit: ![$\[\\frac{Nm}{s}\]$](https://timschneider42.github.io/franky/form_19.png)

</div>

</div>

<span id="a80fbf260b9bbb1d9df330522b2f76568"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a80fbf260b9bbb1d9df330522b2f76568)</span>dtheta

<div class="memitem">

<div class="memproto">

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::dtheta {} |

</div>

<div class="memdoc">

![$\\dot{\\theta}$](https://timschneider42.github.io/franky/form_41.png) Motor velocity. Unit: ![$\[\\frac{rad}{s}\]$](https://timschneider42.github.io/franky/form_24.png)

</div>

</div>

<span id="a5bab6bd3d0b8e3781b80db887808be1e"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a5bab6bd3d0b8e3781b80db887808be1e)</span>EE\_T\_K

<div class="memitem">

<div class="memproto">

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) franky::RobotState::EE\_T\_K {} |

</div>

<div class="memdoc">

![$^{EE}T\_{K}$](https://timschneider42.github.io/franky/form_3.png) Stiffness frame pose in end effector frame.

See also [K frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="aabafb74fb3a4c958ec20d1c944a58ef1"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aabafb74fb3a4c958ec20d1c944a58ef1)</span>elbow

<div class="memitem">

<div class="memproto">

|                                                                             |
| --------------------------------------------------------------------------- |
| [ElbowState](classfranky_1_1_elbow_state.md) franky::RobotState::elbow {} |

</div>

<div class="memdoc">

Elbow configuration.

</div>

</div>

<span id="a69e433ddee972b5b751233b99a6643e9"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a69e433ddee972b5b751233b99a6643e9)</span>elbow\_c

<div class="memitem">

<div class="memproto">

|                                                                                |
| ------------------------------------------------------------------------------ |
| [ElbowState](classfranky_1_1_elbow_state.md) franky::RobotState::elbow\_c {} |

</div>

<div class="memdoc">

Commanded elbow configuration.

</div>

</div>

<span id="aa7c69937e5e9837d62b490dcc8aa255f"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa7c69937e5e9837d62b490dcc8aa255f)</span>elbow\_d

<div class="memitem">

<div class="memproto">

|                                                                                |
| ------------------------------------------------------------------------------ |
| [ElbowState](classfranky_1_1_elbow_state.md) franky::RobotState::elbow\_d {} |

</div>

<div class="memdoc">

Desired elbow configuration.

</div>

</div>

<span id="aa2f851078b2a03f90c33a37bf13d07a1"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa2f851078b2a03f90c33a37bf13d07a1)</span>F\_T\_EE

<div class="memitem">

<div class="memproto">

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) franky::RobotState::F\_T\_EE {} |

</div>

<div class="memdoc">

![$^{F}T\_{EE}$](https://timschneider42.github.io/franky/form_2.png) End effector frame pose in flange frame.

  - See also  
    [F\_T\_NE](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)
    [NE\_T\_EE](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)
    [Robot](classfranky_1_1_robot.md "A class representing a Franka robot.") [for](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [an](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [explanation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [of](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [the](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [F](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [NE](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [and](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [EE](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [frames](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="a32d78a9f6048cdce9f096e2a33b747f1"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a32d78a9f6048cdce9f096e2a33b747f1)</span>F\_x\_Cee

<div class="memitem">

<div class="memproto">

|                                                  |
| ------------------------------------------------ |
| Eigen::Vector3d franky::RobotState::F\_x\_Cee {} |

</div>

<div class="memdoc">

![$^{F}x\_{C\_{EE}}$](https://timschneider42.github.io/franky/form_6.png) Configured center of mass of the end effector load with respect to flange frame.

</div>

</div>

<span id="abbbebbf039f73e41d26193f5acebf536"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#abbbebbf039f73e41d26193f5acebf536)</span>F\_x\_Cload

<div class="memitem">

<div class="memproto">

|                                                    |
| -------------------------------------------------- |
| Eigen::Vector3d franky::RobotState::F\_x\_Cload {} |

</div>

<div class="memdoc">

![$^{F}x\_{C\_{load}}$](https://timschneider42.github.io/franky/form_9.png) Configured center of mass of the external load with respect to flange frame.

</div>

</div>

<span id="a3706cdbd18abaad5acae4b6420c6679c"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a3706cdbd18abaad5acae4b6420c6679c)</span>F\_x\_Ctotal

<div class="memitem">

<div class="memproto">

|                                                     |
| --------------------------------------------------- |
| Eigen::Vector3d franky::RobotState::F\_x\_Ctotal {} |

</div>

<div class="memdoc">

![$^{F}x\_{C\_{total}}$](https://timschneider42.github.io/franky/form_12.png) Combined center of mass of the end effector load and the external load with respect to flange frame.

</div>

</div>

<span id="a9646c969429e0853722837c950820f44"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a9646c969429e0853722837c950820f44)</span>I\_ee

<div class="memitem">

<div class="memproto">

|                                                                                                       |
| ----------------------------------------------------------------------------------------------------- |
| [IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) franky::RobotState::I\_ee {} |

</div>

<div class="memdoc">

![$I\_{EE}$](https://timschneider42.github.io/franky/form_5.png) Configured rotational inertia matrix of the end effector load with respect to center of mass.

</div>

</div>

<span id="ad8590b96b51241bea2620dcc482c0f9a"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#ad8590b96b51241bea2620dcc482c0f9a)</span>I\_load

<div class="memitem">

<div class="memproto">

|                                                                                                         |
| ------------------------------------------------------------------------------------------------------- |
| [IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) franky::RobotState::I\_load {} |

</div>

<div class="memdoc">

![$I\_{load}$](https://timschneider42.github.io/franky/form_8.png) Configured rotational inertia matrix of the external load with respect to center of mass.

</div>

</div>

<span id="a627a19dfeb245fe9929b5dba0de4516b"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a627a19dfeb245fe9929b5dba0de4516b)</span>I\_total

<div class="memitem">

<div class="memproto">

|                                                                                                          |
| -------------------------------------------------------------------------------------------------------- |
| [IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) franky::RobotState::I\_total {} |

</div>

<div class="memdoc">

![$I\_{total}$](https://timschneider42.github.io/franky/form_11.png) Combined rotational inertia matrix of the end effector load and the external load with respect to the center of mass.

</div>

</div>

<span id="a72895f75e936aa0ff27597cac3875be3"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a72895f75e936aa0ff27597cac3875be3)</span>joint\_collision

<div class="memitem">

<div class="memproto">

|                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::joint\_collision {} |

</div>

<div class="memdoc">

Indicates which contact level is activated in which joint. After contact disappears, the value stays the same until a reset command is sent.

  - See also  
    [Robot::setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373 "Set the collision behavior of the robot.") [for](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [setting](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [sensitivity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [values](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).
    Robot::automaticErrorRecovery [for](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [performing](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [a](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [reset](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [after](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [a](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [collision](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="a2e51845f6d79feb2df6069812549c708"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a2e51845f6d79feb2df6069812549c708)</span>joint\_contact

<div class="memitem">

<div class="memproto">

|                                                                                                          |
| -------------------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::joint\_contact {} |

</div>

<div class="memdoc">

Indicates which contact level is activated in which joint. After contact disappears, value turns to zero.

  - See also  
    [Robot::setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373 "Set the collision behavior of the robot.") [for](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [setting](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [sensitivity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [values](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="a1d9419d22b2d3126f4c96b64740079e0"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a1d9419d22b2d3126f4c96b64740079e0)</span>K\_F\_ext\_hat\_K

<div class="memitem">

<div class="memproto">

|                                                                                                             |
| ----------------------------------------------------------------------------------------------------------- |
| [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) franky::RobotState::K\_F\_ext\_hat\_K {} |

</div>

<div class="memdoc">

![$^{K}F\_{K,\\text{ext}}$](https://timschneider42.github.io/franky/form_33.png) Estimated external wrench (force, torque) acting on stiffness frame, expressed relative to the stiffness frame. Forces applied by the robot to the environment are positive, while forces applied by the environment on the robot are negative. Becomes ![$\[0,0,0,0,0,0\]$](https://timschneider42.github.io/franky/form_31.png) when near or in a singularity. See also [Stiffness frame K](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0). Unit: ![$\[N,N,N,Nm,Nm,Nm\]$](https://timschneider42.github.io/franky/form_32.png).

</div>

</div>

<span id="a01699ef2bcc0ac7126882755477c8cc4"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a01699ef2bcc0ac7126882755477c8cc4)</span>last\_motion\_errors

<div class="memitem">

<div class="memproto">

|                                                            |
| ---------------------------------------------------------- |
| franka::Errors franky::RobotState::last\_motion\_errors {} |

</div>

<div class="memdoc">

Contains the errors that aborted the previous motion.

</div>

</div>

<span id="aa5104cf1e290f362c032dd3099191bd8"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa5104cf1e290f362c032dd3099191bd8)</span>m\_ee

<div class="memitem">

<div class="memproto">

|                                                                                               |
| --------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::RobotState::m\_ee {} |

</div>

<div class="memdoc">

![$m\_{EE}$](https://timschneider42.github.io/franky/form_4.png) Configured mass of the end effector.

</div>

</div>

<span id="ac7f17c8d7d1bb49658c872904caa8233"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#ac7f17c8d7d1bb49658c872904caa8233)</span>m\_load

<div class="memitem">

<div class="memproto">

|                                                                                                 |
| ----------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::RobotState::m\_load {} |

</div>

<div class="memdoc">

![$m\_{load}$](https://timschneider42.github.io/franky/form_7.png) Configured mass of the external load.

</div>

</div>

<span id="a8e8ddca4a286bfb33aa94bfbafc7666d"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a8e8ddca4a286bfb33aa94bfbafc7666d)</span>m\_total

<div class="memitem">

<div class="memproto">

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::RobotState::m\_total {} |

</div>

<div class="memdoc">

![$m\_{total}$](https://timschneider42.github.io/franky/form_10.png) Sum of the mass of the end effector and the external load.

</div>

</div>

<span id="a3856ba38e33b30a04b7cca16509debde"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a3856ba38e33b30a04b7cca16509debde)</span>O\_ddP\_EE\_c

<div class="memitem">

<div class="memproto">

|                                                                                                   |
| ------------------------------------------------------------------------------------------------- |
| [TwistAcceleration](classfranky_1_1_twist_acceleration.md) franky::RobotState::O\_ddP\_EE\_c {} |

</div>

<div class="memdoc">

![${^OddP\_{EE}}\_{c}$](https://timschneider42.github.io/franky/form_38.png) Last commanded end effector acceleration in [base frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0). Unit: ![$\[\\frac{m}{s^2},\\frac{m}{s^2},\\frac{m}{s^2},\\frac{rad}{s^2},\\frac{rad}{s^2},\\frac{rad}{s^2}\]$](https://timschneider42.github.io/franky/form_39.png).

</div>

</div>

<span id="a3a35fa21dfce2110e06f3b2476f9734e"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a3a35fa21dfce2110e06f3b2476f9734e)</span>O\_ddP\_EE\_est

<div class="memitem">

<div class="memproto">

|                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- |
| std::optional\<[TwistAcceleration](classfranky_1_1_twist_acceleration.md)\> franky::RobotState::O\_ddP\_EE\_est {} |

</div>

<div class="memdoc">

Estimated end-effector spatial acceleration (linear and angular acceleration) expressed in [base frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0). Computed by franky; not provided by franka firmware. Unit: ![$\[\\frac{m}{s^2},\\frac{m}{s^2},\\frac{m}{s^2},\\frac{rad}{s^2},\\frac{rad}{s^2},\\frac{rad}{s^2}\]$](https://timschneider42.github.io/franky/form_39.png).

</div>

</div>

<span id="aa67ffe8b93078f07f4a3b36bb00650ad"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa67ffe8b93078f07f4a3b36bb00650ad)</span>O\_dP\_EE\_c

<div class="memitem">

<div class="memproto">

|                                                                         |
| ----------------------------------------------------------------------- |
| [Twist](classfranky_1_1_twist.md) franky::RobotState::O\_dP\_EE\_c {} |

</div>

<div class="memdoc">

![${^OdP\_{EE}}\_{c}$](https://timschneider42.github.io/franky/form_37.png) Last commanded end effector twist in [base frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="aa4d24e043152f36d3ad2c3d55e0a0eac"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa4d24e043152f36d3ad2c3d55e0a0eac)</span>O\_dP\_EE\_d

<div class="memitem">

<div class="memproto">

|                                                                         |
| ----------------------------------------------------------------------- |
| [Twist](classfranky_1_1_twist.md) franky::RobotState::O\_dP\_EE\_d {} |

</div>

<div class="memdoc">

![${^OdP\_{EE}}\_{d}$](https://timschneider42.github.io/franky/form_34.png) Desired end effector twist in [base frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0). Unit: ![$\[\\frac{m}{s},\\frac{m}{s},\\frac{m}{s},\\frac{rad}{s},\\frac{rad}{s},\\frac{rad}{s}\]$](https://timschneider42.github.io/franky/form_35.png).

</div>

</div>

<span id="aa05402a790846ad287e136b0364359c6"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa05402a790846ad287e136b0364359c6)</span>O\_dP\_EE\_est

<div class="memitem">

<div class="memproto">

|                                                                                            |
| ------------------------------------------------------------------------------------------ |
| std::optional\<[Twist](classfranky_1_1_twist.md)\> franky::RobotState::O\_dP\_EE\_est {} |

</div>

<div class="memdoc">

Estimated end-effector twist (linear and angular velocity) expressed in [base frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0). Computed by franky; not provided by franka firmware. Unit: ![$\[\\frac{m}{s},\\frac{m}{s},\\frac{m}{s},\\frac{rad}{s},\\frac{rad}{s},\\frac{rad}{s}\]$](https://timschneider42.github.io/franky/form_35.png).

</div>

</div>

<span id="acac3a6e1b9e7f6e19c19aa5df3740b1c"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#acac3a6e1b9e7f6e19c19aa5df3740b1c)</span>O\_F\_ext\_hat\_K

<div class="memitem">

<div class="memproto">

|                                                                                                             |
| ----------------------------------------------------------------------------------------------------------- |
| [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) franky::RobotState::O\_F\_ext\_hat\_K {} |

</div>

<div class="memdoc">

![$^OF\_{K,\\text{ext}}$](https://timschneider42.github.io/franky/form_30.png) Estimated external wrench (force, torque) acting on stiffness frame, expressed relative to the [base frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0). Forces applied by the robot to the environment are positive, while forces applied by the environment on the robot are negative. Becomes ![$\[0,0,0,0,0,0\]$](https://timschneider42.github.io/franky/form_31.png) when near or in a singularity. See also [Stiffness frame K](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0). Unit: ![$\[N,N,N,Nm,Nm,Nm\]$](https://timschneider42.github.io/franky/form_32.png).

</div>

</div>

<span id="a0a9667e0d76a3901c0e9393a8b227c0a"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a0a9667e0d76a3901c0e9393a8b227c0a)</span>O\_T\_EE

<div class="memitem">

<div class="memproto">

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) franky::RobotState::O\_T\_EE {} |

</div>

<div class="memdoc">

![$^{O}T\_{EE}$](https://timschneider42.github.io/franky/form_0.png) Measured end effector pose in [base frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).

</div>

</div>

<span id="aebb25f8a7c0e6b72f2a5f1829a97ea43"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aebb25f8a7c0e6b72f2a5f1829a97ea43)</span>O\_T\_EE\_c

<div class="memitem">

<div class="memproto">

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) franky::RobotState::O\_T\_EE\_c {} |

</div>

<div class="memdoc">

![${^OT\_{EE}}\_{c}$](https://timschneider42.github.io/franky/form_36.png) Last commanded end effector pose of motion generation in [base](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)frame".

</div>

</div>

<span id="a9650368f3c772ed7d46f07f6412b3faf"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a9650368f3c772ed7d46f07f6412b3faf)</span>O\_T\_EE\_d

<div class="memitem">

<div class="memproto">

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) franky::RobotState::O\_T\_EE\_d {} |

</div>

<div class="memdoc">

![${^OT\_{EE}}\_{d}$](https://timschneider42.github.io/franky/form_1.png) Last desired end effector pose of motion generation in [base](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)frame".

</div>

</div>

<span id="adcba9f6e06d0161ee6ec2bb904e2f1cd"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#adcba9f6e06d0161ee6ec2bb904e2f1cd)</span>q

<div class="memitem">

<div class="memproto">

|                                                                                             |
| ------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::q {} |

</div>

<div class="memdoc">

![$q$](https://timschneider42.github.io/franky/form_20.png) Measured joint position. Unit: ![$\[rad\]$](https://timschneider42.github.io/franky/form_21.png)

</div>

</div>

<span id="aae25b9bee828132b2db5a669855bf16a"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aae25b9bee828132b2db5a669855bf16a)</span>q\_d

<div class="memitem">

<div class="memproto">

|                                                                                                |
| ---------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::q\_d {} |

</div>

<div class="memdoc">

![$q\_d$](https://timschneider42.github.io/franky/form_22.png) Desired joint position. Unit: ![$\[rad\]$](https://timschneider42.github.io/franky/form_21.png)

</div>

</div>

<span id="a34a1ba1681f87b6f35061f9595eba3f6"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6)</span>q\_est

<div class="memitem">

<div class="memproto">

|                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------- |
| std::optional\<[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)\> franky::RobotState::q\_est {} |

</div>

<div class="memdoc">

Estimated joint position computed by franky. This value does not come from the franka firmware. Unit: ![$\[rad\]$](https://timschneider42.github.io/franky/form_21.png).

</div>

</div>

<span id="ab2f6b32a306b39eed3170abe1b44a2d8"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#ab2f6b32a306b39eed3170abe1b44a2d8)</span>robot\_mode

<div class="memitem">

<div class="memproto">

|                                                                                     |
| ----------------------------------------------------------------------------------- |
| franka::RobotMode franky::RobotState::robot\_mode = franka::RobotMode::kUserStopped |

</div>

<div class="memdoc">

Current robot mode.

</div>

</div>

<span id="a255794f19c19cb60741ff2e1a3da3410"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a255794f19c19cb60741ff2e1a3da3410)</span>tau\_ext\_hat\_filtered

<div class="memitem">

<div class="memproto">

|                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::tau\_ext\_hat\_filtered {} |

</div>

<div class="memdoc">

![$\\hat{\\tau}\_{\\text{ext}}$](https://timschneider42.github.io/franky/form_29.png) Low-pass filtered torques generated by external forces on the joints. It does not include configured end-effector and load nor the mass and dynamics of the robot. tau\_ext\_hat\_filtered is the error between tau\_J and the expected torques given by the robot model. Unit: ![$\[Nm\]$](https://timschneider42.github.io/franky/form_16.png).

</div>

</div>

<span id="aa1d327630a6eedc9b3bbad3b5d7423b3"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#aa1d327630a6eedc9b3bbad3b5d7423b3)</span>tau\_J

<div class="memitem">

<div class="memproto">

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::tau\_J {} |

</div>

<div class="memdoc">

![$\\tau\_{J}$](https://timschneider42.github.io/franky/form_15.png) Measured link-side joint torque sensor signals. Unit: ![$\[Nm\]$](https://timschneider42.github.io/franky/form_16.png)

</div>

</div>

<span id="a662a010406b9d9833673f5b84238abe7"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a662a010406b9d9833673f5b84238abe7)</span>tau\_J\_d

<div class="memitem">

<div class="memproto">

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::tau\_J\_d {} |

</div>

<div class="memdoc">

![${\\tau\_J}\_d$](https://timschneider42.github.io/franky/form_17.png) Desired link-side joint torque sensor signals without gravity. Unit: ![$\[Nm\]$](https://timschneider42.github.io/franky/form_16.png)

</div>

</div>

<span id="a87a42865d626b106dd186d3886489318"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a87a42865d626b106dd186d3886489318)</span>theta

<div class="memitem">

<div class="memproto">

|                                                                                                 |
| ----------------------------------------------------------------------------------------------- |
| [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) franky::RobotState::theta {} |

</div>

<div class="memdoc">

![$\\theta$](https://timschneider42.github.io/franky/form_40.png) Motor position. Unit: ![$\[rad\]$](https://timschneider42.github.io/franky/form_21.png)

</div>

</div>

<span id="a9b00abaf922d5e0ce79ba8b9296840a6"></span>

## <span class="permalink">[◆ ](structfranky_1_1_robot_state.md#a9b00abaf922d5e0ce79ba8b9296840a6)</span>time

<div class="memitem">

<div class="memproto">

|                                              |
| -------------------------------------------- |
| franka::Duration franky::RobotState::time {} |

</div>

<div class="memdoc">

Strictly monotonically increasing timestamp since robot start.

Inside of control loops [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) parameter of Robot::control can be used instead.

</div>

</div>

-----

The documentation for this struct was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/[robot\_state.hpp](robot__state_8hpp_source.md)
  - /home/runner/work/franky/franky/src/[robot\_state.cpp](robot__state_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
