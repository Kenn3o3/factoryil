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

scope\_guard.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](scope__guard_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#include \<functional\></span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span><span class="preprocessor">\#include \<utility\></span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span>

</div>

<div id="foldopen00009" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00009"></span><span class="lineno"> [9](classfranky_1_1scope__guard.md)</span><span class="keyword">class </span>[scope\_guard](classfranky_1_1scope__guard.md) {

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> [17](classfranky_1_1scope__guard.md#ae2f80a1c31f9c48523d0320e738f8621)</span> <span class="keyword">explicit</span> [scope\_guard](classfranky_1_1scope__guard.md#ae2f80a1c31f9c48523d0320e738f8621)(std::function\<<span class="keywordtype">void</span>()\> [f](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) : f\_(std::move([f](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))) {}

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> 18</span>

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> [19](classfranky_1_1scope__guard.md#a9351b40db417bd66f6d8c0e40c664a4c)</span> [\~scope\_guard](classfranky_1_1scope__guard.md#a9351b40db417bd66f6d8c0e40c664a4c)() { f\_(); }

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span> std::function\<[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)()\> f\_;

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span>};

</div>

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1scope__guard_html" class="ttc">

<div class="ttname">

[franky::scope\_guard](classfranky_1_1scope__guard.md)

</div>

<div class="ttdoc">

A scope guard that executes a function when it goes out of scope.

</div>

<div class="ttdef">

**Definition** scope\_guard.hpp:9

</div>

</div>

<div id="aclassfranky_1_1scope__guard_html_a9351b40db417bd66f6d8c0e40c664a4c" class="ttc">

<div class="ttname">

[franky::scope\_guard::\~scope\_guard](classfranky_1_1scope__guard.md#a9351b40db417bd66f6d8c0e40c664a4c)

</div>

<div class="ttdeci">

\~scope\_guard()

</div>

<div class="ttdef">

**Definition** scope\_guard.hpp:19

</div>

</div>

<div id="aclassfranky_1_1scope__guard_html_ae2f80a1c31f9c48523d0320e738f8621" class="ttc">

<div class="ttname">

[franky::scope\_guard::scope\_guard](classfranky_1_1scope__guard.md#ae2f80a1c31f9c48523d0320e738f8621)

</div>

<div class="ttdeci">

scope\_guard(std::function\< void()\> f)

</div>

<div class="ttdoc">

Constructor that takes a function to execute when the guard goes out of scope.

</div>

<div class="ttdef">

**Definition** scope\_guard.hpp:17

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
