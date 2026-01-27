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

elbow\_state.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](elbow__state_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<array\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<iostream\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<optional\></span>

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

<div class="line">

<span id="l00012"></span><span class="lineno"> [12](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b)</span><span class="keyword">enum class</span> [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) { [kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3) = -1, [kNeutral](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba5c9755c01963e8444ea5ee1802139851) = 0, [kPositive](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43bafe449700ac27fbd09863263d74e7735f) = 1 };

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span>std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream \&os, <span class="keyword">const</span> [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) \&flip\_direction);

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span>

</div>

<div id="foldopen00024" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00024"></span><span class="lineno"> [24](classfranky_1_1_elbow_state.md)</span><span class="keyword">class </span>[ElbowState](classfranky_1_1_elbow_state.md) {

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00033" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00033"></span><span class="lineno"> [33](classfranky_1_1_elbow_state.md#abc13ca8cf645d4bdd8b936ae8beab299)</span> <span class="keyword">explicit</span> [ElbowState](classfranky_1_1_elbow_state.md#abc13ca8cf645d4bdd8b936ae8beab299)(<span class="keywordtype">double</span> [joint\_3\_pos](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114), std::optional\<FlipDirection\> [joint\_4\_flip](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83) = std::nullopt)

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> : joint\_3\_pos\_([joint\_3\_pos](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114)), joint\_4\_flip\_([joint\_4\_flip](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83)) {}

</div>

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span>

</div>

<div id="foldopen00042" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00042"></span><span class="lineno"> [42](classfranky_1_1_elbow_state.md#a01b565b6678b46b95ef784d5a47b83b3)</span> <span class="keyword">explicit</span> [ElbowState](classfranky_1_1_elbow_state.md#a01b565b6678b46b95ef784d5a47b83b3)(<span class="keyword">const</span> std::array\<double, 2\> \&elbow\_state)

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> : joint\_3\_pos\_(elbow\_state\[0\]), joint\_4\_flip\_(\[&\]() -\> std::optional\<[FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b)\> {

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> <span class="keywordflow">if</span> (elbow\_state\[1\] \< 0.0) {

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> <span class="keywordflow">return</span> [FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3);

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span> } <span class="keywordflow">else</span> <span class="keywordflow">if</span> (elbow\_state\[1\] == 0.0) {

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keywordflow">return</span> [FlipDirection::kNeutral](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba5c9755c01963e8444ea5ee1802139851);

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> <span class="keywordflow">return</span> [FlipDirection::kPositive](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43bafe449700ac27fbd09863263d74e7735f);

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span> }

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span> }()) {}

</div>

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span>

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> [53](classfranky_1_1_elbow_state.md#adba9c9a3810c45135ce0401ddd4c291a)</span> [ElbowState](classfranky_1_1_elbow_state.md#adba9c9a3810c45135ce0401ddd4c291a)(<span class="keyword">const</span> [ElbowState](classfranky_1_1_elbow_state.md) &) = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> [54](classfranky_1_1_elbow_state.md#acd2cbc41647013ac53c521f07e9aa8ba)</span> [ElbowState](classfranky_1_1_elbow_state.md#acd2cbc41647013ac53c521f07e9aa8ba)() = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span>

</div>

<div id="foldopen00063" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00063"></span><span class="lineno"> [63](classfranky_1_1_elbow_state.md#a314ba82485911da7ddae7b6cd4c2f548)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> std::array\<double, 2\> [to\_array](classfranky_1_1_elbow_state.md#a314ba82485911da7ddae7b6cd4c2f548)(

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> [FlipDirection](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43b) default\_flip\_direction = [FlipDirection::kNegative](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba25b105cbe0fd4622cdb36360c85e89c3))<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> <span class="keywordflow">return</span> {joint\_3\_pos\_, <span class="keyword">static\_cast\<</span><span class="keywordtype">double</span><span class="keyword">\></span>(joint\_4\_flip\_.value\_or(default\_flip\_direction))};

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> }

