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

twist.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](twist_8hpp.md)

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

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/util.hpp](util_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span>

</div>

<div id="foldopen00013" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00013"></span><span class="lineno"> [13](classfranky_1_1_twist.md)</span><span class="keyword">class </span>[Twist](classfranky_1_1_twist.md) {

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> [15](classfranky_1_1_twist.md#acc5436a6628d7685aacf10d56e915126)</span> [Twist](classfranky_1_1_twist.md#acc5436a6628d7685aacf10d56e915126)(<span class="keyword">const</span> [Twist](classfranky_1_1_twist.md) &[twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span>

</div>

<div id="foldopen00021" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00021"></span><span class="lineno"> [21](classfranky_1_1_twist.md#a9c27d104e1b1ede05906e1a4b8260aa2)</span> <span class="keyword">explicit</span> [Twist](classfranky_1_1_twist.md#a9c27d104e1b1ede05906e1a4b8260aa2)(

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span> Eigen::Vector3d [linear\_velocity](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d) = Eigen::Vector3d::Zero(),

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span> Eigen::Vector3d [angular\_velocity](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4) = Eigen::Vector3d::Zero())

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> : linear\_velocity\_(std::move([linear\_velocity](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d))), angular\_velocity\_(std::move([angular\_velocity](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4))) {}

</div>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span>

</div>

<div id="foldopen00029" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00029"></span><span class="lineno"> [29](classfranky_1_1_twist.md#a39a4f6fc1cca31a7431618657d551f17)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">static</span> [Twist](classfranky_1_1_twist.md) [fromVectorRepr](classfranky_1_1_twist.md#a39a4f6fc1cca31a7431618657d551f17)(<span class="keyword">const</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e)) {

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span> <span class="keywordflow">return</span> [Twist](classfranky_1_1_twist.md){[vector\_repr](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e).head\<3\>(), [vector\_repr](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e).tail\<3\>()};

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span> }

</div>

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span>

</div>

<div id="foldopen00039" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00039"></span><span class="lineno"> [39](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [vector\_repr](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e)()<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< linear\_velocity\_, angular\_velocity\_;

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> <span class="keywordflow">return</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> }

</div>

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span>

</div>

<div id="foldopen00052" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00052"></span><span class="lineno"> [52](classfranky_1_1_twist.md#a3f75fc666b90701fb5b518ca44e7542a)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Twist](classfranky_1_1_twist.md) [transformWith](classfranky_1_1_twist.md#a3f75fc666b90701fb5b518ca44e7542a)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[transformation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> <span class="keywordflow">return</span> [transformWith](classfranky_1_1_twist.md#a3f75fc666b90701fb5b518ca44e7542a)([transformation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).rotation());

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span> }

</div>

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span>

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span> <span class="keyword">template</span> \<<span class="keyword">typename</span> RotationMatrixType\>

</div>

<div id="foldopen00063" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00063"></span><span class="lineno"> [63](classfranky_1_1_twist.md#a8877c2da86231733a7ee309bd6378434)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Twist](classfranky_1_1_twist.md) [transformWith](classfranky_1_1_twist.md#a8877c2da86231733a7ee309bd6378434)(<span class="keyword">const</span> [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> <span class="keywordflow">return</span> [Twist](classfranky_1_1_twist.md){[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \* linear\_velocity\_, [rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \* angular\_velocity\_};

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> }

</div>

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span>

</div>

<div id="foldopen00077" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00077"></span><span class="lineno"> [77](classfranky_1_1_twist.md#a896c0f6949127e1c37f5716b3f771bdb)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Twist](classfranky_1_1_twist.md) [propagateThroughLink](classfranky_1_1_twist.md#a896c0f6949127e1c37f5716b3f771bdb)(<span class="keyword">const</span> Eigen::Vector3d &[link\_translation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> <span class="keywordflow">return</span> [Twist](classfranky_1_1_twist.md){linear\_velocity\_ + angular\_velocity\_.cross([link\_translation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)), angular\_velocity\_};

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> }

</div>

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> [86](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] Eigen::Vector3d [linear\_velocity](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> linear\_velocity\_; }

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span>

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> [93](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] Eigen::Vector3d [angular\_velocity](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> angular\_velocity\_; }

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span>

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> 95</span> <span class="keyword">friend</span> std::ostream &[operator\<\<](classfranky_1_1_twist.md#ac0ce8d662af951bc5d7b3ab17a355790)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Twist](classfranky_1_1_twist.md) &[twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> 96</span>

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> 97</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00098"></span><span class="lineno"> 98</span> Eigen::Vector3d linear\_velocity\_;

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span> Eigen::Vector3d angular\_velocity\_;

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span>};

