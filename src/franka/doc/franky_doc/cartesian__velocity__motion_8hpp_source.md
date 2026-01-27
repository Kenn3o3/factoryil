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

cartesian\_velocity\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](cartesian__velocity__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include "[franky/motion/cartesian\_velocity\_waypoint\_motion.hpp](cartesian__velocity__waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span>

</div>

<div id="foldopen00010" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00010"></span><span class="lineno"> [10](classfranky_1_1_cartesian_velocity_motion.md)</span><span class="keyword">class </span>[CartesianVelocityMotion](classfranky_1_1_cartesian_velocity_motion.md) : <span class="keyword">public</span> [CartesianVelocityWaypointMotion](classfranky_1_1_cartesian_velocity_waypoint_motion.md) {

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> <span class="keyword">explicit</span> [CartesianVelocityMotion](classfranky_1_1_cartesian_velocity_motion.md)(

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span> <span class="keyword">const</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) \&target, <span class="keyword">const</span> franka::Duration \&duration = franka::Duration(1000),

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span> <span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0, <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&frame = Affine::Identity());

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span>};

</div>

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span>

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span>} <span class="comment">// namespace franky</span>

</div>

<div id="acartesian__velocity__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_velocity\_waypoint\_motion.hpp](cartesian__velocity__waypoint__motion_8hpp.md)

</div>

</div>

<div id="aclassfranky_1_1_cartesian_velocity_motion_html" class="ttc">

<div class="ttname">

[franky::CartesianVelocityMotion](classfranky_1_1_cartesian_velocity_motion.md)

</div>

<div class="ttdoc">

Cartesian velocity motion with a single target velocity.

</div>

<div class="ttdef">

**Definition** cartesian\_velocity\_motion.hpp:10

</div>

</div>

<div id="aclassfranky_1_1_cartesian_velocity_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::CartesianVelocityWaypointMotion](classfranky_1_1_cartesian_velocity_waypoint_motion.md)

</div>

<div class="ttdoc">

Cartesian velocity waypoint motion.

</div>

<div class="ttdef">

**Definition** cartesian\_velocity\_waypoint\_motion.hpp:23

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

<div id="aclassfranky_1_1_robot_velocity_html" class="ttc">

<div class="ttname">

[franky::RobotVelocity](classfranky_1_1_robot_velocity.md)

</div>

<div class="ttdoc">

Cartesian velocity of a robot.

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:20

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

<div id="anamespacefranky_html_afab9faf133666ada543b15236a8c4b5f" class="ttc">

<div class="ttname">

[franky::Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)

</div>

<div class="ttdeci">

Eigen::Affine3d Affine

</div>

<div class="ttdef">

**Definition** types.hpp:15

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
