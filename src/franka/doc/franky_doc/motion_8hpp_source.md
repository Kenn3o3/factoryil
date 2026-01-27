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

motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<list\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<mutex\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/robot.hpp](robot_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/robot\_state.hpp](robot__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[reaction.hpp](reaction_8hpp.md)"</span>

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

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="keyword">class </span>Robot;

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span><span class="keyword">class </span>Reaction;

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span>

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div id="foldopen00024" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00024"></span><span class="lineno"> [24](classfranky_1_1_motion.md)</span><span class="keyword">class </span>[Motion](classfranky_1_1_motion.md) {

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> [26](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16)</span> <span class="keyword">virtual</span> [\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16)() = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> [27](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c)</span> <span class="keyword">using </span>[CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) = std::function\<void(

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration, franka::Duration, <span class="keyword">const</span> [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) &)\>;

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span>

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span> <span class="keywordtype">void</span> [addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448)(std::shared\_ptr\<[Reaction\<ControlSignalType\>](classfranky_1_1_reaction.md)\> reaction);

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span>

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span> <span class="keywordtype">void</span> [addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347)(std::shared\_ptr\<[Reaction\<ControlSignalType\>](classfranky_1_1_reaction.md)\> reaction);

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span>

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span> std::vector\<std::shared\_ptr\<Reaction\<ControlSignalType\>\>\> [reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d)();

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span>

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> <span class="keywordtype">void</span> [registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2)([CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) callback);

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span> <span class="keywordtype">void</span> [init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6)([Robot](classfranky_1_1_robot.md) \*[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f), <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<ControlSignalType\> \&previous\_command);

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span>

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) [nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7)(

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time,

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span> <span class="keyword">const</span> std::optional\<ControlSignalType\> \&previous\_command);

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span>

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span> std::shared\_ptr\<Motion\<ControlSignalType\>\> [checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369)(

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time);

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span>

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> 92</span> <span class="keyword">protected</span>:

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> 93</span> <span class="keyword">explicit</span> [Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4)();

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span>

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> [95](classfranky_1_1_motion.md#ad11b300fa7c37e18403af6a17bf663b8)</span> <span class="keyword">virtual</span> <span class="keywordtype">void</span> [initImpl](classfranky_1_1_motion.md#ad11b300fa7c37e18403af6a17bf663b8)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<ControlSignalType\> \&previous\_command) {}

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> 96</span>

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> [97](classfranky_1_1_motion.md#ad2e6f47d30089ee335fecb671618a5f6)</span> <span class="keyword">virtual</span> [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) [nextCommandImpl](classfranky_1_1_motion.md#ad2e6f47d30089ee335fecb671618a5f6)(

</div>

<div class="line">

<span id="l00098"></span><span class="lineno"> 98</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time,

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span> <span class="keyword">const</span> std::optional\<ControlSignalType\> \&previous\_command) = 0;

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span>

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> [101](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)</span> \[\[nodiscard\]\] [Robot](classfranky_1_1_robot.md) \*[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> robot\_; }

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> 102</span>

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> 103</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> 104</span> std::mutex reaction\_mutex\_;

</div>

<div class="line">

<span id="l00105"></span><span class="lineno"> 105</span> std::list\<std::shared\_ptr\<Reaction\<ControlSignalType\>\>\> reactions\_;

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> 106</span> std::mutex callback\_mutex\_;

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span> std::vector\<CallbackType\> callbacks\_;

</div>

<div class="line">

<span id="l00108"></span><span class="lineno"> 108</span> [Robot](classfranky_1_1_robot.md) \*robot\_;

</div>

<div class="line">

<span id="l00109"></span><span class="lineno"> 109</span>};

</div>

</div>

<div class="line">

<span id="l00110"></span><span class="lineno"> 110</span>

</div>

<div class="line">

<span id="l00111"></span><span class="lineno"> 111</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_motion_html_a05ed2a4f6dbcd406f9298a7c8e4e76c2" class="ttc">

<div class="ttname">

[franky::Motion::registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2)

</div>

<div class="ttdeci">

void registerCallback(CallbackType callback)

</div>

<div class="ttdoc">

Register a callback that is called in every step of the motion.

</div>

<div class="ttdef">

**Definition** motion.cpp:24

</div>

</div>

<div id="aclassfranky_1_1_motion_html_a2a0e78863021c3c2116c8500c9386369" class="ttc">

<div class="ttname">

[franky::Motion::checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369)

</div>

<div class="ttdeci">

std::shared\_ptr\< Motion\< ControlSignalType \> \> checkAndCallReactions(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)

</div>

<div class="ttdoc">

Check and call reactions.

</div>

<div class="ttdef">

**Definition** motion.cpp:67

</div>

</div>

<div id="aclassfranky_1_1_motion_html_a3780f86a0c58bdfb959e4d9bb65179d6" class="ttc">

<div class="ttname">

[franky::Motion::init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6)

</div>

<div class="ttdeci">

void init(Robot \*robot, const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command)

</div>

<div class="ttdoc">

Initialize the motion.

</div>