</div>

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> 101</span>

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> [102](namespacefranky.md#a0256b40c0ee5ec119bc38dc87ba95176)</span><span class="keyword">inline</span> [Twist](classfranky_1_1_twist.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Twist](classfranky_1_1_twist.md) &[twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) { <span class="keywordflow">return</span> [twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).[transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)([affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)); }

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> 103</span>

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> 104</span><span class="keyword">template</span> \<<span class="keyword">typename</span> RotationMatrixType\>

</div>

<div id="foldopen00105" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00105"></span><span class="lineno"> [105](namespacefranky.md#a2f4a8e79208c3df8d0226a09aac5cf34)</span>[Twist](classfranky_1_1_twist.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Twist](classfranky_1_1_twist.md) &[twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> 106</span> <span class="keywordflow">return</span> [twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).[transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)([rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span>}

</div>

</div>

<div class="line">

<span id="l00108"></span><span class="lineno"> 108</span>

</div>

<div id="foldopen00109" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00109"></span><span class="lineno"> [109](classfranky_1_1_twist.md#ac0ce8d662af951bc5d7b3ab17a355790)</span><span class="keyword">inline</span> std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Twist](classfranky_1_1_twist.md) &[twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00110"></span><span class="lineno"> 110</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< <span class="stringliteral">"Twist(lin="</span> \<\< [twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).linear\_velocity\_ \<\< <span class="stringliteral">", ang="</span> \<\< [twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).angular\_velocity\_ \<\< <span class="stringliteral">")"</span>;

</div>

<div class="line">

<span id="l00111"></span><span class="lineno"> 111</span> <span class="keywordflow">return</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00112"></span><span class="lineno"> 112</span>}

</div>

</div>

<div class="line">

<span id="l00113"></span><span class="lineno"> 113</span>

</div>

<div class="line">

<span id="l00114"></span><span class="lineno"> 114</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_a9f7b644b3920e5816554b8855854a1aa" class="ttc">

<div class="ttname">

[franky::CartesianState::transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)

</div>

<div class="ttdeci">

CartesianState transformWith(const Affine \&transform) const

</div>

<div class="ttdoc">

Transform the frame of the state by applying the given affine transform.

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:42

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

<div id="aclassfranky_1_1_twist_html_a31a3a4886d8ef4ee37b4d12acec1162e" class="ttc">

<div class="ttname">

[franky::Twist::vector\_repr](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e)

</div>

<div class="ttdeci">

Vector6d vector\_repr() const

</div>

<div class="ttdoc">

Get the vector representation of the twist. It consists of the linear and angular velocities.

</div>

<div class="ttdef">

**Definition** twist.hpp:39

</div>

</div>

<div id="aclassfranky_1_1_twist_html_a39a4f6fc1cca31a7431618657d551f17" class="ttc">

<div class="ttname">

[franky::Twist::fromVectorRepr](classfranky_1_1_twist.md#a39a4f6fc1cca31a7431618657d551f17)

</div>

<div class="ttdeci">

static Twist fromVectorRepr(const Vector6d \&vector\_repr)

</div>

<div class="ttdef">

**Definition** twist.hpp:29

</div>

</div>

<div id="aclassfranky_1_1_twist_html_a3f75fc666b90701fb5b518ca44e7542a" class="ttc">

<div class="ttname">

[franky::Twist::transformWith](classfranky_1_1_twist.md#a3f75fc666b90701fb5b518ca44e7542a)

</div>

<div class="ttdeci">

Twist transformWith(const Affine \&transformation) const

</div>

<div class="ttdoc">

Transform the frame of the twist by applying the given affine transform.

</div>

<div class="ttdef">

**Definition** twist.hpp:52

</div>

</div>

<div id="aclassfranky_1_1_twist_html_a5c704065f92d12266fb0e16e2b2dd61d" class="ttc">

<div class="ttname">

[franky::Twist::linear\_velocity](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d)

</div>

<div class="ttdeci">

Eigen::Vector3d linear\_velocity() const

</div>

<div class="ttdoc">

Get the linear velocity.

</div>

<div class="ttdef">

**Definition** twist.hpp:86

</div>

</div>

<div id="aclassfranky_1_1_twist_html_a8877c2da86231733a7ee309bd6378434" class="ttc">

<div class="ttname">

[franky::Twist::transformWith](classfranky_1_1_twist.md#a8877c2da86231733a7ee309bd6378434)

</div>

<div class="ttdeci">

Twist transformWith(const RotationMatrixType \&rotation) const

</div>

<div class="ttdoc">

Transform the frame of the twist by applying the given rotation.

</div>

<div class="ttdef">

**Definition** twist.hpp:63

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

<div id="aclassfranky_1_1_twist_html_a9c27d104e1b1ede05906e1a4b8260aa2" class="ttc">

<div class="ttname">

[franky::Twist::Twist](classfranky_1_1_twist.md#a9c27d104e1b1ede05906e1a4b8260aa2)

</div>

<div class="ttdeci">

Twist(Eigen::Vector3d linear\_velocity=Eigen::Vector3d::Zero(), Eigen::Vector3d angular\_velocity=Eigen::Vector3d::Zero())

</div>

<div class="ttdef">

**Definition** twist.hpp:21

</div>

</div>

<div id="aclassfranky_1_1_twist_html_ac0ce8d662af951bc5d7b3ab17a355790" class="ttc">

<div class="ttname">

[franky::Twist::operator\<\<](classfranky_1_1_twist.md#ac0ce8d662af951bc5d7b3ab17a355790)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const Twist \&twist)

</div>

<div class="ttdef">

**Definition** twist.hpp:109

</div>

</div>

<div id="aclassfranky_1_1_twist_html_acc5436a6628d7685aacf10d56e915126" class="ttc">

<div class="ttname">

[franky::Twist::Twist](classfranky_1_1_twist.md#acc5436a6628d7685aacf10d56e915126)

</div>

<div class="ttdeci">

Twist(const Twist \&twist)=default

</div>

</div>

<div id="aclassfranky_1_1_twist_html_af1199e9d3b8e06d11c519f99f5e2a4e4" class="ttc">

<div class="ttname">

[franky::Twist::angular\_velocity](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4)

</div>

<div class="ttdeci">

Eigen::Vector3d angular\_velocity() const

</div>

<div class="ttdoc">

Get the angular velocity.

</div>

<div class="ttdef">

**Definition** twist.hpp:93

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

<div id="anamespacefranky_html_a054ba89edc6e3948f2dfb5721aaa8bb4" class="ttc">

<div class="ttname">

[franky::operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)

</div>

<div class="ttdeci">

std::ostream & operator\<\<(std::ostream \&os, const DynamicsLimit\< Vector7d \> \&limit)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:47

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

<div id="autil_8hpp_html" class="ttc">

<div class="ttname">

[util.hpp](util_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
