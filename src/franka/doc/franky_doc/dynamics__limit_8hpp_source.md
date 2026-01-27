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

dynamics\_limit.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](dynamics__limit_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<functional\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<memory\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<mutex\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<sstream\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include \<stdexcept\></span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include \<string\></span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include \<utility\></span>

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

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span><span class="keyword">template</span> \<<span class="keyword">typename</span> LimitType\>

</div>

<div id="foldopen00023" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00023"></span><span class="lineno"> [23](classfranky_1_1_dynamics_limit.md)</span><span class="keyword">class </span>[DynamicsLimit](classfranky_1_1_dynamics_limit.md) {

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00039" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00039"></span><span class="lineno"> [39](classfranky_1_1_dynamics_limit.md#a344e2c223138ec679d26af30e5fdd9e5)</span> [DynamicsLimit](classfranky_1_1_dynamics_limit.md#a344e2c223138ec679d26af30e5fdd9e5)(

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> <span class="keyword">const</span> std::string &[desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad), <span class="keyword">const</span> LimitType \&max\_val, <span class="keyword">const</span> std::shared\_ptr\<std::mutex\> \&write\_mutex,

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> <span class="keyword">const</span> std::function\<<span class="keywordtype">bool</span>()\> \&can\_write\_condition)

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> : [DynamicsLimit](classfranky_1_1_dynamics_limit.md)([desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad), max\_val, write\_mutex, can\_write\_condition, max\_val) {}

</div>

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span>

</div>

<div id="foldopen00059" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00059"></span><span class="lineno"> [59](classfranky_1_1_dynamics_limit.md#addd366f6d40b581abd6463ca61cfd2c5)</span> [DynamicsLimit](classfranky_1_1_dynamics_limit.md#addd366f6d40b581abd6463ca61cfd2c5)(

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span> std::string [desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad), <span class="keyword">const</span> LimitType \&max\_val, <span class="keyword">const</span> std::shared\_ptr\<std::mutex\> \&write\_mutex,

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> <span class="keyword">const</span> std::function\<<span class="keywordtype">bool</span>()\> \&can\_write\_condition, <span class="keyword">const</span> LimitType \&default\_val)

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span> : [max](classfranky_1_1_dynamics_limit.md#a8ad7788915e12262221aa983c0588d62)(max\_val),

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> [desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad)(std::move([desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad))),

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> write\_mutex\_(write\_mutex),

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> value\_(default\_val),

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> can\_write\_condition\_(can\_write\_condition) {}

</div>

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span>

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span> <span class="keyword">template</span> \<<span class="keyword">typename</span> AlternativeType\>

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> [78](classfranky_1_1_dynamics_limit.md#adbb6e9b426e82b05272e2fe3939e8eb5)</span> <span class="keywordtype">void</span> [setFrom](classfranky_1_1_dynamics_limit.md#adbb6e9b426e82b05272e2fe3939e8eb5)(<span class="keyword">const</span> AlternativeType \&value);

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span>

</div>

<div id="foldopen00092" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00092"></span><span class="lineno"> [92](classfranky_1_1_dynamics_limit.md#a13c429626a61ddf6b37ad38e8b7ee9ec)</span> <span class="keywordtype">void</span> [set](classfranky_1_1_dynamics_limit.md#a13c429626a61ddf6b37ad38e8b7ee9ec)(<span class="keyword">const</span> LimitType \&value) {

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> 93</span> std::unique\_lock lock(\*write\_mutex\_);

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span> <span class="keywordflow">if</span> (\!can\_write\_condition\_()) {

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> 95</span> std::stringstream ss;

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> 96</span> ss \<\< <span class="stringliteral">"Cannot set "</span> \<\< [desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad) \<\< <span class="stringliteral">" limit while robot is in control."</span>;

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> 97</span> <span class="keywordflow">throw</span> std::runtime\_error(ss.str());

</div>

<div class="line">

<span id="l00098"></span><span class="lineno"> 98</span> }

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span> check(value);

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span> value\_ = value;

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> 101</span> }

</div>

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> 102</span>

</div>

<div class="line">

<span id="l00110"></span><span class="lineno"> [110](classfranky_1_1_dynamics_limit.md#a39d85438237067ffa3b3829500b01f14)</span> \[\[nodiscard\]\] LimitType [get](classfranky_1_1_dynamics_limit.md#a39d85438237067ffa3b3829500b01f14)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> value\_; }

</div>

<div class="line">

<span id="l00111"></span><span class="lineno"> 111</span>

</div>

<div class="line">

<span id="l00118"></span><span class="lineno"> [118](classfranky_1_1_dynamics_limit.md#a8ad7788915e12262221aa983c0588d62)</span> <span class="keyword">const</span> LimitType [max](classfranky_1_1_dynamics_limit.md#a8ad7788915e12262221aa983c0588d62);

</div>

<div class="line">

<span id="l00119"></span><span class="lineno"> 119</span>

</div>

<div class="line">

<span id="l00126"></span><span class="lineno"> [126](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad)</span> <span class="keyword">const</span> std::string [desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad);

</div>

<div class="line">

<span id="l00127"></span><span class="lineno"> 127</span>

</div>

<div class="line">

<span id="l00128"></span><span class="lineno"> 128</span> <span class="keyword">template</span> \<<span class="keyword">typename</span> LimitTypeStream\>

</div>

<div id="foldopen00129" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00129"></span><span class="lineno"> [129](classfranky_1_1_dynamics_limit.md#a1909095817a8e86989d8c822e3ea2fb3)</span> <span class="keyword">friend</span> std::ostream &[operator\<\<](classfranky_1_1_dynamics_limit.md#a1909095817a8e86989d8c822e3ea2fb3)(std::ostream \&os, <span class="keyword">const</span> [DynamicsLimit\<LimitTypeStream\>](classfranky_1_1_dynamics_limit.md) \&dynamics\_limit);

</div>

<div class="line">

<span id="l00130"></span><span class="lineno"> 130</span>

</div>

<div class="line">

<span id="l00131"></span><span class="lineno"> 131</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00140"></span><span class="lineno"> 140</span> <span class="keywordtype">void</span> check(<span class="keyword">const</span> LimitType \&value) <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00141"></span><span class="lineno"> 141</span>

</div>

<div class="line">

<span id="l00142"></span><span class="lineno"> 142</span> std::shared\_ptr\<std::mutex\> write\_mutex\_;

</div>

<div class="line">

<span id="l00143"></span><span class="lineno"> 143</span> LimitType value\_;

</div>

<div class="line">

<span id="l00144"></span><span class="lineno"> 144</span> std::function\<bool()\> can\_write\_condition\_;

</div>

<div class="line">

<span id="l00145"></span><span class="lineno"> 145</span>};

</div>

<div class="line">

<span id="l00146"></span><span class="lineno"> 146</span>

</div>

<div class="line">

<span id="l00147"></span><span class="lineno"> 147</span><span class="keyword">template</span> \<<span class="keyword">typename</span> LimitTypeStream\>

</div>

<div id="foldopen00148" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00148"></span><span class="lineno"> [148](classfranky_1_1_dynamics_limit.md#a1909095817a8e86989d8c822e3ea2fb3)</span>std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream \&os, <span class="keyword">const</span> [DynamicsLimit\<LimitTypeStream\>](classfranky_1_1_dynamics_limit.md) \&dynamics\_limit) {

</div>

<div class="line">

<span id="l00149"></span><span class="lineno"> 149</span> os \<\< dynamics\_limit.value\_ \<\< <span class="stringliteral">" (max: "</span> \<\< dynamics\_limit.[max](classfranky_1_1_dynamics_limit.md#a8ad7788915e12262221aa983c0588d62) \<\< <span class="stringliteral">")"</span>;

</div>

<div class="line">

<span id="l00150"></span><span class="lineno"> 150</span> <span class="keywordflow">return</span> os;

</div>

<div class="line">

<span id="l00151"></span><span class="lineno"> 151</span>}

</div>

</div>

</div>

<div class="line">

<span id="l00152"></span><span class="lineno"> 152</span>

</div>

<div class="line">

<span id="l00153"></span><span class="lineno"> 153</span>} <span class="comment">// namespace franky</span>

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html" class="ttc">

<div class="ttname">

[franky::DynamicsLimit](classfranky_1_1_dynamics_limit.md)

</div>

<div class="ttdoc">

A template class representing a dynamics limit with a maximum value.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:23

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_a13c429626a61ddf6b37ad38e8b7ee9ec" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::set](classfranky_1_1_dynamics_limit.md#a13c429626a61ddf6b37ad38e8b7ee9ec)

</div>

<div class="ttdeci">

void set(const LimitType \&value)

</div>

<div class="ttdoc">

Set a new value for the limit.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:92

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_a1909095817a8e86989d8c822e3ea2fb3" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::operator\<\<](classfranky_1_1_dynamics_limit.md#a1909095817a8e86989d8c822e3ea2fb3)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const DynamicsLimit\< LimitTypeStream \> \&dynamics\_limit)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:148

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_a344e2c223138ec679d26af30e5fdd9e5" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::DynamicsLimit](classfranky_1_1_dynamics_limit.md#a344e2c223138ec679d26af30e5fdd9e5)

</div>

<div class="ttdeci">

DynamicsLimit(const std::string \&desc, const LimitType \&max\_val, const std::shared\_ptr\< std::mutex \> \&write\_mutex, const std::function\< bool()\> \&can\_write\_condition)

</div>

<div class="ttdoc">

Constructor for DynamicsLimit.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:39

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_a39d85438237067ffa3b3829500b01f14" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::get](classfranky_1_1_dynamics_limit.md#a39d85438237067ffa3b3829500b01f14)

</div>

<div class="ttdeci">

LimitType get() const

</div>

<div class="ttdoc">

Get the current value of the limit.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:110

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_a771e6607930b05b1807b3f891a28c5ad" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad)

</div>

<div class="ttdeci">

const std::string desc

</div>

<div class="ttdoc">

Description of this limit.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:126

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_a8ad7788915e12262221aa983c0588d62" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::max](classfranky_1_1_dynamics_limit.md#a8ad7788915e12262221aa983c0588d62)

</div>

<div class="ttdeci">

const LimitType max

</div>

<div class="ttdoc">

The maximum value this limit can take as defined by Franka.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:118

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_adbb6e9b426e82b05272e2fe3939e8eb5" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::setFrom](classfranky_1_1_dynamics_limit.md#adbb6e9b426e82b05272e2fe3939e8eb5)

</div>

<div class="ttdeci">

void setFrom(const AlternativeType \&value)

</div>

<div class="ttdoc">

Set a new value for the limit with a different type.

</div>

</div>

<div id="aclassfranky_1_1_dynamics_limit_html_addd366f6d40b581abd6463ca61cfd2c5" class="ttc">

<div class="ttname">

[franky::DynamicsLimit::DynamicsLimit](classfranky_1_1_dynamics_limit.md#addd366f6d40b581abd6463ca61cfd2c5)

</div>

<div class="ttdeci">

DynamicsLimit(std::string desc, const LimitType \&max\_val, const std::shared\_ptr\< std::mutex \> \&write\_mutex, const std::function\< bool()\> \&can\_write\_condition, const LimitType \&default\_val)

</div>

<div class="ttdoc">

Constructor for DynamicsLimit.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:59

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

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
