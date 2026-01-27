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

twist\_acceleration.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](twist__acceleration_8hpp.md)

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

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include "[franky/twist.hpp](twist_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/util.hpp](util_8hpp.md)"</span>

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

<div id="foldopen00014" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00014"></span><span class="lineno"> [14](classfranky_1_1_twist_acceleration.md)</span><span class="keyword">class </span>[TwistAcceleration](classfranky_1_1_twist_acceleration.md) {

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> [16](classfranky_1_1_twist_acceleration.md#a99508b6c2741d8f18acca43e538beecb)</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md#a99508b6c2741d8f18acca43e538beecb)(<span class="keyword">const</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) &[twist\_acceleration\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span>

</div>

<div id="foldopen00022" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00022"></span><span class="lineno"> [22](classfranky_1_1_twist_acceleration.md#a12807e75c0b6f39208d1822dbdf2eb28)</span> <span class="keyword">explicit</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md#a12807e75c0b6f39208d1822dbdf2eb28)(

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span> Eigen::Vector3d [linear\_acceleration](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e) = Eigen::Vector3d::Zero(),

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> Eigen::Vector3d [angular\_acceleration](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029) = Eigen::Vector3d::Zero())

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> : linear\_acceleration\_(std::move([linear\_acceleration](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e))), angular\_acceleration\_(std::move([angular\_acceleration](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029))) {}

</div>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span>

</div>

<div id="foldopen00030" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00030"></span><span class="lineno"> [30](classfranky_1_1_twist_acceleration.md#a56735cb015ce872ba1857d7af6081d3a)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">static</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) [fromVectorRepr](classfranky_1_1_twist_acceleration.md#a56735cb015ce872ba1857d7af6081d3a)(<span class="keyword">const</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec)) {

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span> <span class="keywordflow">return</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md){[vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec).head\<3\>(), [vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec).tail\<3\>()};

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span> }

</div>

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span>

</div>

<div id="foldopen00040" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00040"></span><span class="lineno"> [40](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec)()<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< linear\_acceleration\_, angular\_acceleration\_;

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> <span class="keywordflow">return</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> }

</div>

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span>

</div>

<div id="foldopen00053" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00053"></span><span class="lineno"> [53](classfranky_1_1_twist_acceleration.md#a0887f6ede60cbe7ce36dc0541af45a8b)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [TwistAcceleration](classfranky_1_1_twist_acceleration.md) [transformWith](classfranky_1_1_twist_acceleration.md#a0887f6ede60cbe7ce36dc0541af45a8b)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[transformation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span> <span class="keywordflow">return</span> [transformWith](classfranky_1_1_twist_acceleration.md#a0887f6ede60cbe7ce36dc0541af45a8b)([transformation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).rotation());

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span> }

</div>

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> <span class="keyword">template</span> \<<span class="keyword">typename</span> RotationMatrixType\>

</div>

<div id="foldopen00065" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00065"></span><span class="lineno"> [65](classfranky_1_1_twist_acceleration.md#ad32f3d63877f1f0a679677fd4301fc0b)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [TwistAcceleration](classfranky_1_1_twist_acceleration.md) [transformWith](classfranky_1_1_twist_acceleration.md#ad32f3d63877f1f0a679677fd4301fc0b)(<span class="keyword">const</span> [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> <span class="keywordflow">return</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md){[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \* linear\_acceleration\_, [rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \* angular\_acceleration\_};

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span> }

</div>

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span>

</div>

