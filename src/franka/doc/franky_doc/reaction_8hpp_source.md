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

reaction.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](reaction_8hpp.md)

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

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<cmath\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<functional\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include \<iostream\></span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include \<memory\></span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="preprocessor">\#include "[franky/motion/condition.hpp](condition_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="preprocessor">\#include "[franky/motion/motion.hpp](motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span><span class="keyword">class </span>Motion;

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> 18</span>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div id="foldopen00027" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00027"></span><span class="lineno"> [27](classfranky_1_1_reaction.md)</span><span class="keyword">class </span>[Reaction](classfranky_1_1_reaction.md) {

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span> <span class="keyword">using </span>MotionFunc =

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span> std::function\<std::shared\_ptr\<Motion\<ControlSignalType\>\>(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\>;

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span> <span class="keyword">explicit</span> [Reaction](classfranky_1_1_reaction.md)(<span class="keyword">const</span> [Condition](classfranky_1_1_condition.md) &[condition](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710), std::shared\_ptr\<[Motion\<ControlSignalType\>](classfranky_1_1_motion.md)\> [new\_motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">nullptr</span>);

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span>

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> <span class="keyword">explicit</span> [Reaction](classfranky_1_1_reaction.md)([Condition](classfranky_1_1_condition.md) [condition](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710), <span class="keyword">const</span> MotionFunc &[motion\_func](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span>

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span> std::shared\_ptr\<Motion\<ControlSignalType\>\> [operator()](classfranky_1_1_reaction.md#ae2e5dd1a61d3649d638227afbc159aed)(

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span>

</div>

<div id="foldopen00068" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00068"></span><span class="lineno"> [68](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keywordtype">bool</span> [condition](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710)(

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span> <span class="keywordflow">return</span> condition\_([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> }

</div>

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> <span class="keywordtype">void</span> [registerCallback](classfranky_1_1_reaction.md#a7c6c3d1f2cbe80981574bf62137a8951)(<span class="keyword">const</span> std::function\<<span class="keywordtype">void</span>(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\> &[callback](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> MotionFunc motion\_func\_;

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span> [Condition](classfranky_1_1_condition.md) condition\_;

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span> std::mutex callback\_mutex\_;

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span> std::vector\<std::function\<[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\>\> callbacks\_{};

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span>};

</div>

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span>

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_condition_html" class="ttc">

<div class="ttname">

[franky::Condition](classfranky_1_1_condition.md)

</div>

<div class="ttdoc">

A condition on the robot state.

</div>

<div class="ttdef">

**Definition** condition.hpp:16

</div>

</div>

<div id="aclassfranky_1_1_motion_html" class="ttc">

<div class="ttname">

[franky::Motion](classfranky_1_1_motion.md)

</div>

<div class="ttdoc">

Base class for motions.

</div>

<div class="ttdef">

**Definition** motion.hpp:24

</div>

</div>

<div id="aclassfranky_1_1_reaction_html" class="ttc">

<div class="ttname">

[franky::Reaction](classfranky_1_1_reaction.md)

</div>

<div class="ttdoc">

A reaction that can be attached to a motion.

</div>

<div class="ttdef">

**Definition** reaction.hpp:27

</div>

</div>

<div id="aclassfranky_1_1_reaction_html_a12dac9b49fbe8e6f57f90b802ba05710" class="ttc">

<div class="ttname">

[franky::Reaction::condition](classfranky_1_1_reaction.md#a12dac9b49fbe8e6f57f90b802ba05710)

</div>

<div class="ttdeci">

bool condition(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time) const

</div>

<div class="ttdoc">

Check if the condition is met.

</div>

<div class="ttdef">

**Definition** reaction.hpp:68

</div>

</div>

<div id="aclassfranky_1_1_reaction_html_a7c6c3d1f2cbe80981574bf62137a8951" class="ttc">

<div class="ttname">

[franky::Reaction::registerCallback](classfranky_1_1_reaction.md#a7c6c3d1f2cbe80981574bf62137a8951)

</div>

<div class="ttdeci">

void registerCallback(const std::function\< void(const RobotState &, franka::Duration, franka::Duration)\> \&callback)

</div>

<div class="ttdoc">

Register a callback that is called when the condition of this reaction is met.

</div>

<div class="ttdef">

**Definition** reaction.cpp:41

</div>

</div>

<div id="aclassfranky_1_1_reaction_html_ae2e5dd1a61d3649d638227afbc159aed" class="ttc">

<div class="ttname">

[franky::Reaction::operator()](classfranky_1_1_reaction.md#ae2e5dd1a61d3649d638227afbc159aed)

</div>

<div class="ttdeci">

std::shared\_ptr\< Motion\< ControlSignalType \> \> operator()(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)

</div>

<div class="ttdoc">

Get the new motion if the condition is met.

</div>

<div class="ttdef">

**Definition** reaction.cpp:33

</div>

</div>

<div id="acondition_8hpp_html" class="ttc">

<div class="ttname">

[condition.hpp](condition_8hpp.md)

</div>

</div>

<div id="amotion_8hpp_html" class="ttc">

<div class="ttname">

[motion.hpp](motion_8hpp.md)

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

<div id="anamespacefranky_html_a0b6bfc825c262ae89d9b0adcccd97ab0" class="ttc">

<div class="ttname">

[franky::toStdD](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

</div>

<div class="ttdeci">

std::array\< double, dims \> toStdD(const Eigen::Matrix\< double, dims, 1 \> \&vector)

</div>

<div class="ttdef">

**Definition** util.hpp:18

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
