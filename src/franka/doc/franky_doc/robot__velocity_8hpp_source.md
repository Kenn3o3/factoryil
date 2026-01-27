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

robot\_velocity.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](robot__velocity_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/control\_types.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<Eigen/Core\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[franky/elbow\_state.hpp](elbow__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/twist.hpp](twist_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

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

<div id="foldopen00020" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00020"></span><span class="lineno"> [20](classfranky_1_1_robot_velocity.md)</span><span class="keyword">class </span>[RobotVelocity](classfranky_1_1_robot_velocity.md) {

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> [22](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)</span> [RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)();

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span>

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> [24](classfranky_1_1_robot_velocity.md#a05c422e3c640b24a825f0ed2d400fe7b)</span> [RobotVelocity](classfranky_1_1_robot_velocity.md#a05c422e3c640b24a825f0ed2d400fe7b)(<span class="keyword">const</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) &[robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span> <span class="comment">// Suppress implicit conversion warning</span>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span><span class="preprocessor">\#pragma clang diagnostic push</span>

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span><span class="preprocessor">\#pragma clang diagnostic ignored "-Wimplicit-conversion"</span>

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span> [RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)(<span class="keyword">const</span> [Twist](classfranky_1_1_twist.md) &[end\_effector\_twist](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b), std::optional\<double\> [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467) = std::nullopt);

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span><span class="preprocessor">\#pragma clang diagnostic pop</span>

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span>

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> <span class="keyword">explicit</span> [RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)(<span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c), <span class="keywordtype">bool</span> [ignore\_elbow](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>);

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span>

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span> <span class="keyword">explicit</span> [RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)(<span class="keyword">const</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c), std::optional\<double\> [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467) = std::nullopt);

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span>

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span> <span class="keyword">explicit</span> [RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)(franka::CartesianVelocities [franka\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span>

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c)() <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span>

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] franka::CartesianVelocities [as\_franka\_velocity](classfranky_1_1_robot_velocity.md#a03b492d4eb5585514405f78a88a1b6e0)(

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span> <span class="keyword">const</span> std::optional\<ElbowState\> \&elbow\_state = std::nullopt,

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span> [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) [default\_elbow\_flip\_direction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3)) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span>

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> [83](classfranky_1_1_robot_velocity.md#a7e10894668e53f945a34939cc828716e)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) [transform](classfranky_1_1_robot_velocity.md#a7e10894668e53f945a34939cc828716e)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{ <span class="keywordflow">return</span> [transform](classfranky_1_1_robot_velocity.md#a7e10894668e53f945a34939cc828716e)([affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).rotation()); }

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span>

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span> <span class="keyword">template</span> \<<span class="keyword">typename</span> RotationMatrixType\>

</div>

<div id="foldopen00092" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00092"></span><span class="lineno"> [92](classfranky_1_1_robot_velocity.md#a4e2cbc0ba39425815403cffcffdb6545)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) [transform](classfranky_1_1_robot_velocity.md#a4e2cbc0ba39425815403cffcffdb6545)(<span class="keyword">const</span> [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> 93</span> <span class="keywordflow">return</span> {[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \* end\_effector\_twist\_, elbow\_velocity\_};

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span> }

</div>

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> 95</span>

</div>

<div id="foldopen00105" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00105"></span><span class="lineno"> [105](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) [changeEndEffectorFrame](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95)(<span class="keyword">const</span> Eigen::Vector3d &[offset\_world\_frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> 106</span> <span class="keywordflow">return</span> {end\_effector\_twist\_.[propagateThroughLink](classfranky_1_1_twist.md#a896c0f6949127e1c37f5716b3f771bdb)([offset\_world\_frame](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)), elbow\_velocity\_};

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span> }

</div>

</div>

<div class="line">

<span id="l00108"></span><span class="lineno"> 108</span>

</div>

<div id="foldopen00115" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00115"></span><span class="lineno"> [115](classfranky_1_1_robot_velocity.md#aa53f2a9297f426cb327ee4172bd3ccd1)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) [withElbowVelocity](classfranky_1_1_robot_velocity.md#aa53f2a9297f426cb327ee4172bd3ccd1)(<span class="keyword">const</span> std::optional\<double\> [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00116"></span><span class="lineno"> 116</span> <span class="keywordflow">return</span> {end\_effector\_twist\_, [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)};

</div>

<div class="line">

<span id="l00117"></span><span class="lineno"> 117</span> }

</div>

</div>

<div class="line">

<span id="l00118"></span><span class="lineno"> 118</span>

</div>

<div class="line">

