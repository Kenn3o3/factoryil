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
  - [ElbowState](classfranky_1_1_elbow_state.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_elbow_state.md#pub-methods) | [Friends](classfranky_1_1_elbow_state.md#friends) | [List of all members](classfranky_1_1_elbow_state-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::ElbowState Class Reference

</div>

</div>

</div>

<div class="contents">

Elbow state of the robot. [More...](classfranky_1_1_elbow_state.md#details)

`#include <elbow_state.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[ElbowState](classfranky_1_1_elbow_state.md#abc13ca8cf645d4bdd8b936ae8beab299) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [joint\_3\_pos](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114), std::optional\< [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) \> [joint\_4\_flip](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83)=std::nullopt)

 

Construct an elbow state with the given joint position and optional flip direction.  

 

 

[ElbowState](classfranky_1_1_elbow_state.md#a01b565b6678b46b95ef784d5a47b83b3) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 2 \> \&elbow\_state)

 

Construct an elbow state from an array containing joint position and flip direction.  

 

 

[ElbowState](classfranky_1_1_elbow_state.md#adba9c9a3810c45135ce0401ddd4c291a) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ElbowState](classfranky_1_1_elbow_state.md) &)=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

 

[ElbowState](classfranky_1_1_elbow_state.md#acd2cbc41647013ac53c521f07e9aa8ba) ()=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 2 \> 

[to\_array](classfranky_1_1_elbow_state.md#a314ba82485911da7ddae7b6cd4c2f548) ([FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) [default\_flip\_direction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=[FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the joint position and flip direction as an array.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[joint\_3\_pos](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

The position of the 3rd joint.  

 

std::optional\< [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) \> 

[joint\_4\_flip](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

The flip direction of the 4th joint.  

 

## <span id="friends"></span> Friends

std::ostream & 

[operator\<\<](classfranky_1_1_elbow_state.md#a09b74291d96ecf82b9d9a0fff0761d09) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ElbowState](classfranky_1_1_elbow_state.md) \&elbow\_state)

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Elbow state of the robot.

This class encapsulates the elbow state of a robot, which comprises the position of the 3rd joint and the flip direction of the 4th joint. For details see <https://frankarobotics.github.io/libfranka/0.15.3/structfranka_1_1RobotState.md#a43485841c427d70e7f36a912cc3116d1>

</div>

## Constructor & Destructor Documentation

<span id="abc13ca8cf645d4bdd8b936ae8beab299"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#abc13ca8cf645d4bdd8b936ae8beab299)</span>ElbowState() <span class="overload">\[1/4\]</span>

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
<td>franky::ElbowState::ElbowState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> </td>
<td><em>joint_3_pos</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::optional&lt; <a href="namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b" class="el">FlipDirection</a> &gt; </td>
<td><em>joint_4_flip</em> = <code>std::nullopt</code> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">explicit</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Construct an elbow state with the given joint position and optional flip direction.

  - Parameters
    
    |                |                                      |
    | -------------- | ------------------------------------ |
    | joint\_3\_pos  | The position of the 3rd joint.       |
    | joint\_4\_flip | The flip direction of the 4th joint. |
    

</div>

</div>

<span id="a01b565b6678b46b95ef784d5a47b83b3"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#a01b565b6678b46b95ef784d5a47b83b3)</span>ElbowState() <span class="overload">\[2/4\]</span>

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
<td>franky::ElbowState::ElbowState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::array&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a>, 2 &gt; &amp; </td>
<td><em>elbow_state</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">explicit</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Construct an elbow state from an array containing joint position and flip direction.

  - Parameters
    
    |              |                                                          |
    | ------------ | -------------------------------------------------------- |
    | elbow\_state | The joint position and flip direction as a double array. |
    

</div>

</div>

<span id="adba9c9a3810c45135ce0401ddd4c291a"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#adba9c9a3810c45135ce0401ddd4c291a)</span>ElbowState() <span class="overload">\[3/4\]</span>

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
<td>franky::ElbowState::ElbowState</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_elbow_state.md" class="el">ElbowState</a> &amp; </td>
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

<span id="acd2cbc41647013ac53c521f07e9aa8ba"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#acd2cbc41647013ac53c521f07e9aa8ba)</span>ElbowState() <span class="overload">\[4/4\]</span>

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
<td>franky::ElbowState::ElbowState</td>
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

<span id="a8b6265a31a63ec23b100b78f874ca114"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114)</span>joint\_3\_pos()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> franky::ElbowState::joint_3_pos</td>
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

The position of the 3rd joint.

</div>

</div>

<span id="aa9a9b7ec1565e0b1fc5c5d5932148d83"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83)</span>joint\_4\_flip()

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
<td>std::optional&lt; <a href="namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b" class="el">FlipDirection</a> &gt; franky::ElbowState::joint_4_flip</td>
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

The flip direction of the 4th joint.

</div>

</div>

<span id="a314ba82485911da7ddae7b6cd4c2f548"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#a314ba82485911da7ddae7b6cd4c2f548)</span>to\_array()

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
<td>std::array&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a>, 2 &gt; franky::ElbowState::to_array</td>
<td>(</td>
<td><a href="namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b" class="el">FlipDirection</a> </td>
<td><em>default_flip_direction</em> = <code>FlipDirection::kNegative</code></td>
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

Get the joint position and flip direction as an array.

  - Parameters
    
    |                          |                                                          |
    | ------------------------ | -------------------------------------------------------- |
    | default\_flip\_direction | The default flip direction to use if not explicitly set. |
    

<!-- end list -->

  - Returns  
    std::array containing the joint position and flip direction.

</div>

</div>

## Friends And Related Symbol Documentation

<span id="a09b74291d96ecf82b9d9a0fff0761d09"></span>

## <span class="permalink">[◆ ](classfranky_1_1_elbow_state.md#a09b74291d96ecf82b9d9a0fff0761d09)</span>operator\<\<

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_elbow_state.md" class="el">ElbowState</a> &amp; </td>
<td><em>elbow_state</em> </td>
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

  - /home/runner/work/franky/franky/include/franky/[elbow\_state.hpp](elbow__state_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