</div>

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> [71](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> <span class="keywordtype">double</span> [joint\_3\_pos](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> joint\_3\_pos\_; }

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span>

</div>

<div class="line">

<span id="l00076"></span><span class="lineno"> [76](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> std::optional\<FlipDirection\> [joint\_4\_flip](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> joint\_4\_flip\_; }

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span>

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> <span class="keyword">friend</span> std::ostream &[operator\<\<](classfranky_1_1_elbow_state.md#a09b74291d96ecf82b9d9a0fff0761d09)(std::ostream \&os, <span class="keyword">const</span> [ElbowState](classfranky_1_1_elbow_state.md) \&elbow\_state);

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span>

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span> <span class="keywordtype">double</span> joint\_3\_pos\_{0.0};

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> std::optional\<FlipDirection\> joint\_4\_flip\_{std::nullopt};

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span>};

</div>

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span>

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_elbow_state_html" class="ttc">

<div class="ttname">

[franky::ElbowState](classfranky_1_1_elbow_state.md)

</div>

<div class="ttdoc">

Elbow state of the robot.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:24

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_a01b565b6678b46b95ef784d5a47b83b3" class="ttc">

<div class="ttname">

[franky::ElbowState::ElbowState](classfranky_1_1_elbow_state.md#a01b565b6678b46b95ef784d5a47b83b3)

</div>

<div class="ttdeci">

ElbowState(const std::array\< double, 2 \> \&elbow\_state)

</div>

<div class="ttdoc">

Construct an elbow state from an array containing joint position and flip direction.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:42

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_a09b74291d96ecf82b9d9a0fff0761d09" class="ttc">

<div class="ttname">

[franky::ElbowState::operator\<\<](classfranky_1_1_elbow_state.md#a09b74291d96ecf82b9d9a0fff0761d09)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const ElbowState \&elbow\_state)

</div>

<div class="ttdef">

**Definition** elbow\_state.cpp:7

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_a314ba82485911da7ddae7b6cd4c2f548" class="ttc">

<div class="ttname">

[franky::ElbowState::to\_array](classfranky_1_1_elbow_state.md#a314ba82485911da7ddae7b6cd4c2f548)

</div>

<div class="ttdeci">

std::array\< double, 2 \> to\_array(FlipDirection default\_flip\_direction=FlipDirection::kNegative) const

</div>

<div class="ttdoc">

Get the joint position and flip direction as an array.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:63

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_a8b6265a31a63ec23b100b78f874ca114" class="ttc">

<div class="ttname">

[franky::ElbowState::joint\_3\_pos](classfranky_1_1_elbow_state.md#a8b6265a31a63ec23b100b78f874ca114)

</div>

<div class="ttdeci">

double joint\_3\_pos() const

</div>

<div class="ttdoc">

The position of the 3rd joint.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:71

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_aa9a9b7ec1565e0b1fc5c5d5932148d83" class="ttc">

<div class="ttname">

[franky::ElbowState::joint\_4\_flip](classfranky_1_1_elbow_state.md#aa9a9b7ec1565e0b1fc5c5d5932148d83)

</div>

<div class="ttdeci">

std::optional\< FlipDirection \> joint\_4\_flip() const

</div>

<div class="ttdoc">

The flip direction of the 4th joint.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:76

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_abc13ca8cf645d4bdd8b936ae8beab299" class="ttc">

<div class="ttname">

[franky::ElbowState::ElbowState](classfranky_1_1_elbow_state.md#abc13ca8cf645d4bdd8b936ae8beab299)

</div>

<div class="ttdeci">

ElbowState(double joint\_3\_pos, std::optional\< FlipDirection \> joint\_4\_flip=std::nullopt)

</div>

<div class="ttdoc">

Construct an elbow state with the given joint position and optional flip direction.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:33

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_acd2cbc41647013ac53c521f07e9aa8ba" class="ttc">

<div class="ttname">

[franky::ElbowState::ElbowState](classfranky_1_1_elbow_state.md#acd2cbc41647013ac53c521f07e9aa8ba)

</div>

<div class="ttdeci">

ElbowState()=default

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html_adba9c9a3810c45135ce0401ddd4c291a" class="ttc">

<div class="ttname">

[franky::ElbowState::ElbowState](classfranky_1_1_elbow_state.md#adba9c9a3810c45135ce0401ddd4c291a)

</div>

<div class="ttdeci">

ElbowState(const ElbowState &)=default

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

<div id="anamespacefranky_html_aaebafd6d1e78da2a42cf35eb266cb43ba5c9755c01963e8444ea5ee1802139851" class="ttc">

<div class="ttname">

[franky::FlipDirection::kNeutral](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43ba5c9755c01963e8444ea5ee1802139851)

</div>

<div class="ttdeci">

@ kNeutral

</div>

</div>

<div id="anamespacefranky_html_aaebafd6d1e78da2a42cf35eb266cb43bafe449700ac27fbd09863263d74e7735f" class="ttc">

<div class="ttname">

[franky::FlipDirection::kPositive](namespacefranky.md#aaebafd6d1e78da2a42cf35eb266cb43bafe449700ac27fbd09863263d74e7735f)

</div>

<div class="ttdeci">

@ kPositive

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
