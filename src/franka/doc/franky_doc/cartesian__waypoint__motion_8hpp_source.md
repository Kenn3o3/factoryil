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

cartesian\_waypoint\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](cartesian__waypoint__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/robot\_state.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<atomic\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include \<ruckig/ruckig.hpp\></span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/cartesian\_state.hpp](cartesian__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/motion/position\_waypoint\_motion.hpp](position__waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="preprocessor">\#include "[franky/motion/reference\_type.hpp](reference__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="preprocessor">\#include "[franky/robot.hpp](robot_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span><span class="preprocessor">\#include "[franky/robot\_pose.hpp](robot__pose_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span><span class="preprocessor">\#include "[franky/util.hpp](util_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span>

</div>

<div id="foldopen00024" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00024"></span><span class="lineno"> [24](classfranky_1_1_cartesian_waypoint_motion.md)</span><span class="keyword">class </span>[CartesianWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md) : <span class="keyword">public</span> [PositionWaypointMotion](classfranky_1_1_position_waypoint_motion.md)\<franka::CartesianPose, CartesianState\> {

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span> <span class="keyword">explicit</span> [CartesianWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md)(

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span> <span class="keyword">const</span> std::vector\<[PositionWaypoint\<CartesianState\>](structfranky_1_1_position_waypoint.md)\> \&waypoints,

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span> <span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0, <span class="keywordtype">bool</span> return\_when\_finished = <span class="keyword">true</span>,

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) ee\_frame = Affine::Identity());

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span>

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> <span class="keyword">protected</span>:

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> <span class="keywordtype">void</span> [initWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md#a67c60776f12dc2fcb1254c66f0d6d808)(

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::CartesianPose\> \&previous\_command,

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span>

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keywordtype">void</span> [setNewWaypoint](classfranky_1_1_cartesian_waypoint_motion.md#a70fbc0a8282044cb8a8f55e456196021)(

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> std::optional\<franka::CartesianPose\> \&previous\_command,

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> <span class="keyword">const</span> [PositionWaypoint\<CartesianState\>](structfranky_1_1_position_waypoint.md) \&new\_waypoint, ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span>

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span> \[\[nodiscard\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getAbsoluteInputLimits](classfranky_1_1_cartesian_waypoint_motion.md#a493676502c53be9f6f0acf8a82cb8192)() <span class="keyword">const override</span>;

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span>

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> \[\[nodiscard\]\] franka::CartesianPose [getControlSignal](classfranky_1_1_cartesian_waypoint_motion.md#a563ea191260de928f5ea5e32b33a7bc9)(

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, <span class="keyword">const</span> franka::Duration \&time\_step,

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span> <span class="keyword">const</span> std::optional\<franka::CartesianPose\> \&previous\_command,

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span> <span class="keyword">const</span> ruckig::InputParameter\<7\> \&input\_parameter) <span class="keyword">override</span>;

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span>

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> \[\[nodiscard\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getDesiredState](classfranky_1_1_cartesian_waypoint_motion.md#ac112a00b871d27d4dc45deb6eb0ea917)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state) <span class="keyword">const override</span>;

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span>

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> [CartesianState](classfranky_1_1_cartesian_state.md) target\_state\_;

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) ref\_frame\_;

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) ee\_frame\_;

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span>

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> <span class="keyword">static</span> [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) vec\_cart\_rot\_elbow(<span class="keywordtype">double</span> cart, <span class="keywordtype">double</span> rot, <span class="keywordtype">double</span> elbow) {

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> <span class="keywordflow">return</span> {cart, cart, cart, rot, rot, rot, elbow};

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span> }

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span>};

</div>

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span>

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>} <span class="comment">// namespace franky</span>

</div>

<div id="acartesian__state_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_state.hpp](cartesian__state_8hpp.md)

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html" class="ttc">

<div class="ttname">

[franky::CartesianState](classfranky_1_1_cartesian_state.md)

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:17

</div>

</div>

<div id="aclassfranky_1_1_cartesian_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::CartesianWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md)

</div>

<div class="ttdoc">

Cartesian waypoint motion.

</div>

<div class="ttdef">

**Definition** cartesian\_waypoint\_motion.hpp:24

</div>

</div>

<div id="aclassfranky_1_1_cartesian_waypoint_motion_html_a493676502c53be9f6f0acf8a82cb8192" class="ttc">

<div class="ttname">

[franky::CartesianWaypointMotion::getAbsoluteInputLimits](classfranky_1_1_cartesian_waypoint_motion.md#a493676502c53be9f6f0acf8a82cb8192)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getAbsoluteInputLimits() const override

</div>

<div class="ttdef">

**Definition** cartesian\_waypoint\_motion.cpp:125

</div>

</div>

<div id="aclassfranky_1_1_cartesian_waypoint_motion_html_a563ea191260de928f5ea5e32b33a7bc9" class="ttc">

<div class="ttname">

[franky::CartesianWaypointMotion::getControlSignal](classfranky_1_1_cartesian_waypoint_motion.md#a563ea191260de928f5ea5e32b33a7bc9)

</div>

<div class="ttdeci">

franka::CartesianPose getControlSignal(const RobotState \&robot\_state, const franka::Duration \&time\_step, const std::optional\< franka::CartesianPose \> \&previous\_command, const ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** cartesian\_waypoint\_motion.cpp:41

</div>

</div>

<div id="aclassfranky_1_1_cartesian_waypoint_motion_html_a67c60776f12dc2fcb1254c66f0d6d808" class="ttc">

<div class="ttname">

[franky::CartesianWaypointMotion::initWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md#a67c60776f12dc2fcb1254c66f0d6d808)

</div>

<div class="ttdeci">

void initWaypointMotion(const RobotState \&robot\_state, const std::optional\< franka::CartesianPose \> \&previous\_command, ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** cartesian\_waypoint\_motion.cpp:18

</div>

</div>

<div id="aclassfranky_1_1_cartesian_waypoint_motion_html_a70fbc0a8282044cb8a8f55e456196021" class="ttc">

<div class="ttname">

[franky::CartesianWaypointMotion::setNewWaypoint](classfranky_1_1_cartesian_waypoint_motion.md#a70fbc0a8282044cb8a8f55e456196021)

</div>

<div class="ttdeci">

void setNewWaypoint(const RobotState \&robot\_state, const std::optional\< franka::CartesianPose \> \&previous\_command, const PositionWaypoint\< CartesianState \> \&new\_waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) override

</div>

<div class="ttdef">

**Definition** cartesian\_waypoint\_motion.cpp:53

</div>

</div>

<div id="aclassfranky_1_1_cartesian_waypoint_motion_html_ac112a00b871d27d4dc45deb6eb0ea917" class="ttc">

<div class="ttname">

[franky::CartesianWaypointMotion::getDesiredState](classfranky_1_1_cartesian_waypoint_motion.md#ac112a00b871d27d4dc45deb6eb0ea917)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getDesiredState(const RobotState \&robot\_state) const override

</div>

<div class="ttdef">

**Definition** cartesian\_waypoint\_motion.cpp:137

</div>

</div>

<div id="aclassfranky_1_1_position_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::PositionWaypointMotion](classfranky_1_1_position_waypoint_motion.md)

</div>

<div class="ttdoc">

A motion following multiple positional waypoints in a time-optimal way. Works with arbitrary initial ...

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:33

</div>

</div>

<div id="aclassfranky_1_1_relative_dynamics_factor_html" class="ttc">

<div class="ttname">

[franky::RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md)

</div>

<div class="ttdoc">

Relative dynamics factors.

</div>

<div class="ttdef">

**Definition** relative\_dynamics\_factor.hpp:13

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

<div id="aposition__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[position\_waypoint\_motion.hpp](position__waypoint__motion_8hpp.md)

</div>

</div>

<div id="areference__type_8hpp_html" class="ttc">

<div class="ttname">

[reference\_type.hpp](reference__type_8hpp.md)

</div>

</div>

<div id="arobot_8hpp_html" class="ttc">

<div class="ttname">

[robot.hpp](robot_8hpp.md)

</div>

</div>

<div id="arobot__pose_8hpp_html" class="ttc">

<div class="ttname">

[robot\_pose.hpp](robot__pose_8hpp.md)

</div>

</div>

<div id="astructfranky_1_1_position_waypoint_html" class="ttc">

<div class="ttname">

[franky::PositionWaypoint](structfranky_1_1_position_waypoint.md)

</div>

<div class="ttdoc">

A position waypoint with a target and optional parameters.

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:20

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

<div id="autil_8hpp_html" class="ttc">

<div class="ttname">

[util.hpp](util_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
