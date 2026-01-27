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

condition.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](condition_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<[franky/robot\_state.hpp](robot__state_8hpp.md)\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<functional\></span>

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

<div id="foldopen00016" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00016"></span><span class="lineno"> [16](classfranky_1_1_condition.md)</span><span class="keyword">class </span>[Condition](classfranky_1_1_condition.md) {

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4)</span> <span class="keyword">using </span>[CheckFunc](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4) = std::function\<bool(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\>;

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span>

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> <span class="keyword">explicit</span> [Condition](classfranky_1_1_condition.md)([CheckFunc](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4) check\_func, std::string [repr](classfranky_1_1_condition.md#afaae7e02e68860afdf7c40a75bf91d25) = <span class="stringliteral">"NULL"</span>);

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span>

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span> [Condition](classfranky_1_1_condition.md)(<span class="keywordtype">bool</span> constant\_value);

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span>

</div>

<div id="foldopen00042" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00042"></span><span class="lineno"> [42](classfranky_1_1_condition.md#ac8859034fd1f80137f0b87dc5efbb22b)</span> <span class="keyword">inline</span> <span class="keywordtype">bool</span> [operator()](classfranky_1_1_condition.md#ac8859034fd1f80137f0b87dc5efbb22b)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> <span class="keywordflow">return</span> check\_func\_(robot\_state, rel\_time, abs\_time);

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> }

</div>

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> [49](classfranky_1_1_condition.md#afaae7e02e68860afdf7c40a75bf91d25)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> std::string [repr](classfranky_1_1_condition.md#afaae7e02e68860afdf7c40a75bf91d25)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> repr\_; }

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span>

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> [CheckFunc](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4) check\_func\_;

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> std::string repr\_;

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span>};

</div>

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span>

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span>Condition [operator&&](namespacefranky.md#a9998e96cdaba177849f645156d9268eb)(<span class="keyword">const</span> Condition \&c1, <span class="keyword">const</span> Condition \&c2);

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span>

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span>Condition [operator||](namespacefranky.md#aa74d0b230fd802dc79d11c67a5d2066b)(<span class="keyword">const</span> Condition \&c1, <span class="keyword">const</span> Condition \&c2);

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span>

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>Condition [operator==](namespacefranky.md#a1b2d1dd9648934fd5f5e224993e74d7c)(<span class="keyword">const</span> Condition \&c1, <span class="keyword">const</span> Condition \&c2);

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span>

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span>Condition [operator\!=](namespacefranky.md#a94e04eafe4db05368577002db3271805)(<span class="keyword">const</span> Condition \&c1, <span class="keyword">const</span> Condition \&c2);

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span>Condition [operator\!](namespacefranky.md#aaa64d97ddccb5a54b9cc5448f4140d37)(<span class="keyword">const</span> Condition \&c);

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span>

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_condition_html_ac8859034fd1f80137f0b87dc5efbb22b" class="ttc">

<div class="ttname">

[franky::Condition::operator()](classfranky_1_1_condition.md#ac8859034fd1f80137f0b87dc5efbb22b)

</div>

<div class="ttdeci">

bool operator()(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time) const

</div>

<div class="ttdoc">

Check if the condition is met.

</div>

<div class="ttdef">

**Definition** condition.hpp:42

</div>

</div>

<div id="aclassfranky_1_1_condition_html_ae0ccd93e225b1433e704b51767958eb4" class="ttc">

<div class="ttname">

[franky::Condition::CheckFunc](classfranky_1_1_condition.md#ae0ccd93e225b1433e704b51767958eb4)

</div>

<div class="ttdeci">

std::function\< bool(const RobotState &, franka::Duration, franka::Duration)\> CheckFunc

</div>

<div class="ttdef">

**Definition** condition.hpp:18

</div>

</div>

<div id="aclassfranky_1_1_condition_html_afaae7e02e68860afdf7c40a75bf91d25" class="ttc">

<div class="ttname">

[franky::Condition::repr](classfranky_1_1_condition.md#afaae7e02e68860afdf7c40a75bf91d25)

</div>

<div class="ttdeci">

std::string repr() const

</div>

<div class="ttdoc">

The string representation of the condition.

</div>

<div class="ttdef">

**Definition** condition.hpp:49

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

<div id="anamespacefranky_html_a9998e96cdaba177849f645156d9268eb" class="ttc">

<div class="ttname">

[franky::operator&&](namespacefranky.md#a9998e96cdaba177849f645156d9268eb)

</div>

<div class="ttdeci">

Condition operator&&(const Condition \&c1, const Condition \&c2)

</div>

<div class="ttdef">

**Definition** condition.cpp:17

</div>

</div>

<div id="anamespacefranky_html_aa74d0b230fd802dc79d11c67a5d2066b" class="ttc">

<div class="ttname">

[franky::operator||](namespacefranky.md#aa74d0b230fd802dc79d11c67a5d2066b)

</div>

<div class="ttdeci">

Condition operator||(const Condition \&c1, const Condition \&c2)

</div>

<div class="ttdef">

**Definition** condition.cpp:25

</div>

</div>

<div id="anamespacefranky_html_aaa64d97ddccb5a54b9cc5448f4140d37" class="ttc">

<div class="ttname">

[franky::operator\!](namespacefranky.md#aaa64d97ddccb5a54b9cc5448f4140d37)

</div>

<div class="ttdeci">

Condition operator\!(const Condition \&c)

</div>

<div class="ttdef">

**Definition** condition.cpp:49

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
