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

robot\_pose.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](robot__pose_8hpp.md)

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

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

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

<div id="foldopen00019" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00019"></span><span class="lineno"> [19](classfranky_1_1_robot_pose.md)</span><span class="keyword">class </span>[RobotPose](classfranky_1_1_robot_pose.md) {

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span> [RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)();

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span>

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> [23](classfranky_1_1_robot_pose.md#a33ec908498b031c97c384e220f5fa6db)</span> [RobotPose](classfranky_1_1_robot_pose.md#a33ec908498b031c97c384e220f5fa6db)(<span class="keyword">const</span> [RobotPose](classfranky_1_1_robot_pose.md) &[robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> <span class="comment">// Suppress implicit conversion warning</span>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span><span class="preprocessor">\#pragma clang diagnostic push</span>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span><span class="preprocessor">\#pragma clang diagnostic ignored "-Wimplicit-conversion"</span>

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span> [RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)([Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd), std::optional\<ElbowState\> [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55) = std::nullopt);

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span><span class="preprocessor">\#pragma clang diagnostic pop</span>

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span>

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> <span class="keyword">explicit</span> [RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)(

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d), <span class="keywordtype">bool</span> [ignore\_elbow](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>, [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) [flip\_direction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3));

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span>

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span> <span class="keyword">explicit</span> [RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)(<span class="keyword">const</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d), std::optional\<ElbowState\> [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55) = std::nullopt);

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span>

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> <span class="keyword">explicit</span> [RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)(<span class="keyword">const</span> franka::CartesianPose &[franka\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span>

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d)() <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] franka::CartesianPose [as\_franka\_pose](classfranky_1_1_robot_pose.md#a87b43342db37db66af0b1411af496dd2)(

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span> [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) [default\_elbow\_flip\_direction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3)) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span>

</div>

<div id="foldopen00081" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00081"></span><span class="lineno"> [81](classfranky_1_1_robot_pose.md#adc234649707e63232c54d9e392db25c6)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RobotPose](classfranky_1_1_robot_pose.md) [leftTransform](classfranky_1_1_robot_pose.md#adc234649707e63232c54d9e392db25c6)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform)<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> <span class="keywordflow">return</span> {transform \* end\_effector\_pose\_, elbow\_state\_};

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span> }

</div>

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span>

</div>

<div id="foldopen00092" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00092"></span><span class="lineno"> [92](classfranky_1_1_robot_pose.md#afdbee35c5bf294ed93a139cc6280a076)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RobotPose](classfranky_1_1_robot_pose.md) [rightTransform](classfranky_1_1_robot_pose.md#afdbee35c5bf294ed93a139cc6280a076)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform)<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> 93</span> <span class="keywordflow">return</span> {end\_effector\_pose\_ \* transform, elbow\_state\_};

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span> }

