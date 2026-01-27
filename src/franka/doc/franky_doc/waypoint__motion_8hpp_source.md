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

waypoint\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](waypoint__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<ruckig/ruckig.hpp\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/motion/motion.hpp](motion_8hpp.md)"</span>

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

<span id="l00013"></span><span class="lineno"> [13](structfranky_1_1_motion_planner_exception.md)</span><span class="keyword">struct </span>[MotionPlannerException](structfranky_1_1_motion_planner_exception.md) : std::runtime\_error {

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

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span><span class="keyword">template</span> \<<span class="keyword">typename</span> TargetType\>

</div>

<div id="foldopen00036" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00036"></span><span class="lineno"> [36](structfranky_1_1_waypoint.md)</span><span class="keyword">struct </span>[Waypoint](structfranky_1_1_waypoint.md) {

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> [37](structfranky_1_1_waypoint.md#a857fb8417fc17ff5e171494b1d398355)</span> [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [target](structfranky_1_1_waypoint.md#a857fb8417fc17ff5e171494b1d398355);

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span>

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> [39](structfranky_1_1_waypoint.md#a88afd539ed0caff485c32cf830e9e121)</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) [relative\_dynamics\_factor](structfranky_1_1_waypoint.md#a88afd539ed0caff485c32cf830e9e121){1.0};

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span>

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> [41](structfranky_1_1_waypoint.md#ae1532c5f277153a041d626ce4666d382)</span> std::optional\<franka::Duration\> [minimum\_time](structfranky_1_1_waypoint.md#ae1532c5f277153a041d626ce4666d382){std::nullopt};

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span>

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> [43](structfranky_1_1_waypoint.md#a2c1e5c63e3a7447b4699a546e49ed009)</span> franka::Duration [hold\_target\_duration](structfranky_1_1_waypoint.md#a2c1e5c63e3a7447b4699a546e49ed009){0};

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span>

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> [45](structfranky_1_1_waypoint.md#a2a1eae68a4e9d3b9c54a0ff1fd6c9bb2)</span> std::optional\<franka::Duration\> [max\_total\_duration](structfranky_1_1_waypoint.md#a2a1eae68a4e9d3b9c54a0ff1fd6c9bb2){std::nullopt};

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span>};

</div>

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span>

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType, <span class="keyword">typename</span> Waypo<span class="keywordtype">int</span>Type, <span class="keyword">typename</span> TargetType\>

</div>

<div id="foldopen00059" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00059"></span><span class="lineno"> [59](classfranky_1_1_waypoint_motion.md)</span><span class="keyword">class </span>[WaypointMotion](classfranky_1_1_waypoint_motion.md) : <span class="keyword">public</span> [Motion](classfranky_1_1_motion.md)\<ControlSignalType\> {

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span> <span class="keyword">static\_assert</span>(

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> std::is\_base\_of\_v\<Waypoint\<TargetType\>, [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>, <span class="stringliteral">"WaypointType must inherit from Waypoint\<TargetType\>"</span>);

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span>

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00069" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00069"></span><span class="lineno"> [69](classfranky_1_1_waypoint_motion.md#a53c26db8057d1048efafe5a38a372f77)</span> <span class="keyword">explicit</span> [WaypointMotion](classfranky_1_1_waypoint_motion.md#a53c26db8057d1048efafe5a38a372f77)(std::vector\<WaypointType\> [waypoints](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">bool</span> return\_when\_finished = <span class="keyword">true</span>)

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span> : waypoints\_(std::move([waypoints](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))), return\_when\_finished\_(return\_when\_finished), prev\_result\_() {}

</div>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span>

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span> <span class="keyword">protected</span>:

</div>

<div id="foldopen00073" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00073"></span><span class="lineno"> [73](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69)</span> <span class="keywordtype">void</span> [initImpl](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> std::optional\<ControlSignalType\> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> override </span>{

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span> target\_reached\_time\_ = std::nullopt;

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span> waypoint\_started\_time\_ = franka::Duration(0);

</div>

<div class="line">

<span id="l00076"></span><span class="lineno"> 76</span>

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span> waypoint\_iterator\_ = waypoints\_.begin();

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> [initWaypointMotion](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), input\_parameter\_);

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> <span class="keywordflow">if</span> (waypoint\_iterator\_ \!= waypoints\_.end()) {

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span> [checkWaypoint](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)(\*waypoint\_iterator\_);

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span> [setNewWaypoint](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), \*waypoint\_iterator\_, input\_parameter\_);

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> [setInputLimits](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)(\*waypoint\_iterator\_, input\_parameter\_);

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span> prev\_result\_ = ruckig::Result::Working;

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span> prev\_result\_ = ruckig::Result::Finished;

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span> }

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span> }

</div>

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span>

</div>

<div id="foldopen00089" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00089"></span><span class="lineno"> [89](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b)</span> [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) [nextCommandImpl](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b)(

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span> <span class="keyword">const</span> std::optional\<ControlSignalType\> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> override </span>{

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> 92</span> <span class="keyword">const</span> <span class="keyword">auto</span> [expected\_time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = franka::Duration(1);

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> 93</span> <span class="keywordflow">if</span> ([time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> [expected\_time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span> <span class="comment">// In this case, we missed a couple of steps for some reason. Hence,</span>

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> 95</span> <span class="comment">// extrapolate the way the robot does if it does not receive data</span>

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> 96</span> <span class="comment">// (constant acceleration model). See</span>

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> 97</span> <span class="comment">// https://frankaemika.github.io/docs/libfranka.md\#under-the-hood</span>

</div>

<div class="line">

<span id="l00098"></span><span class="lineno"> 98</span> [extrapolateMotion](classfranky_1_1_waypoint_motion.md#a24a6f06d1ca935764c37aa044d191750)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) - [expected\_time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), input\_parameter\_, output\_parameter\_);

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span> output\_parameter\_.pass\_to\_input(input\_parameter\_);

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span> }

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> 101</span>

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> 102</span> <span class="keyword">auto</span> [max\_time\_reached](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>;

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> 103</span> <span class="keywordflow">if</span> (waypoint\_iterator\_ \!= waypoints\_.end() && waypoint\_iterator\_-\>max\_total\_duration.has\_value()) {

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> 104</span> [max\_time\_reached](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) - waypoint\_started\_time\_ \>= waypoint\_iterator\_-\>max\_total\_duration.value();

</div>

<div class="line">

<span id="l00105"></span><span class="lineno"> 105</span> }

</div>

<div class="line">

<span id="l00106"></span><span class="lineno"> 106</span>

</div>

<div class="line">

<span id="l00107"></span><span class="lineno"> 107</span> <span class="keywordflow">if</span> (prev\_result\_ == ruckig::Finished || [max\_time\_reached](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00108"></span><span class="lineno"> 108</span> <span class="keywordflow">if</span> (\!target\_reached\_time\_.has\_value()) {

</div>

<div class="line">

<span id="l00109"></span><span class="lineno"> 109</span> target\_reached\_time\_ = [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00110"></span><span class="lineno"> 110</span> }

</div>

<div class="line">

<span id="l00111"></span><span class="lineno"> 111</span> <span class="keywordflow">if</span> (waypoint\_iterator\_ \!= waypoints\_.end()) {

</div>

<div class="line">

<span id="l00112"></span><span class="lineno"> 112</span> <span class="keyword">auto</span> hold\_target\_duration = waypoint\_iterator\_-\>hold\_target\_duration;

</div>

<div class="line">

<span id="l00113"></span><span class="lineno"> 113</span> <span class="keywordflow">if</span> (waypoint\_iterator\_ + 1 == waypoints\_.end()) {

</div>

<div class="line">

<span id="l00114"></span><span class="lineno"> 114</span> <span class="comment">// Allow cooldown of motion, so that the low-pass filter has time to</span>

</div>

<div class="line">

<span id="l00115"></span><span class="lineno"> 115</span> <span class="comment">// adjust to target values</span>

</div>

<div class="line">

<span id="l00116"></span><span class="lineno"> 116</span> hold\_target\_duration = std::max(hold\_target\_duration, franka::Duration(10));

</div>

<div class="line">

<span id="l00117"></span><span class="lineno"> 117</span> }

</div>

<div class="line">

<span id="l00118"></span><span class="lineno"> 118</span> <span class="keywordflow">if</span> ([rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) - target\_reached\_time\_.value() \>= hold\_target\_duration || [max\_time\_reached](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00119"></span><span class="lineno"> 119</span> target\_reached\_time\_ = std::nullopt;

</div>

<div class="line">

<span id="l00120"></span><span class="lineno"> 120</span> ++waypoint\_iterator\_;

</div>

<div class="line">

<span id="l00121"></span><span class="lineno"> 121</span> <span class="keywordflow">if</span> (waypoint\_iterator\_ \!= waypoints\_.end()) {

</div>

<div class="line">

<span id="l00122"></span><span class="lineno"> 122</span> [checkWaypoint](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)(\*waypoint\_iterator\_);

</div>

<div class="line">

<span id="l00123"></span><span class="lineno"> 123</span> [setNewWaypoint](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), \*waypoint\_iterator\_, input\_parameter\_);

</div>

<div class="line">

<span id="l00124"></span><span class="lineno"> 124</span> [setInputLimits](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)(\*waypoint\_iterator\_, input\_parameter\_);

</div>

<div class="line">

<span id="l00125"></span><span class="lineno"> 125</span> waypoint\_started\_time\_ = [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00126"></span><span class="lineno"> 126</span> }

</div>

<div class="line">

<span id="l00127"></span><span class="lineno"> 127</span> }

</div>

<div class="line">

<span id="l00128"></span><span class="lineno"> 128</span> }

</div>

<div class="line">

<span id="l00129"></span><span class="lineno"> 129</span> <span class="keywordflow">if</span> (waypoint\_iterator\_ == waypoints\_.end()) {

</div>

<div class="line">

<span id="l00130"></span><span class="lineno"> 130</span> <span class="keyword">auto</span> [command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [getControlSignal](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), input\_parameter\_);

</div>

<div class="line">

<span id="l00131"></span><span class="lineno"> 131</span> <span class="keywordflow">if</span> (\!return\_when\_finished\_) <span class="keywordflow">return</span> [command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00132"></span><span class="lineno"> 132</span> <span class="keywordflow">return</span> franka::MotionFinished([command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00133"></span><span class="lineno"> 133</span> }

</div>

<div class="line">

<span id="l00134"></span><span class="lineno"> 134</span> }

</div>

<div class="line">

<span id="l00135"></span><span class="lineno"> 135</span>

</div>

<div class="line">

<span id="l00136"></span><span class="lineno"> 136</span> [assert](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(waypoint\_iterator\_ \!= waypoints\_.end());

</div>

<div class="line">

<span id="l00137"></span><span class="lineno"> 137</span>

</div>

<div class="line">

<span id="l00138"></span><span class="lineno"> 138</span> prev\_result\_ = trajectory\_generator\_.update(input\_parameter\_, output\_parameter\_);

</div>

<div class="line">

<span id="l00139"></span><span class="lineno"> 139</span> <span class="keywordflow">if</span> (prev\_result\_ == ruckig::Result::Working || prev\_result\_ == ruckig::Result::Finished) {

</div>

<div class="line">

<span id="l00140"></span><span class="lineno"> 140</span> <span class="comment">// This is a workaround to prevent NaNs from popping up. Must be some bug</span>

</div>

<div class="line">

<span id="l00141"></span><span class="lineno"> 141</span> <span class="comment">// in ruckig.</span>

</div>

<div class="line">

<span id="l00142"></span><span class="lineno"> 142</span> <span class="keywordflow">for</span> (<span class="keywordtype">int</span> [i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = 0; [i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \< 7; [i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)++) {

</div>

<div class="line">

<span id="l00143"></span><span class="lineno"> 143</span> <span class="keywordflow">if</span> (\!input\_parameter\_.enabled\[[i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]) {

</div>

<div class="line">

<span id="l00144"></span><span class="lineno"> 144</span> output\_parameter\_.new\_position\[[i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = 0.0;

</div>

<div class="line">

<span id="l00145"></span><span class="lineno"> 145</span> output\_parameter\_.new\_velocity\[[i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = 0.0;

</div>

<div class="line">

<span id="l00146"></span><span class="lineno"> 146</span> output\_parameter\_.new\_acceleration\[[i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\] = 0.0;

</div>

<div class="line">

<span id="l00147"></span><span class="lineno"> 147</span> }

</div>

<div class="line">

<span id="l00148"></span><span class="lineno"> 148</span> }

</div>

<div class="line">

<span id="l00149"></span><span class="lineno"> 149</span> output\_parameter\_.pass\_to\_input(input\_parameter\_);

</div>

<div class="line">

<span id="l00150"></span><span class="lineno"> 150</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00151"></span><span class="lineno"> 151</span> <span class="keywordflow">throw</span> [MotionPlannerException](structfranky_1_1_motion_planner_exception.md)(<span class="stringliteral">"Motion planner failed with error code "</span> + std::to\_string(prev\_result\_));

</div>

<div class="line">

<span id="l00152"></span><span class="lineno"> 152</span> }

</div>

<div class="line">

<span id="l00153"></span><span class="lineno"> 153</span>

</div>

<div class="line">

<span id="l00154"></span><span class="lineno"> 154</span> <span class="keywordflow">return</span> [getControlSignal](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)([robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), input\_parameter\_);

</div>

<div class="line">

<span id="l00155"></span><span class="lineno"> 155</span> };

</div>

</div>

<div class="line">

<span id="l00156"></span><span class="lineno"> 156</span>

</div>

<div class="line">

<span id="l00157"></span><span class="lineno"> [157](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8)</span> <span class="keyword">virtual</span> <span class="keywordtype">void</span> [initWaypointMotion](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8)(

</div>

<div class="line">

<span id="l00158"></span><span class="lineno"> 158</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> std::optional\<ControlSignalType\> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00159"></span><span class="lineno"> 159</span> ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) = 0;

</div>

<div class="line">

<span id="l00160"></span><span class="lineno"> 160</span>

</div>

<div class="line">

<span id="l00161"></span><span class="lineno"> [161](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)</span> <span class="keyword">virtual</span> <span class="keywordtype">void</span> [setNewWaypoint](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)(

</div>

<div class="line">

<span id="l00162"></span><span class="lineno"> 162</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> std::optional\<ControlSignalType\> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00163"></span><span class="lineno"> 163</span> <span class="keyword">const</span> [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[new\_waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) = 0;

</div>

<div class="line">

<span id="l00164"></span><span class="lineno"> 164</span>

</div>

<div class="line">

<span id="l00165"></span><span class="lineno"> [165](classfranky_1_1_waypoint_motion.md#a24a6f06d1ca935764c37aa044d191750)</span> <span class="keyword">virtual</span> <span class="keywordtype">void</span> [extrapolateMotion](classfranky_1_1_waypoint_motion.md#a24a6f06d1ca935764c37aa044d191750)(

</div>

<div class="line">

<span id="l00166"></span><span class="lineno"> 166</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> franka::Duration &[time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00167"></span><span class="lineno"> 167</span> <span class="keyword">const</span> ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::OutputParameter\<7\> &[output\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) <span class="keyword">const</span> = 0;

</div>

<div class="line">

<span id="l00168"></span><span class="lineno"> 168</span>

</div>

<div class="line">

<span id="l00169"></span><span class="lineno"> [169](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)</span> <span class="keyword">virtual</span> <span class="keywordtype">void</span> [checkWaypoint](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)(<span class="keyword">const</span> [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))<span class="keyword"> const </span>{}

</div>

<div class="line">

<span id="l00170"></span><span class="lineno"> 170</span>

</div>

<div class="line">

<span id="l00171"></span><span class="lineno"> [171](classfranky_1_1_waypoint_motion.md#ae3c92f31c20dcb7f48107c1991d8be33)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">virtual</span> std::tuple\<Vector7d, Vector7d, Vector7d\> [getAbsoluteInputLimits](classfranky_1_1_waypoint_motion.md#ae3c92f31c20dcb7f48107c1991d8be33)() <span class="keyword">const</span> = 0;

</div>

<div class="line">

<span id="l00172"></span><span class="lineno"> 172</span>

</div>

<div class="line">

<span id="l00173"></span><span class="lineno"> [173](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keyword">virtual</span> [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) [getControlSignal](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)(

</div>

<div class="line">

<span id="l00174"></span><span class="lineno"> 174</span> <span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> franka::Duration &[time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00175"></span><span class="lineno"> 175</span> <span class="keyword">const</span> std::optional\<ControlSignalType\> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) = 0;

</div>

<div class="line">

<span id="l00176"></span><span class="lineno"> 176</span>

</div>

<div class="line">

<span id="l00177"></span><span class="lineno"> [177](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)</span> <span class="keyword">virtual</span> <span class="keywordtype">void</span> [setInputLimits](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)(<span class="keyword">const</span> [WaypointType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[waypoint](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), ruckig::InputParameter\<7\> &[input\_parameter](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) <span class="keyword">const</span> = 0;

</div>

<div class="line">

<span id="l00178"></span><span class="lineno"> 178</span>

</div>

<div class="line">

<span id="l00179"></span><span class="lineno"> 179</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00180"></span><span class="lineno"> 180</span> std::vector\<WaypointType\> waypoints\_;

</div>

<div class="line">

<span id="l00181"></span><span class="lineno"> 181</span> <span class="keywordtype">bool</span> return\_when\_finished\_{<span class="keyword">true</span>};

</div>

<div class="line">

<span id="l00182"></span><span class="lineno"> 182</span>

</div>

<div class="line">

<span id="l00183"></span><span class="lineno"> 183</span> ruckig::Ruckig\<7\> trajectory\_generator\_{[Robot::control\_rate](classfranky_1_1_robot.md#a3155de462f5590cc67b2874acf846f53)};

</div>

<div class="line">

<span id="l00184"></span><span class="lineno"> 184</span> ruckig::Result prev\_result\_;

</div>

<div class="line">

<span id="l00185"></span><span class="lineno"> 185</span> ruckig::InputParameter\<7\> input\_parameter\_;

</div>

<div class="line">

<span id="l00186"></span><span class="lineno"> 186</span> ruckig::OutputParameter\<7\> output\_parameter\_;

</div>

<div class="line">

<span id="l00187"></span><span class="lineno"> 187</span>

</div>

<div class="line">

<span id="l00188"></span><span class="lineno"> 188</span> <span class="keyword">typename</span> std::vector\<WaypointType\>::iterator waypoint\_iterator\_;

</div>

<div class="line">

<span id="l00189"></span><span class="lineno"> 189</span>

</div>

<div class="line">

<span id="l00190"></span><span class="lineno"> 190</span> std::optional\<franka::Duration\> target\_reached\_time\_;

</div>

<div class="line">

<span id="l00191"></span><span class="lineno"> 191</span> franka::Duration waypoint\_started\_time\_;

</div>

<div class="line">

<span id="l00192"></span><span class="lineno"> 192</span>};

</div>

</div>

<div class="line">

<span id="l00193"></span><span class="lineno"> 193</span>

</div>

<div class="line">

<span id="l00194"></span><span class="lineno"> 194</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_robot_html_a3155de462f5590cc67b2874acf846f53" class="ttc">

<div class="ttname">

[franky::Robot::control\_rate](classfranky_1_1_robot.md#a3155de462f5590cc67b2874acf846f53)

</div>

<div class="ttdeci">

static constexpr double control\_rate

</div>

<div class="ttdef">

**Definition** robot.hpp:146

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

<div id="aclassfranky_1_1_waypoint_motion_html_a24a6f06d1ca935764c37aa044d191750" class="ttc">

<div class="ttname">

[franky::WaypointMotion::extrapolateMotion](classfranky_1_1_waypoint_motion.md#a24a6f06d1ca935764c37aa044d191750)

</div>

<div class="ttdeci">

virtual void extrapolateMotion(const RobotState \&robot\_state, const franka::Duration \&time\_step, const ruckig::InputParameter\< 7 \> \&input\_parameter, ruckig::OutputParameter\< 7 \> \&output\_parameter) const =0

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_a2af18e1bfe76ed4e88f87ba03fe04fd8" class="ttc">

<div class="ttname">

[franky::WaypointMotion::initWaypointMotion](classfranky_1_1_waypoint_motion.md#a2af18e1bfe76ed4e88f87ba03fe04fd8)

</div>

<div class="ttdeci">

virtual void initWaypointMotion(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command, ruckig::InputParameter\< 7 \> \&input\_parameter)=0

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_a4a54f0791590e317159518eb0353a199" class="ttc">

<div class="ttname">

[franky::WaypointMotion::setInputLimits](classfranky_1_1_waypoint_motion.md#a4a54f0791590e317159518eb0353a199)

</div>

<div class="ttdeci">

virtual void setInputLimits(const WaypointType \&waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter) const =0

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_a53c26db8057d1048efafe5a38a372f77" class="ttc">

<div class="ttname">

[franky::WaypointMotion::WaypointMotion](classfranky_1_1_waypoint_motion.md#a53c26db8057d1048efafe5a38a372f77)

</div>

<div class="ttdeci">

WaypointMotion(std::vector\< WaypointType \> waypoints, bool return\_when\_finished=true)

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:69

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_a9d8d450f3d2748cc32eb6bd2afd6f46c" class="ttc">

<div class="ttname">

[franky::WaypointMotion::checkWaypoint](classfranky_1_1_waypoint_motion.md#a9d8d450f3d2748cc32eb6bd2afd6f46c)

</div>

<div class="ttdeci">

virtual void checkWaypoint(const WaypointType \&waypoint) const

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:169

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_aa019aeb70e7bc53a5a95a8ac2e2b62eb" class="ttc">

<div class="ttname">

[franky::WaypointMotion::getControlSignal](classfranky_1_1_waypoint_motion.md#aa019aeb70e7bc53a5a95a8ac2e2b62eb)

</div>

<div class="ttdeci">

virtual ControlSignalType getControlSignal(const RobotState \&robot\_state, const franka::Duration \&time\_step, const std::optional\< ControlSignalType \> \&previous\_command, const ruckig::InputParameter\< 7 \> \&input\_parameter)=0

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_aac84c2b66a185a3c21380a395cc49ae0" class="ttc">

<div class="ttname">

[franky::WaypointMotion::setNewWaypoint](classfranky_1_1_waypoint_motion.md#aac84c2b66a185a3c21380a395cc49ae0)

</div>

<div class="ttdeci">

virtual void setNewWaypoint(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command, const WaypointType \&new\_waypoint, ruckig::InputParameter\< 7 \> \&input\_parameter)=0

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_ada8edd9d849ee29244b6c2c1cfa30f69" class="ttc">

<div class="ttname">

[franky::WaypointMotion::initImpl](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69)

</div>

<div class="ttdeci">

void initImpl(const RobotState \&robot\_state, const std::optional\< ControlSignalType \> \&previous\_command) override

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:73

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_ade5d803c15b7f55e55258092788df21b" class="ttc">

<div class="ttname">

[franky::WaypointMotion::nextCommandImpl](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b)

</div>

<div class="ttdeci">

ControlSignalType nextCommandImpl(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< ControlSignalType \> \&previous\_command) override

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:89

</div>

</div>

<div id="aclassfranky_1_1_waypoint_motion_html_ae3c92f31c20dcb7f48107c1991d8be33" class="ttc">

<div class="ttname">

[franky::WaypointMotion::getAbsoluteInputLimits](classfranky_1_1_waypoint_motion.md#ae3c92f31c20dcb7f48107c1991d8be33)

</div>

<div class="ttdeci">

virtual std::tuple\< Vector7d, Vector7d, Vector7d \> getAbsoluteInputLimits() const =0

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

<div id="astructfranky_1_1_motion_planner_exception_html" class="ttc">

<div class="ttname">

[franky::MotionPlannerException](structfranky_1_1_motion_planner_exception.md)

</div>

<div class="ttdoc">

Exception thrown if the motion planner fails.

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:13

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

<div id="astructfranky_1_1_waypoint_html_a2a1eae68a4e9d3b9c54a0ff1fd6c9bb2" class="ttc">

<div class="ttname">

[franky::Waypoint::max\_total\_duration](structfranky_1_1_waypoint.md#a2a1eae68a4e9d3b9c54a0ff1fd6c9bb2)

</div>

<div class="ttdeci">

std::optional\< franka::Duration \> max\_total\_duration

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:45

</div>

</div>

<div id="astructfranky_1_1_waypoint_html_a2c1e5c63e3a7447b4699a546e49ed009" class="ttc">

<div class="ttname">

[franky::Waypoint::hold\_target\_duration](structfranky_1_1_waypoint.md#a2c1e5c63e3a7447b4699a546e49ed009)

</div>

<div class="ttdeci">

franka::Duration hold\_target\_duration

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:43

</div>

</div>

<div id="astructfranky_1_1_waypoint_html_a857fb8417fc17ff5e171494b1d398355" class="ttc">

<div class="ttname">

[franky::Waypoint::target](structfranky_1_1_waypoint.md#a857fb8417fc17ff5e171494b1d398355)

</div>

<div class="ttdeci">

TargetType target

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:37

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

<div id="astructfranky_1_1_waypoint_html_ae1532c5f277153a041d626ce4666d382" class="ttc">

<div class="ttname">

[franky::Waypoint::minimum\_time](structfranky_1_1_waypoint.md#ae1532c5f277153a041d626ce4666d382)

</div>

<div class="ttdeci">

std::optional\< franka::Duration \> minimum\_time

</div>

<div class="ttdef">

**Definition** waypoint\_motion.hpp:41

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
