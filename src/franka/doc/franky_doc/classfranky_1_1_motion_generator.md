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
  - [MotionGenerator](classfranky_1_1_motion_generator.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_motion_generator.md#pub-methods) | [Static Public Attributes](classfranky_1_1_motion_generator.md#pub-static-attribs) | [List of all members](classfranky_1_1_motion_generator-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::MotionGenerator\< ControlSignalType \> Class Template Reference

</div>

</div>

</div>

<div class="contents">

Helper class for handling motions and reactions. [More...](classfranky_1_1_motion_generator.md#details)

`#include <motion_generator.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[MotionGenerator](classfranky_1_1_motion_generator.md#a629d006e1c4b920cd4e1240a5b4e435c) ([Robot](classfranky_1_1_robot.md) \*robot, std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [initial\_motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) 

[operator()](classfranky_1_1_motion_generator.md#a751c6f2d51740e613c6575b1f62e1dfa) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [period](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Update the motion generator and get the next control signal.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[registerUpdateCallback](classfranky_1_1_motion_generator.md#a771a92b07e8c384ec56fd014841ed5f2) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::function\< [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\> &[callback](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Register a callback that is called in every step of the motion.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[updateMotion](classfranky_1_1_motion_generator.md#aecb5394cc1571687e1117e268f91e9c1) (std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [new\_motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Update the current motion.  

 

[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[has\_new\_motion](classfranky_1_1_motion_generator.md#ad0abb8a6c37b8ab8208810bb58250bf8) ()

 

Whether a new motion is available.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[resetTimeUnsafe](classfranky_1_1_motion_generator.md#aaa6cf6fa7c6af2d7b081b19d569c2e0f) ()

 

Reset the time of the motion generator without locking the mutex.  

 

## <span id="pub-static-attribs"></span> Static Public Attributes

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [constexpr](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[REACTION\_RECURSION\_LIMIT](classfranky_1_1_motion_generator.md#a2dceaaa3e924424fc57f68b5e1955712) = 16

 

Maximum recursion limit for reactions. After more than this number of reactions are fired in a single step, the motion generator will throw a [ReactionRecursionException](structfranky_1_1_reaction_recursion_exception.md "Exception thrown when the reaction recursion limit (8) is reached.").  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

<div class="compoundTemplParams">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac)\>  
class franky::MotionGenerator\< ControlSignalType \>

</div>

Helper class for handling motions and reactions.

</div>

## Constructor & Destructor Documentation

<span id="a629d006e1c4b920cd4e1240a5b4e435c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion_generator.md#a629d006e1c4b920cd4e1240a5b4e435c)</span>MotionGenerator()

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
<td><a href="classfranky_1_1_motion_generator.md" class="el">franky::MotionGenerator</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::MotionGenerator</td>
<td>(</td>
<td><a href="classfranky_1_1_robot.md" class="el">Robot</a> * </td>
<td><em>robot</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>std::shared_ptr&lt; <a href="classfranky_1_1_motion.md" class="el">Motion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &gt; </td>
<td><em>initial_motion</em> </td>
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
    
    |                 |                     |
    | --------------- | ------------------- |
    | robot           | The robot instance. |
    | initial\_motion | The initial motion. |
    

</div>

</div>

## Member Function Documentation

<span id="ad0abb8a6c37b8ab8208810bb58250bf8"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion_generator.md#ad0abb8a6c37b8ab8208810bb58250bf8)</span>has\_new\_motion()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                    |   |  |   |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |  | - |  |
| [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::MotionGenerator](classfranky_1_1_motion_generator.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::has\_new\_motion | ( |  | ) |  |

</div>

<div class="memdoc">

Whether a new motion is available.

</div>

</div>

<span id="a751c6f2d51740e613c6575b1f62e1dfa"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion_generator.md#a751c6f2d51740e613c6575b1f62e1dfa)</span>operator()()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                                                                                     |   |                                                                                                                   |                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) [franky::MotionGenerator](classfranky_1_1_motion_generator.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>[::operator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)() | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *robot\_state*, |
|                                                                                                                                                                                                                                                                                                     |   | franka::Duration                                                                                                  | *period*        |
|                                                                                                                                                                                                                                                                                                     | ) |                                                                                                                   |                 |

</div>

<div class="memdoc">

Update the motion generator and get the next control signal.

  - Parameters
    
    |              |                          |
    | ------------ | ------------------------ |
    | robot\_state | The current robot state. |
    | period       | The time step.           |
    

<!-- end list -->

  - Returns  
    The control signal for the robot.

</div>

</div>

<span id="a771a92b07e8c384ec56fd014841ed5f2"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion_generator.md#a771a92b07e8c384ec56fd014841ed5f2)</span>registerUpdateCallback()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_motion_generator.md" class="el">franky::MotionGenerator</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::registerUpdateCallback</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::function&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a>(<a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp;, franka::Duration, franka::Duration)&gt; &amp; </td>
<td><em>callback</em></td>
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

Register a callback that is called in every step of the motion.

  - Parameters
    
    |          |                                                                                                                                                                 |
    | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | callback | The callback to register. Callbacks are called with the robot state, the time step \[s\], the relative time \[s\] and the control signal computed in this step. |
    

</div>

</div>

<span id="aaa6cf6fa7c6af2d7b081b19d569c2e0f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion_generator.md#aaa6cf6fa7c6af2d7b081b19d569c2e0f)</span>resetTimeUnsafe()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                   |   |  |   |  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |  | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::MotionGenerator](classfranky_1_1_motion_generator.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::resetTimeUnsafe | ( |  | ) |  |

</div>

<div class="memdoc">

Reset the time of the motion generator without locking the mutex.

</div>

</div>

<span id="aecb5394cc1571687e1117e268f91e9c1"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion_generator.md#aecb5394cc1571687e1117e268f91e9c1)</span>updateMotion()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                |   |                                                                                                                                              |               |   |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | - | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::MotionGenerator](classfranky_1_1_motion_generator.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::updateMotion | ( | std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> | *new\_motion* | ) |  |

</div>

<div class="memdoc">

Update the current motion.

  - Parameters
    
    |             |                 |
    | ----------- | --------------- |
    | new\_motion | The new motion. |
    

</div>

</div>

## Member Data Documentation

<span id="a2dceaaa3e924424fc57f68b5e1955712"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion_generator.md#a2dceaaa3e924424fc57f68b5e1955712)</span>REACTION\_RECURSION\_LIMIT

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">constexpr</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">size_t</a> <a href="classfranky_1_1_motion_generator.md" class="el">franky::MotionGenerator</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::REACTION_RECURSION_LIMIT = 16</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">static</span><span class="mlabel">constexpr</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Maximum recursion limit for reactions. After more than this number of reactions are fired in a single step, the motion generator will throw a [ReactionRecursionException](structfranky_1_1_reaction_recursion_exception.md "Exception thrown when the reaction recursion limit (8) is reached.").

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/motion/[motion\_generator.hpp](motion__generator_8hpp_source.md)
  - /home/runner/work/franky/franky/src/motion/[motion\_generator.cpp](motion__generator_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
