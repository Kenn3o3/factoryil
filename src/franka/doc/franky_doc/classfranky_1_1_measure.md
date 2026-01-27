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
  - [Measure](classfranky_1_1_measure.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_measure.md#pub-methods) | [Static Public Member Functions](classfranky_1_1_measure.md#pub-static-methods) | [List of all members](classfranky_1_1_measure-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Measure Class Reference

</div>

</div>

</div>

<div class="contents">

A measure on the robot state. [More...](classfranky_1_1_measure.md#details)

`#include <measure.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[Measure](classfranky_1_1_measure.md#a8e0c418da6a3bea828dfd95e50d25d5f) (MeasureFunc [measure\_func](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), std::string [repr](classfranky_1_1_measure.md#a664d5e3506c4665f2be173ec5d2afa6f)="NULL")

 

 

[Measure](classfranky_1_1_measure.md#aefc991686a8b710643f1aa55ffd69c6c) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [constant](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Implicit constructor for constant measures.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[operator()](classfranky_1_1_measure.md#a014ae0622c47aee2a4dd9b9a781d4760) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the value of the measure.  

 

std::string 

[repr](classfranky_1_1_measure.md#a664d5e3506c4665f2be173ec5d2afa6f) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

The string representation of the measure.  

 

## <span id="pub-static-methods"></span> Static Public Member Functions

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) 

[ForceX](classfranky_1_1_measure.md#a7aa92d415e33ca64b07aa598cb5e9ec4) ()

 

A measure that returns the linear force on the end-effector in X direction as by the O\_F\_ext\_hat\_K component of the robot state.  

 

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) 

[ForceY](classfranky_1_1_measure.md#a47fbb5bf68412799ab22234596832793) ()

 

A measure that returns the linear force on the end-effector in Y direction as by the O\_F\_ext\_hat\_K component of the robot state.  

 

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) 

[ForceZ](classfranky_1_1_measure.md#a9f8c4110a4ee5a1b102efaa6a424b0f3) ()

 

A measure that returns the linear force on the end-effector in Z direction as by the O\_F\_ext\_hat\_K component of the robot state.  

 

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) 

[RelTime](classfranky_1_1_measure.md#adc0787238886a53313c11870e58c4d10) ()

 

A measure that returns the relative time since the start of the current motion.  

 

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) 

[AbsTime](classfranky_1_1_measure.md#a98d3cc1b9f211b042de9fd2238938fbc) ()

 

A measure that returns the absolute time since the start of the current chain of motions. The absolute time measures the time since the robot started moving, and is only reset if a motion expires without being replaced by a new motion.  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

A measure on the robot state.

This class defines a measure on the robot state, which can be used to define a condition for a reaction in a motion. Measures support arithmetic operations (+, -, \*, /, ^) and comparisons (==, \!=, \<, \>, \<=, \>=) and can be combined to form more complex measures.

</div>

## Constructor & Destructor Documentation

<span id="a8e0c418da6a3bea828dfd95e50d25d5f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#a8e0c418da6a3bea828dfd95e50d25d5f)</span>Measure() <span class="overload">\[1/2\]</span>

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
<td>franky::Measure::Measure</td>
<td>(</td>
<td>Measure::MeasureFunc </td>
<td><em>measure_func</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::string </td>
<td><em>repr</em> = <code>"NULL"</code> </td>
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
    
    |               |                                                   |
    | ------------- | ------------------------------------------------- |
    | measure\_func | A function that returns the value of the measure. |
    | repr          | A string representation of the measure.           |
    

</div>

</div>

<span id="aefc991686a8b710643f1aa55ffd69c6c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#aefc991686a8b710643f1aa55ffd69c6c)</span>Measure() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                          |   |                                                                  |            |   |  |
| ------------------------ | - | ---------------------------------------------------------------- | ---------- | - |  |
| franky::Measure::Measure | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *constant* | ) |  |

</div>

<div class="memdoc">

Implicit constructor for constant measures.

  - Parameters
    
    |          |                                    |
    | -------- | ---------------------------------- |
    | constant | The constant value of the measure. |
    

</div>

</div>

## Member Function Documentation

<span id="a98d3cc1b9f211b042de9fd2238938fbc"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#a98d3cc1b9f211b042de9fd2238938fbc)</span>AbsTime()

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
<td><a href="classfranky_1_1_measure.md" class="el">Measure</a> franky::Measure::AbsTime</td>
<td>(</td>
<td></td>
<td>)</td>
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

A measure that returns the absolute time since the start of the current chain of motions. The absolute time measures the time since the robot started moving, and is only reset if a motion expires without being replaced by a new motion.

</div>

</div>

<span id="a7aa92d415e33ca64b07aa598cb5e9ec4"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#a7aa92d415e33ca64b07aa598cb5e9ec4)</span>ForceX()

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
<td><a href="classfranky_1_1_measure.md" class="el">Measure</a> franky::Measure::ForceX</td>
<td>(</td>
<td></td>
<td>)</td>
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

A measure that returns the linear force on the end-effector in X direction as by the O\_F\_ext\_hat\_K component of the robot state.

</div>

</div>

<span id="a47fbb5bf68412799ab22234596832793"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#a47fbb5bf68412799ab22234596832793)</span>ForceY()

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
<td><a href="classfranky_1_1_measure.md" class="el">Measure</a> franky::Measure::ForceY</td>
<td>(</td>
<td></td>
<td>)</td>
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

A measure that returns the linear force on the end-effector in Y direction as by the O\_F\_ext\_hat\_K component of the robot state.

</div>

</div>

<span id="a9f8c4110a4ee5a1b102efaa6a424b0f3"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#a9f8c4110a4ee5a1b102efaa6a424b0f3)</span>ForceZ()

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
<td><a href="classfranky_1_1_measure.md" class="el">Measure</a> franky::Measure::ForceZ</td>
<td>(</td>
<td></td>
<td>)</td>
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

A measure that returns the linear force on the end-effector in Z direction as by the O\_F\_ext\_hat\_K component of the robot state.

</div>

</div>

<span id="a014ae0622c47aee2a4dd9b9a781d4760"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#a014ae0622c47aee2a4dd9b9a781d4760)</span>operator()()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> franky::Measure::operator()</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>rel_time</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>abs_time</em> </td>
</tr>
<tr class="even">
<td></td>
<td>)</td>
<td></td>
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

Get the value of the measure.

  - Parameters
    
    |              |                                                                                                                                                                                                      |
    | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | robot\_state | The current robot state.                                                                                                                                                                             |
    | rel\_time    | The time since the start of the current motion.                                                                                                                                                      |
    | abs\_time    | The time since the start of the current chain of motions. This value measures the time since the robot started moving, and is only reset if a motion expires without being replaced by a new motion. |
    

<!-- end list -->

  - Returns  
    The value of the measure.

</div>

</div>

<span id="adc0787238886a53313c11870e58c4d10"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#adc0787238886a53313c11870e58c4d10)</span>RelTime()

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
<td><a href="classfranky_1_1_measure.md" class="el">Measure</a> franky::Measure::RelTime</td>
<td>(</td>
<td></td>
<td>)</td>
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

A measure that returns the relative time since the start of the current motion.

</div>

</div>

<span id="a664d5e3506c4665f2be173ec5d2afa6f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_measure.md#a664d5e3506c4665f2be173ec5d2afa6f)</span>repr()

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
<td>std::string franky::Measure::repr</td>
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

The string representation of the measure.

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/motion/[measure.hpp](measure_8hpp_source.md)
  - /home/runner/work/franky/franky/src/motion/[measure.cpp](measure_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
