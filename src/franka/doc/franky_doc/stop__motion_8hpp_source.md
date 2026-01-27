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

stop\_motion.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](stop__motion_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include "[franky/motion/cartesian\_motion.hpp](cartesian__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include "[franky/motion/cartesian\_velocity\_motion.hpp](cartesian__velocity__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include "[franky/motion/joint\_motion.hpp](joint__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/motion/joint\_velocity\_motion.hpp](joint__velocity__motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/motion/reference\_type.hpp](reference__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> [12](classfranky_1_1_stop_motion.md)</span><span class="keyword">class </span>[StopMotion](classfranky_1_1_stop_motion.md);

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span>

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span><span class="keyword">template</span> \<\>

</div>

<div id="foldopen00018" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](classfranky_1_1_stop_motion_3_01franka_1_1_joint_positions_01_4.md)</span><span class="keyword">class </span>[StopMotion](classfranky_1_1_stop_motion.md)\<franka::[JointPositions](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacae53870521bf0d6aaf73f8435b4c53601)\> : <span class="keyword">public</span> [JointMotion](classfranky_1_1_joint_motion.md) {

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00025" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00025"></span><span class="lineno"> [25](classfranky_1_1_stop_motion_3_01franka_1_1_joint_positions_01_4.md#ab40b9a6791f82a4f5f321fda27652c60)</span> <span class="keyword">explicit</span> [StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_joint_positions_01_4.md#ab40b9a6791f82a4f5f321fda27652c60)(<span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0)

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span> : [JointMotion](classfranky_1_1_joint_motion.md)([JointState](classfranky_1_1_joint_state.md)([Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)::[Zero](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)()), [ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e)::[kRelative](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eaf460a96ab20647996c15854794763384), relative\_dynamics\_factor) {}

</div>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span>};

</div>

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span>

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span><span class="keyword">template</span> \<\>

</div>

<div id="foldopen00033" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00033"></span><span class="lineno"> [33](classfranky_1_1_stop_motion_3_01franka_1_1_joint_velocities_01_4.md)</span><span class="keyword">class </span>[StopMotion](classfranky_1_1_stop_motion.md)\<franka::[JointVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacadecb27858472a616860e32411b1a6854)\> : <span class="keyword">public</span> [JointVelocityMotion](classfranky_1_1_joint_velocity_motion.md) {

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00040" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00040"></span><span class="lineno"> [40](classfranky_1_1_stop_motion_3_01franka_1_1_joint_velocities_01_4.md#ab728e6c9ae095e60e74dd6e1d0337d63)</span> <span class="keyword">explicit</span> [StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_joint_velocities_01_4.md#ab728e6c9ae095e60e74dd6e1d0337d63)(<span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0)

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> : [JointVelocityMotion](classfranky_1_1_joint_velocity_motion.md)([Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4)::[Zero](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(), franka::[Duration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(0), relative\_dynamics\_factor) {}

</div>

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span>};

</div>

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span>

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span><span class="keyword">template</span> \<\>

</div>

<div id="foldopen00048" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00048"></span><span class="lineno"> [48](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_pose_01_4.md)</span><span class="keyword">class </span>[StopMotion](classfranky_1_1_stop_motion.md)\<franka::[CartesianPose](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca982887767b31bb472878f67e6ddbfd9f)\> : <span class="keyword">public</span> [CartesianWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md) {

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00055" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00055"></span><span class="lineno"> [55](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_pose_01_4.md#a5e5d0058e0bf00b8e3b5904b0bf0f1a0)</span> <span class="keyword">explicit</span> [StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_pose_01_4.md#a5e5d0058e0bf00b8e3b5904b0bf0f1a0)(<span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0)

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span> : [CartesianWaypointMotion](classfranky_1_1_cartesian_waypoint_motion.md)(

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span> {[PositionWaypoint\<CartesianState\>](structfranky_1_1_position_waypoint.md){

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> {

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> .[target](structfranky_1_1_waypoint.md#a857fb8417fc17ff5e171494b1d398355) = [RobotPose](classfranky_1_1_robot_pose.md)(),

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span> .hold\_target\_duration = franka::Duration(50),

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> },

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span> [ReferenceType::kRelative](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eaf460a96ab20647996c15854794763384)}},

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> relative\_dynamics\_factor) {}

</div>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span>};

</div>

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span>

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span><span class="keyword">template</span> \<\>

</div>

<div id="foldopen00070" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00070"></span><span class="lineno"> [70](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_velocities_01_4.md)</span><span class="keyword">class </span>[StopMotion](classfranky_1_1_stop_motion.md)\<franka::[CartesianVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca1a276615bdb52bb012d25ccc6ae470d1)\> : <span class="keyword">public</span> [CartesianVelocityMotion](classfranky_1_1_cartesian_velocity_motion.md) {

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00077" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00077"></span><span class="lineno"> [77](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_velocities_01_4.md#acc50ed2297475421f0e9a8a4e9a55dff)</span> <span class="keyword">explicit</span> [StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_velocities_01_4.md#acc50ed2297475421f0e9a8a4e9a55dff)(<span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) \&relative\_dynamics\_factor = 1.0)

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> : [CartesianVelocityMotion](classfranky_1_1_cartesian_velocity_motion.md)([RobotVelocity](classfranky_1_1_robot_velocity.md)(), franka::[Duration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(0), relative\_dynamics\_factor) {}

</div>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span>};

</div>

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span>} <span class="comment">// namespace franky</span>

</div>

<div id="acartesian__motion_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_motion.hpp](cartesian__motion_8hpp.md)

</div>

</div>

<div id="acartesian__velocity__motion_8hpp_html" class="ttc">

<div class="ttname">

[cartesian\_velocity\_motion.hpp](cartesian__velocity__motion_8hpp.md)

</div>

</div>

<div id="aclassfranky_1_1_cartesian_velocity_motion_html" class="ttc">

<div class="ttname">

[franky::CartesianVelocityMotion](classfranky_1_1_cartesian_velocity_motion.md)

</div>

<div class="ttdoc">

Cartesian velocity motion with a single target velocity.

</div>

<div class="ttdef">

**Definition** cartesian\_velocity\_motion.hpp:10

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

<div id="aclassfranky_1_1_joint_motion_html" class="ttc">

<div class="ttname">

[franky::JointMotion](classfranky_1_1_joint_motion.md)

</div>

<div class="ttdoc">

Joint motion with a single target.

</div>

<div class="ttdef">

**Definition** joint\_motion.hpp:12

</div>

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

<div id="aclassfranky_1_1_joint_velocity_motion_html" class="ttc">

<div class="ttname">

[franky::JointVelocityMotion](classfranky_1_1_joint_velocity_motion.md)

</div>

<div class="ttdoc">

Joint velocity motion with a single target.

</div>

<div class="ttdef">

**Definition** joint\_velocity\_motion.hpp:11

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

<div id="aclassfranky_1_1_robot_pose_html" class="ttc">

<div class="ttname">

[franky::RobotPose](classfranky_1_1_robot_pose.md)

</div>

<div class="ttdoc">

Cartesian pose of a robot.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:19

</div>

</div>

<div id="aclassfranky_1_1_robot_velocity_html" class="ttc">

<div class="ttname">

[franky::RobotVelocity](classfranky_1_1_robot_velocity.md)

</div>

<div class="ttdoc">

Cartesian velocity of a robot.

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:20

</div>

</div>

<div id="aclassfranky_1_1_stop_motion_3_01franka_1_1_cartesian_pose_01_4_html_a5e5d0058e0bf00b8e3b5904b0bf0f1a0" class="ttc">

<div class="ttname">

[franky::StopMotion\< franka::CartesianPose \>::StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_pose_01_4.md#a5e5d0058e0bf00b8e3b5904b0bf0f1a0)

</div>

<div class="ttdeci">

StopMotion(const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)

</div>

<div class="ttdef">

**Definition** stop\_motion.hpp:55

</div>

</div>

<div id="aclassfranky_1_1_stop_motion_3_01franka_1_1_cartesian_velocities_01_4_html_acc50ed2297475421f0e9a8a4e9a55dff" class="ttc">

<div class="ttname">

[franky::StopMotion\< franka::CartesianVelocities \>::StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_cartesian_velocities_01_4.md#acc50ed2297475421f0e9a8a4e9a55dff)

</div>

<div class="ttdeci">

StopMotion(const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)

</div>

<div class="ttdef">

**Definition** stop\_motion.hpp:77

</div>

</div>

<div id="aclassfranky_1_1_stop_motion_3_01franka_1_1_joint_positions_01_4_html_ab40b9a6791f82a4f5f321fda27652c60" class="ttc">

<div class="ttname">

[franky::StopMotion\< franka::JointPositions \>::StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_joint_positions_01_4.md#ab40b9a6791f82a4f5f321fda27652c60)

</div>

<div class="ttdeci">

StopMotion(const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)

</div>

<div class="ttdef">

**Definition** stop\_motion.hpp:25

</div>

</div>

<div id="aclassfranky_1_1_stop_motion_3_01franka_1_1_joint_velocities_01_4_html_ab728e6c9ae095e60e74dd6e1d0337d63" class="ttc">

<div class="ttname">

[franky::StopMotion\< franka::JointVelocities \>::StopMotion](classfranky_1_1_stop_motion_3_01franka_1_1_joint_velocities_01_4.md#ab728e6c9ae095e60e74dd6e1d0337d63)

</div>

<div class="ttdeci">

StopMotion(const RelativeDynamicsFactor \&relative\_dynamics\_factor=1.0)

</div>

<div class="ttdef">

**Definition** stop\_motion.hpp:40

</div>

</div>

<div id="aclassfranky_1_1_stop_motion_html" class="ttc">

<div class="ttname">

[franky::StopMotion](classfranky_1_1_stop_motion.md)

</div>

<div class="ttdef">

**Definition** stop\_motion.hpp:12

</div>

</div>

<div id="ajoint__motion_8hpp_html" class="ttc">

<div class="ttname">

[joint\_motion.hpp](joint__motion_8hpp.md)

</div>

</div>

<div id="ajoint__velocity__motion_8hpp_html" class="ttc">

<div class="ttname">

[joint\_velocity\_motion.hpp](joint__velocity__motion_8hpp.md)

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

<div id="anamespacefranky_html_a2354a27cfe3100f07e0ad71513ded80eaf460a96ab20647996c15854794763384" class="ttc">

<div class="ttname">

[franky::ReferenceType::kRelative](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eaf460a96ab20647996c15854794763384)

</div>

<div class="ttdeci">

@ kRelative

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

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaaca1a276615bdb52bb012d25ccc6ae470d1" class="ttc">

<div class="ttname">

[franky::CartesianVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca1a276615bdb52bb012d25ccc6ae470d1)

</div>

<div class="ttdeci">

@ CartesianVelocities

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaaca982887767b31bb472878f67e6ddbfd9f" class="ttc">

<div class="ttname">

[franky::CartesianPose](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaaca982887767b31bb472878f67e6ddbfd9f)

</div>

<div class="ttdeci">

@ CartesianPose

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaacadecb27858472a616860e32411b1a6854" class="ttc">

<div class="ttname">

[franky::JointVelocities](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacadecb27858472a616860e32411b1a6854)

</div>

<div class="ttdeci">

@ JointVelocities

</div>

<div class="ttdef">

**Definition** control\_signal\_type.hpp:8

</div>

</div>

<div id="anamespacefranky_html_a9a12fea9c3341e3437af837efe8ebaacae53870521bf0d6aaf73f8435b4c53601" class="ttc">

<div class="ttname">

[franky::JointPositions](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaacae53870521bf0d6aaf73f8435b4c53601)

</div>

<div class="ttdeci">

@ JointPositions

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

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
