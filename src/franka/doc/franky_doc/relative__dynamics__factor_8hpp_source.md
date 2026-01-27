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

relative\_dynamics\_factor.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](relative__dynamics__factor_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<string\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span>

</div>

<div id="foldopen00013" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00013"></span><span class="lineno"> [13](classfranky_1_1_relative_dynamics_factor.md)</span><span class="keyword">class </span>[RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) {

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> 18</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a7e43b12bb5d338ac74ef57c4fd791a6e)();

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span>

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span> <span class="comment">// Suppress implicit conversion warning</span>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span><span class="preprocessor">\#pragma clang diagnostic push</span>

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span><span class="preprocessor">\#pragma clang diagnostic ignored "-Wimplicit-conversion"</span>

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a7e43b12bb5d338ac74ef57c4fd791a6e)(<span class="keywordtype">double</span> [value](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span><span class="preprocessor">\#pragma clang diagnostic pop</span>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a7e43b12bb5d338ac74ef57c4fd791a6e)(<span class="keywordtype">double</span> [velocity](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074), <span class="keywordtype">double</span> [acceleration](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30), <span class="keywordtype">double</span> [jerk](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be));

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span>

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> [44](classfranky_1_1_relative_dynamics_factor.md#aafb78c44330199e27db6b3f662307c14)</span> <span class="keyword">static</span> <span class="keyword">inline</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) [MAX\_DYNAMICS](classfranky_1_1_relative_dynamics_factor.md#aafb78c44330199e27db6b3f662307c14)() { <span class="keywordflow">return</span> {1.0, 1.0, 1.0, <span class="keyword">true</span>}; }

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> [49](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> <span class="keywordtype">double</span> [velocity](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> velocity\_; }

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span>

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> [54](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> <span class="keywordtype">double</span> [acceleration](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> acceleration\_; }

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span>

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> [59](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> <span class="keywordtype">double</span> [jerk](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> jerk\_; }

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> [64](classfranky_1_1_relative_dynamics_factor.md#a7dbf4dc92014c7533ee0090581308b90)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">inline</span> <span class="keywordtype">bool</span> [max\_dynamics](classfranky_1_1_relative_dynamics_factor.md#a7dbf4dc92014c7533ee0090581308b90)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> max\_dynamics\_; }

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span>

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) [operator\*](classfranky_1_1_relative_dynamics_factor.md#ab5a59d78758ae5fc747cce2df95022f1)(<span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) &[other](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span>

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> <span class="keyword">static</span> <span class="keywordtype">double</span> checkInBounds(<span class="keywordtype">double</span> [value](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> std::string &[name](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a7e43b12bb5d338ac74ef57c4fd791a6e)(<span class="keywordtype">double</span> [velocity](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074), <span class="keywordtype">double</span> [acceleration](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30), <span class="keywordtype">double</span> [jerk](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be), <span class="keywordtype">bool</span> [max\_dynamics](classfranky_1_1_relative_dynamics_factor.md#a7dbf4dc92014c7533ee0090581308b90));

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span>

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span> <span class="keywordtype">double</span> velocity\_, acceleration\_, jerk\_;

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span> <span class="keywordtype">bool</span> max\_dynamics\_;

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span>};

</div>

</div>

<div class="line">

<span id="l00076"></span><span class="lineno"> 76</span>

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md)

</div>

<div class="ttdoc">

Relative dynamics factors.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:13

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html_a1d7f32132b99026d50ad3f683552a4be" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor::jerk](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be)

</div>

<div class="ttdeci">

double jerk() const

</div>

<div class="ttdoc">

Jerk factor.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:59

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html_a34da6e78cb104a1628a7dfb25038cd30" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor::acceleration](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30)

</div>

<div class="ttdeci">

double acceleration() const

</div>

<div class="ttdoc">

Acceleration factor.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:54

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html_a7dbf4dc92014c7533ee0090581308b90" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor::max\_dynamics](classfranky_1_1_relative_dynamics_factor.md#a7dbf4dc92014c7533ee0090581308b90)

</div>

<div class="ttdeci">

bool max\_dynamics() const

</div>

<div class="ttdoc">

Whether the maximum dynamics should be used.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:64

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html_a7e43b12bb5d338ac74ef57c4fd791a6e" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor::RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a7e43b12bb5d338ac74ef57c4fd791a6e)

</div>

<div class="ttdeci">

RelativeDynamicsFactor()

</div>

<div class="ttdoc">

Default constructor which initializes all values to 1.0.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.cpp:8

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html_aafb78c44330199e27db6b3f662307c14" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor::MAX\_DYNAMICS](classfranky_1_1_relative_dynamics_factor.md#aafb78c44330199e27db6b3f662307c14)

</div>

<div class="ttdeci">

static RelativeDynamicsFactor MAX\_DYNAMICS()

</div>

<div class="ttdoc">

Special factor which causes the maximum dynamics to be used, independent of other factors applied els...

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:44

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html_ab5a59d78758ae5fc747cce2df95022f1" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor::operator\*](classfranky_1_1_relative_dynamics_factor.md#ab5a59d78758ae5fc747cce2df95022f1)

</div>

<div class="ttdeci">

RelativeDynamicsFactor operator\*(const RelativeDynamicsFactor \&other) const

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.cpp:28

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html_afd6505e3977f86efea0cae6bd3dca074" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor::velocity](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074)

</div>

<div class="ttdeci">

double velocity() const

</div>

<div class="ttdoc">

Velocity factor.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:49

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

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
