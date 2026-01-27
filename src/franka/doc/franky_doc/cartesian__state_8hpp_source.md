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

cartesian\_state.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](cartesian__state_8hpp.md)

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

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include "[franky/robot\_pose.hpp](robot__pose_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include "[franky/robot\_velocity.hpp](robot__velocity_8hpp.md)"</span>

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

<span id="l00011"></span><span class="lineno"> 11</span><span class="comment">/\*</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="comment"> \* @brief Cartesian state of a robot.</span>

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span><span class="comment"> \*</span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span><span class="comment"> \* This class encapsulates the cartesian state of a robot, which comprises the</span>

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span><span class="comment"> \* end effector pose and the end effector velocity.</span>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span><span class="comment"> \*/</span>

</div>

<div id="foldopen00017" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00017"></span><span class="lineno"> [17](classfranky_1_1_cartesian_state.md)</span><span class="keyword">class </span>[CartesianState](classfranky_1_1_cartesian_state.md) {

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> 18</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span> <span class="comment">// Suppress implicit conversion warning</span>

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span><span class="preprocessor">\#pragma clang diagnostic push</span>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span><span class="preprocessor">\#pragma clang diagnostic ignored "-Wimplicit-conversion"</span>

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> [22](classfranky_1_1_cartesian_state.md#a7764a37806a5bb6cd2539f520ee2333c)</span> [CartesianState](classfranky_1_1_cartesian_state.md#a7764a37806a5bb6cd2539f520ee2333c)(<span class="keyword">const</span> [RobotPose](classfranky_1_1_robot_pose.md) &[pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)) : pose\_([pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)) {}

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span><span class="preprocessor">\#pragma clang diagnostic pop</span>

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span>

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> [29](classfranky_1_1_cartesian_state.md#a5bd6839fb4e69757aa4525b913adfc79)</span> [CartesianState](classfranky_1_1_cartesian_state.md#a5bd6839fb4e69757aa4525b913adfc79)(<span class="keyword">const</span> [RobotPose](classfranky_1_1_robot_pose.md) &[pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b), <span class="keyword">const</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) &[velocity](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f)) : pose\_([pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)), velocity\_([velocity](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f)) {}

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> [31](classfranky_1_1_cartesian_state.md#aae23bc79979e802bb6242d7c720dad4a)</span> [CartesianState](classfranky_1_1_cartesian_state.md#aae23bc79979e802bb6242d7c720dad4a)(<span class="keyword">const</span> [CartesianState](classfranky_1_1_cartesian_state.md) &) = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span>

</div>

<div class="line">

<span id="l00033"></span><span class="lineno"> [33](classfranky_1_1_cartesian_state.md#aafe4a81eeddb9212361603d79b3bb0bd)</span> [CartesianState](classfranky_1_1_cartesian_state.md#aafe4a81eeddb9212361603d79b3bb0bd)() = <span class="keywordflow">default</span>;

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span>

</div>

<div id="foldopen00042" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00042"></span><span class="lineno"> [42](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)</span> \[\[nodiscard\]\] [CartesianState](classfranky_1_1_cartesian_state.md) [transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform)<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span> <span class="keywordflow">return</span> {transform \* pose\_, transform \* velocity\_};

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> }

</div>

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span>

</div>

<div id="foldopen00054" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00054"></span><span class="lineno"> [54](classfranky_1_1_cartesian_state.md#a95522df649508eed67ac81cf21ca1b08)</span> \[\[nodiscard\]\] [CartesianState](classfranky_1_1_cartesian_state.md) [changeEndEffectorFrame](classfranky_1_1_cartesian_state.md#a95522df649508eed67ac81cf21ca1b08)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform)<span class="keyword"> const </span>{

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span> <span class="keyword">auto</span> offset\_world\_frame = pose\_.[end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd)() \* transform.translation();

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span> <span class="keywordflow">return</span> {pose\_.[changeEndEffectorFrame](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba)(transform), velocity\_.[changeEndEffectorFrame](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95)(offset\_world\_frame)};

</div>

<div class="line">

<span id="l00057"></span><span class="lineno"> 57</span> }

</div>

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span>

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> <span class="comment">/\*</span>

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span><span class="comment"> \* @brief Pose component of the state.</span>

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span><span class="comment"> \*/</span>

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> [62](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)</span> \[\[nodiscard\]\] [RobotPose](classfranky_1_1_robot_pose.md) [pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> pose\_; }

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> <span class="comment">/\*</span>

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span><span class="comment"> \* @brief Velocity component of the state.</span>

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span><span class="comment"> \*/</span>

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> [67](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f)</span> \[\[nodiscard\]\] [RobotVelocity](classfranky_1_1_robot_velocity.md) [velocity](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> velocity\_; }

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span>

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> <span class="keyword">friend</span> <span class="keyword">inline</span> std::ostream &[operator\<\<](classfranky_1_1_cartesian_state.md#a4889934eab07f3d4fac6c8c9ea9d3009)(std::ostream \&os, <span class="keyword">const</span> [CartesianState](classfranky_1_1_cartesian_state.md) \&cartesian\_state);

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span> [RobotPose](classfranky_1_1_robot_pose.md) pose\_;

</div>

<div class="line">

<span id="l00073"></span><span class="lineno"> 73</span> [RobotVelocity](classfranky_1_1_robot_velocity.md) velocity\_;

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span>};

</div>

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span>

</div>

<div id="foldopen00076" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00076"></span><span class="lineno"> [76](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)</span><span class="keyword">inline</span> [CartesianState](classfranky_1_1_cartesian_state.md) [operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)(<span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) \&transform, <span class="keyword">const</span> [CartesianState](classfranky_1_1_cartesian_state.md) \&cartesian\_state) {

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span> <span class="keywordflow">return</span> cartesian\_state.[transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)(transform);

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span>}

</div>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span>

</div>

<div id="foldopen00080" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00080"></span><span class="lineno"> [80](classfranky_1_1_cartesian_state.md#a4889934eab07f3d4fac6c8c9ea9d3009)</span><span class="keyword">inline</span> std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream \&os, <span class="keyword">const</span> [CartesianState](classfranky_1_1_cartesian_state.md) \&cartesian\_state) {

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span> os \<\< <span class="stringliteral">"CartesianState(pose="</span> \<\< cartesian\_state.pose\_ \<\< <span class="stringliteral">", velocity="</span> \<\< cartesian\_state.velocity\_ \<\< <span class="stringliteral">")"</span>;

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> <span class="keywordflow">return</span> os;

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span>}

