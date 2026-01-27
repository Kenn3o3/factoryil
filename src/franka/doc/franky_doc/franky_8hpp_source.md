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

</div>

</div>

<div class="header">

<div class="headertitle">

<div class="title">

franky.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](franky_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include "[franky/cartesian\_state.hpp](cartesian__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include "[franky/control\_signal\_type.hpp](control__signal__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include "[franky/elbow\_state.hpp](elbow__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/gripper.hpp](gripper_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/joint\_state.hpp](joint__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="preprocessor">\#include "[franky/model.hpp](model_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/motion/cartesian\_impedance\_motion.hpp](cartesian__impedance__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/motion/cartesian\_motion.hpp](cartesian__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="preprocessor">\#include "[franky/motion/cartesian\_waypoint\_motion.hpp](cartesian__waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="preprocessor">\#include "[franky/motion/condition.hpp](condition_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span><span class="preprocessor">\#include "[franky/motion/exponential\_impedance\_motion.hpp](exponential__impedance__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span><span class="preprocessor">\#include "[franky/motion/impedance\_motion.hpp](impedance__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span><span class="preprocessor">\#include "[franky/motion/joint\_motion.hpp](joint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span><span class="preprocessor">\#include "[franky/motion/joint\_waypoint\_motion.hpp](joint__waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span><span class="preprocessor">\#include "[franky/motion/measure.hpp](measure_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> 18</span><span class="preprocessor">\#include "[franky/motion/motion.hpp](motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span><span class="preprocessor">\#include "[franky/motion/motion\_generator.hpp](motion__generator_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span><span class="preprocessor">\#include "[franky/motion/position\_waypoint\_motion.hpp](position__waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span><span class="preprocessor">\#include "[franky/motion/reaction.hpp](reaction_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span><span class="preprocessor">\#include "[franky/motion/reference\_type.hpp](reference__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span><span class="preprocessor">\#include "[franky/motion/stop\_motion.hpp](stop__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span><span class="preprocessor">\#include "[franky/motion/waypoint\_motion.hpp](waypoint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span><span class="preprocessor">\#include "[franky/robot.hpp](robot_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span><span class="preprocessor">\#include "[franky/robot\_pose.hpp](robot__pose_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span><span class="preprocessor">\#include "[franky/robot\_state.hpp](robot__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span><span class="preprocessor">\#include "[franky/robot\_velocity.hpp](robot__velocity_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span><span class="preprocessor">\#include "[franky/rt\_mutex.hpp](rt__mutex_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span><span class="preprocessor">\#include "[franky/twist.hpp](twist_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span><span class="preprocessor">\#include "[franky/twist\_acceleration.hpp](twist__acceleration_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> 33</span><span class="preprocessor">\#include "[franky/util.hpp](util_8hpp.md)"</span>

</div>

<div id="acartesian__impedance__motion_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_impedance\_motion.hpp](cartesian__impedance__motion_8hpp.md)

</div>

</div>

<div id="acartesian__motion_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_motion.hpp](cartesian__motion_8hpp.md)

</div>

</div>

<div id="acartesian__state_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_state.hpp](cartesian__state_8hpp.md)

</div>

</div>

<div id="acartesian__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_waypoint\_motion.hpp](cartesian__waypoint__motion_8hpp.md)

</div>

</div>

<div id="acondition_8hpp_html" class="ttc">

<div class="ttname">

[condition.hpp](condition_8hpp.md)

</div>

</div>

<div id="acontrol__signal__type_8hpp_html" class="ttc">

<div class="ttname">

[control\_signal\_type.hpp](control__signal__type_8hpp.md)

</div>

</div>

<div id="aelbow__state_8hpp_html" class="ttc">

<div class="ttname">

[elbow\_state.hpp](elbow__state_8hpp.md)

</div>

</div>

<div id="aexponential__impedance__motion_8hpp_html" class="ttc">

<div class="ttname">

[exponential\_impedance\_motion.hpp](exponential__impedance__motion_8hpp.md)

</div>

</div>

<div id="agripper_8hpp_html" class="ttc">

<div class="ttname">

[gripper.hpp](gripper_8hpp.md)

</div>

</div>

<div id="aimpedance__motion_8hpp_html" class="ttc">

<div class="ttname">

[impedance\_motion.hpp](impedance__motion_8hpp.md)

</div>

</div>

<div id="ajoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[joint\_motion.hpp](joint__motion_8hpp.md)

</div>

</div>

<div id="ajoint__state_8hpp_html" class="ttc">

<div class="ttname">

[joint\_state.hpp](joint__state_8hpp.md)

</div>

</div>

<div id="ajoint__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[joint\_waypoint\_motion.hpp](joint__waypoint__motion_8hpp.md)

</div>

</div>

<div id="ameasure_8hpp_html" class="ttc">

<div class="ttname">

[measure.hpp](measure_8hpp.md)

</div>

</div>

<div id="amodel_8hpp_html" class="ttc">

<div class="ttname">

[model.hpp](model_8hpp.md)

</div>

</div>

<div id="amotion_8hpp_html" class="ttc">

<div class="ttname">

[motion.hpp](motion_8hpp.md)

</div>

</div>

<div id="amotion__generator_8hpp_html" class="ttc">

<div class="ttname">

[motion\_generator.hpp](motion__generator_8hpp.md)

</div>

</div>

<div id="aposition__waypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[position\_waypoint\_motion.hpp](position__waypoint__motion_8hpp.md)

</div>

</div>

<div id="areaction_8hpp_html" class="ttc">

<div class="ttname">

[reaction.hpp](reaction_8hpp.md)

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

<div id="arobot__state_8hpp_html" class="ttc">

<div class="ttname">

[robot\_state.hpp](robot__state_8hpp.md)

</div>

</div>

<div id="arobot__velocity_8hpp_html" class="ttc">

<div class="ttname">

[robot\_velocity.hpp](robot__velocity_8hpp.md)

</div>

</div>

<div id="art__mutex_8hpp_html" class="ttc">

<div class="ttname">

[rt\_mutex.hpp](rt__mutex_8hpp.md)

</div>

</div>

<div id="astop__motion_8hpp_html" class="ttc">

<div class="ttname">

[stop\_motion.hpp](stop__motion_8hpp.md)

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

<div id="awaypoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[waypoint\_motion.hpp](waypoint__motion_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
