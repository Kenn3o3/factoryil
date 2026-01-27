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

gripper.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](gripper_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/exception.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<franka/gripper.h\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<future\></span>

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

<div id="foldopen00013" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00013"></span><span class="lineno"> [13](structfranky_1_1_gripper_exception.md)</span><span class="keyword">struct </span>[GripperException](structfranky_1_1_gripper_exception.md) : <span class="keyword">public</span> std::runtime\_error {

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span> <span class="keyword">using </span>std::runtime\_error::runtime\_error;

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span>};

</div>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span>

</div>

<div id="foldopen00021" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00021"></span><span class="lineno"> [21](classfranky_1_1_gripper.md)</span><span class="keyword">class </span>[Gripper](classfranky_1_1_gripper.md) : <span class="keyword">public</span> franka::Gripper {

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> [23](classfranky_1_1_gripper.md#ad496a52d3a7a01926c8fd6e679901a89)</span> <span class="keyword">explicit</span> [Gripper](classfranky_1_1_gripper.md#ad496a52d3a7a01926c8fd6e679901a89)(<span class="keyword">const</span> std::string \&franka\_address) : franka::[Gripper](classfranky_1_1_gripper.md)(franka\_address) {}

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> [25](classfranky_1_1_gripper.md#ac6996e448e7a780d67682743cd836da9)</span> [Gripper](classfranky_1_1_gripper.md#ac6996e448e7a780d67682743cd836da9)([Gripper](classfranky_1_1_gripper.md) &\&gripper) noexcept : franka::Gripper(std::move(gripper)) {}

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span>

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> std::shared\_future\<bool\> [graspAsync](classfranky_1_1_gripper.md#a39998a7c1c4ea04403e9dc74e2459d5f)(

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> <span class="keywordtype">double</span> [width](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e), <span class="keywordtype">double</span> speed, <span class="keywordtype">double</span> force, <span class="keywordtype">double</span> epsilon\_inner = 0.005, <span class="keywordtype">double</span> epsilon\_outer = 0.005);

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span>

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span> std::shared\_future\<bool\> [moveAsync](classfranky_1_1_gripper.md#a9e8dbe460f5b1cf277ad281906fe8ed7)(<span class="keywordtype">double</span> [width](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e), <span class="keywordtype">double</span> speed);

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span>

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span> <span class="keywordtype">bool</span> [open](classfranky_1_1_gripper.md#a6f9b3b3a14eefe618b480a4e932dce24)(<span class="keywordtype">double</span> speed);

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span>

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> std::shared\_future\<bool\> [openAsync](classfranky_1_1_gripper.md#aa1b54a5041bdc3c8161cd8da895388c6)(<span class="keywordtype">double</span> speed);

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span>

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span> std::shared\_future\<bool\> [homingAsync](classfranky_1_1_gripper.md#af81ac0bf44132f338e43e64d8c10ea7e)();

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> std::shared\_future\<bool\> [stopAsync](classfranky_1_1_gripper.md#aa272b7106a9a5262a0bfc76ed36e002b)();

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> [84](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> <span class="keywordtype">double</span> [width](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> [state](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8)().width; }

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span>

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> [89](classfranky_1_1_gripper.md#a792b6d30ee087a4cddba5e3d2320d6e9)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> <span class="keywordtype">bool</span> [is\_grasped](classfranky_1_1_gripper.md#a792b6d30ee087a4cddba5e3d2320d6e9)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> [state](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8)().is\_grasped; }

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span>

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> [94](classfranky_1_1_gripper.md#a5ae2659a6edf6e117fc461f60191c9db)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> <span class="keywordtype">double</span> [max\_width](classfranky_1_1_gripper.md#a5ae2659a6edf6e117fc461f60191c9db)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> [state](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8)().max\_width; }

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> 95</span>

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> [99](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8)</span> \[\[nodiscard\]\] <span class="keyword">inline</span> franka::GripperState [state](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> readOnce(); }

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span>

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> 101</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> 102</span> std::shared\_future\<bool\> current\_future\_;

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> 103</span>

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> 104</span> std::shared\_future\<bool\> setCurrentFuture(std::future\<bool\> future);

</div>

<div class="line">

<span id="l00105"></span><span class="lineno"> 105</span>};

</div>

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> 106</span>

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_gripper_html" class="ttc">

<div class="ttname">

[franky::Gripper](classfranky_1_1_gripper.md)

</div>

<div class="ttdoc">

A wrapper around the franka::Gripper class that adds asynchronous functionality.

</div>

<div class="ttdef">

**Definition** gripper.hpp:21

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_a176c18c2ca98694075eea1085dc65a7e" class="ttc">

<div class="ttname">

[franky::Gripper::width](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e)

</div>

<div class="ttdeci">

double width() const

</div>

<div class="ttdoc">

Current opening width of the gripper \[m\].

</div>

<div class="ttdef">

**Definition** gripper.hpp:84

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_a39998a7c1c4ea04403e9dc74e2459d5f" class="ttc">

<div class="ttname">

[franky::Gripper::graspAsync](classfranky_1_1_gripper.md#a39998a7c1c4ea04403e9dc74e2459d5f)

</div>

<div class="ttdeci">

std::shared\_future\< bool \> graspAsync(double width, double speed, double force, double epsilon\_inner=0.005, double epsilon\_outer=0.005)

</div>

<div class="ttdoc">

Asynchronous variant of the franka::Gripper::grasp function.

</div>

<div class="ttdef">

**Definition** gripper.cpp:4

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_a5ae2659a6edf6e117fc461f60191c9db" class="ttc">

<div class="ttname">

[franky::Gripper::max\_width](classfranky_1_1_gripper.md#a5ae2659a6edf6e117fc461f60191c9db)

</div>

<div class="ttdeci">

double max\_width() const

</div>

<div class="ttdoc">

Maximum width of the gripper \[m\].

</div>

<div class="ttdef">

**Definition** gripper.hpp:94

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_a6f9b3b3a14eefe618b480a4e932dce24" class="ttc">

<div class="ttname">

[franky::Gripper::open](classfranky_1_1_gripper.md#a6f9b3b3a14eefe618b480a4e932dce24)

</div>

<div class="ttdeci">

bool open(double speed)

</div>

<div class="ttdoc">

Opens the gripper fully.

</div>

<div class="ttdef">

**Definition** gripper.cpp:14

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_a792b6d30ee087a4cddba5e3d2320d6e9" class="ttc">

<div class="ttname">

[franky::Gripper::is\_grasped](classfranky_1_1_gripper.md#a792b6d30ee087a4cddba5e3d2320d6e9)

</div>

<div class="ttdeci">

bool is\_grasped() const

</div>

<div class="ttdoc">

Whether the gripper is grasping.

</div>

<div class="ttdef">

**Definition** gripper.hpp:89

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_a9e8dbe460f5b1cf277ad281906fe8ed7" class="ttc">

<div class="ttname">

[franky::Gripper::moveAsync](classfranky_1_1_gripper.md#a9e8dbe460f5b1cf277ad281906fe8ed7)

</div>

<div class="ttdeci">

std::shared\_future\< bool \> moveAsync(double width, double speed)

</div>

<div class="ttdoc">

Asynchronous variant of the franka::Gripper::move function.

</div>

<div class="ttdef">

**Definition** gripper.cpp:10

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_aa1b54a5041bdc3c8161cd8da895388c6" class="ttc">

<div class="ttname">

[franky::Gripper::openAsync](classfranky_1_1_gripper.md#aa1b54a5041bdc3c8161cd8da895388c6)

</div>

<div class="ttdeci">

std::shared\_future\< bool \> openAsync(double speed)

</div>

<div class="ttdoc">

Asynchronous variant of the open function.

</div>

<div class="ttdef">

**Definition** gripper.cpp:16

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_aa272b7106a9a5262a0bfc76ed36e002b" class="ttc">

<div class="ttname">

[franky::Gripper::stopAsync](classfranky_1_1_gripper.md#aa272b7106a9a5262a0bfc76ed36e002b)

</div>

<div class="ttdeci">

std::shared\_future\< bool \> stopAsync()

</div>

<div class="ttdoc">

Asynchronous variant of the franka::Gripper::stop function.

</div>

<div class="ttdef">

**Definition** gripper.cpp:24

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_abb8531bbdefc46cbd15f36a3ad40b1e8" class="ttc">

<div class="ttname">

[franky::Gripper::state](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8)

</div>

<div class="ttdeci">

franka::GripperState state() const

</div>

<div class="ttdoc">

Current gripper state.

</div>

<div class="ttdef">

**Definition** gripper.hpp:99

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_ac6996e448e7a780d67682743cd836da9" class="ttc">

<div class="ttname">

[franky::Gripper::Gripper](classfranky_1_1_gripper.md#ac6996e448e7a780d67682743cd836da9)

</div>

<div class="ttdeci">

Gripper(Gripper &\&gripper) noexcept

</div>

<div class="ttdef">

**Definition** gripper.hpp:25

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_ad496a52d3a7a01926c8fd6e679901a89" class="ttc">

<div class="ttname">

[franky::Gripper::Gripper](classfranky_1_1_gripper.md#ad496a52d3a7a01926c8fd6e679901a89)

</div>

<div class="ttdeci">

Gripper(const std::string \&franka\_address)

</div>

<div class="ttdef">

**Definition** gripper.hpp:23

</div>

</div>

<div id="aclassfranky_1_1_gripper_html_af81ac0bf44132f338e43e64d8c10ea7e" class="ttc">

<div class="ttname">

[franky::Gripper::homingAsync](classfranky_1_1_gripper.md#af81ac0bf44132f338e43e64d8c10ea7e)

</div>

<div class="ttdeci">

std::shared\_future\< bool \> homingAsync()

</div>

<div class="ttdoc">

Asynchronous variant of the franka::Gripper::homing function.

</div>

<div class="ttdef">

**Definition** gripper.cpp:20

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

<div id="astructfranky_1_1_gripper_exception_html" class="ttc">

<div class="ttname">

[franky::GripperException](structfranky_1_1_gripper_exception.md)

</div>

<div class="ttdoc">

Exception thrown by the gripper class.

</div>

<div class="ttdef">

**Definition** gripper.hpp:13

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
