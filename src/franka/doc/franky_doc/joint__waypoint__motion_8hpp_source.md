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

joint\_waypoint\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](joint__waypoint__motion_8hpp.md)

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

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/motion/position\_waypoint\_motion.hpp](position__waypoint__motion_8hpp.md)"</span>

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

<span id="l00019"></span><span class="lineno"> [19](classfranky_1_1_joint_waypoint_motion.md)</span><span class="keyword">class </span>[JointWaypointMotion](classfranky_1_1_joint_waypoint_motion.md) : <span class="keyword">public</span> [PositionWaypointMotion](classfranky_1_1_position_waypoint_motion.md)\<franka::JointPositions, JointState\> {

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span> <span class="keyword">explicit</span> [JointWaypointMotion](classfranky_1_1_joint_waypoint_motion.md)(

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span> <span class="keyword">const</span> std::vector\<[PositionWaypoint\<JointState\>](structfranky_1_1_position_waypoint.md)\> \&waypoints,

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span> <span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0, <span class="keywordtype">bool</span> return\_when\_finished = <span class="keyword">true</span>);

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span>

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span> <span class="keyword">protected</span>:

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> <span class="keywordtype">void</span> [initWaypointMotion](classfranky_1_1_joint_waypoint_motion.md#a8929547df53cb581ae3d048941c1cc3d)(

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::JointPositions\> \&previous\_command,

</div>

<div class="line">

<span id="l00036"></span><span class="lineno"> 36</span> ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span> <span class="keywordtype">void</span> [setNewWaypoint](classfranky_1_1_joint_waypoint_motion.md#ac593e35c498848e339263654c976078d)(

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::JointPositions\> \&previous\_command,

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> <span class="keyword">const</span> [PositionWaypoint\<JointState\>](structfranky_1_1_position_waypoint.md) \&new\_waypoint, ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span>

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> \[\[nodiscard\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getAbsoluteInputLimits](classfranky_1_1_joint_waypoint_motion.md#a861df703835e15f447a9f40affe3625a)() <span class="keyword">const override</span>;

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span>

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> \[\[nodiscard\]\] franka::JointPositions [getControlSignal](classfranky_1_1_joint_waypoint_motion.md#a25acf41fa306d902c797dafa973b9170)(

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> franka::Duration \&time\_step,

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span> <span class="keyword">const</span> std::optional\<franka::JointPositions\> \&previous\_command,

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keyword">const</span> ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> \[\[nodiscard\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getDesiredState](classfranky_1_1_joint_waypoint_motion.md#a6389b5993ad5d5fd416b5f116aad3ec2)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state) <span class="keyword">const override</span>;

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

<div id="aclassfranky_1_1_joint_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::JointWaypointMotion](classfranky_1_1_joint_waypoint_motion.md)

</div>

<div class="ttdoc">

Joint waypoint motion.

</div>

<div class="ttdef">

**Definition** joint\_waypoint\_motion.hpp:19

</div>

</div>

<div id="aclassfranky_1_1_joint_waypoint_motion_html_a25acf41fa306d902c797dafa973b9170" class="ttc">

<div class="ttname">

[franky::JointWaypointMotion::getControlSignal](classfranky_1_1_joint_waypoint_motion.md#a25acf41fa306d902c797dafa973b9170)

</div>

<div class="ttdeci">

franka::JointPositions getControlSignal(const RobotState \&robot\_state, const franka::Duration \&time\_step, const std::optional\< franka::JointPositions \> \&previous\_command, const ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** joint\_waypoint\_motion.cpp:25

</div>

</div>

<div id="aclassfranky_1_1_joint_waypoint_motion_html_a6389b5993ad5d5fd416b5f116aad3ec2" class="ttc">

<div class="ttname">

[franky::JointWaypointMotion::getDesiredState](classfranky_1_1_joint_waypoint_motion.md#a6389b5993ad5d5fd416b5f116aad3ec2)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getDesiredState(const RobotState \&robot\_state) const override

</div>

<div class="ttdef">

**Definition** joint\_waypoint\_motion.cpp:47

</div>

</div>

<div id="aclassfranky_1_1_joint_waypoint_motion_html_a861df703835e15f447a9f40affe3625a" class="ttc">

<div class="ttname">

[franky::JointWaypointMotion::getAbsoluteInputLimits](classfranky_1_1_joint_waypoint_motion.md#a861df703835e15f447a9f40affe3625a)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getAbsoluteInputLimits() const override

</div>

<div class="ttdef">

**Definition** joint\_waypoint\_motion.cpp:42

</div>

</div>

<div id="aclassfranky_1_1_joint_waypoint_motion_html_a8929547df53cb581ae3d048941c1cc3d" class="ttc">

<div class="ttname">

[franky::JointWaypointMotion::initWaypointMotion](classfranky_1_1_joint_waypoint_motion.md#a8929547df53cb581ae3d048941c1cc3d)

</div>

<div class="ttdeci">

void initWaypointMotion(const RobotState \&robot\_state, const std::optional\< franka::JointPositions \> \&previous\_command, ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** joint\_waypoint\_motion.cpp:14

</div>

</div>

<div id="aclassfranky_1_1_joint_waypoint_motion_html_ac593e35c498848e339263654c976078d" class="ttc">

<div class="ttname">

[franky::JointWaypointMotion::setNewWaypoint](classfranky_1_1_joint_waypoint_motion.md#ac593e35c498848e339263654c976078d)

</div>

<div class="ttdeci">

void setNewWaypoint(const RobotState \&robot\_state, const std::optional\< franka::JointPositions \> \&previous\_command, const PositionWaypoint\< JointState \> \&new\_waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** joint\_waypoint\_motion.cpp:31

</div>

</div>

<div id="aclassfranky_1_1_position_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::PositionWaypointMotion](classfranky_1_1_position_waypoint_motion.md)

</div>

<div class="ttdoc">

A motion following multiple positional waypoints in a time-optimal way. Works with arbitrary initial ...

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:33

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

<div id="aposition__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[position\_waypoint\_motion.hpp](position__waypoint__motion_8hpp.md)

</div>

</div>

<div id="astructfranky_1_1_position_waypoint_html" class="ttc">

<div class="ttname">

[franky::PositionWaypoint](structfranky_1_1_position_waypoint.md)

</div>

<div class="ttdoc">

A position waypoint with a target and optional parameters.

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:20

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

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