</div>

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span>

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span>} <span class="comment">// namespace franky</span>

</div>

<div id="aclassfranky_1_1_cartesian_state_html" class="ttc">

<div class="ttname">

[franky::CartesianState](classfranky_1_1_cartesian_state.md)

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:17

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_a4889934eab07f3d4fac6c8c9ea9d3009" class="ttc">

<div class="ttname">

[franky::CartesianState::operator\<\<](classfranky_1_1_cartesian_state.md#a4889934eab07f3d4fac6c8c9ea9d3009)

</div>

<div class="ttdeci">

friend std::ostream & operator\<\<(std::ostream \&os, const CartesianState \&cartesian\_state)

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:80

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_a5bd6839fb4e69757aa4525b913adfc79" class="ttc">

<div class="ttname">

[franky::CartesianState::CartesianState](classfranky_1_1_cartesian_state.md#a5bd6839fb4e69757aa4525b913adfc79)

</div>

<div class="ttdeci">

CartesianState(const RobotPose \&pose, const RobotVelocity \&velocity)

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:29

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_a5e8e2c8161dc22d18a01a0c28897792b" class="ttc">

<div class="ttname">

[franky::CartesianState::pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)

</div>

<div class="ttdeci">

RobotPose pose() const

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:62

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_a7764a37806a5bb6cd2539f520ee2333c" class="ttc">

<div class="ttname">

[franky::CartesianState::CartesianState](classfranky_1_1_cartesian_state.md#a7764a37806a5bb6cd2539f520ee2333c)

</div>

<div class="ttdeci">

CartesianState(const RobotPose \&pose)

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:22

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_a95522df649508eed67ac81cf21ca1b08" class="ttc">

<div class="ttname">

[franky::CartesianState::changeEndEffectorFrame](classfranky_1_1_cartesian_state.md#a95522df649508eed67ac81cf21ca1b08)

</div>

<div class="ttdeci">

CartesianState changeEndEffectorFrame(const Affine \&transform) const

</div>

<div class="ttdoc">

Change the end effector frame of the state by the given affine transform.

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:54

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_a9f7b644b3920e5816554b8855854a1aa" class="ttc">

<div class="ttname">

[franky::CartesianState::transformWith](classfranky_1_1_cartesian_state.md#a9f7b644b3920e5816554b8855854a1aa)

</div>

<div class="ttdeci">

CartesianState transformWith(const Affine \&transform) const

</div>

<div class="ttdoc">

Transform the frame of the state by applying the given affine transform.

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:42

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_aae23bc79979e802bb6242d7c720dad4a" class="ttc">

<div class="ttname">

[franky::CartesianState::CartesianState](classfranky_1_1_cartesian_state.md#aae23bc79979e802bb6242d7c720dad4a)

</div>

<div class="ttdeci">

CartesianState(const CartesianState &)=default

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_aafe4a81eeddb9212361603d79b3bb0bd" class="ttc">

<div class="ttname">

[franky::CartesianState::CartesianState](classfranky_1_1_cartesian_state.md#aafe4a81eeddb9212361603d79b3bb0bd)

</div>

<div class="ttdeci">

CartesianState()=default

</div>

</div>

<div id="aclassfranky_1_1_cartesian_state_html_ac212d0fc0f7b8f05baa3da6389bcf52f" class="ttc">

<div class="ttname">

[franky::CartesianState::velocity](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f)

</div>

<div class="ttdeci">

RobotVelocity velocity() const

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:67

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

<div id="aclassfranky_1_1_robot_pose_html_a132eef8bd15ba00132fb64ed441382ba" class="ttc">

<div class="ttname">

[franky::RobotPose::changeEndEffectorFrame](classfranky_1_1_robot_pose.md#a132eef8bd15ba00132fb64ed441382ba)

</div>

<div class="ttdeci">

RobotPose changeEndEffectorFrame(const Affine \&transform) const

</div>

<div class="ttdoc">

Change the frame of the end effector by applying a transformation from the right side....

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:104

</div>

</div>

<div id="aclassfranky_1_1_robot_pose_html_abe83d0dc121a5e1312ac4f2acdbd9fbd" class="ttc">

<div class="ttname">

[franky::RobotPose::end\_effector\_pose](classfranky_1_1_robot_pose.md#abe83d0dc121a5e1312ac4f2acdbd9fbd)

</div>

<div class="ttdeci">

Affine end\_effector\_pose() const

</div>

<div class="ttdoc">

Get the end effector pose.

</div>

<div class="ttdef">

**Definition** robot\_pose.hpp:121

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

<div id="aclassfranky_1_1_robot_velocity_html_ab7fe3ffb8b3a627027d6441d57223c95" class="ttc">

<div class="ttname">

[franky::RobotVelocity::changeEndEffectorFrame](classfranky_1_1_robot_velocity.md#ab7fe3ffb8b3a627027d6441d57223c95)

</div>

<div class="ttdeci">

RobotVelocity changeEndEffectorFrame(const Eigen::Vector3d \&offset\_world\_frame) const

</div>

<div class="ttdoc">

Change the end-effector frame by adding the given offset to the current end-effector frame....

</div>

<div class="ttdef">

**Definition** robot\_velocity.hpp:105

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

<div id="anamespacefranky_html_a054ba89edc6e3948f2dfb5721aaa8bb4" class="ttc">

<div class="ttname">

[franky::operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)

</div>

<div class="ttdeci">

std::ostream & operator\<\<(std::ostream \&os, const DynamicsLimit\< Vector7d \> \&limit)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:47

</div>

</div>

<div id="anamespacefranky_html_a4c30c0e173a1886238ed773e005be361" class="ttc">

<div class="ttname">

[franky::operator\*](namespacefranky.md#a4c30c0e173a1886238ed773e005be361)

</div>

<div class="ttdeci">

CartesianState operator\*(const Affine \&transform, const CartesianState \&cartesian\_state)

</div>

<div class="ttdef">

**Definition** cartesian\_state.hpp:76

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

<div id="arobot__pose_8hpp_html" class="ttc">

<div class="ttname">

[robot\_pose.hpp](robot__pose_8hpp.md)

</div>

</div>

<div id="arobot__velocity_8hpp_html" class="ttc">

<div class="ttname">

[robot\_velocity.hpp](robot__velocity_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
