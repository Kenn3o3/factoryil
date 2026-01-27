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
  - [Reaction](classfranky_1_1_reaction.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_reaction.md#pub-methods) | [List of all members](classfranky_1_1_reaction-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Reaction\< ControlSignalType \> Class Template Reference

</div>

</div>

</div>

<div class="contents">

A reaction that can be attached to a motion. [More...](classfranky_1_1_reaction.md#details)

`#include <reaction.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[Reaction](classfranky_1_1_reaction.md#ad19e535f89aa97ec6b949ca48390510d) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Condition](classfranky_1_1_condition.md) &[condition](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710), std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [new\_motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=[nullptr](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

 

[Reaction](classfranky_1_1_reaction.md#a2bf1b2f2d5450e197e76f6d556694954) ([Condition](classfranky_1_1_condition.md) [condition](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) MotionFunc &[motion\_func](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> 

[operator()](classfranky_1_1_reaction.md#ae2e5dd1a61d3649d638227afbc159aed) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Get the new motion if the condition is met.  

 

[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[condition](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Check if the condition is met.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[registerCallback](classfranky_1_1_reaction.md#a7c6c3d1f2cbe80981574bf62137a8951) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::function\< [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\> &[callback](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Register a callback that is called when the condition of this reaction is met.  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

<div class="compoundTemplParams">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac)\>  
class franky::Reaction\< ControlSignalType \>

</div>

A reaction that can be attached to a motion.

This class defines a reaction in a motion, which can be used to change the motion based on the robot state. Reactions consist of a condition and a motion that replaces the current motion immediately if the condition is met.

</div>

## Constructor & Destructor Documentation

<span id="ad19e535f89aa97ec6b949ca48390510d"></span>

## <span class="permalink">[◆ ](classfranky_1_1_reaction.md#ad19e535f89aa97ec6b949ca48390510d)</span>Reaction() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="classfranky_1_1_reaction.md" class="el">franky::Reaction</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::Reaction</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_condition.md" class="el">Condition</a> &amp; </td>
<td><em>condition</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::shared_ptr&lt; <a href="classfranky_1_1_motion.md" class="el">Motion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &gt; </td>
<td><em>new_motion</em> = <code>nullptr</code> </td>
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
    
    |             |                                                                 |
    | ----------- | --------------------------------------------------------------- |
    | condition   | The condition that must be met for the reaction to be executed. |
    | new\_motion | The motion that is executed if the condition is met.            |
    

</div>

</div>

<span id="a2bf1b2f2d5450e197e76f6d556694954"></span>

## <span class="permalink">[◆ ](classfranky_1_1_reaction.md#a2bf1b2f2d5450e197e76f6d556694954)</span>Reaction() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="classfranky_1_1_reaction.md" class="el">franky::Reaction</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::Reaction</td>
<td>(</td>
<td><a href="classfranky_1_1_condition.md" class="el">Condition</a> </td>
<td><em>condition</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> MotionFunc &amp; </td>
<td><em>motion_func</em> </td>
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
    
    |              |                                                                            |
    | ------------ | -------------------------------------------------------------------------- |
    | condition    | The condition that must be met for the reaction to be executed.            |
    | motion\_func | A function that returns a motion that is executed if the condition is met. |
    

</div>

</div>

## Member Function Documentation

<span id="a12dac9b49fbe8e6f57f90b802ba05710"></span>

## <span class="permalink">[◆ ](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710)</span>condition()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> <a href="classfranky_1_1_reaction.md" class="el">franky::Reaction</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::condition</td>
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
    True if the condition is met, false otherwise.

</div>

</div>

<span id="ae2e5dd1a61d3649d638227afbc159aed"></span>

## <span class="permalink">[◆ ](classfranky_1_1_reaction.md#ae2e5dd1a61d3649d638227afbc159aed)</span>operator()()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                                                                                                                                       |   |                                                                                                                   |                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [franky::Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>[::operator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)() | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *robot\_state*, |
|                                                                                                                                                                                                                                                                                                                                                       |   | franka::Duration                                                                                                  | *rel\_time*,    |
|                                                                                                                                                                                                                                                                                                                                                       |   | franka::Duration                                                                                                  | *abs\_time*     |
|                                                                                                                                                                                                                                                                                                                                                       | ) |                                                                                                                   |                 |

</div>

<div class="memdoc">

Get the new motion if the condition is met.

  - Parameters
    
    |              |                                                                                                                                                                                                      |
    | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | robot\_state | The current robot state.                                                                                                                                                                             |
    | rel\_time    | The time since the start of the current motion.                                                                                                                                                      |
    | abs\_time    | The time since the start of the current chain of motions. This value measures the time since the robot started moving, and is only reset if a motion expires without being replaced by a new motion. |
    

<!-- end list -->

  - Returns  
    The new motion if the condition is met, or nullptr otherwise.

</div>

</div>

<span id="a7c6c3d1f2cbe80981574bf62137a8951"></span>

## <span class="permalink">[◆ ](classfranky_1_1_reaction.md#a7c6c3d1f2cbe80981574bf62137a8951)</span>registerCallback()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                     |   |                                                                                                                                                                                                                                                                                                           |            |   |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::registerCallback | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::function\< [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\> & | *callback* | ) |  |

</div>

<div class="memdoc">

Register a callback that is called when the condition of this reaction is met.

  - Parameters
    
    |          |                                                                                                                           |
    | -------- | ------------------------------------------------------------------------------------------------------------------------- |
    | callback | The callback to register. Callbacks are called with the robot state, the relative time \[s\] and the absolute time \[s\]. |
    

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/motion/[motion.hpp](motion_8hpp_source.md)
  - /home/runner/work/franky/franky/include/franky/motion/[reaction.hpp](reaction_8hpp_source.md)
  - /home/runner/work/franky/franky/src/motion/[reaction.cpp](reaction_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
