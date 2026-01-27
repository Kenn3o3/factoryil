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

robot\_state.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](robot__state_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="comment">// Adapted from</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span><span class="comment">// https://github.com/frankaemika/libfranka/blob/main/include/franka/robot\_state.h</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<franka/robot\_state.h\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/elbow\_state.hpp](elbow__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[franky/twist.hpp](twist_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/twist\_acceleration.hpp](twist__acceleration_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="preprocessor">\#include "[franky/util.hpp](util_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span>

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span>

</div>

<div id="foldopen00023" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00023"></span><span class="lineno"> [23](structfranky_1_1_robot_state.md)</span><span class="keyword">struct </span>[RobotState](structfranky_1_1_robot_state.md) {

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> <span class="keyword">static</span> [RobotState](structfranky_1_1_robot_state.md) [from\_franka](structfranky_1_1_robot_state.md#a2c4c90f4eac5e22551d97102452f8055)(

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> <span class="keyword">const</span> franka::RobotState &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), std::optional\<Vector7d\> [q\_est](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6) = std::nullopt,

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span> std::optional\<Vector7d\> [dq\_est](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e) = std::nullopt, std::optional\<Vector7d\> [ddq\_est](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c) = std::nullopt,

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span> std::optional\<Twist\> [O\_dP\_EE\_est](structfranky_1_1_robot_state.md#aa05402a790846ad287e136b0364359c6) = std::nullopt, std::optional\<TwistAcceleration\> [O\_ddP\_EE\_est](structfranky_1_1_robot_state.md#a3a35fa21dfce2110e06f3b2476f9734e) = std::nullopt,

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span> std::optional\<double\> [delbow\_est](structfranky_1_1_robot_state.md#acd1c492bd7f6e10b9ecff6cc509d2f90) = std::nullopt, std::optional\<double\> [ddelbow\_est](structfranky_1_1_robot_state.md#ade3beb0d2a00728a316b43c1a6c15229) = std::nullopt);

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span>

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span> <span class="keyword">static</span> [RobotState](structfranky_1_1_robot_state.md) [from\_franka](structfranky_1_1_robot_state.md#a2c4c90f4eac5e22551d97102452f8055)(

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span> <span class="keyword">const</span> franka::RobotState &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Jacobian](namespacefranky.md#ab6d5b94e45f9e74b0a3195f76408bc8b) &[ee\_jacobian](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[q\_est](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6), <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[dq\_est](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e),

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span> <span class="keyword">const</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) &[ddq\_est](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c));

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> [38](structfranky_1_1_robot_state.md#a0a9667e0d76a3901c0e9393a8b227c0a)</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [O\_T\_EE](structfranky_1_1_robot_state.md#a0a9667e0d76a3901c0e9393a8b227c0a){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span>

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> [45](structfranky_1_1_robot_state.md#a9650368f3c772ed7d46f07f6412b3faf)</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [O\_T\_EE\_d](structfranky_1_1_robot_state.md#a9650368f3c772ed7d46f07f6412b3faf){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span>

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> [55](structfranky_1_1_robot_state.md#aa2f851078b2a03f90c33a37bf13d07a1)</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [F\_T\_EE](structfranky_1_1_robot_state.md#aa2f851078b2a03f90c33a37bf13d07a1){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span>

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span><span class="preprocessor">\#ifdef FRANKA\_0\_8</span>

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [F\_T\_NE](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span>

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [NE\_T\_EE](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span><span class="preprocessor">\#endif</span>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span>

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> [86](structfranky_1_1_robot_state.md#a5bab6bd3d0b8e3781b80db887808be1e)</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [EE\_T\_K](structfranky_1_1_robot_state.md#a5bab6bd3d0b8e3781b80db887808be1e){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span>

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> [92](structfranky_1_1_robot_state.md#aa5104cf1e290f362c032dd3099191bd8)</span> <span class="keywordtype">double</span> [m\_ee](structfranky_1_1_robot_state.md#aa5104cf1e290f362c032dd3099191bd8){};

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> 93</span>

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> [99](structfranky_1_1_robot_state.md#a9646c969429e0853722837c950820f44)</span> [IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) [I\_ee](structfranky_1_1_robot_state.md#a9646c969429e0853722837c950820f44){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span>

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> [106](structfranky_1_1_robot_state.md#a32d78a9f6048cdce9f096e2a33b747f1)</span> Eigen::Vector3d [F\_x\_Cee](structfranky_1_1_robot_state.md#a32d78a9f6048cdce9f096e2a33b747f1){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span>

</div>

<div class="line">

<span id="l00112"></span><span class="lineno"> [112](structfranky_1_1_robot_state.md#ac7f17c8d7d1bb49658c872904caa8233)</span> <span class="keywordtype">double</span> [m\_load](structfranky_1_1_robot_state.md#ac7f17c8d7d1bb49658c872904caa8233){};

</div>

<div class="line">

<span id="l00113"></span><span class="lineno"> 113</span>

</div>

<div class="line">

<span id="l00119"></span><span class="lineno"> [119](structfranky_1_1_robot_state.md#ad8590b96b51241bea2620dcc482c0f9a)</span> [IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) [I\_load](structfranky_1_1_robot_state.md#ad8590b96b51241bea2620dcc482c0f9a){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00120"></span><span class="lineno"> 120</span>

</div>

<div class="line">

<span id="l00126"></span><span class="lineno"> [126](structfranky_1_1_robot_state.md#abbbebbf039f73e41d26193f5acebf536)</span> Eigen::Vector3d [F\_x\_Cload](structfranky_1_1_robot_state.md#abbbebbf039f73e41d26193f5acebf536){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00127"></span><span class="lineno"> 127</span>

</div>

<div class="line">

<span id="l00132"></span><span class="lineno"> [132](structfranky_1_1_robot_state.md#a8e8ddca4a286bfb33aa94bfbafc7666d)</span> <span class="keywordtype">double</span> [m\_total](structfranky_1_1_robot_state.md#a8e8ddca4a286bfb33aa94bfbafc7666d){};

</div>

<div class="line">

<span id="l00133"></span><span class="lineno"> 133</span>

</div>

<div class="line">

<span id="l00139"></span><span class="lineno"> [139](structfranky_1_1_robot_state.md#a627a19dfeb245fe9929b5dba0de4516b)</span> [IntertiaMatrix](namespacefranky.md#a0e2202a008accb842c58a0ced1f2b585) [I\_total](structfranky_1_1_robot_state.md#a627a19dfeb245fe9929b5dba0de4516b){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00140"></span><span class="lineno"> 140</span>

</div>

<div class="line">

<span id="l00146"></span><span class="lineno"> [146](structfranky_1_1_robot_state.md#a3706cdbd18abaad5acae4b6420c6679c)</span> Eigen::Vector3d [F\_x\_Ctotal](structfranky_1_1_robot_state.md#a3706cdbd18abaad5acae4b6420c6679c){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00147"></span><span class="lineno"> 147</span>

</div>

<div class="line">

<span id="l00151"></span><span class="lineno"> [151](structfranky_1_1_robot_state.md#aabafb74fb3a4c958ec20d1c944a58ef1)</span> [ElbowState](classfranky_1_1_elbow_state.md) [elbow](structfranky_1_1_robot_state.md#aabafb74fb3a4c958ec20d1c944a58ef1){};

</div>

<div class="line">

<span id="l00152"></span><span class="lineno"> 152</span>

</div>

<div class="line">

<span id="l00156"></span><span class="lineno"> [156](structfranky_1_1_robot_state.md#aa7c69937e5e9837d62b490dcc8aa255f)</span> [ElbowState](classfranky_1_1_elbow_state.md) [elbow\_d](structfranky_1_1_robot_state.md#aa7c69937e5e9837d62b490dcc8aa255f){};

</div>

<div class="line">

<span id="l00157"></span><span class="lineno"> 157</span>

</div>

<div class="line">

<span id="l00161"></span><span class="lineno"> [161](structfranky_1_1_robot_state.md#a69e433ddee972b5b751233b99a6643e9)</span> [ElbowState](classfranky_1_1_elbow_state.md) [elbow\_c](structfranky_1_1_robot_state.md#a69e433ddee972b5b751233b99a6643e9){};

</div>

<div class="line">

<span id="l00162"></span><span class="lineno"> 162</span>

</div>

<div class="line">

<span id="l00166"></span><span class="lineno"> [166](structfranky_1_1_robot_state.md#a3a38c0c7040b305f2d00c2388e0e451c)</span> <span class="keywordtype">double</span> [delbow\_c](structfranky_1_1_robot_state.md#a3a38c0c7040b305f2d00c2388e0e451c){};

</div>

<div class="line">

<span id="l00167"></span><span class="lineno"> 167</span>

</div>

<div class="line">

<span id="l00171"></span><span class="lineno"> [171](structfranky_1_1_robot_state.md#ab6996c44d6d0b34e03cec086d6d16519)</span> <span class="keywordtype">double</span> [ddelbow\_c](structfranky_1_1_robot_state.md#ab6996c44d6d0b34e03cec086d6d16519){};

</div>

<div class="line">

<span id="l00172"></span><span class="lineno"> 172</span>

</div>

<div class="line">

<span id="l00177"></span><span class="lineno"> [177](structfranky_1_1_robot_state.md#aa1d327630a6eedc9b3bbad3b5d7423b3)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [tau\_J](structfranky_1_1_robot_state.md#aa1d327630a6eedc9b3bbad3b5d7423b3){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00178"></span><span class="lineno"> 178</span>

</div>

<div class="line">

<span id="l00184"></span><span class="lineno"> [184](structfranky_1_1_robot_state.md#a662a010406b9d9833673f5b84238abe7)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [tau\_J\_d](structfranky_1_1_robot_state.md#a662a010406b9d9833673f5b84238abe7){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00185"></span><span class="lineno"> 185</span>

</div>

<div class="line">

<span id="l00191"></span><span class="lineno"> [191](structfranky_1_1_robot_state.md#a7691ba4f68ee2c2c88138faa319156f5)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [dtau\_J](structfranky_1_1_robot_state.md#a7691ba4f68ee2c2c88138faa319156f5){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00192"></span><span class="lineno"> 192</span>

</div>

<div class="line">

<span id="l00197"></span><span class="lineno"> [197](structfranky_1_1_robot_state.md#adcba9f6e06d0161ee6ec2bb904e2f1cd)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [q](structfranky_1_1_robot_state.md#adcba9f6e06d0161ee6ec2bb904e2f1cd){};

</div>

<div class="line">

<span id="l00198"></span><span class="lineno"> 198</span>

</div>

<div class="line">

<span id="l00203"></span><span class="lineno"> [203](structfranky_1_1_robot_state.md#aae25b9bee828132b2db5a669855bf16a)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [q\_d](structfranky_1_1_robot_state.md#aae25b9bee828132b2db5a669855bf16a){};

</div>

<div class="line">

<span id="l00204"></span><span class="lineno"> 204</span>

</div>

<div class="line">

<span id="l00209"></span><span class="lineno"> [209](structfranky_1_1_robot_state.md#ae63f90261417b37a6c731076ce4d5cc6)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [dq](structfranky_1_1_robot_state.md#ae63f90261417b37a6c731076ce4d5cc6){};

</div>

<div class="line">

<span id="l00210"></span><span class="lineno"> 210</span>

</div>

<div class="line">

<span id="l00215"></span><span class="lineno"> [215](structfranky_1_1_robot_state.md#a3712f4da986dac8f09fa2af356a81fb9)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [dq\_d](structfranky_1_1_robot_state.md#a3712f4da986dac8f09fa2af356a81fb9){};

</div>

<div class="line">

<span id="l00216"></span><span class="lineno"> 216</span>

</div>

<div class="line">

<span id="l00221"></span><span class="lineno"> [221](structfranky_1_1_robot_state.md#aadf8644c962475b364279719d4d4109f)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [ddq\_d](structfranky_1_1_robot_state.md#aadf8644c962475b364279719d4d4109f){};

</div>

<div class="line">

<span id="l00222"></span><span class="lineno"> 222</span>

</div>

<div class="line">

<span id="l00229"></span><span class="lineno"> [229](structfranky_1_1_robot_state.md#a2e51845f6d79feb2df6069812549c708)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [joint\_contact](structfranky_1_1_robot_state.md#a2e51845f6d79feb2df6069812549c708){};

</div>

<div class="line">

<span id="l00230"></span><span class="lineno"> 230</span>

</div>

<div class="line">

<span id="l00237"></span><span class="lineno"> [237](structfranky_1_1_robot_state.md#a4ea218cbe444c02ba65c9e2f2d9fb9f0)</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [cartesian\_contact](structfranky_1_1_robot_state.md#a4ea218cbe444c02ba65c9e2f2d9fb9f0){};

</div>

<div class="line">

<span id="l00238"></span><span class="lineno"> 238</span>

</div>

<div class="line">

<span id="l00247"></span><span class="lineno"> [247](structfranky_1_1_robot_state.md#a72895f75e936aa0ff27597cac3875be3)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [joint\_collision](structfranky_1_1_robot_state.md#a72895f75e936aa0ff27597cac3875be3){};

</div>

<div class="line">

<span id="l00248"></span><span class="lineno"> 248</span>

</div>

<div class="line">

<span id="l00258"></span><span class="lineno"> [258](structfranky_1_1_robot_state.md#a7a4b2dc3fd3c5bd534b77c7ff2c44a6d)</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [cartesian\_collision](structfranky_1_1_robot_state.md#a7a4b2dc3fd3c5bd534b77c7ff2c44a6d){};

</div>

<div class="line">

<span id="l00259"></span><span class="lineno"> 259</span>

</div>

<div class="line">

<span id="l00267"></span><span class="lineno"> [267](structfranky_1_1_robot_state.md#a255794f19c19cb60741ff2e1a3da3410)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [tau\_ext\_hat\_filtered](structfranky_1_1_robot_state.md#a255794f19c19cb60741ff2e1a3da3410){};

</div>

<div class="line">

<span id="l00268"></span><span class="lineno"> 268</span>

</div>

<div class="line">

<span id="l00278"></span><span class="lineno"> [278](structfranky_1_1_robot_state.md#acac3a6e1b9e7f6e19c19aa5df3740b1c)</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [O\_F\_ext\_hat\_K](structfranky_1_1_robot_state.md#acac3a6e1b9e7f6e19c19aa5df3740b1c){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00279"></span><span class="lineno"> 279</span>

</div>

<div class="line">

<span id="l00289"></span><span class="lineno"> [289](structfranky_1_1_robot_state.md#a1d9419d22b2d3126f4c96b64740079e0)</span> [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) [K\_F\_ext\_hat\_K](structfranky_1_1_robot_state.md#a1d9419d22b2d3126f4c96b64740079e0){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00290"></span><span class="lineno"> 290</span>

</div>

<div class="line">

<span id="l00297"></span><span class="lineno"> [297](structfranky_1_1_robot_state.md#aa4d24e043152f36d3ad2c3d55e0a0eac)</span> [Twist](classfranky_1_1_twist.md) [O\_dP\_EE\_d](structfranky_1_1_robot_state.md#aa4d24e043152f36d3ad2c3d55e0a0eac){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00298"></span><span class="lineno"> 298</span>

</div>

<div class="line">

<span id="l00299"></span><span class="lineno"> 299</span><span class="preprocessor">\#ifdef FRANKA\_0\_9</span>

</div>

<div class="line">

<span id="l00308"></span><span class="lineno"> 308</span> Eigen::Vector3d [O\_ddP\_O](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00309"></span><span class="lineno"> 309</span><span class="preprocessor">\#endif</span>

</div>

<div class="line">

<span id="l00310"></span><span class="lineno"> 310</span>

</div>

<div class="line">

<span id="l00316"></span><span class="lineno"> [316](structfranky_1_1_robot_state.md#aebb25f8a7c0e6b72f2a5f1829a97ea43)</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [O\_T\_EE\_c](structfranky_1_1_robot_state.md#aebb25f8a7c0e6b72f2a5f1829a97ea43){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00317"></span><span class="lineno"> 317</span>

</div>

<div class="line">

<span id="l00322"></span><span class="lineno"> [322](structfranky_1_1_robot_state.md#aa67ffe8b93078f07f4a3b36bb00650ad)</span> [Twist](classfranky_1_1_twist.md) [O\_dP\_EE\_c](structfranky_1_1_robot_state.md#aa67ffe8b93078f07f4a3b36bb00650ad){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00323"></span><span class="lineno"> 323</span>

</div>

<div class="line">

<span id="l00330"></span><span class="lineno"> [330](structfranky_1_1_robot_state.md#a3856ba38e33b30a04b7cca16509debde)</span> [TwistAcceleration](classfranky_1_1_twist_acceleration.md) [O\_ddP\_EE\_c](structfranky_1_1_robot_state.md#a3856ba38e33b30a04b7cca16509debde){}; <span class="comment">// NOLINT(readability-identifier-naming)</span>

</div>

<div class="line">

<span id="l00331"></span><span class="lineno"> 331</span>

</div>

<div class="line">

<span id="l00336"></span><span class="lineno"> [336](structfranky_1_1_robot_state.md#a87a42865d626b106dd186d3886489318)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [theta](structfranky_1_1_robot_state.md#a87a42865d626b106dd186d3886489318){};

</div>

<div class="line">

<span id="l00337"></span><span class="lineno"> 337</span>

</div>

<div class="line">

<span id="l00342"></span><span class="lineno"> [342](structfranky_1_1_robot_state.md#a80fbf260b9bbb1d9df330522b2f76568)</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [dtheta](structfranky_1_1_robot_state.md#a80fbf260b9bbb1d9df330522b2f76568){};

</div>

<div class="line">

<span id="l00343"></span><span class="lineno"> 343</span>

</div>

<div class="line">

<span id="l00347"></span><span class="lineno"> [347](structfranky_1_1_robot_state.md#af874b62c9e403d0c2e581aab20bebb4d)</span> franka::Errors [current\_errors](structfranky_1_1_robot_state.md#af874b62c9e403d0c2e581aab20bebb4d){};

</div>

<div class="line">

<span id="l00348"></span><span class="lineno"> 348</span>

</div>

<div class="line">

<span id="l00352"></span><span class="lineno"> [352](structfranky_1_1_robot_state.md#a01699ef2bcc0ac7126882755477c8cc4)</span> franka::Errors [last\_motion\_errors](structfranky_1_1_robot_state.md#a01699ef2bcc0ac7126882755477c8cc4){};

</div>

<div class="line">

<span id="l00353"></span><span class="lineno"> 353</span>

</div>

<div class="line">

<span id="l00363"></span><span class="lineno"> [363](structfranky_1_1_robot_state.md#a9f615eac9283d889c0b4dfe2a4ecc5c5)</span> <span class="keywordtype">double</span> [control\_command\_success\_rate](structfranky_1_1_robot_state.md#a9f615eac9283d889c0b4dfe2a4ecc5c5){};

</div>

<div class="line">

<span id="l00364"></span><span class="lineno"> 364</span>

</div>

<div class="line">

<span id="l00368"></span><span class="lineno"> [368](structfranky_1_1_robot_state.md#ab2f6b32a306b39eed3170abe1b44a2d8)</span> franka::RobotMode [robot\_mode](structfranky_1_1_robot_state.md#ab2f6b32a306b39eed3170abe1b44a2d8) = franka::RobotMode::kUserStopped;

</div>

<div class="line">

<span id="l00369"></span><span class="lineno"> 369</span>

</div>

<div class="line">

<span id="l00376"></span><span class="lineno"> [376](structfranky_1_1_robot_state.md#a9b00abaf922d5e0ce79ba8b9296840a6)</span> franka::Duration [time](structfranky_1_1_robot_state.md#a9b00abaf922d5e0ce79ba8b9296840a6){};

</div>

<div class="line">

<span id="l00377"></span><span class="lineno"> 377</span>

</div>

<div class="line">

<span id="l00382"></span><span class="lineno"> [382](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6)</span> std::optional\<Vector7d\> [q\_est](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6){};

</div>

<div class="line">

<span id="l00383"></span><span class="lineno"> 383</span>

</div>

<div class="line">

<span id="l00388"></span><span class="lineno"> [388](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e)</span> std::optional\<Vector7d\> [dq\_est](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e){};

</div>

<div class="line">

<span id="l00389"></span><span class="lineno"> 389</span>

</div>

<div class="line">

<span id="l00394"></span><span class="lineno"> [394](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c)</span> std::optional\<Vector7d\> [ddq\_est](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c){};

</div>

<div class="line">

<span id="l00395"></span><span class="lineno"> 395</span>

</div>

<div class="line">

<span id="l00402"></span><span class="lineno"> [402](structfranky_1_1_robot_state.md#aa05402a790846ad287e136b0364359c6)</span> std::optional\<Twist\> [O\_dP\_EE\_est](structfranky_1_1_robot_state.md#aa05402a790846ad287e136b0364359c6){};

</div>

<div class="line">

<span id="l00403"></span><span class="lineno"> 403</span>

</div>

<div class="line">

<span id="l00411"></span><span class="lineno"> [411](structfranky_1_1_robot_state.md#a3a35fa21dfce2110e06f3b2476f9734e)</span> std::optional\<TwistAcceleration\> [O\_ddP\_EE\_est](structfranky_1_1_robot_state.md#a3a35fa21dfce2110e06f3b2476f9734e){};

</div>

<div class="line">

<span id="l00412"></span><span class="lineno"> 412</span>

</div>

<div class="line">

<span id="l00418"></span><span class="lineno"> [418](structfranky_1_1_robot_state.md#acd1c492bd7f6e10b9ecff6cc509d2f90)</span> std::optional\<double\> [delbow\_est](structfranky_1_1_robot_state.md#acd1c492bd7f6e10b9ecff6cc509d2f90){};

</div>

<div class="line">

<span id="l00419"></span><span class="lineno"> 419</span>

</div>

<div class="line">

<span id="l00424"></span><span class="lineno"> [424](structfranky_1_1_robot_state.md#ade3beb0d2a00728a316b43c1a6c15229)</span> std::optional\<double\> [ddelbow\_est](structfranky_1_1_robot_state.md#ade3beb0d2a00728a316b43c1a6c15229){};

</div>

<div class="line">

<span id="l00425"></span><span class="lineno"> 425</span>};

</div>

</div>

<div class="line">

<span id="l00426"></span><span class="lineno"> 426</span>

</div>

<div class="line">

<span id="l00427"></span><span class="lineno"> 427</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_twist_html" class="ttc">

<div class="ttname">

[franky::Twist](classfranky_1_1_twist.md)

</div>

<div class="ttdoc">

Twist of a frame.

</div>

<div class="ttdef">

**Definition** twist.hpp:13

</div>

</div>

<div id="aelbow__state_8hpp_html" class="ttc">

<div class="ttname">

[elbow\_state.hpp](elbow__state_8hpp.md)

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

<div id="astructfranky_1_1_robot_state_html_a01699ef2bcc0ac7126882755477c8cc4" class="ttc">

<div class="ttname">

[franky::RobotState::last\_motion\_errors](structfranky_1_1_robot_state.md#a01699ef2bcc0ac7126882755477c8cc4)

</div>

<div class="ttdeci">

franka::Errors last\_motion\_errors

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:352

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a0a9667e0d76a3901c0e9393a8b227c0a" class="ttc">

<div class="ttname">

[franky::RobotState::O\_T\_EE](structfranky_1_1_robot_state.md#a0a9667e0d76a3901c0e9393a8b227c0a)

</div>

<div class="ttdeci">

Affine O\_T\_EE

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:38

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a1d9419d22b2d3126f4c96b64740079e0" class="ttc">

<div class="ttname">

[franky::RobotState::K\_F\_ext\_hat\_K](structfranky_1_1_robot_state.md#a1d9419d22b2d3126f4c96b64740079e0)

</div>

<div class="ttdeci">

Vector6d K\_F\_ext\_hat\_K

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:289

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a255794f19c19cb60741ff2e1a3da3410" class="ttc">

<div class="ttname">

[franky::RobotState::tau\_ext\_hat\_filtered](structfranky_1_1_robot_state.md#a255794f19c19cb60741ff2e1a3da3410)

</div>

<div class="ttdeci">

Vector7d tau\_ext\_hat\_filtered

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:267

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a2c4c90f4eac5e22551d97102452f8055" class="ttc">

<div class="ttname">

[franky::RobotState::from\_franka](structfranky_1_1_robot_state.md#a2c4c90f4eac5e22551d97102452f8055)

</div>

<div class="ttdeci">

static RobotState from\_franka(const franka::RobotState \&robot\_state, std::optional\< Vector7d \> q\_est=std::nullopt, std::optional\< Vector7d \> dq\_est=std::nullopt, std::optional\< Vector7d \> ddq\_est=std::nullopt, std::optional\< Twist \> O\_dP\_EE\_est=std::nullopt, std::optional\< TwistAcceleration \> O\_ddP\_EE\_est=std::nullopt, std::optional\< double \> delbow\_est=std::nullopt, std::optional\< double \> ddelbow\_est=std::nullopt)

</div>

<div class="ttdef">

**Definition** robot\_state.cpp:7

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a2e51845f6d79feb2df6069812549c708" class="ttc">

<div class="ttname">

[franky::RobotState::joint\_contact](structfranky_1_1_robot_state.md#a2e51845f6d79feb2df6069812549c708)

</div>

<div class="ttdeci">

Vector7d joint\_contact

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:229

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a32d78a9f6048cdce9f096e2a33b747f1" class="ttc">

<div class="ttname">

[franky::RobotState::F\_x\_Cee](structfranky_1_1_robot_state.md#a32d78a9f6048cdce9f096e2a33b747f1)

</div>

<div class="ttdeci">

Eigen::Vector3d F\_x\_Cee

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:106

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a34a1ba1681f87b6f35061f9595eba3f6" class="ttc">

<div class="ttname">

[franky::RobotState::q\_est](structfranky_1_1_robot_state.md#a34a1ba1681f87b6f35061f9595eba3f6)

</div>

<div class="ttdeci">

std::optional\< Vector7d \> q\_est

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:382

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a3706cdbd18abaad5acae4b6420c6679c" class="ttc">

<div class="ttname">

[franky::RobotState::F\_x\_Ctotal](structfranky_1_1_robot_state.md#a3706cdbd18abaad5acae4b6420c6679c)

</div>

<div class="ttdeci">

Eigen::Vector3d F\_x\_Ctotal

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:146

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a3712f4da986dac8f09fa2af356a81fb9" class="ttc">

<div class="ttname">

[franky::RobotState::dq\_d](structfranky_1_1_robot_state.md#a3712f4da986dac8f09fa2af356a81fb9)

</div>

<div class="ttdeci">

Vector7d dq\_d

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:215

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a3856ba38e33b30a04b7cca16509debde" class="ttc">

<div class="ttname">

[franky::RobotState::O\_ddP\_EE\_c](structfranky_1_1_robot_state.md#a3856ba38e33b30a04b7cca16509debde)

</div>

<div class="ttdeci">

TwistAcceleration O\_ddP\_EE\_c

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:330

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a3a35fa21dfce2110e06f3b2476f9734e" class="ttc">

<div class="ttname">

[franky::RobotState::O\_ddP\_EE\_est](structfranky_1_1_robot_state.md#a3a35fa21dfce2110e06f3b2476f9734e)

</div>

<div class="ttdeci">

std::optional\< TwistAcceleration \> O\_ddP\_EE\_est

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:411

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a3a38c0c7040b305f2d00c2388e0e451c" class="ttc">

<div class="ttname">

[franky::RobotState::delbow\_c](structfranky_1_1_robot_state.md#a3a38c0c7040b305f2d00c2388e0e451c)

</div>

<div class="ttdeci">

double delbow\_c

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:166

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a4ea218cbe444c02ba65c9e2f2d9fb9f0" class="ttc">

<div class="ttname">

[franky::RobotState::cartesian\_contact](structfranky_1_1_robot_state.md#a4ea218cbe444c02ba65c9e2f2d9fb9f0)

</div>

<div class="ttdeci">

Vector6d cartesian\_contact

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:237

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a5bab6bd3d0b8e3781b80db887808be1e" class="ttc">

<div class="ttname">

[franky::RobotState::EE\_T\_K](structfranky_1_1_robot_state.md#a5bab6bd3d0b8e3781b80db887808be1e)

</div>

<div class="ttdeci">

Affine EE\_T\_K

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:86

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a627a19dfeb245fe9929b5dba0de4516b" class="ttc">

<div class="ttname">

[franky::RobotState::I\_total](structfranky_1_1_robot_state.md#a627a19dfeb245fe9929b5dba0de4516b)

</div>

<div class="ttdeci">

IntertiaMatrix I\_total

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:139

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a662a010406b9d9833673f5b84238abe7" class="ttc">

<div class="ttname">

[franky::RobotState::tau\_J\_d](structfranky_1_1_robot_state.md#a662a010406b9d9833673f5b84238abe7)

</div>

<div class="ttdeci">

Vector7d tau\_J\_d

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:184

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a69e433ddee972b5b751233b99a6643e9" class="ttc">

<div class="ttname">

[franky::RobotState::elbow\_c](structfranky_1_1_robot_state.md#a69e433ddee972b5b751233b99a6643e9)

</div>

<div class="ttdeci">

ElbowState elbow\_c

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:161

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a72895f75e936aa0ff27597cac3875be3" class="ttc">

<div class="ttname">

[franky::RobotState::joint\_collision](structfranky_1_1_robot_state.md#a72895f75e936aa0ff27597cac3875be3)

</div>

<div class="ttdeci">

Vector7d joint\_collision

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:247

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a7691ba4f68ee2c2c88138faa319156f5" class="ttc">

<div class="ttname">

[franky::RobotState::dtau\_J](structfranky_1_1_robot_state.md#a7691ba4f68ee2c2c88138faa319156f5)

</div>

<div class="ttdeci">

Vector7d dtau\_J

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:191

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a7a4b2dc3fd3c5bd534b77c7ff2c44a6d" class="ttc">

<div class="ttname">

[franky::RobotState::cartesian\_collision](structfranky_1_1_robot_state.md#a7a4b2dc3fd3c5bd534b77c7ff2c44a6d)

</div>

<div class="ttdeci">

Vector6d cartesian\_collision

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:258

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a80fbf260b9bbb1d9df330522b2f76568" class="ttc">

<div class="ttname">

[franky::RobotState::dtheta](structfranky_1_1_robot_state.md#a80fbf260b9bbb1d9df330522b2f76568)

</div>

<div class="ttdeci">

Vector7d dtheta

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:342

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a87a42865d626b106dd186d3886489318" class="ttc">

<div class="ttname">

[franky::RobotState::theta](structfranky_1_1_robot_state.md#a87a42865d626b106dd186d3886489318)

</div>

<div class="ttdeci">

Vector7d theta

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:336

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a8e8ddca4a286bfb33aa94bfbafc7666d" class="ttc">

<div class="ttname">

[franky::RobotState::m\_total](structfranky_1_1_robot_state.md#a8e8ddca4a286bfb33aa94bfbafc7666d)

</div>

<div class="ttdeci">

double m\_total

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:132

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a9646c969429e0853722837c950820f44" class="ttc">

<div class="ttname">

[franky::RobotState::I\_ee](structfranky_1_1_robot_state.md#a9646c969429e0853722837c950820f44)

</div>

<div class="ttdeci">

IntertiaMatrix I\_ee

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:99

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a9650368f3c772ed7d46f07f6412b3faf" class="ttc">

<div class="ttname">

[franky::RobotState::O\_T\_EE\_d](structfranky_1_1_robot_state.md#a9650368f3c772ed7d46f07f6412b3faf)

</div>

<div class="ttdeci">

Affine O\_T\_EE\_d

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:45

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a9b00abaf922d5e0ce79ba8b9296840a6" class="ttc">

<div class="ttname">

[franky::RobotState::time](structfranky_1_1_robot_state.md#a9b00abaf922d5e0ce79ba8b9296840a6)

</div>

<div class="ttdeci">

franka::Duration time

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:376

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_a9f615eac9283d889c0b4dfe2a4ecc5c5" class="ttc">

<div class="ttname">

[franky::RobotState::control\_command\_success\_rate](structfranky_1_1_robot_state.md#a9f615eac9283d889c0b4dfe2a4ecc5c5)

</div>

<div class="ttdeci">

double control\_command\_success\_rate

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:363

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa05402a790846ad287e136b0364359c6" class="ttc">

<div class="ttname">

[franky::RobotState::O\_dP\_EE\_est](structfranky_1_1_robot_state.md#aa05402a790846ad287e136b0364359c6)

</div>

<div class="ttdeci">

std::optional\< Twist \> O\_dP\_EE\_est

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:402

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa1d327630a6eedc9b3bbad3b5d7423b3" class="ttc">

<div class="ttname">

[franky::RobotState::tau\_J](structfranky_1_1_robot_state.md#aa1d327630a6eedc9b3bbad3b5d7423b3)

</div>

<div class="ttdeci">

Vector7d tau\_J

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:177

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa2f851078b2a03f90c33a37bf13d07a1" class="ttc">

<div class="ttname">

[franky::RobotState::F\_T\_EE](structfranky_1_1_robot_state.md#aa2f851078b2a03f90c33a37bf13d07a1)

</div>

<div class="ttdeci">

Affine F\_T\_EE

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:55

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa3c4c83ad4b4a704665db984ebadd84c" class="ttc">

<div class="ttname">

[franky::RobotState::ddq\_est](structfranky_1_1_robot_state.md#aa3c4c83ad4b4a704665db984ebadd84c)

</div>

<div class="ttdeci">

std::optional\< Vector7d \> ddq\_est

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:394

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa4d24e043152f36d3ad2c3d55e0a0eac" class="ttc">

<div class="ttname">

[franky::RobotState::O\_dP\_EE\_d](structfranky_1_1_robot_state.md#aa4d24e043152f36d3ad2c3d55e0a0eac)

</div>

<div class="ttdeci">

Twist O\_dP\_EE\_d

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:297

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa5104cf1e290f362c032dd3099191bd8" class="ttc">

<div class="ttname">

[franky::RobotState::m\_ee](structfranky_1_1_robot_state.md#aa5104cf1e290f362c032dd3099191bd8)

</div>

<div class="ttdeci">

double m\_ee

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:92

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa67ffe8b93078f07f4a3b36bb00650ad" class="ttc">

<div class="ttname">

[franky::RobotState::O\_dP\_EE\_c](structfranky_1_1_robot_state.md#aa67ffe8b93078f07f4a3b36bb00650ad)

</div>

<div class="ttdeci">

Twist O\_dP\_EE\_c

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:322

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aa7c69937e5e9837d62b490dcc8aa255f" class="ttc">

<div class="ttname">

[franky::RobotState::elbow\_d](structfranky_1_1_robot_state.md#aa7c69937e5e9837d62b490dcc8aa255f)

</div>

<div class="ttdeci">

ElbowState elbow\_d

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:156

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aabafb74fb3a4c958ec20d1c944a58ef1" class="ttc">

<div class="ttname">

[franky::RobotState::elbow](structfranky_1_1_robot_state.md#aabafb74fb3a4c958ec20d1c944a58ef1)

</div>

<div class="ttdeci">

ElbowState elbow

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:151

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aadf8644c962475b364279719d4d4109f" class="ttc">

<div class="ttname">

[franky::RobotState::ddq\_d](structfranky_1_1_robot_state.md#aadf8644c962475b364279719d4d4109f)

</div>

<div class="ttdeci">

Vector7d ddq\_d

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:221

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aae25b9bee828132b2db5a669855bf16a" class="ttc">

<div class="ttname">

[franky::RobotState::q\_d](structfranky_1_1_robot_state.md#aae25b9bee828132b2db5a669855bf16a)

</div>

<div class="ttdeci">

Vector7d q\_d

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:203

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aaea1aa7f342609aa0d8b4e917bf2c47e" class="ttc">

<div class="ttname">

[franky::RobotState::dq\_est](structfranky_1_1_robot_state.md#aaea1aa7f342609aa0d8b4e917bf2c47e)

</div>

<div class="ttdeci">

std::optional\< Vector7d \> dq\_est

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:388

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_ab2f6b32a306b39eed3170abe1b44a2d8" class="ttc">

<div class="ttname">

[franky::RobotState::robot\_mode](structfranky_1_1_robot_state.md#ab2f6b32a306b39eed3170abe1b44a2d8)

</div>

<div class="ttdeci">

franka::RobotMode robot\_mode

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:368

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_ab6996c44d6d0b34e03cec086d6d16519" class="ttc">

<div class="ttname">

[franky::RobotState::ddelbow\_c](structfranky_1_1_robot_state.md#ab6996c44d6d0b34e03cec086d6d16519)

</div>

<div class="ttdeci">

double ddelbow\_c

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:171

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_abbbebbf039f73e41d26193f5acebf536" class="ttc">

<div class="ttname">

[franky::RobotState::F\_x\_Cload](structfranky_1_1_robot_state.md#abbbebbf039f73e41d26193f5acebf536)

</div>

<div class="ttdeci">

Eigen::Vector3d F\_x\_Cload

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:126

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_ac7f17c8d7d1bb49658c872904caa8233" class="ttc">

<div class="ttname">

[franky::RobotState::m\_load](structfranky_1_1_robot_state.md#ac7f17c8d7d1bb49658c872904caa8233)

</div>

<div class="ttdeci">

double m\_load

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:112

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_acac3a6e1b9e7f6e19c19aa5df3740b1c" class="ttc">

<div class="ttname">

[franky::RobotState::O\_F\_ext\_hat\_K](structfranky_1_1_robot_state.md#acac3a6e1b9e7f6e19c19aa5df3740b1c)

</div>

<div class="ttdeci">

Vector6d O\_F\_ext\_hat\_K

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:278

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_acd1c492bd7f6e10b9ecff6cc509d2f90" class="ttc">

<div class="ttname">

[franky::RobotState::delbow\_est](structfranky_1_1_robot_state.md#acd1c492bd7f6e10b9ecff6cc509d2f90)

</div>

<div class="ttdeci">

std::optional\< double \> delbow\_est

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:418

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_ad8590b96b51241bea2620dcc482c0f9a" class="ttc">

<div class="ttname">

[franky::RobotState::I\_load](structfranky_1_1_robot_state.md#ad8590b96b51241bea2620dcc482c0f9a)

</div>

<div class="ttdeci">

IntertiaMatrix I\_load

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:119

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_adcba9f6e06d0161ee6ec2bb904e2f1cd" class="ttc">

<div class="ttname">

[franky::RobotState::q](structfranky_1_1_robot_state.md#adcba9f6e06d0161ee6ec2bb904e2f1cd)

</div>

<div class="ttdeci">

Vector7d q

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:197

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_ade3beb0d2a00728a316b43c1a6c15229" class="ttc">

<div class="ttname">

[franky::RobotState::ddelbow\_est](structfranky_1_1_robot_state.md#ade3beb0d2a00728a316b43c1a6c15229)

</div>

<div class="ttdeci">

std::optional\< double \> ddelbow\_est

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:424

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_ae63f90261417b37a6c731076ce4d5cc6" class="ttc">

<div class="ttname">

[franky::RobotState::dq](structfranky_1_1_robot_state.md#ae63f90261417b37a6c731076ce4d5cc6)

</div>

<div class="ttdeci">

Vector7d dq

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:209

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_aebb25f8a7c0e6b72f2a5f1829a97ea43" class="ttc">

<div class="ttname">

[franky::RobotState::O\_T\_EE\_c](structfranky_1_1_robot_state.md#aebb25f8a7c0e6b72f2a5f1829a97ea43)

</div>

<div class="ttdeci">

Affine O\_T\_EE\_c

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:316

</div>

</div>

<div id="astructfranky_1_1_robot_state_html_af874b62c9e403d0c2e581aab20bebb4d" class="ttc">

<div class="ttname">

[franky::RobotState::current\_errors](structfranky_1_1_robot_state.md#af874b62c9e403d0c2e581aab20bebb4d)

</div>

<div class="ttdeci">

franka::Errors current\_errors

</div>

<div class="ttdef">

**Definition** robot\_state.hpp:347

</div>

</div>

<div id="atwist_8hpp_html" class="ttc">

<div class="ttname">

[twist.hpp](twist_8hpp.md)

</div>

</div>

<div id="atwist__acceleration_8hpp_html" class="ttc">

<div class="ttname">

[twist\_acceleration.hpp](twist__acceleration_8hpp.md)

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
