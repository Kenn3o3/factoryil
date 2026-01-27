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

cartesian\_impedance\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](cartesian__impedance__motion_8hpp.md)

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

<span id="l00009"></span><span class="lineno"> 9</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span>

</div>

<div id="foldopen00019" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00019"></span><span class="lineno"> [19](classfranky_1_1_cartesian_impedance_motion.md)</span><span class="keyword">class </span>[CartesianImpedanceMotion](classfranky_1_1_cartesian_impedance_motion.md) : <span class="keyword">public</span> [ImpedanceMotion](classfranky_1_1_impedance_motion.md) {

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00025" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00025"></span><span class="lineno"> [25](structfranky_1_1_cartesian_impedance_motion_1_1_params.md)</span> <span class="keyword">struct </span>[Params](structfranky_1_1_cartesian_impedance_motion_1_1_params.md) : <span class="keyword">public</span> [ImpedanceMotion::Params](structfranky_1_1_impedance_motion_1_1_params.md) {

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> [28](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#a55fe8148f737b8ab7856d39cb5e1733d)</span> <span class="keywordtype">bool</span> [return\_when\_finished](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#a55fe8148f737b8ab7856d39cb5e1733d){<span class="keyword">true</span>};

</div>

<div class="line">

<span id="l00036"></span><span class="lineno"> [36](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#acc7d37d06d998daec4c4a7c8dcfcf3cb)</span> <span class="keywordtype">double</span> [finish\_wait\_factor](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#acc7d37d06d998daec4c4a7c8dcfcf3cb){1.2};

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span> };

</div>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span>

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> <span class="keyword">explicit</span> [CartesianImpedanceMotion](classfranky_1_1_cartesian_impedance_motion.md)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97), franka::Duration duration);

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span>

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span> <span class="keyword">explicit</span> [CartesianImpedanceMotion](classfranky_1_1_cartesian_impedance_motion.md)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97), franka::Duration duration, <span class="keyword">const</span> Params \&params);

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span>

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> <span class="keyword">protected</span>:

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> <span class="keywordtype">void</span> [initImpl](classfranky_1_1_cartesian_impedance_motion.md#a224f09b1b32ab145ff9db2c10220c51d)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::Torques\> \&previous\_command) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span>

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span> std::tuple\<Affine, bool\> [update](classfranky_1_1_cartesian_impedance_motion.md#a9f89c79e4872f1a0fa736ea1ff6ffb93)(

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration time\_step, franka::Duration time) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span>

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) initial\_pose\_;

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span> franka::Duration duration\_;

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> Params params\_;

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span>};

</div>

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_cartesian_impedance_motion_html" class="ttc">

<div class="ttname">

[franky::CartesianImpedanceMotion](classfranky_1_1_cartesian_impedance_motion.md)

</div>

<div class="ttdoc">

Cartesian impedance motion.

</div>

<div class="ttdef">

**Definition** cartesian\_impedance\_motion.hpp:19

</div>

</div>

<div id="aclassfranky_1_1_cartesian_impedance_motion_html_a224f09b1b32ab145ff9db2c10220c51d" class="ttc">

<div class="ttname">

[franky::CartesianImpedanceMotion::initImpl](classfranky_1_1_cartesian_impedance_motion.md#a224f09b1b32ab145ff9db2c10220c51d)

</div>

<div class="ttdeci">

void initImpl(const RobotState \&robot\_state, const std::optional\< franka::Torques \> \&previous\_command) override

</div>

<div class="ttdef">

**Definition** cartesian\_impedance\_motion.cpp:18

</div>

</div>

<div id="aclassfranky_1_1_cartesian_impedance_motion_html_a9f89c79e4872f1a0fa736ea1ff6ffb93" class="ttc">

<div class="ttname">

[franky::CartesianImpedanceMotion::update](classfranky_1_1_cartesian_impedance_motion.md#a9f89c79e4872f1a0fa736ea1ff6ffb93)

</div>

<div class="ttdeci">

std::tuple\< Affine, bool \> update(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration time) override

</div>

<div class="ttdef">

**Definition** cartesian\_impedance\_motion.cpp:24

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

<div id="astructfranky_1_1_cartesian_impedance_motion_1_1_params_html" class="ttc">

<div class="ttname">

[franky::CartesianImpedanceMotion::Params](structfranky_1_1_cartesian_impedance_motion_1_1_params.md)

</div>

<div class="ttdoc">

Parameters for the Cartesian impedance motion.

</div>

<div class="ttdef">

**Definition** cartesian\_impedance\_motion.hpp:25

</div>

</div>

<div id="astructfranky_1_1_cartesian_impedance_motion_1_1_params_html_a55fe8148f737b8ab7856d39cb5e1733d" class="ttc">

<div class="ttname">

[franky::CartesianImpedanceMotion::Params::return\_when\_finished](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#a55fe8148f737b8ab7856d39cb5e1733d)

</div>

<div class="ttdeci">

bool return\_when\_finished

</div>

<div class="ttdef">

**Definition** cartesian\_impedance\_motion.hpp:28

</div>

</div>

<div id="astructfranky_1_1_cartesian_impedance_motion_1_1_params_html_acc7d37d06d998daec4c4a7c8dcfcf3cb" class="ttc">

<div class="ttname">

[franky::CartesianImpedanceMotion::Params::finish\_wait\_factor](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#acc7d37d06d998daec4c4a7c8dcfcf3cb)

</div>

<div class="ttdeci">

double finish\_wait\_factor

</div>

<div class="ttdef">

**Definition** cartesian\_impedance\_motion.hpp:36

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
