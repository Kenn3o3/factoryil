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

exponential\_impedance\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](exponential__impedance__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<Eigen/Core\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<Eigen/Geometry\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<map\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[franky/motion/impedance\_motion.hpp](impedance__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/robot\_pose.hpp](robot__pose_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span>

</div>

<div id="foldopen00021" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00021"></span><span class="lineno"> [21](classfranky_1_1_exponential_impedance_motion.md)</span><span class="keyword">class </span>[ExponentialImpedanceMotion](classfranky_1_1_exponential_impedance_motion.md) : <span class="keyword">public</span> [ImpedanceMotion](classfranky_1_1_impedance_motion.md) {

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00027" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00027"></span><span class="lineno"> [27](structfranky_1_1_exponential_impedance_motion_1_1_params.md)</span> <span class="keyword">struct </span>[Params](structfranky_1_1_exponential_impedance_motion_1_1_params.md) : <span class="keyword">public</span> [ImpedanceMotion::Params](structfranky_1_1_impedance_motion_1_1_params.md) {

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> [29](structfranky_1_1_exponential_impedance_motion_1_1_params.md#ae0c147c8036555b808a53ee71c3f18da)</span> <span class="keywordtype">double</span> [exponential\_decay](structfranky_1_1_exponential_impedance_motion_1_1_params.md#ae0c147c8036555b808a53ee71c3f18da){0.005};

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span> };

</div>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span>

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span> <span class="keyword">explicit</span> [ExponentialImpedanceMotion](classfranky_1_1_exponential_impedance_motion.md)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97));

</div>

<div class="line">

<span id="l00036"></span><span class="lineno"> 36</span>

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> <span class="keyword">explicit</span> [ExponentialImpedanceMotion](classfranky_1_1_exponential_impedance_motion.md)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97), <span class="keyword">const</span> Params \&params);

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span>

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> <span class="keyword">protected</span>:

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> std::tuple\<Affine, bool\> [update](classfranky_1_1_exponential_impedance_motion.md#a09d2d86cfd46ce2238dacf4d471cf9f8)(

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration time\_step, franka::Duration time) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span>

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span> Params params\_;

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span>};

</div>

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span>

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_exponential_impedance_motion_html" class="ttc">

<div class="ttname">

[franky::ExponentialImpedanceMotion](classfranky_1_1_exponential_impedance_motion.md)

</div>

<div class="ttdoc">

Exponential cartesian impedance motion.

</div>

<div class="ttdef">

**Definition** exponential\_impedance\_motion.hpp:21

</div>

</div>

<div id="aclassfranky_1_1_exponential_impedance_motion_html_a09d2d86cfd46ce2238dacf4d471cf9f8" class="ttc">

<div class="ttname">

[franky::ExponentialImpedanceMotion::update](classfranky_1_1_exponential_impedance_motion.md#a09d2d86cfd46ce2238dacf4d471cf9f8)

</div>

<div class="ttdeci">

std::tuple\< Affine, bool \> update(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration time) override

</div>

<div class="ttdef">

**Definition** exponential\_impedance\_motion.cpp:18

</div>

</div>

<div id="aclassfranky_1_1_impedance_motion_html" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)

</div>

<div class="ttdoc">

Base class for client-side cartesian impedance motions.

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:21

</div>

</div>

<div id="aclassfranky_1_1_impedance_motion_html_a1ce961ddf51cd792482fd5ca2b299d97" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97)

</div>

<div class="ttdeci">

Affine target() const

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:58

</div>

</div>

<div id="aimpedance__motion_8hpp_html" class="ttc">

<div class="ttname">

[impedance\_motion.hpp](impedance__motion_8hpp.md)

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

<div id="arobot__pose_8hpp_html" class="ttc">

<div class="ttname">

[robot\_pose.hpp](robot__pose_8hpp.md)

</div>

</div>

<div id="astructfranky_1_1_exponential_impedance_motion_1_1_params_html" class="ttc">

<div class="ttname">

[franky::ExponentialImpedanceMotion::Params](structfranky_1_1_exponential_impedance_motion_1_1_params.md)

</div>

<div class="ttdoc">

Parameters for the exponential cartesian impedance motion.

</div>

<div class="ttdef">

**Definition** exponential\_impedance\_motion.hpp:27

</div>

</div>

<div id="astructfranky_1_1_exponential_impedance_motion_1_1_params_html_ae0c147c8036555b808a53ee71c3f18da" class="ttc">

<div class="ttname">

[franky::ExponentialImpedanceMotion::Params::exponential\_decay](structfranky_1_1_exponential_impedance_motion_1_1_params.md#ae0c147c8036555b808a53ee71c3f18da)

</div>

<div class="ttdeci">

double exponential\_decay

</div>

<div class="ttdef">

**Definition** exponential\_impedance\_motion.hpp:29

</div>

</div>

<div id="astructfranky_1_1_impedance_motion_1_1_params_html" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::Params](structfranky_1_1_impedance_motion_1_1_params.md)

</div>

<div class="ttdoc">

Parameters for the impedance motion.

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:26

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
