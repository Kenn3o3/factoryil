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

</div>

</div>

<div class="header">

<div class="headertitle">

<div class="title">

robot\_state\_estimator.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](robot__state__estimator_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include "[franky/model.hpp](model_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include "[franky/robot\_state.hpp](robot__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span>

</div>

<div id="foldopen00008" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00008"></span><span class="lineno"> [8](classfranky_1_1_robot_state_estimator.md)</span><span class="keyword">class </span>[RobotStateEstimator](classfranky_1_1_robot_state_estimator.md) {

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span> [RobotStateEstimator](classfranky_1_1_robot_state_estimator.md)(

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span> <span class="keywordtype">double</span> [q\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [dq\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [ddq\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [control\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [q\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span> <span class="keywordtype">double</span> [dq\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [q\_d\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [dq\_d\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [ddq\_d\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">double</span> [control\_adaptation\_rate](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> [14](classfranky_1_1_robot_state_estimator.md#a69e0374844fe46ea58ae8c7e0db0c351)</span> [RobotStateEstimator](classfranky_1_1_robot_state_estimator.md#a69e0374844fe46ea58ae8c7e0db0c351)(<span class="keyword">const</span> [RobotStateEstimator](classfranky_1_1_robot_state_estimator.md) &) = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span> [RobotState](structfranky_1_1_robot_state.md) [update](classfranky_1_1_robot_state_estimator.md#a7a1712e861d5790171fc0d9ec467687d)(<span class="keyword">const</span> franka::RobotState &[franka\_robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Model](classfranky_1_1_model.md) \&model);

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span>

</div>

<div id="foldopen00018" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](classfranky_1_1_robot_state_estimator.md#a832d262bc83ad2d21a5e8c9f63838cbb)</span> [RobotState](structfranky_1_1_robot_state.md) [operator()](classfranky_1_1_robot_state_estimator.md#a832d262bc83ad2d21a5e8c9f63838cbb)(<span class="keyword">const</span> franka::RobotState &[franka\_robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Model](classfranky_1_1_model.md) \&model) {

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span> <span class="keywordflow">return</span> [update](classfranky_1_1_robot_state_estimator.md#a7a1712e861d5790171fc0d9ec467687d)([franka\_robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), model);

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span> }

</div>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span>

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span> <span class="keywordtype">double</span> q\_process\_var\_;

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> <span class="keywordtype">double</span> dq\_process\_var\_;

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> <span class="keywordtype">double</span> ddq\_process\_var\_;

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span> <span class="keywordtype">double</span> control\_process\_var\_;

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span> <span class="keywordtype">double</span> control\_adaptation\_rate\_;

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span>

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span> Eigen::Matrix\<double, 5, 6\> h\_mat\_;

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span> Eigen::Matrix\<double, 5, 5\> r\_mat\_;

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span>

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span> std::optional\<franka::Duration\> prev\_time\_{};

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span> Eigen::Matrix\<double, 6, 7\> joint\_state\_mean\_;

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> std::array\<Eigen::Matrix\<double, 6, 6\>, 7\> joint\_state\_covar\_;

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span>};

</div>

</div>

<div class="line">

<span id="l00036"></span><span class="lineno"> 36</span>

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_model_html" class="ttc">

<div class="ttname">

[franky::Model](classfranky_1_1_model.md)

</div>

<div class="ttdoc">

A wrapper around franka::Model that uses Eigen types.

</div>

<div class="ttdef">

**Definition** model.hpp:18

</div>

</div>

<div id="aclassfranky_1_1_robot_state_estimator_html" class="ttc">

<div class="ttname">

[franky::RobotStateEstimator](classfranky_1_1_robot_state_estimator.md)

</div>

<div class="ttdef">

**Definition** robot\_state\_estimator.hpp:8

</div>

</div>

<div id="aclassfranky_1_1_robot_state_estimator_html_a69e0374844fe46ea58ae8c7e0db0c351" class="ttc">

<div class="ttname">

[franky::RobotStateEstimator::RobotStateEstimator](classfranky_1_1_robot_state_estimator.md#a69e0374844fe46ea58ae8c7e0db0c351)

</div>

<div class="ttdeci">

RobotStateEstimator(const RobotStateEstimator &)=default

</div>

</div>

<div id="aclassfranky_1_1_robot_state_estimator_html_a7a1712e861d5790171fc0d9ec467687d" class="ttc">

<div class="ttname">

[franky::RobotStateEstimator::update](classfranky_1_1_robot_state_estimator.md#a7a1712e861d5790171fc0d9ec467687d)

</div>

<div class="ttdeci">

RobotState update(const franka::RobotState \&franka\_robot\_state, const Model \&model)

</div>

<div class="ttdef">

**Definition** robot\_state\_estimator.cpp:32

</div>

</div>

<div id="aclassfranky_1_1_robot_state_estimator_html_a832d262bc83ad2d21a5e8c9f63838cbb" class="ttc">

<div class="ttname">

[franky::RobotStateEstimator::operator()](classfranky_1_1_robot_state_estimator.md#a832d262bc83ad2d21a5e8c9f63838cbb)

</div>

<div class="ttdeci">

RobotState operator()(const franka::RobotState \&franka\_robot\_state, const Model \&model)

</div>

<div class="ttdef">

**Definition** robot\_state\_estimator.hpp:18

</div>

</div>

<div id="amodel_8hpp_html" class="ttc">

<div class="ttname">

[model.hpp](model_8hpp.md)

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

<div id="arobot__state_8hpp_html" class="ttc">

<div class="ttname">

[robot\_state.hpp](robot__state_8hpp.md)

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
