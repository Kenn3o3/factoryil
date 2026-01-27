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
  - [ImpedanceMotion](classfranky_1_1_impedance_motion.md)

</div>

</div>

<div class="header">

<div class="summary">

[Classes](classfranky_1_1_impedance_motion.md#nested-classes) | [Public Member Functions](classfranky_1_1_impedance_motion.md#pub-methods) | [Protected Member Functions](classfranky_1_1_impedance_motion.md#pro-methods) | [List of all members](classfranky_1_1_impedance_motion-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::ImpedanceMotion Class Reference<span class="mlabels"><span class="mlabel">abstract</span></span>

</div>

</div>

</div>

<div class="contents">

Base class for client-side cartesian impedance motions. [More...](classfranky_1_1_impedance_motion.md#details)

`#include <impedance_motion.hpp>`

<div class="dynheader">

Inheritance diagram for franky::ImpedanceMotion:

</div>

<div class="dyncontent">

<div class="center">

![](classfranky_1_1_impedance_motion.png)

</div>

</div>

## <span id="nested-classes"></span> Classes

</div>

struct  

[Params](structfranky_1_1_impedance_motion_1_1_params.md)

 

Parameters for the impedance motion. [More...](structfranky_1_1_impedance_motion_1_1_params.md#details)  

 

## <span id="pub-methods"></span> Public Member Functions

 

[ImpedanceMotion](classfranky_1_1_impedance_motion.md#a60d55400835651bf37a1593f72e1a5cf) ([Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Params](structfranky_1_1_impedance_motion_1_1_params.md) &[params](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

![-](closed.png) Public Member Functions inherited from [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md)

virtual 

[\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16) ()=default

 

void 

[addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448) (std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< franka::Torques \> \> reaction)

 

Add a reaction to the motion.  

 

void 

[addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347) (std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< franka::Torques \> \> reaction)

 

Add a reaction to the front of the reaction list.  

 

std::vector\< std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< franka::Torques \> \> \> 

[reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d) ()

 

Currently registered reactions of the motion.  

 

void 

[registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2) ([CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) callback)

 

Register a callback that is called in every step of the motion.  

 

void 

[init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6) ([Robot](classfranky_1_1_robot.md) \*robot, const [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, const std::optional\< franka::Torques \> \&previous\_command)

 

Initialize the motion.  

 

franka::Torques 

[nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7) (const [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< franka::Torques \> \&previous\_command)

 

Get the next command of the motion.  

 

std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< franka::Torques \> \> 

[checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369) (const [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)

 

Check and call reactions.  

 

## <span id="pro-methods"></span> Protected Member Functions

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[initImpl](classfranky_1_1_impedance_motion.md#a87fe10bf698cbc2b55db0a354fa9d250) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< franka::Torques \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [override](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

franka::Torques 

[nextCommandImpl](classfranky_1_1_impedance_motion.md#a6594ab5628923b88cce26903ae02077c) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< franka::Torques \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [override](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[intermediate\_target](classfranky_1_1_impedance_motion.md#aabd59d6e0609d88130d71426324d12e2) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::tuple\< [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f), [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[update](classfranky_1_1_impedance_motion.md#aee9a6e23b63db2ebc49c6615b461189c) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration time)=0

 

![-](closed.png) Protected Member Functions inherited from [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md)

 

[Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4) ()

 

[Robot](classfranky_1_1_robot.md) \* 

[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f) () const

 

## <span id="inherited"></span> Additional Inherited Members

![-](closed.png) Public Types inherited from [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md)

using 

[CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) = std::function\< void(const [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration, franka::Duration, const franka::Torques &)\>

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Base class for client-side cartesian impedance motions.

This motion is a implements a cartesian impedance controller on the client side and does not use Franka's internal impedance controller. Instead, it uses Franka's internal torque controller and calculates the torques itself.

</div>

## Constructor & Destructor Documentation

<span id="a60d55400835651bf37a1593f72e1a5cf"></span>

## <span class="permalink">[◆ ](classfranky_1_1_impedance_motion.md#a60d55400835651bf37a1593f72e1a5cf)</span>ImpedanceMotion()

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
<td>franky::ImpedanceMotion::ImpedanceMotion</td>
<td>(</td>
<td><a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> </td>
<td><em>target</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_impedance_motion_1_1_params.md" class="el">Params</a> &amp; </td>
<td><em>params</em> </td>
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
    
    |        |                            |
    | ------ | -------------------------- |
    | target | The target pose.           |
    | params | Parameters for the motion. |
    

</div>

</div>

## Member Function Documentation

<span id="a87fe10bf698cbc2b55db0a354fa9d250"></span>

## <span class="permalink">[◆ ](classfranky_1_1_impedance_motion.md#a87fe10bf698cbc2b55db0a354fa9d250)</span>initImpl()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> franky::ImpedanceMotion::initImpl</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; franka::Torques &gt; &amp; </td>
<td><em>previous_command</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">override</span><span class="mlabel">protected</span><span class="mlabel">virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Reimplemented from [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md#ad11b300fa7c37e18403af6a17bf663b8).

</div>

</div>

<span id="aabd59d6e0609d88130d71426324d12e2"></span>

## <span class="permalink">[◆ ](classfranky_1_1_impedance_motion.md#aabd59d6e0609d88130d71426324d12e2)</span>intermediate\_target()

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
<td><a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> franky::ImpedanceMotion::intermediate_target</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">protected</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a6594ab5628923b88cce26903ae02077c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_impedance_motion.md#a6594ab5628923b88cce26903ae02077c)</span>nextCommandImpl()

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
<td>franka::Torques franky::ImpedanceMotion::nextCommandImpl</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>time_step</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>rel_time</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>abs_time</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; franka::Torques &gt; &amp; </td>
<td><em>previous_command</em> </td>
</tr>
<tr class="even">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">override</span><span class="mlabel">protected</span><span class="mlabel">virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Implements [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md#ad2e6f47d30089ee335fecb671618a5f6).

</div>

</div>

<span id="a1ce961ddf51cd792482fd5ca2b299d97"></span>

## <span class="permalink">[◆ ](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97)</span>target()

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
<td><a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> franky::ImpedanceMotion::target</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">protected</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="aee9a6e23b63db2ebc49c6615b461189c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_impedance_motion.md#aee9a6e23b63db2ebc49c6615b461189c)</span>update()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> std::tuple&lt; <a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> &gt; franky::ImpedanceMotion::update</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>time_step</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>time</em> </td>
</tr>
<tr class="even">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">protected</span><span class="mlabel">pure virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Implemented in [franky::CartesianImpedanceMotion](classfranky_1_1_cartesian_impedance_motion.md#a9f89c79e4872f1a0fa736ea1ff6ffb93), and [franky::ExponentialImpedanceMotion](classfranky_1_1_exponential_impedance_motion.md#a09d2d86cfd46ce2238dacf4d471cf9f8).

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/motion/[impedance\_motion.hpp](impedance__motion_8hpp_source.md)
  - /home/runner/work/franky/franky/src/motion/[impedance\_motion.cpp](impedance__motion_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
