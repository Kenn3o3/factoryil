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

<div class="headertitle">

<div class="title">

franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \> Member List

</div>

</div>

</div>

<div class="contents">

This is the complete list of members for [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md), including all inherited members.

|                                                                                                                                                                                                                                                                                            |                                                                                                                 |                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448)(std::shared\_ptr\< Reaction\< ControlSignalType \> \> reaction)                                                                                                                                               | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347)(std::shared\_ptr\< Reaction\< ControlSignalType \> \> reaction)                                                                                                                                          | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) typedef                                                                                                                                                                                                      | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369)(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)                                                                                                            | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [checkWaypoint](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)(const WaypointType \&waypoint) const                                                                                                                                                               | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span> |
| [extrapolateMotion](classfranky_1_1_waypoint_motion.md#a24a6f06d1ca935764c37aa044d191750)(const RobotState \&robot\_state, const franka::Duration \&time\_step, const ruckig::InputParameter\< 7 \> \&input\_parameter, ruckig::OutputParameter\< 7 \> \&output\_parameter) const =0     | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [getAbsoluteInputLimits](classfranky_1_1_waypoint_motion.md#ae3c92f31c20dcb7f48107c1991d8be33)() const =0                                                                                                                                                                                | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [getControlSignal](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)(const RobotState \&robot\_state, const franka::Duration \&time\_step, const std::optional\< ControlSignalType \> \&previous\_command, const ruckig::InputParameter\< 7 \> \&input\_parameter)=0 | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6)(Robot \*robot, const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command)                                                                                                      | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [initImpl](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69)(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command) override                                                                                               | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span> |
| [initWaypointMotion](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8)(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command, ruckig::InputParameter\< 7 \> \&input\_parameter)=0                                          | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4)()                                                                                                                                                                                                                  | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            | <span class="mlabel">explicit</span><span class="mlabel">protected</span>                                  |
| [nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7)(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< ControlSignalType \> \&previous\_command)                         | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [nextCommandImpl](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b)(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< ControlSignalType \> \&previous\_command) override   | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span> |
| [reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d)()                                                                                                                                                                                                               | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2)(CallbackType callback)                                                                                                                                                                                   | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            |                                                                                                            |
| [robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)() const                                                                                                                                                                                                             | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            | <span class="mlabel">inline</span><span class="mlabel">protected</span>                                    |
| [setInputLimits](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)(const WaypointType \&waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) const =0                                                                                                         | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [setNewWaypoint](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command, const WaypointType \&new\_waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter)=0          | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [WaypointMotion](classfranky_1_1_waypoint_motion.md#a53c26db8057d1048efafe5a38a372f77)(std::vector\< WaypointType \> waypoints, bool return\_when\_finished=true)                                                                                                                        | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md) | <span class="mlabel">inline</span><span class="mlabel">explicit</span>                                     |
| [\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16)()=default                                                                                                                                                                                                        | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                            | <span class="mlabel">virtual</span>                                                                        |

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
