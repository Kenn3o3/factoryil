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
  - [WaypointMotion](classfranky_1_1_waypoint_motion.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_waypoint_motion.md#pub-methods) | [Protected Member Functions](classfranky_1_1_waypoint_motion.md#pro-methods) | [List of all members](classfranky_1_1_waypoint_motion-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \> Class Template Reference<span class="mlabels"><span class="mlabel">abstract</span></span>

</div>

</div>

</div>

<div class="contents">

A motion following multiple waypoints in a time-optimal way. Works with arbitrary initial conditions. [More...](classfranky_1_1_waypoint_motion.md#details)

`#include <waypoint_motion.hpp>`

<div class="dynheader">

Inheritance diagram for franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>:

</div>

<div class="dyncontent">

<div class="center">

![](classfranky_1_1_waypoint_motion.png)

</div>

</div>

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[WaypointMotion](classfranky_1_1_waypoint_motion.md#a53c26db8057d1048efafe5a38a372f77) (std::vector\< [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> [waypoints](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) return\_when\_finished=[true](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

![-](closed.png) Public Member Functions inherited from [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16) ()=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448) (std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [reaction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Add a reaction to the motion.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347) (std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [reaction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Add a reaction to the front of the reaction list.  

 

std::vector\< std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> \> 

[reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d) ()

 

Currently registered reactions of the motion.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2) ([CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) [callback](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Register a callback that is called in every step of the motion.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6) ([Robot](classfranky_1_1_robot.md) \*[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Initialize the motion.  

 

[ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) 

[nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Get the next command of the motion.  

 

std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> 

[checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Check and call reactions.  

 

## <span id="pro-methods"></span> Protected Member Functions

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[initImpl](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [override](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) 

[nextCommandImpl](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [override](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[initWaypointMotion](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::InputParameter\< 7 \> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))=0

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[setNewWaypoint](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[new\_waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::InputParameter\< 7 \> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))=0

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[extrapolateMotion](classfranky_1_1_waypoint_motion.md#a24a6f06d1ca935764c37aa044d191750) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::Duration &[time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) ruckig::InputParameter\< 7 \> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::OutputParameter\< 7 \> &[output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) =0

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[checkWaypoint](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::tuple\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4), [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4), [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \> 

[getAbsoluteInputLimits](classfranky_1_1_waypoint_motion.md#ae3c92f31c20dcb7f48107c1991d8be33) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) =0

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) 

[getControlSignal](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::Duration &[time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) ruckig::InputParameter\< 7 \> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))=0

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[setInputLimits](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::InputParameter\< 7 \> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) =0

 

![-](closed.png) Protected Member Functions inherited from [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)

 

[Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4) ()

 

[Robot](classfranky_1_1_robot.md) \* 

[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

## <span id="inherited"></span> Additional Inherited Members

![-](closed.png) Public Types inherited from [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)

[using](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) = std::function\< [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration, franka::Duration, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) &)\>

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

<div class="compoundTemplParams">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac), [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>  
class franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>

</div>

A motion following multiple waypoints in a time-optimal way. Works with arbitrary initial conditions.

  - Template Parameters
    
    |                   |                                                                                                                                                                |
    | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ControlSignalType | The type of the control signal. Either franka::Torques, franka::JointVelocities, franka::CartesianVelocities, franka::JointPositions or franka::CartesianPose. |
    | WaypointType      | The type of the waypoints. Must subclass Waypoint\<TargetType\>.                                                                                               |
    | TargetType        | The type of the target of the waypoints.                                                                                                                       |
    

</div>

## Constructor & Destructor Documentation

<span id="a53c26db8057d1048efafe5a38a372f77"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#a53c26db8057d1048efafe5a38a372f77)</span>WaypointMotion()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::WaypointMotion</td>
<td>(</td>
<td>std::vector&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a> &gt; </td>
<td><em>waypoints</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> </td>
<td><em>return_when_finished</em> = <code>true</code> </td>
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

  - Parameters
    
    |                        |                                                                                              |
    | ---------------------- | -------------------------------------------------------------------------------------------- |
    | waypoints              | The waypoints to follow.                                                                     |
    | return\_when\_finished | Whether to end the motion when the last waypoint is reached or keep holding the last target. |
    

</div>

</div>

## Member Function Documentation

<span id="a9d8d450f3d2748cc32eb6bd2afd6f46c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)</span>checkWaypoint()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::checkWaypoint</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a> &amp; </td>
<td><em>waypoint</em></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a24a6f06d1ca935764c37aa044d191750"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#a24a6f06d1ca935764c37aa044d191750)</span>extrapolateMotion()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::extrapolateMotion</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> franka::Duration &amp; </td>
<td><em>time_step</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> ruckig::InputParameter&lt; 7 &gt; &amp; </td>
<td><em>input_parameter</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ruckig::OutputParameter&lt; 7 &gt; &amp; </td>
<td><em>output_parameter</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">protected</span><span class="mlabel">pure virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Implemented in [franky::PositionWaypointMotion\< ControlSignalType, TargetType \>](classfranky_1_1_position_waypoint_motion.md#a345e479ffc4f38dba2a1128805108e19), [franky::PositionWaypointMotion\< franka::CartesianPose, CartesianState \>](classfranky_1_1_position_waypoint_motion.md#a345e479ffc4f38dba2a1128805108e19), [franky::PositionWaypointMotion\< franka::JointPositions, JointState \>](classfranky_1_1_position_waypoint_motion.md#a345e479ffc4f38dba2a1128805108e19), [franky::VelocityWaypointMotion\< ControlSignalType, TargetType \>](classfranky_1_1_velocity_waypoint_motion.md#aca3cabe4405f7132c4001388d248cc67), [franky::VelocityWaypointMotion\< franka::CartesianVelocities, RobotVelocity \>](classfranky_1_1_velocity_waypoint_motion.md#aca3cabe4405f7132c4001388d248cc67), and [franky::VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>](classfranky_1_1_velocity_waypoint_motion.md#aca3cabe4405f7132c4001388d248cc67).

</div>

</div>

<span id="ae3c92f31c20dcb7f48107c1991d8be33"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#ae3c92f31c20dcb7f48107c1991d8be33)</span>getAbsoluteInputLimits()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> std::tuple&lt; <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a>, <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a>, <a href="namespacefranky.md#a4c36e6539a78f808bf759142dec935c4" class="el">Vector7d</a> &gt; <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::getAbsoluteInputLimits</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">protected</span><span class="mlabel">pure virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Implemented in [franky::CartesianVelocityWaypointMotion](classfranky_1_1_cartesian_velocity_waypoint_motion.md#a8653d525b32035e8b774da7b7fb6051e), [franky::CartesianWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md#a493676502c53be9f6f0acf8a82cb8192), [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md#a655f188e3b100a957854ac920bf2595b), [franky::JointWaypointMotion](classfranky_1_1_joint_waypoint_motion.md#a861df703835e15f447a9f40affe3625a), [franky::PositionWaypointMotion\< ControlSignalType, TargetType \>](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714), [franky::PositionWaypointMotion\< franka::CartesianPose, CartesianState \>](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714), [franky::PositionWaypointMotion\< franka::JointPositions, JointState \>](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714), [franky::VelocityWaypointMotion\< ControlSignalType, TargetType \>](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c), [franky::VelocityWaypointMotion\< franka::CartesianVelocities, RobotVelocity \>](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c), and [franky::VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c).

</div>

</div>

<span id="aa019aeb70e7bc53a5a95a8ac2e2b62eb"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)</span>getControlSignal()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::getControlSignal</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> franka::Duration &amp; </td>
<td><em>time_step</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &amp; </td>
<td><em>previous_command</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> ruckig::InputParameter&lt; 7 &gt; &amp; </td>
<td><em>input_parameter</em> </td>
</tr>
<tr class="odd">
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

</div>

</div>

<span id="ada8edd9d849ee29244b6c2c1cfa30f69"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69)</span>initImpl()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::initImpl</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &amp; </td>
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
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">override</span><span class="mlabel">protected</span><span class="mlabel">virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Reimplemented from [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md#ad11b300fa7c37e18403af6a17bf663b8).

</div>

</div>

<span id="a2af18e1bfe76ed4e88f87ba03fe04fd8"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8)</span>initWaypointMotion()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::initWaypointMotion</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &amp; </td>
<td><em>previous_command</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ruckig::InputParameter&lt; 7 &gt; &amp; </td>
<td><em>input_parameter</em> </td>
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

</div>

</div>

<span id="ade5d803c15b7f55e55258092788df21b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b)</span>nextCommandImpl()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::nextCommandImpl</td>
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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &amp; </td>
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
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">override</span><span class="mlabel">protected</span><span class="mlabel">virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Implements [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md#ad2e6f47d30089ee335fecb671618a5f6).

</div>

</div>

<span id="a4a54f0791590e317159518eb0353a199"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)</span>setInputLimits()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::setInputLimits</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a> &amp; </td>
<td><em>waypoint</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ruckig::InputParameter&lt; 7 &gt; &amp; </td>
<td><em>input_parameter</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">protected</span><span class="mlabel">pure virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Implemented in [franky::PositionWaypointMotion\< ControlSignalType, TargetType \>](classfranky_1_1_position_waypoint_motion.md#a8ebb35ebb3363acfec93c9228418804a), and [franky::VelocityWaypointMotion\< ControlSignalType, TargetType \>](classfranky_1_1_velocity_waypoint_motion.md#a1cfd2cbfa762565d6d95a9db2d911fba).

</div>

</div>

<span id="aac84c2b66a185a3c21380a395cc49ae0"></span>

## <span class="permalink">[◆ ](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)</span>setNewWaypoint()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_waypoint_motion.md" class="el">franky::WaypointMotion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a>, <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">TargetType</a> &gt;::setNewWaypoint</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &amp; </td>
<td><em>previous_command</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">WaypointType</a> &amp; </td>
<td><em>new_waypoint</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ruckig::InputParameter&lt; 7 &gt; &amp; </td>
<td><em>input_parameter</em> </td>
</tr>
<tr class="odd">
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

</div>

</div>

-----

The documentation for this class was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/motion/[waypoint\_motion.hpp](waypoint__motion_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
