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

velocity\_waypoint\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](velocity__waypoint__motion_8hpp.md)

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

<span id="l00017"></span><span class="lineno"> 17</span><span class="keyword">template</span> \<<span class="keyword">typename</span> TargetType\>

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](namespacefranky.md#a7af3aea8bf2e7bc0f366814328c1fb32)</span><span class="keyword">using </span>[VelocityWaypoint](structfranky_1_1_waypoint.md) = [Waypoint\<TargetType\>](structfranky_1_1_waypoint.md);

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span>

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType, <span class="keyword">typename</span> TargetType\>

</div>

<div id="foldopen00029" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00029"></span><span class="lineno"> [29](classfranky_1_1_velocity_waypoint_motion.md)</span><span class="keyword">class </span>[VelocityWaypointMotion](classfranky_1_1_velocity_waypoint_motion.md) : <span class="keyword">public</span> [WaypointMotion](classfranky_1_1_waypoint_motion.md)\<ControlSignalType, VelocityWaypoint\<TargetType\>, TargetType\> {

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00037" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00037"></span><span class="lineno"> [37](classfranky_1_1_velocity_waypoint_motion.md#aa7cb87ffe6b03a25bf14efbb3e547405)</span> <span class="keyword">explicit</span> [VelocityWaypointMotion](classfranky_1_1_velocity_waypoint_motion.md#aa7cb87ffe6b03a25bf14efbb3e547405)(

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span> std::vector\<[VelocityWaypoint\<TargetType\>](structfranky_1_1_waypoint.md)\> [waypoints](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0)

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span> : [WaypointMotion](classfranky_1_1_waypoint_motion.md)\<[ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac), [VelocityWaypoint](structfranky_1_1_waypoint.md)\<[TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>, [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>([waypoints](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [true](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)),

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span> relative\_dynamics\_factor\_(relative\_dynamics\_factor) {}

</div>

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span>

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span> <span class="keyword">protected</span>:

</div>

<div id="foldopen00043" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00043"></span><span class="lineno"> [43](classfranky_1_1_velocity_waypoint_motion.md#a1cfd2cbfa762565d6d95a9db2d911fba)</span> <span class="keywordtype">void</span> [setInputLimits](classfranky_1_1_velocity_waypoint_motion.md#a1cfd2cbfa762565d6d95a9db2d911fba)(

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> <span class="keyword">const</span> [VelocityWaypoint\<TargetType\>](structfranky_1_1_waypoint.md) &[waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const override </span>{

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> <span class="keyword">auto</span> \[[vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [acc\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [jerk\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = [getAbsoluteInputLimits](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c)();

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span>

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keyword">auto</span> relative\_dynamics\_factor =

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span> [waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).relative\_dynamics\_factor \* relative\_dynamics\_factor\_ \* this-\>[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)()-\>[relative\_dynamics\_factor](classfranky_1_1_robot.md#a43f2f6dde0cca1f8c21fa6c1fb1b28c0)();

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span>

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span> input\_parameter.max\_velocity = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(relative\_dynamics\_factor.acceleration() \* [acc\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00051"></span><span class="lineno"> 51</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).max\_acceleration = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(relative\_dynamics\_factor.jerk() \* [jerk\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).max\_jerk = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(Vector7d::Constant(std::numeric\_limits\<double\>::infinity()));

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span>

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span> <span class="keywordflow">if</span> (relative\_dynamics\_factor.max\_dynamics()) {

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).synchronization = ruckig::Synchronization::TimeIfNecessary;

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span> [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).synchronization = ruckig::Synchronization::Time;

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> <span class="keywordflow">if</span> ([waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).minimum\_time.has\_value()) [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).minimum\_duration = [waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).minimum\_time.value().toSec();

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> }

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span> }

</div>

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span>

</div>

<div id="foldopen00062" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00062"></span><span class="lineno"> [62](classfranky_1_1_velocity_waypoint_motion.md#aca3cabe4405f7132c4001388d248cc67)</span> <span class="keywordtype">void</span> [extrapolateMotion](classfranky_1_1_velocity_waypoint_motion.md#aca3cabe4405f7132c4001388d248cc67)(

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> franka::Duration &[time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> <span class="keyword">const</span> ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::OutputParameter\<7\> &[output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const override </span>{

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> <span class="keyword">auto</span> \[[vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [acc\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [jerk\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = [getAbsoluteInputLimits](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c)();

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span>

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span> <span class="comment">// We use the desired state here as this is likely what the robot uses</span>

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span> <span class="comment">// internally as well</span>

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> <span class="keyword">auto</span> \[[vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [acc\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [\_](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = [getDesiredState](classfranky_1_1_velocity_waypoint_motion.md#abccc66187b0b5f52604217f4d44bd842)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> <span class="keyword">auto</span> [vel](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [toEigenD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).current\_position);

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span>

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span> <span class="comment">// Retain difference between desired state and motion planner state</span>

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span> <span class="keyword">auto</span> [vel\_diff](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [vel](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) - [vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span>

</div>

<div class="line">

<span id="l00076"></span><span class="lineno"> 76</span> <span class="keyword">auto</span> [new\_vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = ([vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) + [acc\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \* [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).toSec()).[cwiseMin](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)).cwiseMax(-[vel\_lim](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span>

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> <span class="comment">// Franka assumes a constant acceleration model if no new input is received.</span>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> <span class="comment">// See https://frankaemika.github.io/docs/libfranka.md\#under-the-hood</span>

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span> [output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).new\_acceleration = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(Vector7d::Zero());

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span> [output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).new\_velocity = [input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).current\_velocity;

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> [output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).new\_position = [toStdD\<7\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([new\_vel\_d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) + [vel\_diff](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span> }

</div>

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span>

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> [85](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] std::tuple\<Vector7d, Vector7d, Vector7d\> [getAbsoluteInputLimits](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c)() <span class="keyword">const override</span> = 0;

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span>

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> [87](classfranky_1_1_velocity_waypoint_motion.md#abccc66187b0b5f52604217f4d44bd842)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">virtual</span> std::tuple\<Vector7d, Vector7d, Vector7d\> [getDesiredState](classfranky_1_1_velocity_waypoint_motion.md#abccc66187b0b5f52604217f4d44bd842)(

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) <span class="keyword">const</span> = 0;

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span>

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) relative\_dynamics\_factor\_;

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> 92</span>};

</div>

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> 93</span>

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_velocity_waypoint_motion_html" class="ttc">

<div class="ttname">

[franky::VelocityWaypointMotion](classfranky_1_1_velocity_waypoint_motion.md)

</div>

<div class="ttdoc">

A motion following multiple positional waypoints in a time-optimal way. Works with arbitrary initial ...

</div>

<div class="ttdef">

**Definition** velocity\_waypoint\_motion.hpp:29

</div>

</div>

<div id="aclassfranky_1_1_velocity_waypoint_motion_html_a1cfd2cbfa762565d6d95a9db2d911fba" class="ttc">

<div class="ttname">

[franky::VelocityWaypointMotion::setInputLimits](classfranky_1_1_velocity_waypoint_motion.md#a1cfd2cbfa762565d6d95a9db2d911fba)

</div>

<div class="ttdeci">

void setInputLimits(const VelocityWaypoint\< TargetType \> \&waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) const override

</div>

<div class="ttdef">

**Definition** velocity\_waypoint\_motion.hpp:43

</div>

</div>

<div id="aclassfranky_1_1_velocity_waypoint_motion_html_aa7cb87ffe6b03a25bf14efbb3e547405" class="ttc">

<div class="ttname">

[franky::VelocityWaypointMotion::VelocityWaypointMotion](classfranky_1_1_velocity_waypoint_motion.md#aa7cb87ffe6b03a25bf14efbb3e547405)

</div>

<div class="ttdeci">

VelocityWaypointMotion(std::vector\< VelocityWaypoint\< TargetType \> \> waypoints, const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)

</div>

<div class="ttdef">

**Definition** velocity\_waypoint\_motion.hpp:37

</div>

</div>

<div id="aclassfranky_1_1_velocity_waypoint_motion_html_abccc66187b0b5f52604217f4d44bd842" class="ttc">

<div class="ttname">

[franky::VelocityWaypointMotion::getDesiredState](classfranky_1_1_velocity_waypoint_motion.md#abccc66187b0b5f52604217f4d44bd842)

</div>

<div class="ttdeci">

virtual std::tuple\< Vector7d, Vector7d, Vector7d \> getDesiredState(const RobotState \&robot\_state) const =0

</div>

</div>

<div id="aclassfranky_1_1_velocity_waypoint_motion_html_abe56780579a68ee495edb7436f62441c" class="ttc">

<div class="ttname">

[franky::VelocityWaypointMotion::getAbsoluteInputLimits](classfranky_1_1_velocity_waypoint_motion.md#abe56780579a68ee495edb7436f62441c)

</div>

<div class="ttdeci">

std::tuple\< Vector7d, Vector7d, Vector7d \> getAbsoluteInputLimits() const override=0

</div>

</div>

<div id="aclassfranky_1_1_velocity_waypoint_motion_html_aca3cabe4405f7132c4001388d248cc67" class="ttc">

<div class="ttname">

[franky::VelocityWaypointMotion::extrapolateMotion](classfranky_1_1_velocity_waypoint_motion.md#aca3cabe4405f7132c4001388d248cc67)

</div>

<div class="ttdeci">

void extrapolateMotion(const RobotState \&robot\_state, const franka::Duration \&time\_step, const ruckig::InputParameter\< 7 \> \&input\_parameter, ruckig::OutputParameter\< 7 \> \&output\_parameter) const override

</div>

<div class="ttdef">

**Definition** velocity\_waypoint\_motion.hpp:62

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
