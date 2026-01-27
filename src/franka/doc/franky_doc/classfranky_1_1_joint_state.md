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
  - [JointState](classfranky_1_1_joint_state.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_joint_state.md#pub-methods) | [Friends](classfranky_1_1_joint_state.md#friends) | [List of all members](classfranky_1_1_joint_state-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::JointState Class Reference

</div>

</div>

</div>

<div class="contents">

Joint state of a robot. [More...](classfranky_1_1_joint_state.md#details)

`#include <joint_state.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[JointState](classfranky_1_1_joint_state.md#a58de323134a7b11599dafbcb3d9fcf1c) ([Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0))

 

Construct a joint state with the given joint positions and zero velocities.  

 

 

[JointState](classfranky_1_1_joint_state.md#ad4a1bcb1c1f08f59f160c64f05462c1b) ([Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0), [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100))

 

 

[JointState](classfranky_1_1_joint_state.md#a568e0e11672f5d9ad1f42b1d6cb9a576) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [JointState](classfranky_1_1_joint_state.md) &)=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

 

[JointState](classfranky_1_1_joint_state.md#a330222fd0fea56aef1c1a7a6eb918e9b) ()=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

The position component of the state.  

 

[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) 

[velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

The velocity component of the state.  

 

## <span id="friends"></span> Friends

std::ostream & 

[operator\<\<](classfranky_1_1_joint_state.md#a2b906651631f453efd46507ffbee9a5a) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [JointState](classfranky_1_1_joint_state.md) &[joint\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Joint state of a robot.

This class encapsulates the joint state of a robot, which comprises the joint positions and the joint velocities.

</div>

## Constructor & Destructor Documentation

<span id="a58de323134a7b11599dafbcb3d9fcf1c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_joint_state.md#a58de323134a7b11599dafbcb3d9fcf1c)</span>JointState() <span class="overload">\[1/4\]</span>

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
<td>franky::JointState::JointState</td>
<td>(</td>
<td><a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> </td>
<td><em>position</em></td>
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

Construct a joint state with the given joint positions and zero velocities.

  - Parameters
    
    |          |                      |
    | -------- | -------------------- |
    | position | The joint positions. |
    

</div>

</div>

<span id="ad4a1bcb1c1f08f59f160c64f05462c1b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_joint_state.md#ad4a1bcb1c1f08f59f160c64f05462c1b)</span>JointState() <span class="overload">\[2/4\]</span>

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
<td>franky::JointState::JointState</td>
<td>(</td>
<td><a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> </td>
<td><em>position</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> </td>
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
    
    |          |                       |
    | -------- | --------------------- |
    | position | The joint positions.  |
    | velocity | The joint velocities. |
    

</div>

</div>

<span id="a568e0e11672f5d9ad1f42b1d6cb9a576"></span>

## <span class="permalink">[◆ ](classfranky_1_1_joint_state.md#a568e0e11672f5d9ad1f42b1d6cb9a576)</span>JointState() <span class="overload">\[3/4\]</span>

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
<td>franky::JointState::JointState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_joint_state.md" class="el">JointState</a> &amp; </td>
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

<span id="a330222fd0fea56aef1c1a7a6eb918e9b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_joint_state.md#a330222fd0fea56aef1c1a7a6eb918e9b)</span>JointState() <span class="overload">\[4/4\]</span>

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
<td>franky::JointState::JointState</td>
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

<span id="addd9bedce775d28cef880644b635ccf0"></span>

## <span class="permalink">[◆ ](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0)</span>position()

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
<td><a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> franky::JointState::position</td>
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

The position component of the state.

</div>

</div>

<span id="a5210d159dcb06ea28000f90060acf100"></span>

## <span class="permalink">[◆ ](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100)</span>velocity()

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
<td><a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> franky::JointState::velocity</td>
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

The velocity component of the state.

</div>

</div>

## Friends And Related Symbol Documentation

<span id="a2b906651631f453efd46507ffbee9a5a"></span>

## <span class="permalink">[◆ ](classfranky_1_1_joint_state.md#a2b906651631f453efd46507ffbee9a5a)</span>operator\<\<

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_joint_state.md" class="el">JointState</a> &amp; </td>
<td><em>joint_state</em> </td>
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

  - /home/runner/work/franky/franky/include/franky/[joint\_state.hpp](joint__state_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
