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

impedance\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](impedance__motion_8hpp.md)

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

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<Eigen/Geometry\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<map\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[franky/motion/motion.hpp](motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/motion/reference\_type.hpp](reference__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/robot\_pose.hpp](robot__pose_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span>

</div>

<div id="foldopen00021" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00021"></span><span class="lineno"> [21](classfranky_1_1_impedance_motion.md)</span><span class="keyword">class </span>[ImpedanceMotion](classfranky_1_1_impedance_motion.md) : <span class="keyword">public</span> [Motion](classfranky_1_1_motion.md)\<franka::Torques\> {

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00026" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00026"></span><span class="lineno"> [26](structfranky_1_1_impedance_motion_1_1_params.md)</span> <span class="keyword">struct </span>[Params](structfranky_1_1_impedance_motion_1_1_params.md) {

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> [28](structfranky_1_1_impedance_motion_1_1_params.md#a38a921916482fa544b8f6583c8f6850f)</span> [ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e) [target\_type](structfranky_1_1_impedance_motion_1_1_params.md#a38a921916482fa544b8f6583c8f6850f){[ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)};

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> [31](structfranky_1_1_impedance_motion_1_1_params.md#a122b129596499ae590225f7b1fe3bfd0)</span> <span class="keywordtype">double</span> [translational\_stiffness](structfranky_1_1_impedance_motion_1_1_params.md#a122b129596499ae590225f7b1fe3bfd0){2000};

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span>

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> [34](structfranky_1_1_impedance_motion_1_1_params.md#afddc6620238e8713fe4e9c3ad507a4cc)</span> <span class="keywordtype">double</span> [rotational\_stiffness](structfranky_1_1_impedance_motion_1_1_params.md#afddc6620238e8713fe4e9c3ad507a4cc){200};

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span>

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> [37](structfranky_1_1_impedance_motion_1_1_params.md#aa83f8133fcb021ce23b1e0bc998d4499)</span> Eigen::Vector\<double, 6\> [force\_constraints](structfranky_1_1_impedance_motion_1_1_params.md#aa83f8133fcb021ce23b1e0bc998d4499);

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span>

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> [40](structfranky_1_1_impedance_motion_1_1_params.md#aaa14fc3684c6a91038cf13a86dd865f9)</span> Eigen::Vector\<bool, 6\> [force\_constraints\_active](structfranky_1_1_impedance_motion_1_1_params.md#aaa14fc3684c6a91038cf13a86dd865f9){Eigen::Vector\<bool, 6\>::Zero()};

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> };

</div>

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span>

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keyword">explicit</span> [ImpedanceMotion](classfranky_1_1_impedance_motion.md)([Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97), <span class="keyword">const</span> Params \&params);

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> <span class="keyword">protected</span>:

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span> <span class="keywordtype">void</span> [initImpl](classfranky_1_1_impedance_motion.md#a87fe10bf698cbc2b55db0a354fa9d250)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::Torques\> \&previous\_command) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span>

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> franka::Torques [nextCommandImpl](classfranky_1_1_impedance_motion.md#a6594ab5628923b88cce26903ae02077c)(

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time,

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span> <span class="keyword">const</span> std::optional\<franka::Torques\> \&previous\_command) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span>

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> [56](classfranky_1_1_impedance_motion.md#aabd59d6e0609d88130d71426324d12e2)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [intermediate\_target](classfranky_1_1_impedance_motion.md#aabd59d6e0609d88130d71426324d12e2)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> intermediate\_target\_; }

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span>

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> [58](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> absolute\_target\_; }

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span>

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> [60](classfranky_1_1_impedance_motion.md#aee9a6e23b63db2ebc49c6615b461189c)</span> <span class="keyword">virtual</span> std::tuple\<Affine, bool\> [update](classfranky_1_1_impedance_motion.md#aee9a6e23b63db2ebc49c6615b461189c)(

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration time\_step, franka::Duration time) = 0;

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span>

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) absolute\_target\_;

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) target\_;

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> [Params](structfranky_1_1_impedance_motion_1_1_params.md) params\_;

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span>

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span> Eigen::Matrix\<double, 6, 6\> stiffness, damping;

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) intermediate\_target\_;

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> std::unique\_ptr\<franka::Model\> model\_;

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span>};

</div>

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span>

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_impedance_motion_html" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)

</div>

<div class="ttdoc">

Base class for client-side cartesian impedance motions.

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:21

</div>

</div>

<div id="aclassfranky_1_1_impedance_motion_html_a1ce961ddf51cd792482fd5ca2b299d97" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97)

</div>

<div class="ttdeci">

Affine target() const

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:58

</div>

</div>

<div id="aclassfranky_1_1_impedance_motion_html_a6594ab5628923b88cce26903ae02077c" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::nextCommandImpl](classfranky_1_1_impedance_motion.md#a6594ab5628923b88cce26903ae02077c)

</div>

<div class="ttdeci">

franka::Torques nextCommandImpl(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< franka::Torques \> \&previous\_command) override

</div>

<div class="ttdef">

**Definition** impedance\_motion.cpp:32

</div>

</div>

<div id="aclassfranky_1_1_impedance_motion_html_a87fe10bf698cbc2b55db0a354fa9d250" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::initImpl](classfranky_1_1_impedance_motion.md#a87fe10bf698cbc2b55db0a354fa9d250)

</div>

<div class="ttdeci">

void initImpl(const RobotState \&robot\_state, const std::optional\< franka::Torques \> \&previous\_command) override

</div>

<div class="ttdef">

**Definition** impedance\_motion.cpp:23

</div>

</div>

<div id="aclassfranky_1_1_impedance_motion_html_aabd59d6e0609d88130d71426324d12e2" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::intermediate\_target](classfranky_1_1_impedance_motion.md#aabd59d6e0609d88130d71426324d12e2)

</div>

<div class="ttdeci">

Affine intermediate\_target() const

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:56

</div>

</div>

<div id="aclassfranky_1_1_impedance_motion_html_aee9a6e23b63db2ebc49c6615b461189c" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::update](classfranky_1_1_impedance_motion.md#aee9a6e23b63db2ebc49c6615b461189c)

</div>

<div class="ttdeci">

virtual std::tuple\< Affine, bool \> update(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration time)=0

</div>

</div>

<div id="aclassfranky_1_1_motion_html" class="ttc">

<div class="ttname">

[franky::Motion](classfranky_1_1_motion.md)

</div>

<div class="ttdoc">

Base class for motions.

</div>

<div class="ttdef">

**Definition** motion.hpp:24

</div>

</div>

<div id="amotion_8hpp_html" class="ttc">

<div class="ttname">

[motion.hpp](motion_8hpp.md)

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

<div id="anamespacefranky_html_a2354a27cfe3100f07e0ad71513ded80e" class="ttc">

<div class="ttname">

[franky::ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e)

</div>

<div class="ttdeci">

ReferenceType

</div>

<div class="ttdoc">

Enum class for reference types.

</div>

<div class="ttdef">

**Definition** reference\_type.hpp:11

</div>

</div>

<div id="anamespacefranky_html_a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a" class="ttc">

<div class="ttname">

[franky::ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)

</div>

<div class="ttdeci">

@ kAbsolute

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

<div id="areference__type_8hpp_html" class="ttc">

<div class="ttname">

[reference\_type.hpp](reference__type_8hpp.md)

</div>

</div>

<div id="arobot__pose_8hpp_html" class="ttc">

<div class="ttname">

[robot\_pose.hpp](robot__pose_8hpp.md)

</div>

</div>

<div id="astructfranky_1_1_impedance_motion_1_1_params_html" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::Params](structfranky_1_1_impedance_motion_1_1_params.md)

</div>

<div class="ttdoc">

Parameters for the impedance motion.

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:26

</div>

</div>

<div id="astructfranky_1_1_impedance_motion_1_1_params_html_a122b129596499ae590225f7b1fe3bfd0" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::Params::translational\_stiffness](structfranky_1_1_impedance_motion_1_1_params.md#a122b129596499ae590225f7b1fe3bfd0)

</div>

<div class="ttdeci">

double translational\_stiffness

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:31

</div>

</div>

<div id="astructfranky_1_1_impedance_motion_1_1_params_html_a38a921916482fa544b8f6583c8f6850f" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::Params::target\_type](structfranky_1_1_impedance_motion_1_1_params.md#a38a921916482fa544b8f6583c8f6850f)

</div>

<div class="ttdeci">

ReferenceType target\_type

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:28

</div>

</div>

<div id="astructfranky_1_1_impedance_motion_1_1_params_html_aa83f8133fcb021ce23b1e0bc998d4499" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::Params::force\_constraints](structfranky_1_1_impedance_motion_1_1_params.md#aa83f8133fcb021ce23b1e0bc998d4499)

</div>

<div class="ttdeci">

Eigen::Vector\< double, 6 \> force\_constraints

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:37

</div>

</div>

<div id="astructfranky_1_1_impedance_motion_1_1_params_html_aaa14fc3684c6a91038cf13a86dd865f9" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::Params::force\_constraints\_active](structfranky_1_1_impedance_motion_1_1_params.md#aaa14fc3684c6a91038cf13a86dd865f9)

</div>

<div class="ttdeci">

Eigen::Vector\< bool, 6 \> force\_constraints\_active

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:40

</div>

</div>

<div id="astructfranky_1_1_impedance_motion_1_1_params_html_afddc6620238e8713fe4e9c3ad507a4cc" class="ttc">

<div class="ttname">

[franky::ImpedanceMotion::Params::rotational\_stiffness](structfranky_1_1_impedance_motion_1_1_params.md#afddc6620238e8713fe4e9c3ad507a4cc)

</div>

<div class="ttdeci">

double rotational\_stiffness

</div>

<div class="ttdef">

**Definition** impedance\_motion.hpp:34

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