<span id="l00124"></span><span class="lineno"> [124](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> [Twist](classfranky_1_1_twist.md) [end\_effector\_twist](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> end\_effector\_twist\_; }

</div>

<div class="line">

<span id="l00125"></span><span class="lineno"> 125</span>

</div>

<div class="line">

<span id="l00131"></span><span class="lineno"> [131](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> std::optional\<double\> [elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> elbow\_velocity\_; }

</div>

<div class="line">

<span id="l00132"></span><span class="lineno"> 132</span>

</div>

<div class="line">

<span id="l00133"></span><span class="lineno"> 133</span> <span class="keyword">friend</span> std::ostream &[operator\<\<](classfranky_1_1_robot_velocity.md#a5650119c96c36dfba8aaf863df12e0aa)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) &[robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00134"></span><span class="lineno"> 134</span>

</div>

<div class="line">

<span id="l00135"></span><span class="lineno"> 135</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00136"></span><span class="lineno"> 136</span> [Twist](classfranky_1_1_twist.md) end\_effector\_twist\_;

</div>

<div class="line">

<span id="l00137"></span><span class="lineno"> 137</span> std::optional\<double\> elbow\_velocity\_ = std::nullopt;

</div>

<div class="line">

<span id="l00138"></span><span class="lineno"> 138</span>};

</div>

</div>

<div class="line">

<span id="l00139"></span><span class="lineno"> 139</span>

</div>

<div id="foldopen00140" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00140"></span><span class="lineno"> [140](namespacefranky.md#a27bbe5029544c4333715a85a7a43eaf5)</span><span class="keyword">inline</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) &[robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00141"></span><span class="lineno"> 141</span> <span class="keywordflow">return</span> [robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).transform([affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00142"></span><span class="lineno"> 142</span>}

</div>

</div>

<div class="line">

<span id="l00143"></span><span class="lineno"> 143</span>

</div>

<div class="line">

<span id="l00144"></span><span class="lineno"> 144</span><span class="keyword">template</span> \<<span class="keyword">typename</span> RotationMatrixType\>

</div>

<div id="foldopen00145" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00145"></span><span class="lineno"> [145](namespacefranky.md#ac6fc3324a4cf6df2787a64d6e84abb24)</span><span class="keyword">inline</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) &[robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00146"></span><span class="lineno"> 146</span> <span class="keywordflow">return</span> [robot\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).transform([rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00147"></span><span class="lineno"> 147</span>}

</div>

</div>

<div class="line">

<span id="l00148"></span><span class="lineno"> 148</span>

</div>

<div class="line">

<span id="l00149"></span><span class="lineno"> 149</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_robot_velocity_html_a03b492d4eb5585514405f78a88a1b6e0" class="ttc">

<div class="ttname">

[franky::RobotVelocity::as\_franka\_velocity](classfranky_1_1_robot_velocity.md#a03b492d4eb5585514405f78a88a1b6e0)

</div>

<div class="ttdeci">

franka::CartesianVelocities as\_franka\_velocity(const std::optional\< ElbowState \> \&elbow\_state=std::nullopt, FlipDirection default\_elbow\_flip\_direction=FlipDirection::kNegative) const

</div>

<div class="ttdoc">

Get the franka velocity.

</div>

<div class="ttdef">

**Definition** robot\_velocity.cpp:41

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_a05c422e3c640b24a825f0ed2d400fe7b" class="ttc">

<div class="ttname">

[franky::RobotVelocity::RobotVelocity](classfranky_1_1_robot_velocity.md#a05c422e3c640b24a825f0ed2d400fe7b)

</div>

<div class="ttdeci">

RobotVelocity(const RobotVelocity \&robot\_velocity)

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_a4e2cbc0ba39425815403cffcffdb6545" class="ttc">

<div class="ttname">

[franky::RobotVelocity::transform](classfranky_1_1_robot_velocity.md#a4e2cbc0ba39425815403cffcffdb6545)

</div>

<div class="ttdeci">

RobotVelocity transform(const RotationMatrixType \&rotation) const

</div>

<div class="ttdoc">

Transform the frame of the velocity by applying the given rotation.

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:92

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_a5650119c96c36dfba8aaf863df12e0aa" class="ttc">

<div class="ttname">

[franky::RobotVelocity::operator\<\<](classfranky_1_1_robot_velocity.md#a5650119c96c36dfba8aaf863df12e0aa)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const RobotVelocity \&robot\_velocity)

</div>

<div class="ttdef">

**Definition** robot\_velocity.cpp:48

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_a7e10894668e53f945a34939cc828716e" class="ttc">

<div class="ttname">

[franky::RobotVelocity::transform](classfranky_1_1_robot_velocity.md#a7e10894668e53f945a34939cc828716e)

</div>

<div class="ttdeci">

RobotVelocity transform(const Affine \&affine) const

</div>

<div class="ttdoc">

Transform the frame of the velocity by applying the given affine transform.

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:83

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_aa53f2a9297f426cb327ee4172bd3ccd1" class="ttc">

<div class="ttname">

[franky::RobotVelocity::withElbowVelocity](classfranky_1_1_robot_velocity.md#aa53f2a9297f426cb327ee4172bd3ccd1)

</div>

<div class="ttdeci">

RobotVelocity withElbowVelocity(const std::optional\< double \> elbow\_velocity) const

</div>

<div class="ttdoc">

Get the velocity with a new elbow velocity.

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:115

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_ab5457d7739425402e41821a66d7ab32c" class="ttc">

<div class="ttname">

[franky::RobotVelocity::vector\_repr](classfranky_1_1_robot_velocity.md#ab5457d7739425402e41821a66d7ab32c)

</div>

<div class="ttdeci">

Vector7d vector\_repr() const

</div>

<div class="ttdoc">

Get the vector representation of the velocity. It consists of the linear and angular velocity of the ...

</div>

<div class="ttdef">

**Definition** robot\_velocity.cpp:35

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_ab7fe3ffb8b3a627027d6441d57223c95" class="ttc">

<div class="ttname">

[franky::RobotVelocity::changeEndEffectorFrame](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95)

</div>

<div class="ttdeci">

RobotVelocity changeEndEffectorFrame(const Eigen::Vector3d \&offset\_world\_frame) const

</div>

<div class="ttdoc">

Change the end-effector frame by adding the given offset to the current end-effector frame....

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:105

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_ac7f635a3ee546c5fb8c0d6ffbd3e0467" class="ttc">

<div class="ttname">

[franky::RobotVelocity::elbow\_velocity](classfranky_1_1_robot_velocity.md#ac7f635a3ee546c5fb8c0d6ffbd3e0467)

</div>

<div class="ttdeci">

std::optional\< double \> elbow\_velocity() const

</div>

<div class="ttdoc">

Get the elbow velocity.

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:131

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_addf40a07374fd18d74d84c7027291b2b" class="ttc">

<div class="ttname">

[franky::RobotVelocity::end\_effector\_twist](classfranky_1_1_robot_velocity.md#addf40a07374fd18d74d84c7027291b2b)

</div>

<div class="ttdeci">

Twist end\_effector\_twist() const

</div>

<div class="ttdoc">

Get the end effector twist.

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:124

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html_afe5611a93ddbac86a054f5c9dd7c2310" class="ttc">

<div class="ttname">

[franky::RobotVelocity::RobotVelocity](classfranky_1_1_robot_velocity.md#afe5611a93ddbac86a054f5c9dd7c2310)

</div>

<div class="ttdeci">

RobotVelocity()

</div>

</div>

<div id="aclassfranky_1_1_twist_html" class="ttc">

<div class="ttname">

[franky::Twist](classfranky_1_1_twist.md)

</div>

<div class="ttdoc">

Twist of a frame.

</div>

<div class="ttdef">

**Definition** twist.hpp:13

</div>

</div>

<div id="aclassfranky_1_1_twist_html_a896c0f6949127e1c37f5716b3f771bdb" class="ttc">

<div class="ttname">

[franky::Twist::propagateThroughLink](classfranky_1_1_twist.md#a896c0f6949127e1c37f5716b3f771bdb)

</div>

<div class="ttdeci">

Twist propagateThroughLink(const Eigen::Vector3d \&link\_translation) const

</div>

<div class="ttdoc">

Propagate the twist through a link with the given translation. Hence, suppose this twist is the twist...

</div>

<div class="ttdef">

**Definition** twist.hpp:77

</div>

</div>

<div id="aelbow__state_8hpp_html" class="ttc">

<div class="ttname">

[elbow\_state.hpp](elbow__state_8hpp.md)

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

<div id="anamespacefranky_html_a4c30c0e173a1886238ed773e005be361" class="ttc">

<div class="ttname">

[franky::operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)

</div>

<div class="ttdeci">

CartesianState operator\*(const Affine \&transform, const CartesianState \&cartesian\_state)

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:76

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

<div id="anamespacefranky_html_a92a07a88df41e482914cf4f9f2dddecb" class="ttc">

<div class="ttname">

[franky::Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb)

</div>

<div class="ttdeci">

Eigen::Vector\< double, 6 \> Vector6d

</div>

<div class="ttdef">

**Definition** types.hpp:10

</div>

</div>

<div id="anamespacefranky_html_aaebafd6d1e78da2a42cf35eb266cb43b" class="ttc">

<div class="ttname">

[franky::FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b)

</div>

<div class="ttdeci">

FlipDirection

</div>

<div class="ttdoc">

Flip direction of a joint.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:12

</div>

</div>

<div id="anamespacefranky_html_aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3" class="ttc">

<div class="ttname">

[franky::FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3)

</div>

<div class="ttdeci">

@ kNegative

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

<div id="atwist_8hpp_html" class="ttc">

<div class="ttname">

[twist.hpp](twist_8hpp.md)

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