<div id="foldopen00082" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00082"></span><span class="lineno"> [82](classfranky_1_1_twist_acceleration.md#a0cb4b6497e1332cb717b6f3d132de65f)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [TwistAcceleration](classfranky_1_1_twist_acceleration.md) [propagateThroughLink](classfranky_1_1_twist_acceleration.md#a0cb4b6497e1332cb717b6f3d132de65f)(

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span> <span class="keyword">const</span> Eigen::Vector3d &[link\_translation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> Eigen::Vector3d &[base\_angular\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span> Eigen::Vector3d [propagated\_linear\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) =

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span> linear\_acceleration\_ + angular\_acceleration\_.cross([link\_translation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) +

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span> [base\_angular\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).cross([base\_angular\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).cross([link\_translation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)));

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span>

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span> <span class="keywordflow">return</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md){[propagated\_linear\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), angular\_acceleration\_};

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span> }

</div>

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span>

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> [96](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] Eigen::Vector3d [linear\_acceleration](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> linear\_acceleration\_; }

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> 97</span>

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> [103](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] Eigen::Vector3d [angular\_acceleration](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> angular\_acceleration\_; }

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> 104</span>

</div>

<div class="line">

<span id="l00105"></span><span class="lineno"> 105</span> <span class="keyword">friend</span> std::ostream &[operator\<\<](classfranky_1_1_twist_acceleration.md#a85106207596cbe76f085e987a937b129)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) &[twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> 106</span>

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00108"></span><span class="lineno"> 108</span> Eigen::Vector3d linear\_acceleration\_;

</div>

<div class="line">

<span id="l00109"></span><span class="lineno"> 109</span> Eigen::Vector3d angular\_acceleration\_;

</div>

<div class="line">

<span id="l00110"></span><span class="lineno"> 110</span>};

</div>

</div>

<div class="line">

<span id="l00111"></span><span class="lineno"> 111</span>

</div>

<div id="foldopen00112" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00112"></span><span class="lineno"> [112](namespacefranky.md#a2b1e35d7df27b7601383320cc6741364)</span><span class="keyword">inline</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) &[twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00113"></span><span class="lineno"> 113</span> <span class="keywordflow">return</span> [twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).[transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)([affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00114"></span><span class="lineno"> 114</span>}

</div>

</div>

<div class="line">

<span id="l00115"></span><span class="lineno"> 115</span>

</div>

<div class="line">

<span id="l00116"></span><span class="lineno"> 116</span><span class="keyword">template</span> \<<span class="keyword">typename</span> RotationMatrixType\>

</div>

<div id="foldopen00117" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00117"></span><span class="lineno"> [117](namespacefranky.md#afd137103448128c37c560427e7d995da)</span>[TwistAcceleration](classfranky_1_1_twist_acceleration.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) &[twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00118"></span><span class="lineno"> 118</span> <span class="keywordflow">return</span> [twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).[transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)([rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00119"></span><span class="lineno"> 119</span>}

</div>

</div>

<div class="line">

<span id="l00120"></span><span class="lineno"> 120</span>

</div>

<div id="foldopen00121" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00121"></span><span class="lineno"> [121](classfranky_1_1_twist_acceleration.md#a85106207596cbe76f085e987a937b129)</span><span class="keyword">inline</span> std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) &[twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00122"></span><span class="lineno"> 122</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< <span class="stringliteral">"TwistAcceleration(lin="</span> \<\< [twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).linear\_acceleration\_

</div>

<div class="line">

<span id="l00123"></span><span class="lineno"> 123</span> \<\< <span class="stringliteral">", ang="</span> \<\< [twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).angular\_acceleration\_ \<\< <span class="stringliteral">")"</span>;

</div>

<div class="line">

<span id="l00124"></span><span class="lineno"> 124</span> <span class="keywordflow">return</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00125"></span><span class="lineno"> 125</span>}

</div>

</div>

<div class="line">

<span id="l00126"></span><span class="lineno"> 126</span>

</div>

<div class="line">

<span id="l00127"></span><span class="lineno"> 127</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_twist_acceleration_html" class="ttc">

<div class="ttname">

[franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md)

</div>

<div class="ttdoc">

TwistAcceleration acceleration of a frame (2nd derivative of a pose).

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:14

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a0887f6ede60cbe7ce36dc0541af45a8b" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::transformWith](classfranky_1_1_twist_acceleration.md#a0887f6ede60cbe7ce36dc0541af45a8b)

</div>

<div class="ttdeci">

TwistAcceleration transformWith(const Affine \&transformation) const

</div>

<div class="ttdoc">

Transform the frame of the twist acceleration by applying the given affine transform.

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:53

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a0cb4b6497e1332cb717b6f3d132de65f" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::propagateThroughLink](classfranky_1_1_twist_acceleration.md#a0cb4b6497e1332cb717b6f3d132de65f)

</div>

<div class="ttdeci">

TwistAcceleration propagateThroughLink(const Eigen::Vector3d \&link\_translation, const Eigen::Vector3d \&base\_angular\_velocity) const

</div>

<div class="ttdoc">

Propagate the twist acceleration through a link with the given translation. Hence,...

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:82

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a12807e75c0b6f39208d1822dbdf2eb28" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::TwistAcceleration](classfranky_1_1_twist_acceleration.md#a12807e75c0b6f39208d1822dbdf2eb28)

</div>

<div class="ttdeci">

TwistAcceleration(Eigen::Vector3d linear\_acceleration=Eigen::Vector3d::Zero(), Eigen::Vector3d angular\_acceleration=Eigen::Vector3d::Zero())

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:22

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a56735cb015ce872ba1857d7af6081d3a" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::fromVectorRepr](classfranky_1_1_twist_acceleration.md#a56735cb015ce872ba1857d7af6081d3a)

</div>

<div class="ttdeci">

static TwistAcceleration fromVectorRepr(const Vector6d \&vector\_repr)

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:30

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a6d6cabb998123f95bc7af53e428f7029" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::angular\_acceleration](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029)

</div>

<div class="ttdeci">

Eigen::Vector3d angular\_acceleration() const

</div>

<div class="ttdoc">

Get the angular acceleration.

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:103

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a85106207596cbe76f085e987a937b129" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::operator\<\<](classfranky_1_1_twist_acceleration.md#a85106207596cbe76f085e987a937b129)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const TwistAcceleration \&twist\_acceleration)

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:121

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a99508b6c2741d8f18acca43e538beecb" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::TwistAcceleration](classfranky_1_1_twist_acceleration.md#a99508b6c2741d8f18acca43e538beecb)

</div>

<div class="ttdeci">

TwistAcceleration(const TwistAcceleration \&twist\_acceleration\_acceleration)=default

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_a9d91f3165e9017533f063603aad7dc4e" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::linear\_acceleration](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e)

</div>

<div class="ttdeci">

Eigen::Vector3d linear\_acceleration() const

</div>

<div class="ttdoc">

Get the linear acceleration.

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:96

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_aae1e4fd8a259657bbad3082ca943d5ec" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec)

</div>

<div class="ttdeci">

Vector6d vector\_repr() const

</div>

<div class="ttdoc">

Get the vector representation of the twist acceleration. It consists of the linear and angular veloci...

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:40

</div>

</div>

<div id="aclassfranky_1_1_twist_acceleration_html_ad32f3d63877f1f0a679677fd4301fc0b" class="ttc">

<div class="ttname">

[franky::TwistAcceleration::transformWith](classfranky_1_1_twist_acceleration.md#ad32f3d63877f1f0a679677fd4301fc0b)

</div>

<div class="ttdeci">

TwistAcceleration transformWith(const RotationMatrixType \&rotation) const

</div>

<div class="ttdoc">

Transform the frame of the twist acceleration by applying the given rotation.

</div>

<div class="ttdef">

**Definition** twist\_acceleration.hpp:65

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

<div id="autil_8hpp_html" class="ttc">

<div class="ttname">

[util.hpp](util_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