</div>

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> 95</span>

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> [104](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RobotPose](classfranky_1_1_robot_pose.md) [changeEndEffectorFrame](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform)<span class="keyword"> const </span>{ <span class="keywordflow">return</span> [rightTransform](classfranky_1_1_robot_pose.md#afdbee35c5bf294ed93a139cc6280a076)(transform); }

</div>

<div class="line">

<span id="l00105"></span><span class="lineno"> 105</span>

</div>

<div id="foldopen00112" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00112"></span><span class="lineno"> [112](classfranky_1_1_robot_pose.md#a79b9d1d5960fe44eebda0d309c868e1a)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RobotPose](classfranky_1_1_robot_pose.md) [withElbowState](classfranky_1_1_robot_pose.md#a79b9d1d5960fe44eebda0d309c868e1a)(<span class="keyword">const</span> std::optional\<ElbowState\> [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00113"></span><span class="lineno"> 113</span> <span class="keywordflow">return</span> {end\_effector\_pose\_, [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)};

</div>

<div class="line">

<span id="l00114"></span><span class="lineno"> 114</span> }

</div>

</div>

<div class="line">

<span id="l00115"></span><span class="lineno"> 115</span>

</div>

<div class="line">

<span id="l00121"></span><span class="lineno"> [121](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> end\_effector\_pose\_; }

</div>

<div class="line">

<span id="l00122"></span><span class="lineno"> 122</span>

</div>

<div class="line">

<span id="l00128"></span><span class="lineno"> [128](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] std::optional\<ElbowState\> [elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> elbow\_state\_; }

</div>

<div class="line">

<span id="l00129"></span><span class="lineno"> 129</span>

</div>

<div class="line">

<span id="l00130"></span><span class="lineno"> 130</span> <span class="keyword">friend</span> std::ostream &[operator\<\<](classfranky_1_1_robot_pose.md#abd7aca5ba4c84f9ad7257f1de3b94cb0)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [RobotPose](classfranky_1_1_robot_pose.md) &[robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00131"></span><span class="lineno"> 131</span>

</div>

<div class="line">

<span id="l00132"></span><span class="lineno"> 132</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00133"></span><span class="lineno"> 133</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) end\_effector\_pose\_;

</div>

<div class="line">

<span id="l00134"></span><span class="lineno"> 134</span> std::optional\<ElbowState\> elbow\_state\_;

</div>

<div class="line">

<span id="l00135"></span><span class="lineno"> 135</span>};

</div>

</div>

<div class="line">

<span id="l00136"></span><span class="lineno"> 136</span>

</div>

<div id="foldopen00137" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00137"></span><span class="lineno"> [137](namespacefranky.md#a0636706f1ecb60b215ce13072d61f0c0)</span><span class="keyword">inline</span> [RobotPose](classfranky_1_1_robot_pose.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [RobotPose](classfranky_1_1_robot_pose.md) &[robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[right\_transform](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00138"></span><span class="lineno"> 138</span> <span class="keywordflow">return</span> [robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).rightTransform([right\_transform](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00139"></span><span class="lineno"> 139</span>}

</div>

</div>

<div class="line">

<span id="l00140"></span><span class="lineno"> 140</span>

</div>

<div id="foldopen00141" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00141"></span><span class="lineno"> [141](namespacefranky.md#afe836097f81e29d3b6c9ac722a078d0d)</span><span class="keyword">inline</span> [RobotPose](classfranky_1_1_robot_pose.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[left\_transform](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [RobotPose](classfranky_1_1_robot_pose.md) &[robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00142"></span><span class="lineno"> 142</span> <span class="keywordflow">return</span> [robot\_pose](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).leftTransform([left\_transform](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00143"></span><span class="lineno"> 143</span>}

</div>

</div>

<div class="line">

<span id="l00144"></span><span class="lineno"> 144</span>

</div>

<div class="line">

<span id="l00145"></span><span class="lineno"> 145</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_robot_pose_html" class="ttc">

<div class="ttname">

[franky::RobotPose](classfranky_1_1_robot_pose.md)

</div>

<div class="ttdoc">

Cartesian pose of a robot.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:19

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_a132eef8bd15ba00132fb64ed441382ba" class="ttc">

<div class="ttname">

[franky::RobotPose::changeEndEffectorFrame](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba)

</div>

<div class="ttdeci">

RobotPose changeEndEffectorFrame(const Affine \&transform) const

</div>

<div class="ttdoc">

Change the frame of the end effector by applying a transformation from the right side....

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:104

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_a2dbca2efd3922f5b8a0954e778dcd197" class="ttc">

<div class="ttname">

[franky::RobotPose::RobotPose](classfranky_1_1_robot_pose.md#a2dbca2efd3922f5b8a0954e778dcd197)

</div>

<div class="ttdeci">

RobotPose()

</div>

<div class="ttdef">

**Definition** robot\_pose.cpp:51

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_a33ec908498b031c97c384e220f5fa6db" class="ttc">

<div class="ttname">

[franky::RobotPose::RobotPose](classfranky_1_1_robot_pose.md#a33ec908498b031c97c384e220f5fa6db)

</div>

<div class="ttdeci">

RobotPose(const RobotPose \&robot\_pose)

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_a49bde12b0fbe8a2cc7e95c923b170c8d" class="ttc">

<div class="ttname">

[franky::RobotPose::vector\_repr](classfranky_1_1_robot_pose.md#a49bde12b0fbe8a2cc7e95c923b170c8d)

</div>

<div class="ttdeci">

Vector7d vector\_repr() const

</div>

<div class="ttdoc">

Get the vector representation of the pose, which consists of the end effector position and orientatio...

</div>

<div class="ttdef">

**Definition** robot\_pose.cpp:34

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_a79b9d1d5960fe44eebda0d309c868e1a" class="ttc">

<div class="ttname">

[franky::RobotPose::withElbowState](classfranky_1_1_robot_pose.md#a79b9d1d5960fe44eebda0d309c868e1a)

</div>

<div class="ttdeci">

RobotPose withElbowState(const std::optional\< ElbowState \> elbow\_state) const

</div>

<div class="ttdoc">

Get the pose with a new elbow state.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:112

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_a87b43342db37db66af0b1411af496dd2" class="ttc">

<div class="ttname">

[franky::RobotPose::as\_franka\_pose](classfranky_1_1_robot_pose.md#a87b43342db37db66af0b1411af496dd2)

</div>

<div class="ttdeci">

franka::CartesianPose as\_franka\_pose(FlipDirection default\_elbow\_flip\_direction=FlipDirection::kNegative) const

</div>

<div class="ttdoc">

Convert this pose to a franka pose.

</div>

<div class="ttdef">

**Definition** robot\_pose.cpp:43

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_abd7aca5ba4c84f9ad7257f1de3b94cb0" class="ttc">

<div class="ttname">

[franky::RobotPose::operator\<\<](classfranky_1_1_robot_pose.md#abd7aca5ba4c84f9ad7257f1de3b94cb0)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const RobotPose \&robot\_pose)

</div>

<div class="ttdef">

**Definition** robot\_pose.cpp:53

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_abe83d0dc121a5e1312ac4f2acdbd9fbd" class="ttc">

<div class="ttname">

[franky::RobotPose::end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd)

</div>

<div class="ttdeci">

Affine end\_effector\_pose() const

</div>

<div class="ttdoc">

Get the end effector pose.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:121

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_aca6a0cfec885c9aa09800603b2487a55" class="ttc">

<div class="ttname">

[franky::RobotPose::elbow\_state](classfranky_1_1_robot_pose.md#aca6a0cfec885c9aa09800603b2487a55)

</div>

<div class="ttdeci">

std::optional\< ElbowState \> elbow\_state() const

</div>

<div class="ttdoc">

Get the elbow state.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:128

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_adc234649707e63232c54d9e392db25c6" class="ttc">

<div class="ttname">

[franky::RobotPose::leftTransform](classfranky_1_1_robot_pose.md#adc234649707e63232c54d9e392db25c6)

</div>

<div class="ttdeci">

RobotPose leftTransform(const Affine \&transform) const

</div>

<div class="ttdoc">

Transform this pose with a given affine transformation from the left side.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:81

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_afdbee35c5bf294ed93a139cc6280a076" class="ttc">

<div class="ttname">

[franky::RobotPose::rightTransform](classfranky_1_1_robot_pose.md#afdbee35c5bf294ed93a139cc6280a076)

</div>

<div class="ttdeci">

RobotPose rightTransform(const Affine \&transform) const

</div>

<div class="ttdoc">

Transform this pose with a given affine transformation from the right side.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:92

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

<div id="atypes_8hpp_html" class="ttc">

<div class="ttname">

[types.hpp](types_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
