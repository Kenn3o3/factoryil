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

  - [include](dir_d44c64559bbebec7f509842c48db8b23.md)
  - [franky](dir_8c3170b11fac4cb7639acbce82cfa383.md)
  - [motion](dir_187b2dfc241887d0d9fc7ba40130fa9d.md)

</div>

</div>

<div class="header">

<div class="headertitle">

<div class="title">

joint\_velocity\_waypoint\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](joint__velocity__waypoint__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/robot\_state.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<atomic\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include \<ruckig/ruckig.hpp\></span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/joint\_state.hpp](joint__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/motion/velocity\_waypoint\_motion.hpp](velocity__waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span>

</div>

<div id="foldopen00019" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00019"></span><span class="lineno"> [19](classfranky_1_1_joint_velocity_waypoint_motion.md)</span><span class="keyword">class </span>[JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md) : <span class="keyword">public</span> [VelocityWaypointMotion](classfranky_1_1_velocity_waypoint_motion.md)\<franka::JointVelocities, Vector7d\> {

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span> <span class="keyword">explicit</span> [JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)(

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span> <span class="keyword">const</span> std::vector\<[VelocityWaypoint\<Vector7d\>](structfranky_1_1_waypoint.md)\> \&waypoints,

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span> <span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0);

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span> <span class="keyword">protected</span>:

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span> <span class="keywordtype">void</span> [checkWaypoint](classfranky_1_1_joint_velocity_waypoint_motion.md#aac255554d579fa569e527d38827cb403)(<span class="keyword">const</span> [VelocityWaypoint\<Vector7d\>](structfranky_1_1_waypoint.md) \&waypoint) <span class="keyword">const override</span>;

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span>

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> <span class="keywordtype">void</span> [initWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md#a94d486b1c454ef9d64794b0243118c69)(

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::JointVelocities\> \&previous\_command,

</div>

<div class="line">

<span id="l00036"></span><span class="lineno"> 36</span> ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span> <span class="keywordtype">void</span> [setNewWaypoint](classfranky_1_1_joint_velocity_waypoint_motion.md#aac99f45e9da8310f5573cc6fafc669bf)(

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::JointVelocities\> \&previous\_command,

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> <span class="keyword">const</span> [VelocityWaypoint\<Vector7d\>](structfranky_1_1_waypoint.md) \&new\_waypoint, ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span>

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> \[\[nodiscard\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getAbsoluteInputLimits](classfranky_1_1_joint_velocity_waypoint_motion.md#a655f188e3b100a957854ac920bf2595b)() <span class="keyword">const override</span>;

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span>

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> \[\[nodiscard\]\] franka::JointVelocities [getControlSignal](classfranky_1_1_joint_velocity_waypoint_motion.md#a5bd0458f8263aae4360647bfb5bb72a2)(

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> franka::Duration \&time\_step,

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span> <span class="keyword">const</span> std::optional\<franka::JointVelocities\> \&previous\_command,

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keyword">const</span> ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> \[\[nodiscard\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getDesiredState](classfranky_1_1_joint_velocity_waypoint_motion.md#a2402d5ec4c9bc70d7a0f036e5375e272)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state) <span class="keyword">const override</span>;

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span>};

</div>

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span>

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_joint_velocity_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::JointVelocityWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md)

</div>

<div class="ttdoc">

Joint velocity waypoint motion.

</div>

<div class="ttdef">

**Definition** joint\_velocity\_waypoint\_motion.hpp:19

</div>

</div>

<div id="aclassfranky_1_1_joint_velocity_waypoint_motion_html_a2402d5ec4c9bc70d7a0f036e5375e272" class="ttc">

<div class="ttname">

[franky::JointVelocityWaypointMotion::getDesiredState](classfranky_1_1_joint_velocity_waypoint_motion.md#a2402d5ec4c9bc70d7a0f036e5375e272)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getDesiredState(const RobotState \&robot\_state) const override

</div>

<div class="ttdef">

**Definition** joint\_velocity\_waypoint\_motion.cpp:51

</div>

</div>

<div id="aclassfranky_1_1_joint_velocity_waypoint_motion_html_a5bd0458f8263aae4360647bfb5bb72a2" class="ttc">

<div class="ttname">

[franky::JointVelocityWaypointMotion::getControlSignal](classfranky_1_1_joint_velocity_waypoint_motion.md#a5bd0458f8263aae4360647bfb5bb72a2)

</div>

<div class="ttdeci">

franka::JointVelocities getControlSignal(const RobotState \&robot\_state, const franka::Duration \&time\_step, const std::optional\< franka::JointVelocities \> \&previous\_command, const ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** joint\_velocity\_waypoint\_motion.cpp:31

</div>

</div>

<div id="aclassfranky_1_1_joint_velocity_waypoint_motion_html_a655f188e3b100a957854ac920bf2595b" class="ttc">

<div class="ttname">

[franky::JointVelocityWaypointMotion::getAbsoluteInputLimits](classfranky_1_1_joint_velocity_waypoint_motion.md#a655f188e3b100a957854ac920bf2595b)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getAbsoluteInputLimits() const override

</div>

<div class="ttdef">

**Definition** joint\_velocity\_waypoint\_motion.cpp:46

</div>

</div>

<div id="aclassfranky_1_1_joint_velocity_waypoint_motion_html_a94d486b1c454ef9d64794b0243118c69" class="ttc">

<div class="ttname">

[franky::JointVelocityWaypointMotion::initWaypointMotion](classfranky_1_1_joint_velocity_waypoint_motion.md#a94d486b1c454ef9d64794b0243118c69)

</div>

<div class="ttdeci">

void initWaypointMotion(const RobotState \&robot\_state, const std::optional\< franka::JointVelocities \> \&previous\_command, ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** joint\_velocity\_waypoint\_motion.cpp:20

</div>

</div>

<div id="aclassfranky_1_1_joint_velocity_waypoint_motion_html_aac255554d579fa569e527d38827cb403" class="ttc">

<div class="ttname">

[franky::JointVelocityWaypointMotion::checkWaypoint](classfranky_1_1_joint_velocity_waypoint_motion.md#aac255554d579fa569e527d38827cb403)

</div>

<div class="ttdeci">

void checkWaypoint(const VelocityWaypoint\< Vector7d \> \&waypoint) const override

</div>

<div class="ttdef">

**Definition** joint\_velocity\_waypoint\_motion.cpp:11

</div>

</div>

<div id="aclassfranky_1_1_joint_velocity_waypoint_motion_html_aac99f45e9da8310f5573cc6fafc669bf" class="ttc">

<div class="ttname">

[franky::JointVelocityWaypointMotion::setNewWaypoint](classfranky_1_1_joint_velocity_waypoint_motion.md#aac99f45e9da8310f5573cc6fafc669bf)

</div>

<div class="ttdeci">

void setNewWaypoint(const RobotState \&robot\_state, const std::optional\< franka::JointVelocities \> \&previous\_command, const VelocityWaypoint\< Vector7d \> \&new\_waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** joint\_velocity\_waypoint\_motion.cpp:37

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md)

</div>

<div class="ttdoc">

Relative dynamics factors.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:13

</div>

</div>

<div id="aclassfranky_1_1_velocity_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::VelocityWaypointMotion](classfranky_1_1_velocity_waypoint_motion.md)

</div>

<div class="ttdoc">

A motion following multiple positional waypoints in a time-optimal way. Works with arbitrary initial ...

</div>

<div class="ttdef">

**Definition** velocity\_waypoint\_motion.hpp:29

</div>

</div>

<div id="ajoint__state_8hpp_html" class="ttc">

<div class="ttname">

[joint\_state.hpp](joint__state_8hpp.md)

</div>

</div>

<div id="anamespacefranky_html" class="ttc">

<div class="ttname">

[franky](namespacefranky.md)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:8

</div>

</div>

<div id="astructfranky_1_1_robot_state_html" class="ttc">

<div class="ttname">

[franky::RobotState](structfranky_1_1_robot_state.md)

</div>

<div class="ttdoc">

Full state of the robot.

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:23

</div>

</div>

<div id="astructfranky_1_1_waypoint_html" class="ttc">

<div class="ttname">

[franky::Waypoint](structfranky_1_1_waypoint.md)

</div>

<div class="ttdoc">

A waypoint with a target and optional parameters.

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:36

</div>

</div>

<div id="avelocity__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[velocity\_waypoint\_motion.hpp](velocity__waypoint__motion_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
