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

measure.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](measure_8hpp.md)

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

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<functional\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<iostream\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[franky/motion/condition.hpp](condition_8hpp.md)"</span>

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

<div id="foldopen00020" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00020"></span><span class="lineno"> [20](classfranky_1_1_measure.md)</span><span class="keyword">class </span>[Measure](classfranky_1_1_measure.md) {

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span> <span class="keyword">using </span>MeasureFunc = std::function\<double(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\>;

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span>

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span> <span class="keyword">explicit</span> [Measure](classfranky_1_1_measure.md)(MeasureFunc measure\_func, std::string [repr](classfranky_1_1_measure.md#a664d5e3506c4665f2be173ec5d2afa6f) = <span class="stringliteral">"NULL"</span>);

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span>

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> [Measure](classfranky_1_1_measure.md)(<span class="keywordtype">double</span> constant);

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span>

</div>

<div id="foldopen00046" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00046"></span><span class="lineno"> [46](classfranky_1_1_measure.md#a014ae0622c47aee2a4dd9b9a781d4760)</span> <span class="keyword">inline</span> <span class="keywordtype">double</span> [operator()](classfranky_1_1_measure.md#a014ae0622c47aee2a4dd9b9a781d4760)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keywordflow">return</span> measure\_func\_(robot\_state, rel\_time, abs\_time);

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span> }

</div>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span>

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> [53](classfranky_1_1_measure.md#a664d5e3506c4665f2be173ec5d2afa6f)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> std::string [repr](classfranky_1_1_measure.md#a664d5e3506c4665f2be173ec5d2afa6f)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> repr\_; }

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span>

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> <span class="keyword">static</span> [Measure](classfranky_1_1_measure.md) [ForceX](classfranky_1_1_measure.md#a7aa92d415e33ca64b07aa598cb5e9ec4)();

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> <span class="keyword">static</span> [Measure](classfranky_1_1_measure.md) [ForceY](classfranky_1_1_measure.md#a47fbb5bf68412799ab22234596832793)();

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> <span class="keyword">static</span> [Measure](classfranky_1_1_measure.md) [ForceZ](classfranky_1_1_measure.md#a9f8c4110a4ee5a1b102efaa6a424b0f3)();

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span>

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span> <span class="keyword">static</span> [Measure](classfranky_1_1_measure.md) [RelTime](classfranky_1_1_measure.md#adc0787238886a53313c11870e58c4d10)();

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span>

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span> <span class="keyword">static</span> [Measure](classfranky_1_1_measure.md) [AbsTime](classfranky_1_1_measure.md#a98d3cc1b9f211b042de9fd2238938fbc)();

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span>

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span> MeasureFunc measure\_func\_;

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span> std::string repr\_;

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span>};

</div>

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span>

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> [92](namespacefranky.md#aec1faf1176412ec30ace8d9360cd2219)</span>[Condition](classfranky_1_1_condition.md) [operator==](namespacefranky.md#a1b2d1dd9648934fd5f5e224993e74d7c)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> [93](namespacefranky.md#ad0fd48f95175ccff51a008422b0c79d3)</span>[Condition](classfranky_1_1_condition.md) [operator\!=](namespacefranky.md#a94e04eafe4db05368577002db3271805)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> [94](namespacefranky.md#a5bf2ceb580fd8b51d8423d17fb9e07c8)</span>[Condition](classfranky_1_1_condition.md) [operator\<=](namespacefranky.md#a5bf2ceb580fd8b51d8423d17fb9e07c8)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> [95](namespacefranky.md#ac292d7f5a4917cd61c4fe03d39122cbb)</span>[Condition](classfranky_1_1_condition.md) [operator\>=](namespacefranky.md#ac292d7f5a4917cd61c4fe03d39122cbb)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> [96](namespacefranky.md#a64f30e1c601485d8fc082abd272481ba)</span>[Condition](classfranky_1_1_condition.md) [operator\<](namespacefranky.md#a64f30e1c601485d8fc082abd272481ba)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> [97](namespacefranky.md#ab8f28e1eb83ddefdf341ea8644dc0392)</span>[Condition](classfranky_1_1_condition.md) [operator\>](namespacefranky.md#ab8f28e1eb83ddefdf341ea8644dc0392)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00098"></span><span class="lineno"> 98</span>

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> [99](namespacefranky.md#a3154ceacb8374282106cf479a8efb47b)</span>[Measure](classfranky_1_1_measure.md) [operator+](namespacefranky.md#a3154ceacb8374282106cf479a8efb47b)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> [100](namespacefranky.md#ade53467cfbd74e6684940c1e2e98bfe9)</span>[Measure](classfranky_1_1_measure.md) [operator-](namespacefranky.md#ae1c89933ac509cfab2c71192d55b4176)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> [101](namespacefranky.md#ada1326a1aed3004af977c08461d30169)</span>[Measure](classfranky_1_1_measure.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> [102](namespacefranky.md#affb71a7e2efda9caca54bdf81cc56d68)</span>[Measure](classfranky_1_1_measure.md) [operator/](namespacefranky.md#affb71a7e2efda9caca54bdf81cc56d68)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m1, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m2);

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> 103</span>

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> 104</span>[Measure](classfranky_1_1_measure.md) [operator-](namespacefranky.md#ae1c89933ac509cfab2c71192d55b4176)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&m);

</div>

<div class="line">

<span id="l00105"></span><span class="lineno"> 105</span>

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> 106</span>[Measure](classfranky_1_1_measure.md) [measure\_pow](namespacefranky.md#a0a18805109d5f09280f8830ce2970d3e)(<span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&base, <span class="keyword">const</span> [Measure](classfranky_1_1_measure.md) \&exponent);

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span>

</div>

<div class="line">

<span id="l00108"></span><span class="lineno"> 108</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_measure_html" class="ttc">

<div class="ttname">

[franky::Measure](classfranky_1_1_measure.md)

</div>

<div class="ttdoc">

A measure on the robot state.

</div>

<div class="ttdef">

**Definition** measure.hpp:20

</div>

</div>

<div id="aclassfranky_1_1_measure_html_a014ae0622c47aee2a4dd9b9a781d4760" class="ttc">

<div class="ttname">

[franky::Measure::operator()](classfranky_1_1_measure.md#a014ae0622c47aee2a4dd9b9a781d4760)

</div>

<div class="ttdeci">

double operator()(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time) const

</div>

<div class="ttdoc">

Get the value of the measure.

</div>

<div class="ttdef">

**Definition** measure.hpp:46

</div>

</div>

<div id="aclassfranky_1_1_measure_html_a47fbb5bf68412799ab22234596832793" class="ttc">

<div class="ttname">

[franky::Measure::ForceY](classfranky_1_1_measure.md#a47fbb5bf68412799ab22234596832793)

</div>

<div class="ttdeci">

static Measure ForceY()

</div>

<div class="ttdoc">

A measure that returns the linear force on the end-effector in Y direction as by the O\_F\_ext\_hat\_K co...

</div>

<div class="ttdef">

**Definition** measure.cpp:49

</div>

</div>

<div id="aclassfranky_1_1_measure_html_a664d5e3506c4665f2be173ec5d2afa6f" class="ttc">

<div class="ttname">

[franky::Measure::repr](classfranky_1_1_measure.md#a664d5e3506c4665f2be173ec5d2afa6f)

</div>

<div class="ttdeci">

std::string repr() const

</div>

<div class="ttdoc">

The string representation of the measure.

</div>

<div class="ttdef">

**Definition** measure.hpp:53

</div>

</div>

<div id="aclassfranky_1_1_measure_html_a7aa92d415e33ca64b07aa598cb5e9ec4" class="ttc">

<div class="ttname">

[franky::Measure::ForceX](classfranky_1_1_measure.md#a7aa92d415e33ca64b07aa598cb5e9ec4)

</div>

<div class="ttdeci">

static Measure ForceX()

</div>

<div class="ttdoc">

A measure that returns the linear force on the end-effector in X direction as by the O\_F\_ext\_hat\_K co...

</div>

<div class="ttdef">

**Definition** measure.cpp:41

</div>

</div>

<div id="aclassfranky_1_1_measure_html_a98d3cc1b9f211b042de9fd2238938fbc" class="ttc">

<div class="ttname">

[franky::Measure::AbsTime](classfranky_1_1_measure.md#a98d3cc1b9f211b042de9fd2238938fbc)

</div>

<div class="ttdeci">

static Measure AbsTime()

</div>

<div class="ttdoc">

A measure that returns the absolute time since the start of the current chain of motions....

</div>

<div class="ttdef">

**Definition** measure.cpp:73

</div>

</div>

<div id="aclassfranky_1_1_measure_html_a9f8c4110a4ee5a1b102efaa6a424b0f3" class="ttc">

<div class="ttname">

[franky::Measure::ForceZ](classfranky_1_1_measure.md#a9f8c4110a4ee5a1b102efaa6a424b0f3)

</div>

<div class="ttdeci">

static Measure ForceZ()

</div>

<div class="ttdoc">

A measure that returns the linear force on the end-effector in Z direction as by the O\_F\_ext\_hat\_K co...

</div>

<div class="ttdef">

**Definition** measure.cpp:57

</div>

</div>

<div id="aclassfranky_1_1_measure_html_adc0787238886a53313c11870e58c4d10" class="ttc">

<div class="ttname">

[franky::Measure::RelTime](classfranky_1_1_measure.md#adc0787238886a53313c11870e58c4d10)

</div>

<div class="ttdeci">

static Measure RelTime()

</div>

<div class="ttdoc">

A measure that returns the relative time since the start of the current motion.

</div>

<div class="ttdef">

**Definition** measure.cpp:65

</div>

</div>

<div id="acondition_8hpp_html" class="ttc">

<div class="ttname">

[condition.hpp](condition_8hpp.md)

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

<div id="anamespacefranky_html_a0a18805109d5f09280f8830ce2970d3e" class="ttc">

<div class="ttname">

[franky::measure\_pow](namespacefranky.md#a0a18805109d5f09280f8830ce2970d3e)

</div>

<div class="ttdeci">

Measure measure\_pow(const Measure \&base, const Measure \&exponent)

</div>

<div class="ttdef">

**Definition** measure.cpp:93

</div>

</div>

<div id="anamespacefranky_html_a1b2d1dd9648934fd5f5e224993e74d7c" class="ttc">

<div class="ttname">

[franky::operator==](namespacefranky.md#a1b2d1dd9648934fd5f5e224993e74d7c)

</div>

<div class="ttdeci">

Condition operator==(const Condition \&c1, const Condition \&c2)

</div>

<div class="ttdef">

**Definition** condition.cpp:33

</div>

</div>

<div id="anamespacefranky_html_a3154ceacb8374282106cf479a8efb47b" class="ttc">

<div class="ttname">

[franky::operator+](namespacefranky.md#a3154ceacb8374282106cf479a8efb47b)

</div>

<div class="ttdeci">

Measure operator+(const Measure \&m1, const Measure \&m2)

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

<div id="anamespacefranky_html_a5bf2ceb580fd8b51d8423d17fb9e07c8" class="ttc">

<div class="ttname">

[franky::operator\<=](namespacefranky.md#a5bf2ceb580fd8b51d8423d17fb9e07c8)

</div>

<div class="ttdeci">

Condition operator\<=(const Measure \&m1, const Measure \&m2)

</div>

</div>

<div id="anamespacefranky_html_a64f30e1c601485d8fc082abd272481ba" class="ttc">

<div class="ttname">

[franky::operator\<](namespacefranky.md#a64f30e1c601485d8fc082abd272481ba)

</div>

<div class="ttdeci">

Condition operator\<(const Measure \&m1, const Measure \&m2)

</div>

</div>

<div id="anamespacefranky_html_a94e04eafe4db05368577002db3271805" class="ttc">

<div class="ttname">

[franky::operator\!=](namespacefranky.md#a94e04eafe4db05368577002db3271805)

</div>

<div class="ttdeci">

Condition operator\!=(const Condition \&c1, const Condition \&c2)

</div>

<div class="ttdef">

**Definition** condition.cpp:41

</div>

</div>

<div id="anamespacefranky_html_ab8f28e1eb83ddefdf341ea8644dc0392" class="ttc">

<div class="ttname">

[franky::operator\>](namespacefranky.md#ab8f28e1eb83ddefdf341ea8644dc0392)

</div>

<div class="ttdeci">

Condition operator\>(const Measure \&m1, const Measure \&m2)

</div>

</div>

<div id="anamespacefranky_html_ac292d7f5a4917cd61c4fe03d39122cbb" class="ttc">

<div class="ttname">

[franky::operator\>=](namespacefranky.md#ac292d7f5a4917cd61c4fe03d39122cbb)

</div>

<div class="ttdeci">

Condition operator\>=(const Measure \&m1, const Measure \&m2)

</div>

</div>

<div id="anamespacefranky_html_ae1c89933ac509cfab2c71192d55b4176" class="ttc">

<div class="ttname">

[franky::operator-](namespacefranky.md#ae1c89933ac509cfab2c71192d55b4176)

</div>

<div class="ttdeci">

Measure operator-(const Measure \&m)

</div>

<div class="ttdef">

**Definition** measure.cpp:103

</div>

</div>

<div id="anamespacefranky_html_affb71a7e2efda9caca54bdf81cc56d68" class="ttc">

<div class="ttname">

[franky::operator/](namespacefranky.md#affb71a7e2efda9caca54bdf81cc56d68)

</div>

<div class="ttdeci">

Measure operator/(const Measure \&m1, const Measure \&m2)

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