<div class="ttdef">

**Definition** motion.cpp:50

</div>

</div>

<div id="aclassfranky_1_1_motion_html_a4a279dafcbb7ae10605f58d27a3a368f" class="ttc">

<div class="ttname">

[franky::Motion::robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)

</div>

<div class="ttdeci">

Robot \* robot() const

</div>

<div class="ttdef">

**Definition** motion.hpp:101

</div>

</div>

<div id="aclassfranky_1_1_motion_html_a52f0efb3e6c876f480eceb75a18d7448" class="ttc">

<div class="ttname">

[franky::Motion::addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448)

</div>

<div class="ttdeci">

void addReaction(std::shared\_ptr\< Reaction\< ControlSignalType \> \> reaction)

</div>

<div class="ttdoc">

Add a reaction to the motion.

</div>

<div class="ttdef">

**Definition** motion.cpp:30

</div>

</div>

<div id="aclassfranky_1_1_motion_html_a8fdbf32e0808fb2f01514f83ee964347" class="ttc">

<div class="ttname">

[franky::Motion::addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347)

</div>

<div class="ttdeci">

void addReactionFront(std::shared\_ptr\< Reaction\< ControlSignalType \> \> reaction)

</div>

<div class="ttdoc">

Add a reaction to the front of the reaction list.

</div>

<div class="ttdef">

**Definition** motion.cpp:37

</div>

</div>

<div id="aclassfranky_1_1_motion_html_aa6d72b7a606055fc444bf2da0c463d16" class="ttc">

<div class="ttname">

[franky::Motion::\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16)

</div>

<div class="ttdeci">

virtual \~Motion()=default

</div>

</div>

<div id="aclassfranky_1_1_motion_html_aabc4cfc38ed77466ca94be5b1c38fc6c" class="ttc">

<div class="ttname">

[franky::Motion::CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c)

</div>

<div class="ttdeci">

std::function\< void(const RobotState &, franka::Duration, franka::Duration, franka::Duration, const ControlSignalType &)\> CallbackType

</div>

<div class="ttdef">

**Definition** motion.hpp:28

</div>

</div>

<div id="aclassfranky_1_1_motion_html_ab18f33f97f86e9fb838fb6d6d79915b4" class="ttc">

<div class="ttname">

[franky::Motion::Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4)

</div>

<div class="ttdeci">

Motion()

</div>

<div class="ttdef">

**Definition** motion.cpp:18

</div>

</div>

<div id="aclassfranky_1_1_motion_html_abc04c5fe350635cf36bc1e459736ddb7" class="ttc">

<div class="ttname">

[franky::Motion::nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7)

</div>

<div class="ttdeci">

ControlSignalType nextCommand(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< ControlSignalType \> \&previous\_command)

</div>

<div class="ttdoc">

Get the next command of the motion.

</div>

<div class="ttdef">

**Definition** motion.cpp:57

</div>

</div>

<div id="aclassfranky_1_1_motion_html_ad11b300fa7c37e18403af6a17bf663b8" class="ttc">

<div class="ttname">

[franky::Motion::initImpl](classfranky_1_1_motion.md#ad11b300fa7c37e18403af6a17bf663b8)

</div>

<div class="ttdeci">

virtual void initImpl(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command)

</div>

<div class="ttdef">

**Definition** motion.hpp:95

</div>

</div>

<div id="aclassfranky_1_1_motion_html_ad2e6f47d30089ee335fecb671618a5f6" class="ttc">

<div class="ttname">

[franky::Motion::nextCommandImpl](classfranky_1_1_motion.md#ad2e6f47d30089ee335fecb671618a5f6)

</div>

<div class="ttdeci">

virtual ControlSignalType nextCommandImpl(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< ControlSignalType \> \&previous\_command)=0

</div>

</div>

<div id="aclassfranky_1_1_motion_html_aed40663a195eb68318799d19451c5a0d" class="ttc">

<div class="ttname">

[franky::Motion::reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d)

</div>

<div class="ttdeci">

std::vector\< std::shared\_ptr\< Reaction\< ControlSignalType \> \> \> reactions()

</div>

<div class="ttdoc">

Currently registered reactions of the motion.

</div>

<div class="ttdef">

**Definition** motion.cpp:44

</div>

</div>

<div id="aclassfranky_1_1_reaction_html" class="ttc">

<div class="ttname">

[franky::Reaction](classfranky_1_1_reaction.md)

</div>

<div class="ttdoc">

A reaction that can be attached to a motion.

</div>

<div class="ttdef">

**Definition** reaction.hpp:27

</div>

</div>

<div id="aclassfranky_1_1_robot_html" class="ttc">

<div class="ttname">

[franky::Robot](classfranky_1_1_robot.md)

</div>

<div class="ttdoc">

A class representing a Franka robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:47

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

<div id="areaction_8hpp_html" class="ttc">

<div class="ttname">

[reaction.hpp](reaction_8hpp.md)

</div>

</div>

<div id="arobot_8hpp_html" class="ttc">

<div class="ttname">

[robot.hpp](robot_8hpp.md)

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
