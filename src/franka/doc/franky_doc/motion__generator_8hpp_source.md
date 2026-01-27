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

motion\_generator.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](motion__generator_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/duration.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<franka/robot\_state.h\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<memory\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include \<mutex\></span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include "[franky/robot\_state.hpp](robot__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="preprocessor">\#include "ruckig/ruckig.hpp"</span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span>

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span>

</div>

<div id="foldopen00018" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](structfranky_1_1_reaction_recursion_exception.md)</span><span class="keyword">struct </span>[ReactionRecursionException](structfranky_1_1_reaction_recursion_exception.md) : <span class="keyword">public</span> std::runtime\_error {

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span> <span class="keyword">using </span>std::runtime\_error::runtime\_error;

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span>};

</div>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span>

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span><span class="keyword">class </span>[Robot](classfranky_1_1_robot.md);

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span>

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span><span class="keyword">class </span>[Motion](classfranky_1_1_motion.md);

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span>

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span><span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div id="foldopen00031" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00031"></span><span class="lineno"> [31](classfranky_1_1_motion_generator.md)</span><span class="keyword">class </span>[MotionGenerator](classfranky_1_1_motion_generator.md) {

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> [38](classfranky_1_1_motion_generator.md#a2dceaaa3e924424fc57f68b5e1955712)</span> <span class="keyword">static</span> <span class="keyword">constexpr</span> <span class="keywordtype">size\_t</span> [REACTION\_RECURSION\_LIMIT](classfranky_1_1_motion_generator.md#a2dceaaa3e924424fc57f68b5e1955712) = 16;

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span>

</div>

<div class="line">

<span id="l00044"></span><span class="lineno"> 44</span> <span class="keyword">explicit</span> [MotionGenerator](classfranky_1_1_motion_generator.md)([Robot](classfranky_1_1_robot.md) \*robot, std::shared\_ptr\<[Motion\<ControlSignalType\>](classfranky_1_1_motion.md)\> initial\_motion);

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span>

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) [operator()](classfranky_1_1_motion_generator.md#a751c6f2d51740e613c6575b1f62e1dfa)(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) \&robot\_state, franka::Duration period);

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span>

</div>

<div id="foldopen00060" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00060"></span><span class="lineno"> [60](classfranky_1_1_motion_generator.md#a771a92b07e8c384ec56fd014841ed5f2)</span> <span class="keyword">inline</span> <span class="keywordtype">void</span> [registerUpdateCallback](classfranky_1_1_motion_generator.md#a771a92b07e8c384ec56fd014841ed5f2)(

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span> <span class="keyword">const</span> std::function\<<span class="keywordtype">void</span>(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\> \&callback) {

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span> update\_callbacks\_.push\_back(callback);

</div>

<div class="line">

<span id="l00063"></span><span class="lineno"> 63</span> }

</div>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span>

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> <span class="keywordtype">void</span> [updateMotion](classfranky_1_1_motion_generator.md#aecb5394cc1571687e1117e268f91e9c1)(std::shared\_ptr\<[Motion\<ControlSignalType\>](classfranky_1_1_motion.md)\> new\_motion);

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span> <span class="keywordtype">bool</span> [has\_new\_motion](classfranky_1_1_motion_generator.md#ad0abb8a6c37b8ab8208810bb58250bf8)();

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span>

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> <span class="keywordtype">void</span> [resetTimeUnsafe](classfranky_1_1_motion_generator.md#aaa6cf6fa7c6af2d7b081b19d569c2e0f)();

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span> std::shared\_ptr\<Motion\<ControlSignalType\>\> initial\_motion\_;

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> 83</span> std::shared\_ptr\<Motion\<ControlSignalType\>\> current\_motion\_;

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span> std::shared\_ptr\<Motion\<ControlSignalType\>\> new\_motion\_;

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span> std::vector\<std::function\<void(<span class="keyword">const</span> [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration)\>\> update\_callbacks\_;

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span> std::mutex new\_motion\_mutex\_;

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span> std::optional\<ControlSignalType\> previous\_command\_;

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span>

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span> franka::Duration abs\_time\_{0};

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span> franka::Duration rel\_time\_offset\_{0};

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span> Robot \*robot\_;

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

<div id="aclassfranky_1_1_motion_generator_html" class="ttc">

<div class="ttname">

[franky::MotionGenerator](classfranky_1_1_motion_generator.md)

</div>

<div class="ttdoc">

Helper class for handling motions and reactions.

</div>

<div class="ttdef">

**Definition** motion\_generator.hpp:31

</div>

</div>

<div id="aclassfranky_1_1_motion_generator_html_a2dceaaa3e924424fc57f68b5e1955712" class="ttc">

<div class="ttname">

[franky::MotionGenerator::REACTION\_RECURSION\_LIMIT](classfranky_1_1_motion_generator.md#a2dceaaa3e924424fc57f68b5e1955712)

</div>

<div class="ttdeci">

static constexpr size\_t REACTION\_RECURSION\_LIMIT

</div>

<div class="ttdoc">

Maximum recursion limit for reactions. After more than this number of reactions are fired in a single...

</div>

<div class="ttdef">

**Definition** motion\_generator.hpp:38

</div>

</div>

<div id="aclassfranky_1_1_motion_generator_html_a751c6f2d51740e613c6575b1f62e1dfa" class="ttc">

<div class="ttname">

[franky::MotionGenerator::operator()](classfranky_1_1_motion_generator.md#a751c6f2d51740e613c6575b1f62e1dfa)

</div>

<div class="ttdeci">

ControlSignalType operator()(const RobotState \&robot\_state, franka::Duration period)

</div>

<div class="ttdoc">

Update the motion generator and get the next control signal.

</div>

<div class="ttdef">

**Definition** motion\_generator.cpp:27

</div>

</div>

<div id="aclassfranky_1_1_motion_generator_html_a771a92b07e8c384ec56fd014841ed5f2" class="ttc">

<div class="ttname">

[franky::MotionGenerator::registerUpdateCallback](classfranky_1_1_motion_generator.md#a771a92b07e8c384ec56fd014841ed5f2)

</div>

<div class="ttdeci">

void registerUpdateCallback(const std::function\< void(const RobotState &, franka::Duration, franka::Duration)\> \&callback)

</div>

<div class="ttdoc">

Register a callback that is called in every step of the motion.

</div>

<div class="ttdef">

**Definition** motion\_generator.hpp:60

</div>

</div>

<div id="aclassfranky_1_1_motion_generator_html_aaa6cf6fa7c6af2d7b081b19d569c2e0f" class="ttc">

<div class="ttname">

[franky::MotionGenerator::resetTimeUnsafe](classfranky_1_1_motion_generator.md#aaa6cf6fa7c6af2d7b081b19d569c2e0f)

</div>

<div class="ttdeci">

void resetTimeUnsafe()

</div>

<div class="ttdoc">

Reset the time of the motion generator without locking the mutex.

</div>

<div class="ttdef">

**Definition** motion\_generator.cpp:90

</div>

</div>

<div id="aclassfranky_1_1_motion_generator_html_ad0abb8a6c37b8ab8208810bb58250bf8" class="ttc">

<div class="ttname">

[franky::MotionGenerator::has\_new\_motion](classfranky_1_1_motion_generator.md#ad0abb8a6c37b8ab8208810bb58250bf8)

</div>

<div class="ttdeci">

bool has\_new\_motion()

</div>

<div class="ttdoc">

Whether a new motion is available.

</div>

<div class="ttdef">

**Definition** motion\_generator.cpp:85

</div>

</div>

<div id="aclassfranky_1_1_motion_generator_html_aecb5394cc1571687e1117e268f91e9c1" class="ttc">

<div class="ttname">

[franky::MotionGenerator::updateMotion](classfranky_1_1_motion_generator.md#aecb5394cc1571687e1117e268f91e9c1)

</div>

<div class="ttdeci">

void updateMotion(std::shared\_ptr\< Motion\< ControlSignalType \> \> new\_motion)

</div>

<div class="ttdoc">

Update the current motion.

</div>

<div class="ttdef">

**Definition** motion\_generator.cpp:79

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

<div id="arobot__state_8hpp_html" class="ttc">

<div class="ttname">

[robot\_state.hpp](robot__state_8hpp.md)

</div>

</div>

<div id="astructfranky_1_1_reaction_recursion_exception_html" class="ttc">

<div class="ttname">

[franky::ReactionRecursionException](structfranky_1_1_reaction_recursion_exception.md)

</div>

<div class="ttdoc">

Exception thrown when the reaction recursion limit (8) is reached.

</div>

<div class="ttdef">

**Definition** motion\_generator.hpp:18

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

<div id="atypes_8hpp_html" class="ttc">

<div class="ttname">

[types.hpp](types_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
