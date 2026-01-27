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
  - [Condition](classfranky_1_1_condition.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Types](classfranky_1_1_condition.md#pub-types) | [Public Member Functions](classfranky_1_1_condition.md#pub-methods) | [List of all members](classfranky_1_1_condition-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Condition Class Reference

</div>

</div>

</div>

<div class="contents">

A condition on the robot state. [More...](classfranky_1_1_condition.md#details)

`#include <condition.hpp>`

## <span id="pub-types"></span> Public Types

</div>

[using](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[CheckFunc](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4) = std::function\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\>

 

## <span id="pub-methods"></span> Public Member Functions

 

[Condition](classfranky_1_1_condition.md#adf78d10504bce34caef779390e108644) ([CheckFunc](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4) [check\_func](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), std::string [repr](classfranky_1_1_condition.md#afaae7e02e68860afdf7c40a75bf91d25)="NULL")

 

 

[Condition](classfranky_1_1_condition.md#af73a963ea6eab3309116b399b9726c76) ([bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [constant\_value](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Implicit constructor for constant conditions.  

 

[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[operator()](classfranky_1_1_condition.md#ac8859034fd1f80137f0b87dc5efbb22b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Check if the condition is met.  

 

std::string 

[repr](classfranky_1_1_condition.md#afaae7e02e68860afdf7c40a75bf91d25) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

The string representation of the condition.  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

A condition on the robot state.

This class defines a condition on the robot state, which can be used to define a condition for a reaction in a motion. Conditions support logical operations (&&, ||, ==, \!=, \!) and can be combined to form more complex conditions.

</div>

## Member Typedef Documentation

<span id="ae0ccd93e225b1433e704b51767958eb4"></span>

## <span class="permalink">[◆ ](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4)</span>CheckFunc

<div class="memitem">

<div class="memproto">

|                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [using](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Condition::CheckFunc](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4) = std::function\<[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\> |

</div>

<div class="memdoc">

</div>

</div>

## Constructor & Destructor Documentation

<span id="adf78d10504bce34caef779390e108644"></span>

## <span class="permalink">[◆ ](classfranky_1_1_condition.md#adf78d10504bce34caef779390e108644)</span>Condition() <span class="overload">\[1/2\]</span>

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
<td>franky::Condition::Condition</td>
<td>(</td>
<td><a href="classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4" class="el">Condition::CheckFunc</a> </td>
<td><em>check_func</em>,</td>
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
    
    |             |                                                       |
    | ----------- | ----------------------------------------------------- |
    | check\_func | A function that returns true if the condition is met. |
    | repr        | A string representation of the condition.             |
    

</div>

</div>

<span id="af73a963ea6eab3309116b399b9726c76"></span>

## <span class="permalink">[◆ ](classfranky_1_1_condition.md#af73a963ea6eab3309116b399b9726c76)</span>Condition() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                              |   |                                                                |                   |   |  |
| ---------------------------- | - | -------------------------------------------------------------- | ----------------- | - |  |
| franky::Condition::Condition | ( | [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *constant\_value* | ) |  |

</div>

<div class="memdoc">

Implicit constructor for constant conditions.

  - Parameters
    
    |                 |                                      |
    | --------------- | ------------------------------------ |
    | constant\_value | The constant value of the condition. |
    

</div>

</div>

## Member Function Documentation

<span id="ac8859034fd1f80137f0b87dc5efbb22b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_condition.md#ac8859034fd1f80137f0b87dc5efbb22b)</span>operator()()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> franky::Condition::operator()</td>
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

Check if the condition is met.

  - Parameters
    
    |              |                                                                                                                                                                                                      |
    | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | robot\_state | The current robot state.                                                                                                                                                                             |
    | rel\_time    | The time since the start of the current motion.                                                                                                                                                      |
    | abs\_time    | The time since the start of the current chain of motions. This value measures the time since the robot started moving, and is only reset if a motion expires without being replaced by a new motion. |
    

<!-- end list -->

  - Returns  
    True if the condition is met.

</div>

</div>

<span id="afaae7e02e68860afdf7c40a75bf91d25"></span>

## <span class="permalink">[◆ ](classfranky_1_1_condition.md#afaae7e02e68860afdf7c40a75bf91d25)</span>repr()

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
<td>std::string franky::Condition::repr</td>
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

The string representation of the condition.

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/motion/[condition.hpp](condition_8hpp_source.md)
  - /home/runner/work/franky/franky/src/motion/[condition.cpp](condition_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
