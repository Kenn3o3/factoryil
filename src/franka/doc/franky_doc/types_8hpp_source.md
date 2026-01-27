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

types.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](types_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<Eigen/Geometry\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<array\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<unsupported/Eigen/EulerAngles\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<variant\></span>

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

<div class="line">

<span id="l00010"></span><span class="lineno"> [10](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb)</span><span class="keyword">using </span>[Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) = Eigen::Vector\<double, 6\>;

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> [11](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)</span><span class="keyword">using </span>[Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) = Eigen::Vector\<double, 7\>;

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> [12](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b)</span><span class="keyword">using </span>[Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) = Eigen::Matrix\<double, 6, 7\>;

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> [13](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585)</span><span class="keyword">using </span>[IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) = Eigen::Matrix\<double, 3, 3\>;

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span>

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> [15](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)</span><span class="keyword">using </span>[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) = Eigen::Affine3d;

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span>

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)</span><span class="keyword">using </span>[Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66) = std::variant\<std::array\<double, dims\>, Eigen::Vector\<double, dims\>\>;

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span>

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> [21](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9)</span><span class="keyword">using </span>[ScalarOrArray](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) = std::variant\<double, Array\<dims\>\>;

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span>

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span>} <span class="comment">// namespace franky</span>

</div>

<div id="anamespacefranky_html" class="ttc">

<div class="ttname">

[franky](namespacefranky.md)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:8

</div>

</div>

<div id="anamespacefranky_html_a0e2202a008accb842c58a0ced1f2b585" class="ttc">

<div class="ttname">

[franky::IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585)

</div>

<div class="ttdeci">

Eigen::Matrix\< double, 3, 3 \> IntertiaMatrix

</div>

<div class="ttdef">

**Definition** types.hpp:13

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

<div id="anamespacefranky_html_ab6d5b94e45f9e74b0a3195f76408bc8b" class="ttc">

<div class="ttname">

[franky::Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b)

</div>

<div class="ttdeci">

Eigen::Matrix\< double, 6, 7 \> Jacobian

</div>

<div class="ttdef">

**Definition** types.hpp:12

</div>

</div>

<div id="anamespacefranky_html_ae77a95d5f13271457b8c8fb645da3bd9" class="ttc">

<div class="ttname">

[franky::ScalarOrArray](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9)

</div>

<div class="ttdeci">

std::variant\< double, Array\< dims \> \> ScalarOrArray

</div>

<div class="ttdef">

**Definition** types.hpp:21

</div>

</div>

<div id="anamespacefranky_html_ae9a820b03821a3e69e1e2eb1db33ea66" class="ttc">

<div class="ttname">

[franky::Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)

</div>

<div class="ttdeci">

std::variant\< std::array\< double, dims \>, Eigen::Vector\< double, dims \> \> Array

</div>

<div class="ttdef">

**Definition** types.hpp:18

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

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
