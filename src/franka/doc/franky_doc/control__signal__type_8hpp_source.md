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

control\_signal\_type.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](control__signal__type_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> [8](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca982887767b31bb472878f67e6ddbfd9f)</span><span class="keyword">enum</span> [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) { [Torques](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacafebe00005b96de2fff86702fc305174a), [JointVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacadecb27858472a616860e32411b1a6854), [JointPositions](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacae53870521bf0d6aaf73f8435b4c53601), [CartesianVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca1a276615bdb52bb012d25ccc6ae470d1), [CartesianPose](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca982887767b31bb472878f67e6ddbfd9f) };

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span>} <span class="comment">// namespace franky</span>

</div>

<div id="anamespacefranky_html" class="ttc">

<div class="ttname">

[franky](namespacefranky.md)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaac" class="ttc">

<div class="ttname">

[franky::ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac)

</div>

<div class="ttdeci">

ControlSignalType

</div>

<div class="ttdoc">

Type of control signal.

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaaca1a276615bdb52bb012d25ccc6ae470d1" class="ttc">

<div class="ttname">

[franky::CartesianVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca1a276615bdb52bb012d25ccc6ae470d1)

</div>

<div class="ttdeci">

@ CartesianVelocities

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaaca982887767b31bb472878f67e6ddbfd9f" class="ttc">

<div class="ttname">

[franky::CartesianPose](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca982887767b31bb472878f67e6ddbfd9f)

</div>

<div class="ttdeci">

@ CartesianPose

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaacadecb27858472a616860e32411b1a6854" class="ttc">

<div class="ttname">

[franky::JointVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacadecb27858472a616860e32411b1a6854)

</div>

<div class="ttdeci">

@ JointVelocities

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaacae53870521bf0d6aaf73f8435b4c53601" class="ttc">

<div class="ttname">

[franky::JointPositions](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacae53870521bf0d6aaf73f8435b4c53601)

</div>

<div class="ttdeci">

@ JointPositions

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaacafebe00005b96de2fff86702fc305174a" class="ttc">

<div class="ttname">

[franky::Torques](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacafebe00005b96de2fff86702fc305174a)

</div>

<div class="ttdeci">

@ Torques

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
