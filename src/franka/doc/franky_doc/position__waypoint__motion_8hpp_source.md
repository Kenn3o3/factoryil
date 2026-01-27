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

position\_waypoint\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](position__waypoint__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<ruckig/ruckig.hpp\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include "[franky/motion/reference\_type.hpp](reference__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/motion/waypoint\_motion.hpp](waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/relative\_dynamics\_factor.hpp](relative__dynamics__factor_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[franky/util.hpp](util_8hpp.md)"</span>

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

<span id="l00019"></span><span class="lineno"> 19</span><span class="keyword">template</span> \<<span class="keyword">typename</span> TargetType\>

</div>

<div id="foldopen00020" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00020"></span><span class="lineno"> [20](structfranky_1_1_position_waypoint.md)</span><span class="keyword">struct </span>[PositionWaypoint](structfranky_1_1_position_waypoint.md) : <span class="keyword">public</span> [Waypoint](structfranky_1_1_waypoint.md)\<TargetType\> {

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> [21](structfranky_1_1_position_waypoint.md#ac5dee69cb4ee3ab71a80cd54244ad220)</span> [ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e) [reference\_type](structfranky_1_1_position_waypoint.md#ac5dee69cb4ee3ab71a80cd54244ad220){[ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)};

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span>};

</div>

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span>

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType, <span class="keyword">typename</span> TargetType\>

</div>

<div id="foldopen00033" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00033"></span><span class="lineno"> [33](classfranky_1_1_position_waypoint_motion.md)</span><span class="keyword">class </span>[PositionWaypointMotion](classfranky_1_1_position_waypoint_motion.md) : <span class="keyword">public</span> [WaypointMotion](classfranky_1_1_waypoint_motion.md)\<ControlSignalType, PositionWaypoint\<TargetType\>, TargetType\> {

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00043" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00043"></span><span class="lineno"> [43](classfranky_1_1_position_waypoint_motion.md#ad5d16a0e7416918355c6110df27a93e4)</span> <span class="keyword">explicit</span> [PositionWaypointMotion](classfranky_1_1_position_waypoint_motion.md#ad5d16a0e7416918355c6110df27a93e4)(

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> std::vector\<[PositionWaypoint\<TargetType\>](structfranky_1_1_position_waypoint.md)\> waypoints, <span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0,

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> <span class="keywordtype">bool</span> return\_when\_finished = <span class="keyword">true</span>)

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span> : [WaypointMotion](classfranky_1_1_waypoint_motion.md)\<[ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac), [PositionWaypoint](structfranky_1_1_position_waypoint.md)\<TargetType\>, TargetType\>(waypoints, return\_when\_finished),

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> relative\_dynamics\_factor\_(relative\_dynamics\_factor) {}

</div>

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> <span class="keyword">protected</span>:

</div>

<div id="foldopen00050" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00050"></span><span class="lineno"> [50](classfranky_1_1_position_waypoint_motion.md#a8ebb35ebb3363acfec93c9228418804a)</span> <span class="keywordtype">void</span> [setInputLimits](classfranky_1_1_position_waypoint_motion.md#a8ebb35ebb3363acfec93c9228418804a)(

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span> <span class="keyword">const</span> [PositionWaypoint\<TargetType\>](structfranky_1_1_position_waypoint.md) \&waypoint, ruckig::InputParameter\<7\> \&input\_parameter)<span class="keyword"> const override </span>{

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> <span class="keyword">auto</span> \[vel\_lim, acc\_lim, jerk\_lim\] = [getAbsoluteInputLimits](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714)();

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span>

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span> <span class="keyword">auto</span> relative\_dynamics\_factor =

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span> waypoint.[relative\_dynamics\_factor](structfranky_1_1_waypoint.md#a88afd539ed0caff485c32cf830e9e121) \* relative\_dynamics\_factor\_ \* this-\>[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)()-\>[relative\_dynamics\_factor](classfranky_1_1_robot.md#a43f2f6dde0cca1f8c21fa6c1fb1b28c0)();

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span>

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span> input\_parameter.max\_velocity = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(relative\_dynamics\_factor.velocity() \* [vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).max\_acceleration = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(relative\_dynamics\_factor.acceleration() \* [acc\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).max\_jerk = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(relative\_dynamics\_factor.jerk() \* [jerk\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> <span class="keywordflow">if</span> (relative\_dynamics\_factor.max\_dynamics()) {

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).synchronization = ruckig::Synchronization::TimeIfNecessary;

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).synchronization = ruckig::Synchronization::Time;

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> <span class="keywordflow">if</span> ([waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).minimum\_time.has\_value()) [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).minimum\_duration = [waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).minimum\_time.value().toSec();

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> }

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span> }

</div>

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span>

</div>

<div id="foldopen00069" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00069"></span><span class="lineno"> [69](classfranky_1_1_position_waypoint_motion.md#a345e479ffc4f38dba2a1128805108e19)</span> <span class="keywordtype">void</span> [extrapolateMotion](classfranky_1_1_position_waypoint_motion.md#a345e479ffc4f38dba2a1128805108e19)(

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> franka::Duration &[time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> <span class="keyword">const</span> ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::OutputParameter\<7\> &[output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const override </span>{

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span> <span class="keyword">auto</span> \[[vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [acc\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [jerk\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = [getAbsoluteInputLimits](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714)();

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span>

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span> <span class="comment">// We use the desired state here as this is likely what the robot uses</span>

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span> <span class="comment">// internally as well</span>

</div>

<div class="line">

<span id="l00076"></span><span class="lineno"> 76</span> <span class="keyword">auto</span> \[[pos\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [acc\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = [getDesiredState](classfranky_1_1_position_waypoint_motion.md#a144c55eb67315d3e260690f2633e9942)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span>

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> <span class="keyword">auto</span> [vel](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [toEigenD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).current\_velocity);

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> <span class="keyword">auto</span> [pos](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [toEigenD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).current\_position);

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span> <span class="keyword">auto</span> [vel\_delta](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [acc\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \* [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).toSec();

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> <span class="keyword">auto</span> [new\_vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = ([vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) + [vel\_delta](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)).[cwiseMin](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)).cwiseMax(-[vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span> <span class="keyword">auto</span> [new\_pos](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [pos](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) + ([vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) + [new\_vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) \* [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).toSec() / 2.0;

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span> <span class="keyword">auto</span> [new\_vel](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = ([vel](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) + [vel\_delta](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)).[cwiseMin](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)).cwiseMax(-[vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span>

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span> <span class="comment">// Franka assumes a constant acceleration model if no new input is received.</span>

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span> <span class="comment">// See https://frankaemika.github.io/docs/libfranka.md\#under-the-hood</span>

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span> [output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).new\_acceleration = [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).current\_acceleration;

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span> [output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).new\_velocity = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([new\_vel](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span> [output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).new\_position = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([new\_pos](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span> }

</div>

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> 92</span>

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> [93](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getAbsoluteInputLimits](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714)() <span class="keyword">const override</span> = 0;

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span>

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> [95](classfranky_1_1_position_waypoint_motion.md#a144c55eb67315d3e260690f2633e9942)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">virtual</span> std::tuple\<Vector7d, Vector7d, Vector7d\> [getDesiredState](classfranky_1_1_position_waypoint_motion.md#a144c55eb67315d3e260690f2633e9942)(

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> 96</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) <span class="keyword">const</span> = 0;

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> 97</span>

</div>

<div class="line">

<span id="l00098"></span><span class="lineno"> 98</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) relative\_dynamics\_factor\_;

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span>};

</div>

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> 101</span>

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> 102</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_position_waypoint_motion_html_a144c55eb67315d3e260690f2633e9942" class="ttc">

<div class="ttname">

[franky::PositionWaypointMotion::getDesiredState](classfranky_1_1_position_waypoint_motion.md#a144c55eb67315d3e260690f2633e9942)

</div>

<div class="ttdeci">

virtual std::tuple\< Vector7d, Vector7d, Vector7d \> getDesiredState(const RobotState \&robot\_state) const =0

</div>

</div>

<div id="aclassfranky_1_1_position_waypoint_motion_html_a345e479ffc4f38dba2a1128805108e19" class="ttc">

<div class="ttname">

[franky::PositionWaypointMotion::extrapolateMotion](classfranky_1_1_position_waypoint_motion.md#a345e479ffc4f38dba2a1128805108e19)

</div>

<div class="ttdeci">

void extrapolateMotion(const RobotState \&robot\_state, const franka::Duration \&time\_step, const ruckig::InputParameter\< 7 \> \&input\_parameter, ruckig::OutputParameter\< 7 \> \&output\_parameter) const override

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:69

</div>

</div>

<div id="aclassfranky_1_1_position_waypoint_motion_html_a8ebb35ebb3363acfec93c9228418804a" class="ttc">

<div class="ttname">

[franky::PositionWaypointMotion::setInputLimits](classfranky_1_1_position_waypoint_motion.md#a8ebb35ebb3363acfec93c9228418804a)

</div>

<div class="ttdeci">

void setInputLimits(const PositionWaypoint\< TargetType \> \&waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) const override

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:50

</div>

</div>

<div id="aclassfranky_1_1_position_waypoint_motion_html_a98d70e2d1e3113b5e5f86da03a21f714" class="ttc">

<div class="ttname">

[franky::PositionWaypointMotion::getAbsoluteInputLimits](classfranky_1_1_position_waypoint_motion.md#a98d70e2d1e3113b5e5f86da03a21f714)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getAbsoluteInputLimits() const override=0

</div>

</div>

<div id="aclassfranky_1_1_position_waypoint_motion_html_ad5d16a0e7416918355c6110df27a93e4" class="ttc">

<div class="ttname">

[franky::PositionWaypointMotion::PositionWaypointMotion](classfranky_1_1_position_waypoint_motion.md#ad5d16a0e7416918355c6110df27a93e4)

</div>

<div class="ttdeci">

PositionWaypointMotion(std::vector\< PositionWaypoint\< TargetType \> \> waypoints, const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0, bool return\_when\_finished=true)

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:43

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

<div id="aclassfranky_1_1_robot_html_a43f2f6dde0cca1f8c21fa6c1fb1b28c0" class="ttc">

<div class="ttname">

[franky::Robot::relative\_dynamics\_factor](classfranky_1_1_robot.md#a43f2f6dde0cca1f8c21fa6c1fb1b28c0)

</div>

<div class="ttdeci">

RelativeDynamicsFactor relative\_dynamics\_factor()

</div>

<div class="ttdoc">

Returns the current global relative dynamics factor of the robot.

</div>

<div class="ttdef">

**Definition** robot.cpp:123

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::WaypointMotion](classfranky_1_1_waypoint_motion.md)

</div>

<div class="ttdoc">

A motion following multiple waypoints in a time-optimal way. Works with arbitrary initial conditions.

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:59

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

<div id="areference__type_8hpp_html" class="ttc">

<div class="ttname">

[reference\_type.hpp](reference__type_8hpp.md)

</div>

</div>

<div id="arelative__dynamics__factor_8hpp_html" class="ttc">

<div class="ttname">

[relative\_dynamics\_factor.hpp](relative__dynamics__factor_8hpp.md)

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

<div id="astructfranky_1_1_position_waypoint_html_ac5dee69cb4ee3ab71a80cd54244ad220" class="ttc">

<div class="ttname">

[franky::PositionWaypoint::reference\_type](structfranky_1_1_position_waypoint.md#ac5dee69cb4ee3ab71a80cd54244ad220)

</div>

<div class="ttdeci">

ReferenceType reference\_type

</div>

<div class="ttdef">

**Definition** position\_waypoint\_motion.hpp:21

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

<div id="astructfranky_1_1_waypoint_html" class="ttc">

<div class="ttname">

[franky::Waypoint](structfranky_1_1_waypoint.md)

</div>

<div class="ttdoc">

A waypoint with a target and optional parameters.

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:36

</div>

</div>

<div id="astructfranky_1_1_waypoint_html_a88afd539ed0caff485c32cf830e9e121" class="ttc">

<div class="ttname">

[franky::Waypoint::relative\_dynamics\_factor](structfranky_1_1_waypoint.md#a88afd539ed0caff485c32cf830e9e121)

</div>

<div class="ttdeci">

RelativeDynamicsFactor relative\_dynamics\_factor

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:39

</div>

</div>

<div id="autil_8hpp_html" class="ttc">

<div class="ttname">

[util.hpp](util_8hpp.md)

</div>

</div>

<div id="awaypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[waypoint\_motion.hpp](waypoint__motion_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
