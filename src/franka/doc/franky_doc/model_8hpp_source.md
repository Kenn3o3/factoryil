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

model.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](model_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/model.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<[franky/robot\_state.hpp](robot__state_8hpp.md)\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span>

</div>

<div id="foldopen00018" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](classfranky_1_1_model.md)</span><span class="keyword">class </span>[Model](classfranky_1_1_model.md) {

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span> <span class="keyword">explicit</span> [Model](classfranky_1_1_model.md)(franka::Model model);

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> [25](classfranky_1_1_model.md#a0e0f5759222c436e411fee99f1cc2d93)</span> [Model](classfranky_1_1_model.md#a0e0f5759222c436e411fee99f1cc2d93)(<span class="keyword">const</span> [Model](classfranky_1_1_model.md) &) = <span class="keyword">delete</span>;

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> [26](classfranky_1_1_model.md#a5b3f54790270c3d9118a9595abfbcc8f)</span> [Model](classfranky_1_1_model.md) &[operator=](classfranky_1_1_model.md#a5b3f54790270c3d9118a9595abfbcc8f)(<span class="keyword">const</span> [Model](classfranky_1_1_model.md) &) = <span class="keyword">delete</span>;

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span>

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span> [Model](classfranky_1_1_model.md)([Model](classfranky_1_1_model.md) &\&other) <span class="keyword">noexcept</span>;

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span> [Model](classfranky_1_1_model.md) &[operator=](classfranky_1_1_model.md#a5b3f54790270c3d9118a9595abfbcc8f)([Model](classfranky_1_1_model.md) &\&other) <span class="keyword">noexcept</span>;

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span> \[\[nodiscard\]\] [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [pose](classfranky_1_1_model.md#a09d525af34503e95214f7bd07e616e64)(franka::Frame frame, <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&state) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> \[\[nodiscard\]\] [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [pose](classfranky_1_1_model.md#a09d525af34503e95214f7bd07e616e64)(franka::Frame frame, <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&F\_T\_EE, <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&EE\_T\_K) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span>

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> \[\[nodiscard\]\] [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) [bodyJacobian](classfranky_1_1_model.md#a2473ad35c5b1cd9f89c80293ac84b434)(franka::Frame frame, <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&state) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span>

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> \[\[nodiscard\]\] [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) [bodyJacobian](classfranky_1_1_model.md#a2473ad35c5b1cd9f89c80293ac84b434)(

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span> franka::Frame frame, <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&F\_T\_EE, <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&EE\_T\_K) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> \[\[nodiscard\]\] [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) [zeroJacobian](classfranky_1_1_model.md#ad5c6a7ac820f5e4df98525e3a9acda81)(franka::Frame frame, <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&state) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span> \[\[nodiscard\]\] [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) [zeroJacobian](classfranky_1_1_model.md#ad5c6a7ac820f5e4df98525e3a9acda81)(

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span> franka::Frame frame, <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&F\_T\_EE, <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&EE\_T\_K) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> 92</span>

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span> \[\[nodiscard\]\] Eigen::Matrix\<double, 7, 7\> [mass](classfranky_1_1_model.md#a2b68eeac2f6990175097787f948d4f5b)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&state) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span>

</div>

<div class="line">

<span id="l00110"></span><span class="lineno"> 110</span> \[\[nodiscard\]\] Eigen::Matrix\<double, 7, 7\> [mass](classfranky_1_1_model.md#a2b68eeac2f6990175097787f948d4f5b)(

</div>

<div class="line">

<span id="l00111"></span><span class="lineno"> 111</span> <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, <span class="keyword">const</span> Eigen::Matrix3d \&I\_total, <span class="keywordtype">double</span> m\_total, <span class="keyword">const</span> Eigen::Vector3d \&F\_x\_Ctotal) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00112"></span><span class="lineno"> 112</span>

</div>

<div class="line">

<span id="l00119"></span><span class="lineno"> 119</span> \[\[nodiscard\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [coriolis](classfranky_1_1_model.md#ab71c9e3f23f6963568f2bb42397d1599)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&state) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00120"></span><span class="lineno"> 120</span>

</div>

<div class="line">

<span id="l00131"></span><span class="lineno"> 131</span> \[\[nodiscard\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [coriolis](classfranky_1_1_model.md#ab71c9e3f23f6963568f2bb42397d1599)(

</div>

<div class="line">

<span id="l00132"></span><span class="lineno"> 132</span> <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&dq, <span class="keyword">const</span> Eigen::Matrix3d \&I\_total, <span class="keywordtype">double</span> m\_total,

</div>

<div class="line">

<span id="l00133"></span><span class="lineno"> 133</span> <span class="keyword">const</span> Eigen::Vector3d \&F\_x\_Ctotal) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00134"></span><span class="lineno"> 134</span>

</div>

<div class="line">

<span id="l00142"></span><span class="lineno"> 142</span> \[\[nodiscard\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [gravity](classfranky_1_1_model.md#a72889aed517ceb27c48baf30b21b20e5)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&state, <span class="keyword">const</span> Eigen::Vector3d \&gravity\_earth) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00143"></span><span class="lineno"> 143</span>

</div>

<div class="line">

<span id="l00151"></span><span class="lineno"> 151</span> \[\[nodiscard\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [gravity](classfranky_1_1_model.md#a72889aed517ceb27c48baf30b21b20e5)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&state) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00152"></span><span class="lineno"> 152</span>

</div>

<div class="line">

<span id="l00163"></span><span class="lineno"> 163</span> \[\[nodiscard\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [gravity](classfranky_1_1_model.md#a72889aed517ceb27c48baf30b21b20e5)(

</div>

<div class="line">

<span id="l00164"></span><span class="lineno"> 164</span> <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \&q, <span class="keywordtype">double</span> m\_total, <span class="keyword">const</span> Eigen::Vector3d \&F\_x\_Ctotal,

</div>

<div class="line">

<span id="l00165"></span><span class="lineno"> 165</span> <span class="keyword">const</span> Eigen::Vector3d \&gravity\_earth = {0., 0., -9.81}) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00166"></span><span class="lineno"> 166</span>

</div>

<div class="line">

<span id="l00167"></span><span class="lineno"> 167</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00168"></span><span class="lineno"> 168</span> franka::Model model\_;

</div>

<div class="line">

<span id="l00169"></span><span class="lineno"> 169</span>};

</div>

</div>

<div class="line">

<span id="l00170"></span><span class="lineno"> 170</span>

</div>

<div class="line">

<span id="l00171"></span><span class="lineno"> 171</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_model_html_a09d525af34503e95214f7bd07e616e64" class="ttc">

<div class="ttname">

[franky::Model::pose](classfranky_1_1_model.md#a09d525af34503e95214f7bd07e616e64)

</div>

<div class="ttdeci">

Affine pose(franka::Frame frame, const RobotState \&state) const

</div>

<div class="ttdoc">

Calculates the pose of a frame relative to the base frame.

</div>

<div class="ttdef">

**Definition** model.cpp:18

</div>

</div>

<div id="aclassfranky_1_1_model_html_a0e0f5759222c436e411fee99f1cc2d93" class="ttc">

<div class="ttname">

[franky::Model::Model](classfranky_1_1_model.md#a0e0f5759222c436e411fee99f1cc2d93)

</div>

<div class="ttdeci">

Model(const Model &)=delete

</div>

</div>

<div id="aclassfranky_1_1_model_html_a2473ad35c5b1cd9f89c80293ac84b434" class="ttc">

<div class="ttname">

[franky::Model::bodyJacobian](classfranky_1_1_model.md#a2473ad35c5b1cd9f89c80293ac84b434)

</div>

<div class="ttdeci">

Jacobian bodyJacobian(franka::Frame frame, const RobotState \&state) const

</div>

<div class="ttdoc">

Calculates the body Jacobian in base frame.

</div>

<div class="ttdef">

**Definition** model.cpp:27

</div>

</div>

<div id="aclassfranky_1_1_model_html_a2b68eeac2f6990175097787f948d4f5b" class="ttc">

<div class="ttname">

[franky::Model::mass](classfranky_1_1_model.md#a2b68eeac2f6990175097787f948d4f5b)

</div>

<div class="ttdeci">

Eigen::Matrix\< double, 7, 7 \> mass(const RobotState \&state) const

</div>

<div class="ttdoc">

Calculates the mass matrix.

</div>

<div class="ttdef">

**Definition** model.cpp:45

</div>

</div>

<div id="aclassfranky_1_1_model_html_a5b3f54790270c3d9118a9595abfbcc8f" class="ttc">

<div class="ttname">

[franky::Model::operator=](classfranky_1_1_model.md#a5b3f54790270c3d9118a9595abfbcc8f)

</div>

<div class="ttdeci">

Model & operator=(const Model &)=delete

</div>

</div>

<div id="aclassfranky_1_1_model_html_a72889aed517ceb27c48baf30b21b20e5" class="ttc">

<div class="ttname">

[franky::Model::gravity](classfranky_1_1_model.md#a72889aed517ceb27c48baf30b21b20e5)

</div>

<div class="ttdeci">

Vector7d gravity(const RobotState \&state, const Eigen::Vector3d \&gravity\_earth) const

</div>

<div class="ttdoc">

Calculates the gravity vector.

</div>

<div class="ttdef">

**Definition** model.cpp:65

</div>

</div>

<div id="aclassfranky_1_1_model_html_ab71c9e3f23f6963568f2bb42397d1599" class="ttc">

<div class="ttname">

[franky::Model::coriolis](classfranky_1_1_model.md#ab71c9e3f23f6963568f2bb42397d1599)

</div>

<div class="ttdeci">

Vector7d coriolis(const RobotState \&state) const

</div>

<div class="ttdoc">

Calculates the Coriolis force vector.

</div>

<div class="ttdef">

**Definition** model.cpp:54

</div>

</div>

<div id="aclassfranky_1_1_model_html_ad5c6a7ac820f5e4df98525e3a9acda81" class="ttc">

<div class="ttname">

[franky::Model::zeroJacobian](classfranky_1_1_model.md#ad5c6a7ac820f5e4df98525e3a9acda81)

</div>

<div class="ttdeci">

Jacobian zeroJacobian(franka::Frame frame, const RobotState \&state) const

</div>

<div class="ttdoc">

Calculates the zero Jacobian in base frame.

</div>

<div class="ttdef">

**Definition** model.cpp:36

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

<div id="anamespacefranky_html_a4c36e6539a78f808bf759142dec935c4" class="ttc">

<div class="ttname">

[franky::Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)

</div>

<div class="ttdeci">

Eigen::Vector\< double, 7 \> Vector7d

</div>

<div class="ttdef">

**Definition** types.hpp:11

</div>

</div>

<div id="anamespacefranky_html_ab6d5b94e45f9e74b0a3195f76408bc8b" class="ttc">

<div class="ttname">

[franky::Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b)

</div>

<div class="ttdeci">

Eigen::Matrix\< double, 6, 7 \> Jacobian

</div>

<div class="ttdef">

**Definition** types.hpp:12

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

<div id="atypes_8hpp_html" class="ttc">

<div class="ttname">

[types.hpp](types_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
