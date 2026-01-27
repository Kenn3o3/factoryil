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

joint\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](joint__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include "[franky/joint\_state.hpp](joint__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include "[franky/motion/joint\_waypoint\_motion.hpp](joint__waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include "[franky/motion/reference\_type.hpp](reference__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span>

</div>

<div id="foldopen00012" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00012"></span><span class="lineno"> [12](classfranky_1_1_joint_motion.md)</span><span class="keyword">class </span>[JointMotion](classfranky_1_1_joint_motion.md) : <span class="keyword">public</span> [JointWaypointMotion](classfranky_1_1_joint_waypoint_motion.md) {

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span> <span class="keyword">explicit</span> [JointMotion](classfranky_1_1_joint_motion.md)(

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span> <span class="keyword">const</span> [JointState](classfranky_1_1_joint_state.md) \&target, [ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e) reference\_type = [ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a),

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> <span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0, <span class="keywordtype">bool</span> return\_when\_finished = <span class="keyword">true</span>);

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span>};

</div>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_joint_motion_html" class="ttc">

<div class="ttname">

[franky::JointMotion](classfranky_1_1_joint_motion.md)

</div>

<div class="ttdoc">

Joint motion with a single target.

</div>

<div class="ttdef">

**Definition** joint\_motion.hpp:12

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html" class="ttc">

<div class="ttname">

[franky::JointState](classfranky_1_1_joint_state.md)

</div>

<div class="ttdoc">

Joint state of a robot.

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:16

</div>

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

<div id="ajoint__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[joint\_waypoint\_motion.hpp](joint__waypoint__motion_8hpp.md)

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

<div id="anamespacefranky_html_a2354a27cfe3100f07e0ad71513ded80e" class="ttc">

<div class="ttname">

[franky::ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e)

</div>

<div class="ttdeci">

ReferenceType

</div>

<div class="ttdoc">

Enum class for reference types.

</div>

<div class="ttdef">

**Definition** reference\_type.hpp:11

</div>

</div>

<div id="anamespacefranky_html_a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a" class="ttc">

<div class="ttname">

[franky::ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)

</div>

<div class="ttdeci">

@ kAbsolute

</div>

</div>

<div id="areference__type_8hpp_html" class="ttc">

<div class="ttname">

[reference\_type.hpp](reference__type_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
