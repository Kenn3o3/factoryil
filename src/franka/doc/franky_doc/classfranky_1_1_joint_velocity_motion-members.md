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
  - [JointVelocityMotion](classfranky_1_1_joint_velocity_motion.md)

</div>

</div>

<div class="header">

<div class="headertitle">

<div class="title">

franky::JointVelocityMotion Member List

</div>

</div>

</div>

<div class="contents">

This is the complete list of members for [franky::JointVelocityMotion](classfranky_1_1_joint_velocity_motion.md), including all inherited members.

|                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                        |                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448)(std::shared\_ptr\< Reaction\< ControlSignalType \> \> reaction)                                                                                                                                                                                                              | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347)(std::shared\_ptr\< Reaction\< ControlSignalType \> \> reaction)                                                                                                                                                                                                         | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) typedef                                                                                                                                                                                                                                                                     | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369)(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)                                                                                                                                                                           | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [checkWaypoint](classfranky_1_1_joint_velocity_waypoint_motion.md#aac255554d579fa569e527d38827cb403)(const VelocityWaypoint\< Vector7d \> \&waypoint) const override                                                                                                                                                                                    | [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)                             | <span class="mlabel">protected</span>                                                                      |
| [VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>::checkWaypoint](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)(const WaypointType \&waypoint) const                                                                                                                                                               | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span> |
| [extrapolateMotion](classfranky_1_1_velocity_waypoint_motion.md#aca3cabe4405f7132c4001388d248cc67)(const RobotState \&robot\_state, const franka::Duration \&time\_step, const ruckig::InputParameter\< 7 \> \&input\_parameter, ruckig::OutputParameter\< 7 \> \&output\_parameter) const override                                                     | [franky::VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>](classfranky_1_1_velocity_waypoint_motion.md) | <span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span> |
| [getAbsoluteInputLimits](classfranky_1_1_joint_velocity_waypoint_motion.md#a655f188e3b100a957854ac920bf2595b)() const override                                                                                                                                                                                                                          | [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)                             | <span class="mlabel">protected</span><span class="mlabel">virtual</span>                                   |
| [getControlSignal](classfranky_1_1_joint_velocity_waypoint_motion.md#a5bd0458f8263aae4360647bfb5bb72a2)(const RobotState \&robot\_state, const franka::Duration \&time\_step, const std::optional\< franka::JointVelocities \> \&previous\_command, const ruckig::InputParameter\< 7 \> \&input\_parameter) override                                    | [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)                             | <span class="mlabel">protected</span>                                                                      |
| [VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>::getControlSignal](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)(const RobotState \&robot\_state, const franka::Duration \&time\_step, const std::optional\< ControlSignalType \> \&previous\_command, const ruckig::InputParameter\< 7 \> \&input\_parameter)=0 | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [getDesiredState](classfranky_1_1_joint_velocity_waypoint_motion.md#a2402d5ec4c9bc70d7a0f036e5375e272)(const RobotState \&robot\_state) const override                                                                                                                                                                                                  | [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)                             | <span class="mlabel">protected</span><span class="mlabel">virtual</span>                                   |
| [init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6)(Robot \*robot, const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command)                                                                                                                                                                     | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [initImpl](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69)(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command) override                                                                                                                                                              | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span> |
| [initWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md#a94d486b1c454ef9d64794b0243118c69)(const RobotState \&robot\_state, const std::optional\< franka::JointVelocities \> \&previous\_command, ruckig::InputParameter\< 7 \> \&input\_parameter) override                                                                             | [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)                             | <span class="mlabel">protected</span>                                                                      |
| [VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>::initWaypointMotion](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8)(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command, ruckig::InputParameter\< 7 \> \&input\_parameter)=0                                          | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [JointVelocityMotion](classfranky_1_1_joint_velocity_motion.md#ae8bed7cd056b9e11ca73e82e7e115659)(const Vector7d \&target, const franka::Duration \&duration=franka::Duration(1000), const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)                                                                                                     | [franky::JointVelocityMotion](classfranky_1_1_joint_velocity_motion.md)                                              | <span class="mlabel">explicit</span>                                                                       |
| [JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md#a42129c9f2d942dfe5200425f1eaed709)(const std::vector\< VelocityWaypoint\< Vector7d \> \> \&waypoints, const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)                                                                                                    | [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)                             | <span class="mlabel">explicit</span>                                                                       |
| [Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4)()                                                                                                                                                                                                                                                                                 | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   | <span class="mlabel">explicit</span><span class="mlabel">protected</span>                                  |
| [nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7)(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< ControlSignalType \> \&previous\_command)                                                                                        | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [nextCommandImpl](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b)(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< ControlSignalType \> \&previous\_command) override                                                                  | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span> |
| [reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d)()                                                                                                                                                                                                                                                                              | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2)(CallbackType callback)                                                                                                                                                                                                                                                  | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   |                                                                                                            |
| [robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)() const                                                                                                                                                                                                                                                                            | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   | <span class="mlabel">inline</span><span class="mlabel">protected</span>                                    |
| [setInputLimits](classfranky_1_1_velocity_waypoint_motion.md#a1cfd2cbfa762565d6d95a9db2d911fba)(const VelocityWaypoint\< Vector7d \> \&waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) const override                                                                                                                                       | [franky::VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>](classfranky_1_1_velocity_waypoint_motion.md) | <span class="mlabel">inline</span><span class="mlabel">protected</span>                                    |
| [franky::WaypointMotion::setInputLimits](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)(const WaypointType \&waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) const =0                                                                                                                                                | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [setNewWaypoint](classfranky_1_1_joint_velocity_waypoint_motion.md#aac99f45e9da8310f5573cc6fafc669bf)(const RobotState \&robot\_state, const std::optional\< franka::JointVelocities \> \&previous\_command, const VelocityWaypoint\< Vector7d \> \&new\_waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) override                           | [franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)                             | <span class="mlabel">protected</span>                                                                      |
| [VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>::setNewWaypoint](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command, const WaypointType \&new\_waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter)=0          | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span>                              |
| [VelocityWaypointMotion](classfranky_1_1_velocity_waypoint_motion.md#aa7cb87ffe6b03a25bf14efbb3e547405)(std::vector\< VelocityWaypoint\< Vector7d \> \> waypoints, const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)                                                                                                                       | [franky::VelocityWaypointMotion\< franka::JointVelocities, Vector7d \>](classfranky_1_1_velocity_waypoint_motion.md) | <span class="mlabel">inline</span><span class="mlabel">explicit</span>                                     |
| [WaypointMotion](classfranky_1_1_waypoint_motion.md#a53c26db8057d1048efafe5a38a372f77)(std::vector\< WaypointType \> waypoints, bool return\_when\_finished=true)                                                                                                                                                                                       | [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md)        | <span class="mlabel">inline</span><span class="mlabel">explicit</span>                                     |
| [\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16)()=default                                                                                                                                                                                                                                                                       | [franky::Motion\< ControlSignalType \>](classfranky_1_1_motion.md)                                                   | <span class="mlabel">virtual</span>                                                                        |

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
