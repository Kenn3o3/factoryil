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

joint\_state.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](joint__state_8hpp.md)

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

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include "[franky/robot\_pose.hpp](robot__pose_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/robot\_velocity.hpp](robot__velocity_8hpp.md)"</span>

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

<div id="foldopen00016" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00016"></span><span class="lineno"> [16](classfranky_1_1_joint_state.md)</span><span class="keyword">class </span>[JointState](classfranky_1_1_joint_state.md) {

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> 18</span> <span class="comment">// Suppress implicit conversion warning</span>

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span><span class="preprocessor">\#pragma clang diagnostic push</span>

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span><span class="preprocessor">\#pragma clang diagnostic ignored "-Wimplicit-conversion"</span>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> [27](classfranky_1_1_joint_state.md#a58de323134a7b11599dafbcb3d9fcf1c)</span> [JointState](classfranky_1_1_joint_state.md#a58de323134a7b11599dafbcb3d9fcf1c)([Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0)) : position\_(std::move([position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0))), velocity\_([Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)::Zero()) {}

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span><span class="preprocessor">\#pragma clang diagnostic pop</span>

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span>

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> [34](classfranky_1_1_joint_state.md#ad4a1bcb1c1f08f59f160c64f05462c1b)</span> [JointState](classfranky_1_1_joint_state.md#ad4a1bcb1c1f08f59f160c64f05462c1b)([Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0), [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100)) : position\_(std::move([position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0))), velocity\_(std::move([velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100))) {}

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span>

</div>

<div class="line">

<span id="l00036"></span><span class="lineno"> [36](classfranky_1_1_joint_state.md#a568e0e11672f5d9ad1f42b1d6cb9a576)</span> [JointState](classfranky_1_1_joint_state.md#a568e0e11672f5d9ad1f42b1d6cb9a576)(<span class="keyword">const</span> [JointState](classfranky_1_1_joint_state.md) &) = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> [38](classfranky_1_1_joint_state.md#a330222fd0fea56aef1c1a7a6eb918e9b)</span> [JointState](classfranky_1_1_joint_state.md#a330222fd0fea56aef1c1a7a6eb918e9b)() = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span>

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> [43](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> position\_; }

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span>

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> [48](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> velocity\_; }

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span>

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span> <span class="keyword">friend</span> std::ostream &[operator\<\<](classfranky_1_1_joint_state.md#a2b906651631f453efd46507ffbee9a5a)(std::ostream \&os, <span class="keyword">const</span> [JointState](classfranky_1_1_joint_state.md) \&joint\_state);

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span>

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) position\_;

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) velocity\_;

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span>};

</div>

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span>

</div>

<div id="foldopen00057" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00057"></span><span class="lineno"> [57](classfranky_1_1_joint_state.md#a2b906651631f453efd46507ffbee9a5a)</span><span class="keyword">inline</span> std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream \&os, <span class="keyword">const</span> [JointState](classfranky_1_1_joint_state.md) \&joint\_state) {

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> os \<\< <span class="stringliteral">"JointState(position="</span> \<\< joint\_state.position\_ \<\< <span class="stringliteral">", velocity="</span> \<\< joint\_state.velocity\_ \<\< <span class="stringliteral">")"</span>;

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> <span class="keywordflow">return</span> os;

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>}

</div>

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span>

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_joint_state_html" class="ttc">

<div class="ttname">

[franky::JointState](classfranky_1_1_joint_state.md)

</div>

<div class="ttdoc">

Joint state of a robot.

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:16

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_a2b906651631f453efd46507ffbee9a5a" class="ttc">

<div class="ttname">

[franky::JointState::operator\<\<](classfranky_1_1_joint_state.md#a2b906651631f453efd46507ffbee9a5a)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const JointState \&joint\_state)

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:57

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_a330222fd0fea56aef1c1a7a6eb918e9b" class="ttc">

<div class="ttname">

[franky::JointState::JointState](classfranky_1_1_joint_state.md#a330222fd0fea56aef1c1a7a6eb918e9b)

</div>

<div class="ttdeci">

JointState()=default

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_a5210d159dcb06ea28000f90060acf100" class="ttc">

<div class="ttname">

[franky::JointState::velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100)

</div>

<div class="ttdeci">

Vector7d velocity() const

</div>

<div class="ttdoc">

The velocity component of the state.

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:48

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_a568e0e11672f5d9ad1f42b1d6cb9a576" class="ttc">

<div class="ttname">

[franky::JointState::JointState](classfranky_1_1_joint_state.md#a568e0e11672f5d9ad1f42b1d6cb9a576)

</div>

<div class="ttdeci">

JointState(const JointState &)=default

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_a58de323134a7b11599dafbcb3d9fcf1c" class="ttc">

<div class="ttname">

[franky::JointState::JointState](classfranky_1_1_joint_state.md#a58de323134a7b11599dafbcb3d9fcf1c)

</div>

<div class="ttdeci">

JointState(Vector7d position)

</div>

<div class="ttdoc">

Construct a joint state with the given joint positions and zero velocities.

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:27

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_ad4a1bcb1c1f08f59f160c64f05462c1b" class="ttc">

<div class="ttname">

[franky::JointState::JointState](classfranky_1_1_joint_state.md#ad4a1bcb1c1f08f59f160c64f05462c1b)

</div>

<div class="ttdeci">

JointState(Vector7d position, Vector7d velocity)

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:34

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_addd9bedce775d28cef880644b635ccf0" class="ttc">

<div class="ttname">

[franky::JointState::position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0)

</div>

<div class="ttdeci">

Vector7d position() const

</div>

<div class="ttdoc">

The position component of the state.

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:43

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

<div id="arobot__pose_8hpp_html" class="ttc">

<div class="ttname">

[robot\_pose.hpp](robot__pose_8hpp.md)

</div>

</div>

<div id="arobot__velocity_8hpp_html" class="ttc">

<div class="ttname">

[robot\_velocity.hpp](robot__velocity_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
