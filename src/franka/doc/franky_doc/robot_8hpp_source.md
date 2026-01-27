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

robot.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](robot_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/control\_types.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span><span class="preprocessor">\#include \<franka/duration.h\></span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<franka/exception.h\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<franka/robot.h\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span><span class="preprocessor">\#include \<franka/robot\_state.h\></span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span>

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span><span class="preprocessor">\#include \<exception\></span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="preprocessor">\#include \<future\></span>

</div>

<div class="line">

<span id="l00011"></span><span class="lineno"> 11</span><span class="preprocessor">\#include \<optional\></span>

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span><span class="preprocessor">\#include \<stdexcept\></span>

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span><span class="preprocessor">\#include \<variant\></span>

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span>

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span><span class="preprocessor">\#include "[franky/cartesian\_state.hpp](cartesian__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span><span class="preprocessor">\#include "[franky/control\_signal\_type.hpp](control__signal__type_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span><span class="preprocessor">\#include "[franky/dynamics\_limit.hpp](dynamics__limit_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00018"></span><span class="lineno"> 18</span><span class="preprocessor">\#include "[franky/joint\_state.hpp](joint__state_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span><span class="preprocessor">\#include "[franky/model.hpp](model_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span><span class="preprocessor">\#include "[franky/motion/motion.hpp](motion_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span><span class="preprocessor">\#include "[franky/motion/motion\_generator.hpp](motion__generator_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span><span class="preprocessor">\#include "[franky/relative\_dynamics\_factor.hpp](relative__dynamics__factor_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00023"></span><span class="lineno"> 23</span><span class="preprocessor">\#include "[franky/robot\_pose.hpp](robot__pose_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span><span class="preprocessor">\#include "[franky/robot\_state\_estimator.hpp](robot__state__estimator_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span><span class="preprocessor">\#include "[franky/robot\_velocity.hpp](robot__velocity_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span><span class="preprocessor">\#include "[franky/types.hpp](types_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span><span class="preprocessor">\#include "[franky/util.hpp](util_8hpp.md)"</span>

</div>

<div class="line">

<span id="l00028"></span><span class="lineno"> 28</span>

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span>

</div>

<div id="foldopen00037" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00037"></span><span class="lineno"> [37](structfranky_1_1_invalid_motion_type_exception.md)</span><span class="keyword">struct </span>[InvalidMotionTypeException](structfranky_1_1_invalid_motion_type_exception.md) : std::runtime\_error {

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span> <span class="keyword">using </span>std::runtime\_error::runtime\_error;

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span>};

</div>

</div>

<div class="line">

<span id="l00040"></span><span class="lineno"> 40</span>

</div>

<div id="foldopen00047" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00047"></span><span class="lineno"> [47](classfranky_1_1_robot.md)</span><span class="keyword">class </span>[Robot](classfranky_1_1_robot.md) : <span class="keyword">public</span> franka::Robot {

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span> <span class="keyword">public</span>:

</div>

<div id="foldopen00052" class="foldopen" data-start="{" data-end="};">

<div class="line">

<span id="l00052"></span><span class="lineno"> [52](structfranky_1_1_robot_1_1_params.md)</span> <span class="keyword">struct </span>[Params](structfranky_1_1_robot_1_1_params.md) {

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> [59](structfranky_1_1_robot_1_1_params.md#a232bd0323512dd23a1e6003c906eb328)</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) [relative\_dynamics\_factor](structfranky_1_1_robot_1_1_params.md#a232bd0323512dd23a1e6003c906eb328){1.0};

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> [64](structfranky_1_1_robot_1_1_params.md#ac52be6b32e29563c8bb6576679bcbfa5)</span> <span class="keywordtype">double</span> [default\_torque\_threshold](structfranky_1_1_robot_1_1_params.md#ac52be6b32e29563c8bb6576679bcbfa5){20.0};

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span>

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> [69](structfranky_1_1_robot_1_1_params.md#a2535f117ddde7fd4294eeb952d4746bd)</span> <span class="keywordtype">double</span> [default\_force\_threshold](structfranky_1_1_robot_1_1_params.md#a2535f117ddde7fd4294eeb952d4746bd){30.0};

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>

</div>

<div class="line">

<span id="l00076"></span><span class="lineno"> [76](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083)</span> franka::ControllerMode [controller\_mode](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083){franka::ControllerMode::kJointImpedance};

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span>

</div>

<div class="line">

<span id="l00083"></span><span class="lineno"> [83](structfranky_1_1_robot_1_1_params.md#a7c8199f22e083645746aa47020c97d56)</span> franka::RealtimeConfig [realtime\_config](structfranky_1_1_robot_1_1_params.md#a7c8199f22e083645746aa47020c97d56){franka::RealtimeConfig::kEnforce};

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span>

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> [88](structfranky_1_1_robot_1_1_params.md#ae6c5c63f100b88ae3fc1ae3dcd50c44e)</span> <span class="keywordtype">double</span> [kalman\_q\_process\_var](structfranky_1_1_robot_1_1_params.md#ae6c5c63f100b88ae3fc1ae3dcd50c44e) = 0.0001;

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span>

</div>

<div class="line">

<span id="l00093"></span><span class="lineno"> [93](structfranky_1_1_robot_1_1_params.md#a1e9c37c50668090f408db94e12e54bc9)</span> <span class="keywordtype">double</span> [kalman\_dq\_process\_var](structfranky_1_1_robot_1_1_params.md#a1e9c37c50668090f408db94e12e54bc9) = 0.001;

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span>

</div>

<div class="line">

<span id="l00098"></span><span class="lineno"> [98](structfranky_1_1_robot_1_1_params.md#acd2d77ccd361a615b18b0a89fa0b2dd0)</span> <span class="keywordtype">double</span> [kalman\_ddq\_process\_var](structfranky_1_1_robot_1_1_params.md#acd2d77ccd361a615b18b0a89fa0b2dd0) = 0.1;

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span>

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> [103](structfranky_1_1_robot_1_1_params.md#a62b242c8c50ac828af9ac497b3cba801)</span> <span class="keywordtype">double</span> [kalman\_control\_process\_var](structfranky_1_1_robot_1_1_params.md#a62b242c8c50ac828af9ac497b3cba801) = 1;

</div>

<div class="line">

<span id="l00104"></span><span class="lineno"> 104</span>

</div>

<div class="line">

<span id="l00109"></span><span class="lineno"> [109](structfranky_1_1_robot_1_1_params.md#a304e57064f927eb2c00757a1d86d2e08)</span> <span class="keywordtype">double</span> [kalman\_q\_obs\_var](structfranky_1_1_robot_1_1_params.md#a304e57064f927eb2c00757a1d86d2e08) = 0.01;

</div>

<div class="line">

<span id="l00110"></span><span class="lineno"> 110</span>

</div>

<div class="line">

<span id="l00115"></span><span class="lineno"> [115](structfranky_1_1_robot_1_1_params.md#a2bccca1dff1d1cd4c4d7d1f0cae03f7b)</span> <span class="keywordtype">double</span> [kalman\_dq\_obs\_var](structfranky_1_1_robot_1_1_params.md#a2bccca1dff1d1cd4c4d7d1f0cae03f7b) = 0.1;

</div>

<div class="line">

<span id="l00116"></span><span class="lineno"> 116</span>

</div>

<div class="line">

<span id="l00121"></span><span class="lineno"> [121](structfranky_1_1_robot_1_1_params.md#a78a7c309785935bab49cdb24b5a750a8)</span> <span class="keywordtype">double</span> [kalman\_q\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#a78a7c309785935bab49cdb24b5a750a8) = 0.0001;

</div>

<div class="line">

<span id="l00122"></span><span class="lineno"> 122</span>

</div>

<div class="line">

<span id="l00127"></span><span class="lineno"> [127](structfranky_1_1_robot_1_1_params.md#a51f8d9dbacca9c18de1b2429bea65dae)</span> <span class="keywordtype">double</span> [kalman\_dq\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#a51f8d9dbacca9c18de1b2429bea65dae) = 0.0001;

</div>

<div class="line">

<span id="l00128"></span><span class="lineno"> 128</span>

</div>

<div class="line">

<span id="l00133"></span><span class="lineno"> [133](structfranky_1_1_robot_1_1_params.md#abeaee212f2cac08ce47158dc44bb6b71)</span> <span class="keywordtype">double</span> [kalman\_ddq\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#abeaee212f2cac08ce47158dc44bb6b71) = 0.0001;

</div>

<div class="line">

<span id="l00134"></span><span class="lineno"> 134</span>

</div>

<div class="line">

<span id="l00139"></span><span class="lineno"> [139](structfranky_1_1_robot_1_1_params.md#a28da04d85b05bdc0483931fdb5ee9665)</span> <span class="keywordtype">double</span> [kalman\_control\_adaptation\_rate](structfranky_1_1_robot_1_1_params.md#a28da04d85b05bdc0483931fdb5ee9665) = 0.1;

</div>

<div class="line">

<span id="l00140"></span><span class="lineno"> 140</span> };

</div>

</div>

<div class="line">

<span id="l00141"></span><span class="lineno"> 141</span>

</div>

<div class="line">

<span id="l00143"></span><span class="lineno"> [143](classfranky_1_1_robot.md#aba9f9254a1af4fea2af758c450399c4c)</span> <span class="keyword">static</span> <span class="keyword">constexpr</span> <span class="keywordtype">size\_t</span> [degrees\_of\_freedoms](classfranky_1_1_robot.md#aba9f9254a1af4fea2af758c450399c4c){7};

</div>

<div class="line">

<span id="l00144"></span><span class="lineno"> 144</span>

</div>

<div class="line">

<span id="l00146"></span><span class="lineno"> [146](classfranky_1_1_robot.md#a3155de462f5590cc67b2874acf846f53)</span> <span class="keyword">static</span> <span class="keyword">constexpr</span> <span class="keywordtype">double</span> [control\_rate](classfranky_1_1_robot.md#a3155de462f5590cc67b2874acf846f53){0.001};

</div>

<div class="line">

<span id="l00147"></span><span class="lineno"> 147</span>

</div>

<div class="line">

<span id="l00151"></span><span class="lineno"> 151</span> <span class="keyword">explicit</span> [Robot](classfranky_1_1_robot.md)(<span class="keyword">const</span> std::string &[fci\_hostname](classfranky_1_1_robot.md#a25ca7e90c8a10848921fb35a378a7d33));

</div>

<div class="line">

<span id="l00152"></span><span class="lineno"> 152</span>

</div>

<div class="line">

<span id="l00157"></span><span class="lineno"> 157</span> <span class="keyword">explicit</span> [Robot](classfranky_1_1_robot.md)(<span class="keyword">const</span> std::string &[fci\_hostname](classfranky_1_1_robot.md#a25ca7e90c8a10848921fb35a378a7d33), <span class="keyword">const</span> Params &[params](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00158"></span><span class="lineno"> 158</span>

</div>

<div class="line">

<span id="l00159"></span><span class="lineno"> 159</span> <span class="keyword">using </span>franka::Robot::setCollisionBehavior;

</div>

<div class="line">

<span id="l00160"></span><span class="lineno"> 160</span>

</div>

<div class="line">

<span id="l00168"></span><span class="lineno"> 168</span> <span class="keywordtype">void</span> [setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373)(<span class="keyword">const</span> [ScalarOrArray\<7\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[torque\_threshold](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [ScalarOrArray\<6\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[force\_threshold](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00169"></span><span class="lineno"> 169</span>

</div>

<div class="line">

<span id="l00182"></span><span class="lineno"> 182</span> <span class="keywordtype">void</span> [setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373)(

</div>

<div class="line">

<span id="l00183"></span><span class="lineno"> 183</span> <span class="keyword">const</span> [ScalarOrArray\<7\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[lower\_torque\_threshold](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [ScalarOrArray\<7\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[upper\_torque\_threshold](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00184"></span><span class="lineno"> 184</span> <span class="keyword">const</span> [ScalarOrArray\<6\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[lower\_force\_threshold](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [ScalarOrArray\<6\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[upper\_force\_threshold](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00185"></span><span class="lineno"> 185</span>

</div>

<div class="line">

<span id="l00206"></span><span class="lineno"> 206</span> <span class="keywordtype">void</span> [setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373)(

</div>

<div class="line">

<span id="l00207"></span><span class="lineno"> 207</span> <span class="keyword">const</span> [ScalarOrArray\<7\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[lower\_torque\_threshold\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00208"></span><span class="lineno"> 208</span> <span class="keyword">const</span> [ScalarOrArray\<7\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[upper\_torque\_threshold\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00209"></span><span class="lineno"> 209</span> <span class="keyword">const</span> [ScalarOrArray\<7\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[lower\_torque\_threshold\_nominal](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [ScalarOrArray\<7\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[upper\_torque\_threshold\_nominal](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00210"></span><span class="lineno"> 210</span> <span class="keyword">const</span> [ScalarOrArray\<6\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[lower\_force\_threshold\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00211"></span><span class="lineno"> 211</span> <span class="keyword">const</span> [ScalarOrArray\<6\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[upper\_force\_threshold\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [ScalarOrArray\<6\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[lower\_force\_threshold\_nominal](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00212"></span><span class="lineno"> 212</span> <span class="keyword">const</span> [ScalarOrArray\<6\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[upper\_force\_threshold\_nominal](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00213"></span><span class="lineno"> 213</span>

</div>

<div class="line">

<span id="l00219"></span><span class="lineno"> 219</span> <span class="keywordtype">bool</span> [recoverFromErrors](classfranky_1_1_robot.md#a7389f6e088ba456dd689c093ee6640e0)();

</div>

<div class="line">

<span id="l00220"></span><span class="lineno"> 220</span>

</div>

<div class="line">

<span id="l00225"></span><span class="lineno"> 225</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keywordtype">bool</span> [hasErrors](classfranky_1_1_robot.md#ad3d89c3fd930ea6590d0abd10fbdb755)();

</div>

<div class="line">

<span id="l00226"></span><span class="lineno"> 226</span>

</div>

<div class="line">

<span id="l00231"></span><span class="lineno"> [231](classfranky_1_1_robot.md#adf04b2531a0ac4a16a759cc048d82e15)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RobotPose](classfranky_1_1_robot_pose.md) [currentPose](classfranky_1_1_robot.md#adf04b2531a0ac4a16a759cc048d82e15)() { <span class="keywordflow">return</span> [currentCartesianState](classfranky_1_1_robot.md#a4d2595f5969257dd18dce4997d59f7cd)().[pose](classfranky_1_1_cartesian_state.md#a5e8e2c8161dc22d18a01a0c28897792b)(); }

</div>

<div class="line">

<span id="l00232"></span><span class="lineno"> 232</span>

</div>

<div class="line">

<span id="l00237"></span><span class="lineno"> [237](classfranky_1_1_robot.md#acb900ba5048aa792f4c16150703d8a6b)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RobotVelocity](classfranky_1_1_robot_velocity.md) [currentCartesianVelocity](classfranky_1_1_robot.md#acb900ba5048aa792f4c16150703d8a6b)() { <span class="keywordflow">return</span> [currentCartesianState](classfranky_1_1_robot.md#a4d2595f5969257dd18dce4997d59f7cd)().[velocity](classfranky_1_1_cartesian_state.md#ac212d0fc0f7b8f05baa3da6389bcf52f)(); }

</div>

<div class="line">

<span id="l00238"></span><span class="lineno"> 238</span>

</div>

<div id="foldopen00243" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00243"></span><span class="lineno"> [243](classfranky_1_1_robot.md#a4d2595f5969257dd18dce4997d59f7cd)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [CartesianState](classfranky_1_1_cartesian_state.md) [currentCartesianState](classfranky_1_1_robot.md#a4d2595f5969257dd18dce4997d59f7cd)() {

</div>

<div class="line">

<span id="l00244"></span><span class="lineno"> 244</span> <span class="keyword">auto</span> [s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [state](classfranky_1_1_robot.md#a5ee4537b589a74f8df79be730967bab7)();

</div>

<div class="line">

<span id="l00245"></span><span class="lineno"> 245</span> <span class="keywordflow">return</span> {

</div>

<div class="line">

<span id="l00246"></span><span class="lineno"> 246</span> {[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)(Eigen::Matrix4d::Map([s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).O\_T\_EE.data())), [ElbowState](classfranky_1_1_elbow_state.md){[s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).elbow}}, [RobotVelocity](classfranky_1_1_robot_velocity.md)([s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).O\_dP\_EE\_c, [s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).delbow\_c)};

</div>

<div class="line">

<span id="l00247"></span><span class="lineno"> 247</span> }

</div>

</div>

<div class="line">

<span id="l00248"></span><span class="lineno"> 248</span>

</div>

<div id="foldopen00253" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00253"></span><span class="lineno"> [253](classfranky_1_1_robot.md#aab5abbad176d18599f25a4204e354cfb)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [JointState](classfranky_1_1_joint_state.md) [currentJointState](classfranky_1_1_robot.md#aab5abbad176d18599f25a4204e354cfb)() {

</div>

<div class="line">

<span id="l00254"></span><span class="lineno"> 254</span> <span class="keyword">auto</span> [s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = [state](classfranky_1_1_robot.md#a5ee4537b589a74f8df79be730967bab7)();

</div>

<div class="line">

<span id="l00255"></span><span class="lineno"> 255</span> <span class="keywordflow">return</span> {[s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).q, [s](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).dq};

</div>

<div class="line">

<span id="l00256"></span><span class="lineno"> 256</span> }

</div>

</div>

<div class="line">

<span id="l00257"></span><span class="lineno"> 257</span>

</div>

<div class="line">

<span id="l00262"></span><span class="lineno"> [262](classfranky_1_1_robot.md#a4aae0b9dbfe4d88615810d1743c43646)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [currentJointPositions](classfranky_1_1_robot.md#a4aae0b9dbfe4d88615810d1743c43646)() { <span class="keywordflow">return</span> [currentJointState](classfranky_1_1_robot.md#aab5abbad176d18599f25a4204e354cfb)().[position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0)(); }

</div>

<div class="line">

<span id="l00263"></span><span class="lineno"> 263</span>

</div>

<div class="line">

<span id="l00268"></span><span class="lineno"> [268](classfranky_1_1_robot.md#a2d118e16b5789a8442c486cca80ed3c6)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) [currentJointVelocities](classfranky_1_1_robot.md#a2d118e16b5789a8442c486cca80ed3c6)() { <span class="keywordflow">return</span> [currentJointState](classfranky_1_1_robot.md#aab5abbad176d18599f25a4204e354cfb)().[velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100)(); }

</div>

<div class="line">

<span id="l00269"></span><span class="lineno"> 269</span>

</div>

<div class="line">

<span id="l00274"></span><span class="lineno"> 274</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RobotState](structfranky_1_1_robot_state.md) [state](classfranky_1_1_robot.md#a5ee4537b589a74f8df79be730967bab7)();

</div>

<div class="line">

<span id="l00275"></span><span class="lineno"> 275</span>

</div>

<div class="line">

<span id="l00280"></span><span class="lineno"> 280</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) [relative\_dynamics\_factor](classfranky_1_1_robot.md#a43f2f6dde0cca1f8c21fa6c1fb1b28c0)();

</div>

<div class="line">

<span id="l00281"></span><span class="lineno"> 281</span>

</div>

<div class="line">

<span id="l00286"></span><span class="lineno"> 286</span> <span class="keywordtype">void</span> [setRelativeDynamicsFactor](classfranky_1_1_robot.md#ad19caa63f0237d39463e5a3dd0b3e793)(<span class="keyword">const</span> [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) &[relative\_dynamics\_factor](classfranky_1_1_robot.md#a43f2f6dde0cca1f8c21fa6c1fb1b28c0));

</div>

<div class="line">

<span id="l00287"></span><span class="lineno"> 287</span>

</div>

<div class="line">

<span id="l00292"></span><span class="lineno"> 292</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keywordtype">bool</span> [is\_in\_control](classfranky_1_1_robot.md#a971c769d2725f11c3437d28f9ad6de61)();

</div>

<div class="line">

<span id="l00293"></span><span class="lineno"> 293</span>

</div>

<div class="line">

<span id="l00297"></span><span class="lineno"> 297</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] std::string [fci\_hostname](classfranky_1_1_robot.md#a25ca7e90c8a10848921fb35a378a7d33)() <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00298"></span><span class="lineno"> 298</span>

</div>

<div class="line">

<span id="l00302"></span><span class="lineno"> 302</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] std::optional\<ControlSignalType\> [current\_control\_signal\_type](classfranky_1_1_robot.md#a15b55042954d0bec0f2190abf2c8bb59)();

</div>

<div class="line">

<span id="l00303"></span><span class="lineno"> 303</span>

</div>

<div class="line">

<span id="l00310"></span><span class="lineno"> [310](classfranky_1_1_robot.md#ad22fb0483ab2b3402b28b6f35dccaf9f)</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] std::shared\_ptr\<const Model\> [model](classfranky_1_1_robot.md#ad22fb0483ab2b3402b28b6f35dccaf9f)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> model\_; }

</div>

<div class="line">

<span id="l00311"></span><span class="lineno"> 311</span>

</div>

<div class="line">

<span id="l00312"></span><span class="lineno"> 312</span><span class="preprocessor">\#ifdef FRANKA\_0\_15</span>

</div>

<div class="line">

<span id="l00317"></span><span class="lineno"> 317</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] std::string [model\_urdf](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)()<span class="keyword"> const </span>{ <span class="keywordflow">return</span> [model\_urdf\_](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0); }

</div>

<div class="line">

<span id="l00318"></span><span class="lineno"> 318</span><span class="preprocessor">\#endif</span>

</div>

<div class="line">

<span id="l00319"></span><span class="lineno"> 319</span>

</div>

<div id="foldopen00324" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00324"></span><span class="lineno"> [324](classfranky_1_1_robot.md#a2f48445583c522dd798e312bdbacf864)</span> <span class="keywordtype">bool</span> [joinMotion](classfranky_1_1_robot.md#a2f48445583c522dd798e312bdbacf864)() {

</div>

<div class="line">

<span id="l00325"></span><span class="lineno"> 325</span> std::unique\_lock [lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(\*control\_mutex\_);

</div>

<div class="line">

<span id="l00326"></span><span class="lineno"> 326</span> <span class="keywordflow">return</span> joinMotionUnsafe([lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00327"></span><span class="lineno"> 327</span> }

</div>

</div>

<div class="line">

<span id="l00328"></span><span class="lineno"> 328</span>

</div>

<div class="line">

<span id="l00337"></span><span class="lineno"> 337</span> <span class="keyword">template</span> \<<span class="keyword">class</span> Rep, <span class="keyword">class</span> Period\>

</div>

<div id="foldopen00338" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00338"></span><span class="lineno"> [338](classfranky_1_1_robot.md#a114a614ee78f9b554dd9aaef8fe2a1d8)</span> <span class="keywordtype">bool</span> [joinMotion](classfranky_1_1_robot.md#a114a614ee78f9b554dd9aaef8fe2a1d8)(<span class="keyword">const</span> std::chrono::duration\<Rep, Period\> &[timeout](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00339"></span><span class="lineno"> 339</span> std::unique\_lock [lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(\*control\_mutex\_);

</div>

<div class="line">

<span id="l00340"></span><span class="lineno"> 340</span> <span class="keywordflow">return</span> [joinMotionUnsafe\<Rep, Period\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [timeout](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00341"></span><span class="lineno"> 341</span> }

</div>

</div>

<div class="line">

<span id="l00342"></span><span class="lineno"> 342</span>

</div>

<div class="line">

<span id="l00349"></span><span class="lineno"> 349</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\]

</div>

<div id="foldopen00350" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00350"></span><span class="lineno"> [350](classfranky_1_1_robot.md#afb00fbee84e00d09f3c8dedbfe5708f4)</span> <span class="keywordtype">bool</span> [pollMotion](classfranky_1_1_robot.md#afb00fbee84e00d09f3c8dedbfe5708f4)() {

</div>

<div class="line">

<span id="l00351"></span><span class="lineno"> 351</span> <span class="keywordflow">return</span> [joinMotion](classfranky_1_1_robot.md#a2f48445583c522dd798e312bdbacf864)(std::chrono::milliseconds(0));

</div>

<div class="line">

<span id="l00352"></span><span class="lineno"> 352</span> }

</div>

</div>

<div class="line">

<span id="l00353"></span><span class="lineno"> 353</span>

</div>

<div class="line">

<span id="l00354"></span><span class="lineno"> 354</span> <span class="comment">// These helper functions are needed as the implicit template deduction does</span>

</div>

<div class="line">

<span id="l00355"></span><span class="lineno"> 355</span> <span class="comment">// not work on subclasses of Motion</span>

</div>

<div class="line">

<span id="l00356"></span><span class="lineno"> 356</span>

</div>

<div id="foldopen00362" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00362"></span><span class="lineno"> [362](classfranky_1_1_robot.md#a2142a3e3b425407d33d4c472f5094dba)</span> <span class="keywordtype">void</span> [move](classfranky_1_1_robot.md#a2142a3e3b425407d33d4c472f5094dba)(<span class="keyword">const</span> std::shared\_ptr\<[Motion\<franka::CartesianPose\>](classfranky_1_1_motion.md)\> &[motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">bool</span> [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>) {

</div>

<div class="line">

<span id="l00363"></span><span class="lineno"> 363</span> [moveInternal\<franka::CartesianPose\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(

</div>

<div class="line">

<span id="l00364"></span><span class="lineno"> 364</span> [motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), \[<span class="keyword">this</span>\](<span class="keyword">const</span> ControlFunc\<franka::CartesianPose\> &[m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) { [control](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), params\_.[controller\_mode](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083)); }, [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00365"></span><span class="lineno"> 365</span> }

</div>

</div>

<div class="line">

<span id="l00366"></span><span class="lineno"> 366</span>

</div>

<div id="foldopen00372" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00372"></span><span class="lineno"> [372](classfranky_1_1_robot.md#ad014400edfd5bb1cf837fd09765ac5ce)</span> <span class="keywordtype">void</span> [move](classfranky_1_1_robot.md#ad014400edfd5bb1cf837fd09765ac5ce)(<span class="keyword">const</span> std::shared\_ptr\<[Motion\<franka::CartesianVelocities\>](classfranky_1_1_motion.md)\> &[motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">bool</span> [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>) {

</div>

<div class="line">

<span id="l00373"></span><span class="lineno"> 373</span> [moveInternal\<franka::CartesianVelocities\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(

</div>

<div class="line">

<span id="l00374"></span><span class="lineno"> 374</span> [motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00375"></span><span class="lineno"> 375</span> \[<span class="keyword">this</span>\](<span class="keyword">const</span> ControlFunc\<franka::CartesianVelocities\> &[m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) { [control](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), params\_.[controller\_mode](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083)); },

</div>

<div class="line">

<span id="l00376"></span><span class="lineno"> 376</span> [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00377"></span><span class="lineno"> 377</span> }

</div>

</div>

<div class="line">

<span id="l00378"></span><span class="lineno"> 378</span>

</div>

<div id="foldopen00384" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00384"></span><span class="lineno"> [384](classfranky_1_1_robot.md#a0e44e9689e22525b286633a43c7eb443)</span> <span class="keywordtype">void</span> [move](classfranky_1_1_robot.md#a0e44e9689e22525b286633a43c7eb443)(<span class="keyword">const</span> std::shared\_ptr\<[Motion\<franka::JointPositions\>](classfranky_1_1_motion.md)\> &[motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">bool</span> [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>) {

</div>

<div class="line">

<span id="l00385"></span><span class="lineno"> 385</span> [moveInternal\<franka::JointPositions\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(

</div>

<div class="line">

<span id="l00386"></span><span class="lineno"> 386</span> [motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), \[<span class="keyword">this</span>\](<span class="keyword">const</span> ControlFunc\<franka::JointPositions\> &[m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) { [control](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), params\_.[controller\_mode](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083)); }, [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00387"></span><span class="lineno"> 387</span> }

</div>

</div>

<div class="line">

<span id="l00388"></span><span class="lineno"> 388</span>

</div>

<div id="foldopen00394" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00394"></span><span class="lineno"> [394](classfranky_1_1_robot.md#aa031b868eacc474676306c3d581f43e7)</span> <span class="keywordtype">void</span> [move](classfranky_1_1_robot.md#aa031b868eacc474676306c3d581f43e7)(<span class="keyword">const</span> std::shared\_ptr\<[Motion\<franka::JointVelocities\>](classfranky_1_1_motion.md)\> &[motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">bool</span> [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>) {

</div>

<div class="line">

<span id="l00395"></span><span class="lineno"> 395</span> [moveInternal\<franka::JointVelocities\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(

</div>

<div class="line">

<span id="l00396"></span><span class="lineno"> 396</span> [motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), \[<span class="keyword">this</span>\](<span class="keyword">const</span> ControlFunc\<franka::JointVelocities\> &[m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) { [control](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), params\_.[controller\_mode](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083)); }, [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00397"></span><span class="lineno"> 397</span> }

</div>

</div>

<div class="line">

<span id="l00398"></span><span class="lineno"> 398</span>

</div>

<div id="foldopen00404" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00404"></span><span class="lineno"> [404](classfranky_1_1_robot.md#a4c1066ea03a41b71998d6560a97e7fb1)</span> <span class="keywordtype">void</span> [move](classfranky_1_1_robot.md#a4c1066ea03a41b71998d6560a97e7fb1)(<span class="keyword">const</span> std::shared\_ptr\<[Motion\<franka::Torques\>](classfranky_1_1_motion.md)\> &[motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">bool</span> [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>) {

</div>

<div class="line">

<span id="l00405"></span><span class="lineno"> 405</span> [moveInternal\<franka::Torques\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), \[<span class="keyword">this</span>\](<span class="keyword">const</span> ControlFunc\<franka::Torques\> &[m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) { [control](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)); }, [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00406"></span><span class="lineno"> 406</span> }

</div>

</div>

<div class="line">

<span id="l00407"></span><span class="lineno"> 407</span>

</div>

<div class="line">

<span id="l00408"></span><span class="lineno"> 408</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00409"></span><span class="lineno"> 409</span> std::shared\_ptr\<const Model\> model\_;

</div>

<div class="line">

<span id="l00410"></span><span class="lineno"> 410</span><span class="preprocessor">\#ifdef FRANKA\_0\_15</span>

</div>

<div class="line">

<span id="l00411"></span><span class="lineno"> 411</span> std::string [model\_urdf\_](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00412"></span><span class="lineno"> 412</span><span class="preprocessor">\#endif</span>

</div>

<div class="line">

<span id="l00413"></span><span class="lineno"> 413</span>

</div>

<div class="line">

<span id="l00414"></span><span class="lineno"> 414</span> <span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div class="line">

<span id="l00415"></span><span class="lineno"> 415</span> <span class="keyword">using </span>ControlFunc = std::function\<[ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac)(<span class="keyword">const</span> franka::RobotState &, franka::Duration)\>;

</div>

<div class="line">

<span id="l00416"></span><span class="lineno"> 416</span> <span class="keyword">using </span>MotionGeneratorVariant = std::variant\<

</div>

<div class="line">

<span id="l00417"></span><span class="lineno"> 417</span> std::nullopt\_t, [MotionGenerator\<franka::Torques\>](classfranky_1_1_motion_generator.md), [MotionGenerator\<franka::JointVelocities\>](classfranky_1_1_motion_generator.md),

</div>

<div class="line">

<span id="l00418"></span><span class="lineno"> 418</span> [MotionGenerator\<franka::JointPositions\>](classfranky_1_1_motion_generator.md), [MotionGenerator\<franka::CartesianVelocities\>](classfranky_1_1_motion_generator.md),

</div>

<div class="line">

<span id="l00419"></span><span class="lineno"> 419</span> [MotionGenerator\<franka::CartesianPose\>](classfranky_1_1_motion_generator.md)\>;

</div>

<div class="line">

<span id="l00420"></span><span class="lineno"> 420</span>

</div>

<div class="line">

<span id="l00422"></span><span class="lineno"> 422</span> std::string fci\_hostname\_;

</div>

<div class="line">

<span id="l00423"></span><span class="lineno"> 423</span> Params params\_;

</div>

<div class="line">

<span id="l00424"></span><span class="lineno"> 424</span> [RobotState](structfranky_1_1_robot_state.md) current\_state\_;

</div>

<div class="line">

<span id="l00425"></span><span class="lineno"> 425</span> std::mutex state\_mutex\_;

</div>

<div class="line">

<span id="l00426"></span><span class="lineno"> 426</span> std::shared\_ptr\<std::mutex\> control\_mutex\_;

</div>

<div class="line">

<span id="l00427"></span><span class="lineno"> 427</span> std::condition\_variable control\_finished\_condition\_;

</div>

<div class="line">

<span id="l00428"></span><span class="lineno"> 428</span> std::exception\_ptr control\_exception\_;

</div>

<div class="line">

<span id="l00429"></span><span class="lineno"> 429</span> std::thread control\_thread\_;

</div>

<div class="line">

<span id="l00430"></span><span class="lineno"> 430</span> MotionGeneratorVariant motion\_generator\_{std::nullopt};

</div>

<div class="line">

<span id="l00431"></span><span class="lineno"> 431</span> <span class="keywordtype">bool</span> motion\_generator\_running\_{<span class="keyword">false</span>};

</div>

<div class="line">

<span id="l00432"></span><span class="lineno"> 432</span>

</div>

<div class="line">

<span id="l00433"></span><span class="lineno"> 433</span> \[\[[nodiscard](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]\] <span class="keywordtype">bool</span> is\_in\_control\_unsafe() <span class="keyword">const</span>;

</div>

<div class="line">

<span id="l00434"></span><span class="lineno"> 434</span>

</div>

<div class="line">

<span id="l00435"></span><span class="lineno"> 435</span> <span class="keyword">public</span>:

</div>

<div class="line">

<span id="l00436"></span><span class="lineno"> 436</span> <span class="comment">// IMPORTANT: this has to come after control\_mutex\_ as otherwise</span>

</div>

<div class="line">

<span id="l00437"></span><span class="lineno"> 437</span> <span class="comment">// control\_mutex\_ will be uninitialized when passed to the constructor of the</span>

</div>

<div class="line">

<span id="l00438"></span><span class="lineno"> 438</span> <span class="comment">// DynamicsLimit class Limits provided by Franka for the FR3:</span>

</div>

<div class="line">

<span id="l00439"></span><span class="lineno"> 439</span> <span class="comment">// https://frankaemika.github.io/docs/control\_parameters.md</span>

</div>

<div class="line">

<span id="l00440"></span><span class="lineno"> 440</span> <span class="comment">// clang-format off</span>

</div>

<div class="line">

<span id="l00444"></span><span class="lineno"> [444](classfranky_1_1_robot.md#a7165eb847d474a244c6fba5b595cd84b)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [translation\_velocity\_limit](classfranky_1_1_robot.md#a7165eb847d474a244c6fba5b595cd84b);

</div>

<div class="line">

<span id="l00445"></span><span class="lineno"> 445</span>

</div>

<div class="line">

<span id="l00449"></span><span class="lineno"> [449](classfranky_1_1_robot.md#a83a0166687db4309de4f9cd7b76eb723)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [rotation\_velocity\_limit](classfranky_1_1_robot.md#a83a0166687db4309de4f9cd7b76eb723);

</div>

<div class="line">

<span id="l00450"></span><span class="lineno"> 450</span>

</div>

<div class="line">

<span id="l00454"></span><span class="lineno"> [454](classfranky_1_1_robot.md#a823551f59caa0f025f1d6af381e38471)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [elbow\_velocity\_limit](classfranky_1_1_robot.md#a823551f59caa0f025f1d6af381e38471);

</div>

<div class="line">

<span id="l00455"></span><span class="lineno"> 455</span>

</div>

<div class="line">

<span id="l00459"></span><span class="lineno"> [459](classfranky_1_1_robot.md#ad31901ce61f3fce2adf885c776b7bb8a)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [translation\_acceleration\_limit](classfranky_1_1_robot.md#ad31901ce61f3fce2adf885c776b7bb8a);

</div>

<div class="line">

<span id="l00460"></span><span class="lineno"> 460</span>

</div>

<div class="line">

<span id="l00464"></span><span class="lineno"> [464](classfranky_1_1_robot.md#ae7725e4fffdc28b8db727068a105707a)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [rotation\_acceleration\_limit](classfranky_1_1_robot.md#ae7725e4fffdc28b8db727068a105707a);

</div>

<div class="line">

<span id="l00465"></span><span class="lineno"> 465</span>

</div>

<div class="line">

<span id="l00469"></span><span class="lineno"> [469](classfranky_1_1_robot.md#a3790d2dd31a3b2e2ccc32f39b11816fb)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [elbow\_acceleration\_limit](classfranky_1_1_robot.md#a3790d2dd31a3b2e2ccc32f39b11816fb);

</div>

<div class="line">

<span id="l00470"></span><span class="lineno"> 470</span>

</div>

<div class="line">

<span id="l00474"></span><span class="lineno"> [474](classfranky_1_1_robot.md#a676d0b273cc01dd02fa536ce07992a73)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [translation\_jerk\_limit](classfranky_1_1_robot.md#a676d0b273cc01dd02fa536ce07992a73);

</div>

<div class="line">

<span id="l00475"></span><span class="lineno"> 475</span>

</div>

<div class="line">

<span id="l00479"></span><span class="lineno"> [479](classfranky_1_1_robot.md#ace7d9414a2e80b4a6c760578ebd382d3)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [rotation\_jerk\_limit](classfranky_1_1_robot.md#ace7d9414a2e80b4a6c760578ebd382d3);

</div>

<div class="line">

<span id="l00480"></span><span class="lineno"> 480</span>

</div>

<div class="line">

<span id="l00484"></span><span class="lineno"> [484](classfranky_1_1_robot.md#a87e2193710fe1cc287a21729bba88106)</span> [DynamicsLimit\<double\>](classfranky_1_1_dynamics_limit.md) [elbow\_jerk\_limit](classfranky_1_1_robot.md#a87e2193710fe1cc287a21729bba88106);

</div>

<div class="line">

<span id="l00485"></span><span class="lineno"> 485</span>

</div>

<div class="line">

<span id="l00489"></span><span class="lineno"> [489](classfranky_1_1_robot.md#a4d5a68c15c97aba59872e6795ed1500f)</span> [DynamicsLimit\<Vector7d\>](classfranky_1_1_dynamics_limit.md) [joint\_velocity\_limit](classfranky_1_1_robot.md#a4d5a68c15c97aba59872e6795ed1500f);

</div>

<div class="line">

<span id="l00490"></span><span class="lineno"> 490</span>

</div>

<div class="line">

<span id="l00494"></span><span class="lineno"> [494](classfranky_1_1_robot.md#a0348db847ba5ddaae49c0dcb48f4a710)</span> [DynamicsLimit\<Vector7d\>](classfranky_1_1_dynamics_limit.md) [joint\_acceleration\_limit](classfranky_1_1_robot.md#a0348db847ba5ddaae49c0dcb48f4a710);

</div>

<div class="line">

<span id="l00495"></span><span class="lineno"> 495</span>

</div>

<div class="line">

<span id="l00499"></span><span class="lineno"> [499](classfranky_1_1_robot.md#aa3bd3f0843a7c2c4aeae3d5c21d506b9)</span> [DynamicsLimit\<Vector7d\>](classfranky_1_1_dynamics_limit.md) [joint\_jerk\_limit](classfranky_1_1_robot.md#aa3bd3f0843a7c2c4aeae3d5c21d506b9);

</div>

<div class="line">

<span id="l00500"></span><span class="lineno"> 500</span>

</div>

<div class="line">

<span id="l00501"></span><span class="lineno"> 501</span> <span class="comment">// clang-format on</span>

</div>

<div class="line">

<span id="l00502"></span><span class="lineno"> 502</span>

</div>

<div class="line">

<span id="l00503"></span><span class="lineno"> 503</span> <span class="keyword">private</span>:

</div>

<div class="line">

<span id="l00504"></span><span class="lineno"> 504</span> <span class="keyword">template</span> \<<span class="keyword">class</span> Rep = <span class="keywordtype">long</span>, <span class="keyword">class</span> Period = std::ratio\<1\>\>

</div>

<div class="line">

<span id="l00505"></span><span class="lineno"> 505</span> <span class="keywordtype">bool</span> joinMotionUnsafe(

</div>

<div class="line">

<span id="l00506"></span><span class="lineno"> 506</span> std::unique\_lock\<std::mutex\> &[lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00507"></span><span class="lineno"> 507</span> <span class="keyword">const</span> std::optional\<std::chrono::duration\<Rep, Period\>\> &[timeout](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = std::nullopt) {

</div>

<div class="line">

<span id="l00508"></span><span class="lineno"> 508</span> <span class="keywordflow">while</span> (motion\_generator\_running\_) {

</div>

<div class="line">

<span id="l00509"></span><span class="lineno"> 509</span> <span class="keywordflow">if</span> ([timeout](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).has\_value()) {

</div>

<div class="line">

<span id="l00510"></span><span class="lineno"> 510</span> <span class="keywordflow">if</span> (control\_finished\_condition\_.wait\_for([lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [timeout](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).value()) == std::cv\_status::timeout) {

</div>

<div class="line">

<span id="l00511"></span><span class="lineno"> 511</span> <span class="keywordflow">return</span> <span class="keyword">false</span>;

</div>

<div class="line">

<span id="l00512"></span><span class="lineno"> 512</span> }

</div>

<div class="line">

<span id="l00513"></span><span class="lineno"> 513</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00514"></span><span class="lineno"> 514</span> control\_finished\_condition\_.wait([lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00515"></span><span class="lineno"> 515</span> }

</div>

<div class="line">

<span id="l00516"></span><span class="lineno"> 516</span> }

</div>

<div class="line">

<span id="l00517"></span><span class="lineno"> 517</span> <span class="keywordflow">if</span> (control\_thread\_.joinable()) control\_thread\_.join();

</div>

<div class="line">

<span id="l00518"></span><span class="lineno"> 518</span> <span class="keywordflow">if</span> (control\_exception\_ \!= <span class="keyword">nullptr</span>) {

</div>

<div class="line">

<span id="l00519"></span><span class="lineno"> 519</span> <span class="keyword">auto</span> [control\_exception](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = control\_exception\_;

</div>

<div class="line">

<span id="l00520"></span><span class="lineno"> 520</span> control\_exception\_ = <span class="keyword">nullptr</span>;

</div>

<div class="line">

<span id="l00521"></span><span class="lineno"> 521</span> std::rethrow\_exception([control\_exception](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00522"></span><span class="lineno"> 522</span> }

</div>

<div class="line">

<span id="l00523"></span><span class="lineno"> 523</span> <span class="keywordflow">return</span> <span class="keyword">true</span>;

</div>

<div class="line">

<span id="l00524"></span><span class="lineno"> 524</span> }

</div>

<div class="line">

<span id="l00525"></span><span class="lineno"> 525</span>

</div>

<div class="line">

<span id="l00526"></span><span class="lineno"> 526</span> <span class="keyword">template</span> \<<span class="keyword">typename</span> ControlSignalType\>

</div>

<div class="line">

<span id="l00527"></span><span class="lineno"> 527</span> <span class="keywordtype">void</span> moveInternal(

</div>

<div class="line">

<span id="l00528"></span><span class="lineno"> 528</span> <span class="keyword">const</span> std::shared\_ptr\<[Motion\<ControlSignalType\>](classfranky_1_1_motion.md)\> &[motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0),

</div>

<div class="line">

<span id="l00529"></span><span class="lineno"> 529</span> <span class="keyword">const</span> std::function\<<span class="keywordtype">void</span>(<span class="keyword">const</span> [ControlFunc\<ControlSignalType\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &)\> &[control\_func\_executor](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keywordtype">bool</span> [async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00530"></span><span class="lineno"> 530</span> <span class="keywordflow">if</span> ([motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) == <span class="keyword">nullptr</span>) {

</div>

<div class="line">

<span id="l00531"></span><span class="lineno"> 531</span> <span class="keywordflow">throw</span> std::invalid\_argument(<span class="stringliteral">"The motion must not be null."</span>);

</div>

<div class="line">

<span id="l00532"></span><span class="lineno"> 532</span> }

</div>

<div class="line">

<span id="l00533"></span><span class="lineno"> 533</span> { <span class="comment">// Do not remove brace, it is needed to scope the lock</span>

</div>

<div class="line">

<span id="l00534"></span><span class="lineno"> 534</span> std::unique\_lock [lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(\*control\_mutex\_);

</div>

<div class="line">

<span id="l00535"></span><span class="lineno"> 535</span> <span class="keywordflow">if</span> (is\_in\_control\_unsafe() && motion\_generator\_running\_) {

</div>

<div class="line">

<span id="l00536"></span><span class="lineno"> 536</span> <span class="keywordflow">if</span> (\!std::holds\_alternative\<[MotionGenerator\<ControlSignalType\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>(motion\_generator\_)) {

</div>

<div class="line">

<span id="l00537"></span><span class="lineno"> 537</span> <span class="keywordflow">throw</span> InvalidMotionTypeException(

</div>

<div class="line">

<span id="l00538"></span><span class="lineno"> 538</span> <span class="stringliteral">"The type of motion cannot change during runtime. Please ensure "</span>

</div>

<div class="line">

<span id="l00539"></span><span class="lineno"> 539</span> <span class="stringliteral">"that the "</span>

</div>

<div class="line">

<span id="l00540"></span><span class="lineno"> 540</span> <span class="stringliteral">"previous motion finished before using a new type of motion."</span>);

</div>

<div class="line">

<span id="l00541"></span><span class="lineno"> 541</span> }

</div>

<div class="line">

<span id="l00542"></span><span class="lineno"> 542</span> std::get\<MotionGenerator\<ControlSignalType\>\>(motion\_generator\_).updateMotion([motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00543"></span><span class="lineno"> 543</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00544"></span><span class="lineno"> 544</span> joinMotionUnsafe([lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00545"></span><span class="lineno"> 545</span>

</div>

<div class="line">

<span id="l00546"></span><span class="lineno"> 546</span> motion\_generator\_.emplace\<[MotionGenerator\<ControlSignalType\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>(<span class="keyword">this</span>, [motion](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00547"></span><span class="lineno"> 547</span> <span class="keyword">auto</span> [motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = \&std::get\<MotionGenerator\<ControlSignalType\>\>(motion\_generator\_);

</div>

<div class="line">

<span id="l00548"></span><span class="lineno"> 548</span> [motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)-\>registerUpdateCallback(

</div>

<div class="line">

<span id="l00549"></span><span class="lineno"> 549</span> \[<span class="keyword">this</span>\](<span class="keyword">const</span> RobotState &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [duration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration time) {

</div>

<div class="line">

<span id="l00550"></span><span class="lineno"> 550</span> std::lock\_guard [lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(state\_mutex\_);

</div>

<div class="line">

<span id="l00551"></span><span class="lineno"> 551</span> current\_state\_ = [robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00552"></span><span class="lineno"> 552</span> });

</div>

<div class="line">

<span id="l00553"></span><span class="lineno"> 553</span> motion\_generator\_running\_ = <span class="keyword">true</span>;

</div>

<div class="line">

<span id="l00554"></span><span class="lineno"> 554</span> control\_thread\_ = std::thread(\[<span class="keyword">this</span>, [control\_func\_executor](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\]() {

</div>

<div class="line">

<span id="l00555"></span><span class="lineno"> 555</span> <span class="keywordflow">try</span> {

</div>

<div class="line">

<span id="l00556"></span><span class="lineno"> 556</span> <span class="keywordtype">bool</span> [done](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">false</span>;

</div>

<div class="line">

<span id="l00557"></span><span class="lineno"> 557</span> RobotStateEstimator [robot\_state\_estimator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(

</div>

<div class="line">

<span id="l00558"></span><span class="lineno"> 558</span> params\_.kalman\_q\_process\_var,

</div>

<div class="line">

<span id="l00559"></span><span class="lineno"> 559</span> params\_.kalman\_dq\_process\_var,

</div>

<div class="line">

<span id="l00560"></span><span class="lineno"> 560</span> params\_.kalman\_ddq\_process\_var,

</div>

<div class="line">

<span id="l00561"></span><span class="lineno"> 561</span> params\_.kalman\_control\_process\_var,

</div>

<div class="line">

<span id="l00562"></span><span class="lineno"> 562</span> params\_.kalman\_q\_obs\_var,

</div>

<div class="line">

<span id="l00563"></span><span class="lineno"> 563</span> params\_.kalman\_dq\_obs\_var,

</div>

<div class="line">

<span id="l00564"></span><span class="lineno"> 564</span> params\_.kalman\_q\_d\_obs\_var,

</div>

<div class="line">

<span id="l00565"></span><span class="lineno"> 565</span> params\_.kalman\_dq\_d\_obs\_var,

</div>

<div class="line">

<span id="l00566"></span><span class="lineno"> 566</span> params\_.kalman\_ddq\_d\_obs\_var,

</div>

<div class="line">

<span id="l00567"></span><span class="lineno"> 567</span> params\_.kalman\_control\_adaptation\_rate);

</div>

<div class="line">

<span id="l00568"></span><span class="lineno"> 568</span> <span class="keywordflow">while</span> (\![done](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00569"></span><span class="lineno"> 569</span> [control\_func\_executor](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(

</div>

<div class="line">

<span id="l00570"></span><span class="lineno"> 570</span> \[<span class="keyword">this</span>, [motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), &[robot\_state\_estimator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\](<span class="keyword">const</span> franka::RobotState &[rs](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00571"></span><span class="lineno"> 571</span> <span class="keywordflow">return</span> (\*[motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))([robot\_state\_estimator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).update([rs](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), \*model\_), [d](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00572"></span><span class="lineno"> 572</span> });

</div>

<div class="line">

<span id="l00573"></span><span class="lineno"> 573</span> std::unique\_lock [lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(\*control\_mutex\_);

</div>

<div class="line">

<span id="l00574"></span><span class="lineno"> 574</span>

</div>

<div class="line">

<span id="l00575"></span><span class="lineno"> 575</span> <span class="comment">// This code is just for the case that a new motion is set just</span>

</div>

<div class="line">

<span id="l00576"></span><span class="lineno"> 576</span> <span class="comment">// after the old one terminates. If this happens, we need to</span>

</div>

<div class="line">

<span id="l00577"></span><span class="lineno"> 577</span> <span class="comment">// continue with this motion, unless an exception occurs.</span>

</div>

<div class="line">

<span id="l00578"></span><span class="lineno"> 578</span> [done](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = \![motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)-\>has\_new\_motion();

</div>

<div class="line">

<span id="l00579"></span><span class="lineno"> 579</span> <span class="keywordflow">if</span> ([motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)-\>has\_new\_motion()) {

</div>

<div class="line">

<span id="l00580"></span><span class="lineno"> 580</span> [motion\_generator](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)-\>resetTimeUnsafe();

</div>

<div class="line">

<span id="l00581"></span><span class="lineno"> 581</span> } <span class="keywordflow">else</span> {

</div>

<div class="line">

<span id="l00582"></span><span class="lineno"> 582</span> [done](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = <span class="keyword">true</span>;

</div>

<div class="line">

<span id="l00583"></span><span class="lineno"> 583</span> motion\_generator\_running\_ = <span class="keyword">false</span>;

</div>

<div class="line">

<span id="l00584"></span><span class="lineno"> 584</span> control\_finished\_condition\_.notify\_all();

</div>

<div class="line">

<span id="l00585"></span><span class="lineno"> 585</span> }

</div>

<div class="line">

<span id="l00586"></span><span class="lineno"> 586</span> }

</div>

<div class="line">

<span id="l00587"></span><span class="lineno"> 587</span> } <span class="keywordflow">catch</span> (...) {

</div>

<div class="line">

<span id="l00588"></span><span class="lineno"> 588</span> std::unique\_lock [lock](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(\*control\_mutex\_);

</div>

<div class="line">

<span id="l00589"></span><span class="lineno"> 589</span> control\_exception\_ = std::current\_exception();

</div>

<div class="line">

<span id="l00590"></span><span class="lineno"> 590</span> motion\_generator\_running\_ = <span class="keyword">false</span>;

</div>

<div class="line">

<span id="l00591"></span><span class="lineno"> 591</span> control\_finished\_condition\_.notify\_all();

</div>

<div class="line">

<span id="l00592"></span><span class="lineno"> 592</span> }

</div>

<div class="line">

<span id="l00593"></span><span class="lineno"> 593</span> });

</div>

<div class="line">

<span id="l00594"></span><span class="lineno"> 594</span> }

</div>

<div class="line">

<span id="l00595"></span><span class="lineno"> 595</span> }

</div>

<div class="line">

<span id="l00596"></span><span class="lineno"> 596</span> <span class="keywordflow">if</span> (\![async](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [joinMotion](classfranky_1_1_robot.md#a2f48445583c522dd798e312bdbacf864)();

</div>

<div class="line">

<span id="l00597"></span><span class="lineno"> 597</span> }

</div>

<div class="line">

<span id="l00598"></span><span class="lineno"> 598</span>};

</div>

</div>

<div class="line">

<span id="l00599"></span><span class="lineno"> 599</span>

</div>

<div class="line">

<span id="l00600"></span><span class="lineno"> 600</span>} <span class="comment">// namespace franky</span>

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

<div id="aclassfranky_1_1_dynamics_limit_html" class="ttc">

<div class="ttname">

[franky::DynamicsLimit](classfranky_1_1_dynamics_limit.md)

</div>

<div class="ttdoc">

A template class representing a dynamics limit with a maximum value.

</div>

<div class="ttdef">

**Definition** dynamics\_limit.hpp:23

</div>

</div>

<div id="aclassfranky_1_1_elbow_state_html" class="ttc">

<div class="ttname">

[franky::ElbowState](classfranky_1_1_elbow_state.md)

</div>

<div class="ttdoc">

Elbow state of the robot.

</div>

<div class="ttdef">

**Definition** elbow\_state.hpp:24

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

<div id="aclassfranky_1_1_joint_state_html_a5210d159dcb06ea28000f90060acf100" class="ttc">

<div class="ttname">

[franky::JointState::velocity](classfranky_1_1_joint_state.md#a5210d159dcb06ea28000f90060acf100)

</div>

<div class="ttdeci">

Vector7d velocity() const

</div>

<div class="ttdoc">

The velocity component of the state.

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:48

</div>

</div>

<div id="aclassfranky_1_1_joint_state_html_addd9bedce775d28cef880644b635ccf0" class="ttc">

<div class="ttname">

[franky::JointState::position](classfranky_1_1_joint_state.md#addd9bedce775d28cef880644b635ccf0)

</div>

<div class="ttdeci">

Vector7d position() const

</div>

<div class="ttdoc">

The position component of the state.

</div>

<div class="ttdef">

**Definition** joint\_state.hpp:43

</div>

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

<div id="aclassfranky_1_1_robot_html_a0348db847ba5ddaae49c0dcb48f4a710" class="ttc">

<div class="ttname">

[franky::Robot::joint\_acceleration\_limit](classfranky_1_1_robot.md#a0348db847ba5ddaae49c0dcb48f4a710)

</div>

<div class="ttdeci">

DynamicsLimit\< Vector7d \> joint\_acceleration\_limit

</div>

<div class="ttdoc">

Joint acceleration limit \[rad/s²\].

</div>

<div class="ttdef">

**Definition** robot.hpp:494

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a0e44e9689e22525b286633a43c7eb443" class="ttc">

<div class="ttname">

[franky::Robot::move](classfranky_1_1_robot.md#a0e44e9689e22525b286633a43c7eb443)

</div>

<div class="ttdeci">

void move(const std::shared\_ptr\< Motion\< franka::JointPositions \> \> \&motion, bool async=false)

</div>

<div class="ttdoc">

Execute the given motion.

</div>

<div class="ttdef">

**Definition** robot.hpp:384

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a114a614ee78f9b554dd9aaef8fe2a1d8" class="ttc">

<div class="ttname">

[franky::Robot::joinMotion](classfranky_1_1_robot.md#a114a614ee78f9b554dd9aaef8fe2a1d8)

</div>

<div class="ttdeci">

bool joinMotion(const std::chrono::duration\< Rep, Period \> \&timeout)

</div>

<div class="ttdoc">

Wait for the current motion to finish with a timeout. Throw any exceptions that occurred during the m...

</div>

<div class="ttdef">

**Definition** robot.hpp:338

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a15b55042954d0bec0f2190abf2c8bb59" class="ttc">

<div class="ttname">

[franky::Robot::current\_control\_signal\_type](classfranky_1_1_robot.md#a15b55042954d0bec0f2190abf2c8bb59)

</div>

<div class="ttdeci">

std::optional\< ControlSignalType \> current\_control\_signal\_type()

</div>

<div class="ttdoc">

The type of the current control signal.

</div>

<div class="ttdef">

**Definition** robot.cpp:112

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a2142a3e3b425407d33d4c472f5094dba" class="ttc">

<div class="ttname">

[franky::Robot::move](classfranky_1_1_robot.md#a2142a3e3b425407d33d4c472f5094dba)

</div>

<div class="ttdeci">

void move(const std::shared\_ptr\< Motion\< franka::CartesianPose \> \> \&motion, bool async=false)

</div>

<div class="ttdoc">

Execute the given motion.

</div>

<div class="ttdef">

**Definition** robot.hpp:362

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a25ca7e90c8a10848921fb35a378a7d33" class="ttc">

<div class="ttname">

[franky::Robot::fci\_hostname](classfranky_1_1_robot.md#a25ca7e90c8a10848921fb35a378a7d33)

</div>

<div class="ttdeci">

std::string fci\_hostname() const

</div>

<div class="ttdoc">

The hostname of the robot.

</div>

<div class="ttdef">

**Definition** robot.cpp:110

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a2d118e16b5789a8442c486cca80ed3c6" class="ttc">

<div class="ttname">

[franky::Robot::currentJointVelocities](classfranky_1_1_robot.md#a2d118e16b5789a8442c486cca80ed3c6)

</div>

<div class="ttdeci">

Vector7d currentJointVelocities()

</div>

<div class="ttdoc">

Returns the current joint velocities of the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:268

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a2f48445583c522dd798e312bdbacf864" class="ttc">

<div class="ttname">

[franky::Robot::joinMotion](classfranky_1_1_robot.md#a2f48445583c522dd798e312bdbacf864)

</div>

<div class="ttdeci">

bool joinMotion()

</div>

<div class="ttdoc">

Wait for the current motion to finish. Throw any exceptions that occurred during the motion.

</div>

<div class="ttdef">

**Definition** robot.hpp:324

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

<div id="aclassfranky_1_1_robot_html_a3790d2dd31a3b2e2ccc32f39b11816fb" class="ttc">

<div class="ttname">

[franky::Robot::elbow\_acceleration\_limit](classfranky_1_1_robot.md#a3790d2dd31a3b2e2ccc32f39b11816fb)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> elbow\_acceleration\_limit

</div>

<div class="ttdoc">

Elbow acceleration limit \[rad/s²\].

</div>

<div class="ttdef">

**Definition** robot.hpp:469

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

<div id="aclassfranky_1_1_robot_html_a4aae0b9dbfe4d88615810d1743c43646" class="ttc">

<div class="ttname">

[franky::Robot::currentJointPositions](classfranky_1_1_robot.md#a4aae0b9dbfe4d88615810d1743c43646)

</div>

<div class="ttdeci">

Vector7d currentJointPositions()

</div>

<div class="ttdoc">

Returns the current joint positions of the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:262

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a4c1066ea03a41b71998d6560a97e7fb1" class="ttc">

<div class="ttname">

[franky::Robot::move](classfranky_1_1_robot.md#a4c1066ea03a41b71998d6560a97e7fb1)

</div>

<div class="ttdeci">

void move(const std::shared\_ptr\< Motion\< franka::Torques \> \> \&motion, bool async=false)

</div>

<div class="ttdoc">

Execute the given motion.

</div>

<div class="ttdef">

**Definition** robot.hpp:404

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a4d2595f5969257dd18dce4997d59f7cd" class="ttc">

<div class="ttname">

[franky::Robot::currentCartesianState](classfranky_1_1_robot.md#a4d2595f5969257dd18dce4997d59f7cd)

</div>

<div class="ttdeci">

CartesianState currentCartesianState()

</div>

<div class="ttdoc">

Returns the current cartesian state of the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:243

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a4d5a68c15c97aba59872e6795ed1500f" class="ttc">

<div class="ttname">

[franky::Robot::joint\_velocity\_limit](classfranky_1_1_robot.md#a4d5a68c15c97aba59872e6795ed1500f)

</div>

<div class="ttdeci">

DynamicsLimit\< Vector7d \> joint\_velocity\_limit

</div>

<div class="ttdoc">

Joint velocity limit \[rad/s\].

</div>

<div class="ttdef">

**Definition** robot.hpp:489

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a5ee4537b589a74f8df79be730967bab7" class="ttc">

<div class="ttname">

[franky::Robot::state](classfranky_1_1_robot.md#a5ee4537b589a74f8df79be730967bab7)

</div>

<div class="ttdeci">

RobotState state()

</div>

<div class="ttdoc">

Returns the current state of the robot.

</div>

<div class="ttdef">

**Definition** robot.cpp:60

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a676d0b273cc01dd02fa536ce07992a73" class="ttc">

<div class="ttname">

[franky::Robot::translation\_jerk\_limit](classfranky_1_1_robot.md#a676d0b273cc01dd02fa536ce07992a73)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> translation\_jerk\_limit

</div>

<div class="ttdoc">

Translational jerk limit \[m/s³\].

</div>

<div class="ttdef">

**Definition** robot.hpp:474

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a7165eb847d474a244c6fba5b595cd84b" class="ttc">

<div class="ttname">

[franky::Robot::translation\_velocity\_limit](classfranky_1_1_robot.md#a7165eb847d474a244c6fba5b595cd84b)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> translation\_velocity\_limit

</div>

<div class="ttdoc">

Translational velocity limit \[m/s\].

</div>

<div class="ttdef">

**Definition** robot.hpp:444

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a7389f6e088ba456dd689c093ee6640e0" class="ttc">

<div class="ttname">

[franky::Robot::recoverFromErrors](classfranky_1_1_robot.md#a7389f6e088ba456dd689c093ee6640e0)

</div>

<div class="ttdeci">

bool recoverFromErrors()

</div>

<div class="ttdoc">

Calls the automatic error recovery of the robot and returns whether the recovery was successful.

</div>

<div class="ttdef">

**Definition** robot.cpp:55

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a823551f59caa0f025f1d6af381e38471" class="ttc">

<div class="ttname">

[franky::Robot::elbow\_velocity\_limit](classfranky_1_1_robot.md#a823551f59caa0f025f1d6af381e38471)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> elbow\_velocity\_limit

</div>

<div class="ttdoc">

Elbow velocity limit \[rad/s\].

</div>

<div class="ttdef">

**Definition** robot.hpp:454

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a83a0166687db4309de4f9cd7b76eb723" class="ttc">

<div class="ttname">

[franky::Robot::rotation\_velocity\_limit](classfranky_1_1_robot.md#a83a0166687db4309de4f9cd7b76eb723)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> rotation\_velocity\_limit

</div>

<div class="ttdoc">

Rotational velocity limit \[rad/s\].

</div>

<div class="ttdef">

**Definition** robot.hpp:449

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a87e2193710fe1cc287a21729bba88106" class="ttc">

<div class="ttname">

[franky::Robot::elbow\_jerk\_limit](classfranky_1_1_robot.md#a87e2193710fe1cc287a21729bba88106)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> elbow\_jerk\_limit

</div>

<div class="ttdoc">

Elbow jerk limit \[rad/s³\].

</div>

<div class="ttdef">

**Definition** robot.hpp:484

</div>

</div>

<div id="aclassfranky_1_1_robot_html_a971c769d2725f11c3437d28f9ad6de61" class="ttc">

<div class="ttname">

[franky::Robot::is\_in\_control](classfranky_1_1_robot.md#a971c769d2725f11c3437d28f9ad6de61)

</div>

<div class="ttdeci">

bool is\_in\_control()

</div>

<div class="ttdoc">

Whether the robot is currently in control, i.e. a motion is being executed.

</div>

<div class="ttdef">

**Definition** robot.cpp:105

</div>

</div>

<div id="aclassfranky_1_1_robot_html_aa031b868eacc474676306c3d581f43e7" class="ttc">

<div class="ttname">

[franky::Robot::move](classfranky_1_1_robot.md#aa031b868eacc474676306c3d581f43e7)

</div>

<div class="ttdeci">

void move(const std::shared\_ptr\< Motion\< franka::JointVelocities \> \> \&motion, bool async=false)

</div>

<div class="ttdoc">

Execute the given motion.

</div>

<div class="ttdef">

**Definition** robot.hpp:394

</div>

</div>

<div id="aclassfranky_1_1_robot_html_aa3bd3f0843a7c2c4aeae3d5c21d506b9" class="ttc">

<div class="ttname">

[franky::Robot::joint\_jerk\_limit](classfranky_1_1_robot.md#aa3bd3f0843a7c2c4aeae3d5c21d506b9)

</div>

<div class="ttdeci">

DynamicsLimit\< Vector7d \> joint\_jerk\_limit

</div>

<div class="ttdoc">

Joint jerk limit \[rad/s³\].

</div>

<div class="ttdef">

**Definition** robot.hpp:499

</div>

</div>

<div id="aclassfranky_1_1_robot_html_aab5abbad176d18599f25a4204e354cfb" class="ttc">

<div class="ttname">

[franky::Robot::currentJointState](classfranky_1_1_robot.md#aab5abbad176d18599f25a4204e354cfb)

</div>

<div class="ttdeci">

JointState currentJointState()

</div>

<div class="ttdoc">

Returns the current joint state of the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:253

</div>

</div>

<div id="aclassfranky_1_1_robot_html_aad586cb00aa450d5c51bc8260b9ad373" class="ttc">

<div class="ttname">

[franky::Robot::setCollisionBehavior](classfranky_1_1_robot.md#aad586cb00aa450d5c51bc8260b9ad373)

</div>

<div class="ttdeci">

void setCollisionBehavior(const ScalarOrArray\< 7 \> \&torque\_threshold, const ScalarOrArray\< 6 \> \&force\_threshold)

</div>

<div class="ttdoc">

Set the collision behavior of the robot.

</div>

<div class="ttdef">

**Definition** robot.cpp:72

</div>

</div>

<div id="aclassfranky_1_1_robot_html_aba9f9254a1af4fea2af758c450399c4c" class="ttc">

<div class="ttname">

[franky::Robot::degrees\_of\_freedoms](classfranky_1_1_robot.md#aba9f9254a1af4fea2af758c450399c4c)

</div>

<div class="ttdeci">

static constexpr size\_t degrees\_of\_freedoms

</div>

<div class="ttdef">

**Definition** robot.hpp:143

</div>

</div>

<div id="aclassfranky_1_1_robot_html_acb900ba5048aa792f4c16150703d8a6b" class="ttc">

<div class="ttname">

[franky::Robot::currentCartesianVelocity](classfranky_1_1_robot.md#acb900ba5048aa792f4c16150703d8a6b)

</div>

<div class="ttdeci">

RobotVelocity currentCartesianVelocity()

</div>

<div class="ttdoc">

Returns the current cartesian velocity of the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:237

</div>

</div>

<div id="aclassfranky_1_1_robot_html_ace7d9414a2e80b4a6c760578ebd382d3" class="ttc">

<div class="ttname">

[franky::Robot::rotation\_jerk\_limit](classfranky_1_1_robot.md#ace7d9414a2e80b4a6c760578ebd382d3)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> rotation\_jerk\_limit

</div>

<div class="ttdoc">

Rotational jerk limit \[rad/s³\].

</div>

<div class="ttdef">

**Definition** robot.hpp:479

</div>

</div>

<div id="aclassfranky_1_1_robot_html_ad014400edfd5bb1cf837fd09765ac5ce" class="ttc">

<div class="ttname">

[franky::Robot::move](classfranky_1_1_robot.md#ad014400edfd5bb1cf837fd09765ac5ce)

</div>

<div class="ttdeci">

void move(const std::shared\_ptr\< Motion\< franka::CartesianVelocities \> \> \&motion, bool async=false)

</div>

<div class="ttdoc">

Execute the given motion.

</div>

<div class="ttdef">

**Definition** robot.hpp:372

</div>

</div>

<div id="aclassfranky_1_1_robot_html_ad19caa63f0237d39463e5a3dd0b3e793" class="ttc">

<div class="ttname">

[franky::Robot::setRelativeDynamicsFactor](classfranky_1_1_robot.md#ad19caa63f0237d39463e5a3dd0b3e793)

</div>

<div class="ttdeci">

void setRelativeDynamicsFactor(const RelativeDynamicsFactor \&relative\_dynamics\_factor)

</div>

<div class="ttdoc">

Sets the global relative dynamics factor of the robot.

</div>

<div class="ttdef">

**Definition** robot.cpp:128

</div>

</div>

<div id="aclassfranky_1_1_robot_html_ad22fb0483ab2b3402b28b6f35dccaf9f" class="ttc">

<div class="ttname">

[franky::Robot::model](classfranky_1_1_robot.md#ad22fb0483ab2b3402b28b6f35dccaf9f)

</div>

<div class="ttdeci">

std::shared\_ptr\< const Model \> model() const

</div>

<div class="ttdoc">

The model of the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:310

</div>

</div>

<div id="aclassfranky_1_1_robot_html_ad31901ce61f3fce2adf885c776b7bb8a" class="ttc">

<div class="ttname">

[franky::Robot::translation\_acceleration\_limit](classfranky_1_1_robot.md#ad31901ce61f3fce2adf885c776b7bb8a)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> translation\_acceleration\_limit

</div>

<div class="ttdoc">

Translational acceleration limit \[m/s²\].

</div>

<div class="ttdef">

**Definition** robot.hpp:459

</div>

</div>

<div id="aclassfranky_1_1_robot_html_ad3d89c3fd930ea6590d0abd10fbdb755" class="ttc">

<div class="ttname">

[franky::Robot::hasErrors](classfranky_1_1_robot.md#ad3d89c3fd930ea6590d0abd10fbdb755)

</div>

<div class="ttdeci">

bool hasErrors()

</div>

<div class="ttdoc">

Returns whether the robot has errors.

</div>

<div class="ttdef">

**Definition** robot.cpp:53

</div>

</div>

<div id="aclassfranky_1_1_robot_html_adf04b2531a0ac4a16a759cc048d82e15" class="ttc">

<div class="ttname">

[franky::Robot::currentPose](classfranky_1_1_robot.md#adf04b2531a0ac4a16a759cc048d82e15)

</div>

<div class="ttdeci">

RobotPose currentPose()

</div>

<div class="ttdoc">

Returns the current pose of the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:231

</div>

</div>

<div id="aclassfranky_1_1_robot_html_ae7725e4fffdc28b8db727068a105707a" class="ttc">

<div class="ttname">

[franky::Robot::rotation\_acceleration\_limit](classfranky_1_1_robot.md#ae7725e4fffdc28b8db727068a105707a)

</div>

<div class="ttdeci">

DynamicsLimit\< double \> rotation\_acceleration\_limit

</div>

<div class="ttdoc">

Rotational acceleration limit \[rad/s²\].

</div>

<div class="ttdef">

**Definition** robot.hpp:464

</div>

</div>

<div id="aclassfranky_1_1_robot_html_afb00fbee84e00d09f3c8dedbfe5708f4" class="ttc">

<div class="ttname">

[franky::Robot::pollMotion](classfranky_1_1_robot.md#afb00fbee84e00d09f3c8dedbfe5708f4)

</div>

<div class="ttdeci">

bool pollMotion()

</div>

<div class="ttdoc">

Check whether the robot is still in motion. This function is non-blocking and returns immediately....

</div>

<div class="ttdef">

**Definition** robot.hpp:350

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

<div id="acontrol__signal__type_8hpp_html" class="ttc">

<div class="ttname">

[control\_signal\_type.hpp](control__signal__type_8hpp.md)

</div>

</div>

<div id="adynamics__limit_8hpp_html" class="ttc">

<div class="ttname">

[dynamics\_limit.hpp](dynamics__limit_8hpp.md)

</div>

</div>

<div id="ajoint__state_8hpp_html" class="ttc">

<div class="ttname">

[joint\_state.hpp](joint__state_8hpp.md)

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

<div id="anamespacefranky_html_ae77a95d5f13271457b8c8fb645da3bd9" class="ttc">

<div class="ttname">

[franky::ScalarOrArray](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9)

</div>

<div class="ttdeci">

std::variant\< double, Array\< dims \> \> ScalarOrArray

</div>

<div class="ttdef">

**Definition** types.hpp:21

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

<div id="arelative__dynamics__factor_8hpp_html" class="ttc">

<div class="ttname">

[relative\_dynamics\_factor.hpp](relative__dynamics__factor_8hpp.md)

</div>

</div>

<div id="arobot__pose_8hpp_html" class="ttc">

<div class="ttname">

[robot\_pose.hpp](robot__pose_8hpp.md)

</div>

</div>

<div id="arobot__state__estimator_8hpp_html" class="ttc">

<div class="ttname">

[robot\_state\_estimator.hpp](robot__state__estimator_8hpp.md)

</div>

</div>

<div id="arobot__velocity_8hpp_html" class="ttc">

<div class="ttname">

[robot\_velocity.hpp](robot__velocity_8hpp.md)

</div>

</div>

<div id="astructfranky_1_1_invalid_motion_type_exception_html" class="ttc">

<div class="ttname">

[franky::InvalidMotionTypeException](structfranky_1_1_invalid_motion_type_exception.md)

</div>

<div class="ttdoc">

Exception thrown when an invalid motion type is used.

</div>

<div class="ttdef">

**Definition** robot.hpp:37

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html" class="ttc">

<div class="ttname">

[franky::Robot::Params](structfranky_1_1_robot_1_1_params.md)

</div>

<div class="ttdoc">

Global parameters for the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:52

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a1e9c37c50668090f408db94e12e54bc9" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_dq\_process\_var](structfranky_1_1_robot_1_1_params.md#a1e9c37c50668090f408db94e12e54bc9)

</div>

<div class="ttdeci">

double kalman\_dq\_process\_var

</div>

<div class="ttdoc">

Kalman parameter: process noise variance of the velocity.

</div>

<div class="ttdef">

**Definition** robot.hpp:93

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a232bd0323512dd23a1e6003c906eb328" class="ttc">

<div class="ttname">

[franky::Robot::Params::relative\_dynamics\_factor](structfranky_1_1_robot_1_1_params.md#a232bd0323512dd23a1e6003c906eb328)

</div>

<div class="ttdeci">

RelativeDynamicsFactor relative\_dynamics\_factor

</div>

<div class="ttdoc">

Relative dynamics factor for the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:59

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a2535f117ddde7fd4294eeb952d4746bd" class="ttc">

<div class="ttname">

[franky::Robot::Params::default\_force\_threshold](structfranky_1_1_robot_1_1_params.md#a2535f117ddde7fd4294eeb952d4746bd)

</div>

<div class="ttdeci">

double default\_force\_threshold

</div>

<div class="ttdoc">

Default force threshold for collision behavior.

</div>

<div class="ttdef">

**Definition** robot.hpp:69

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a28da04d85b05bdc0483931fdb5ee9665" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_control\_adaptation\_rate](structfranky_1_1_robot_1_1_params.md#a28da04d85b05bdc0483931fdb5ee9665)

</div>

<div class="ttdeci">

double kalman\_control\_adaptation\_rate

</div>

<div class="ttdoc">

Kalman parameter: rate of adaptation of the robot state to the desired robot state.

</div>

<div class="ttdef">

**Definition** robot.hpp:139

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a2bccca1dff1d1cd4c4d7d1f0cae03f7b" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_dq\_obs\_var](structfranky_1_1_robot_1_1_params.md#a2bccca1dff1d1cd4c4d7d1f0cae03f7b)

</div>

<div class="ttdeci">

double kalman\_dq\_obs\_var

</div>

<div class="ttdoc">

Kalman parameter: observation noise variance of measured joint velocities.

</div>

<div class="ttdef">

**Definition** robot.hpp:115

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a304e57064f927eb2c00757a1d86d2e08" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_q\_obs\_var](structfranky_1_1_robot_1_1_params.md#a304e57064f927eb2c00757a1d86d2e08)

</div>

<div class="ttdeci">

double kalman\_q\_obs\_var

</div>

<div class="ttdoc">

Kalman parameter: observation noise variance of measured joint positions.

</div>

<div class="ttdef">

**Definition** robot.hpp:109

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a51f8d9dbacca9c18de1b2429bea65dae" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_dq\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#a51f8d9dbacca9c18de1b2429bea65dae)

</div>

<div class="ttdeci">

double kalman\_dq\_d\_obs\_var

</div>

<div class="ttdoc">

Kalman parameter: observation noise variance of desired joint velocities.

</div>

<div class="ttdef">

**Definition** robot.hpp:127

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a598cc77f3116a601bac482ddc4c74083" class="ttc">

<div class="ttname">

[franky::Robot::Params::controller\_mode](structfranky_1_1_robot_1_1_params.md#a598cc77f3116a601bac482ddc4c74083)

</div>

<div class="ttdeci">

franka::ControllerMode controller\_mode

</div>

<div class="ttdoc">

Default controller mode for the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:76

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a62b242c8c50ac828af9ac497b3cba801" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_control\_process\_var](structfranky_1_1_robot_1_1_params.md#a62b242c8c50ac828af9ac497b3cba801)

</div>

<div class="ttdeci">

double kalman\_control\_process\_var

</div>

<div class="ttdoc">

Kalman parameter: process noise variance of the control signal.

</div>

<div class="ttdef">

**Definition** robot.hpp:103

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a78a7c309785935bab49cdb24b5a750a8" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_q\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#a78a7c309785935bab49cdb24b5a750a8)

</div>

<div class="ttdeci">

double kalman\_q\_d\_obs\_var

</div>

<div class="ttdoc">

Kalman parameter: observation noise variance of desired joint positions.

</div>

<div class="ttdef">

**Definition** robot.hpp:121

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_a7c8199f22e083645746aa47020c97d56" class="ttc">

<div class="ttname">

[franky::Robot::Params::realtime\_config](structfranky_1_1_robot_1_1_params.md#a7c8199f22e083645746aa47020c97d56)

</div>

<div class="ttdeci">

franka::RealtimeConfig realtime\_config

</div>

<div class="ttdoc">

Default realtime configuration for the robot.

</div>

<div class="ttdef">

**Definition** robot.hpp:83

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_abeaee212f2cac08ce47158dc44bb6b71" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_ddq\_d\_obs\_var](structfranky_1_1_robot_1_1_params.md#abeaee212f2cac08ce47158dc44bb6b71)

</div>

<div class="ttdeci">

double kalman\_ddq\_d\_obs\_var

</div>

<div class="ttdoc">

Kalman parameter: observation noise variance of desired joint accelerations.

</div>

<div class="ttdef">

**Definition** robot.hpp:133

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_ac52be6b32e29563c8bb6576679bcbfa5" class="ttc">

<div class="ttname">

[franky::Robot::Params::default\_torque\_threshold](structfranky_1_1_robot_1_1_params.md#ac52be6b32e29563c8bb6576679bcbfa5)

</div>

<div class="ttdeci">

double default\_torque\_threshold

</div>

<div class="ttdoc">

Default torque threshold for collision behavior.

</div>

<div class="ttdef">

**Definition** robot.hpp:64

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_acd2d77ccd361a615b18b0a89fa0b2dd0" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_ddq\_process\_var](structfranky_1_1_robot_1_1_params.md#acd2d77ccd361a615b18b0a89fa0b2dd0)

</div>

<div class="ttdeci">

double kalman\_ddq\_process\_var

</div>

<div class="ttdoc">

Kalman parameter: process noise variance of the acceleration.

</div>

<div class="ttdef">

**Definition** robot.hpp:98

</div>

</div>

<div id="astructfranky_1_1_robot_1_1_params_html_ae6c5c63f100b88ae3fc1ae3dcd50c44e" class="ttc">

<div class="ttname">

[franky::Robot::Params::kalman\_q\_process\_var](structfranky_1_1_robot_1_1_params.md#ae6c5c63f100b88ae3fc1ae3dcd50c44e)

</div>

<div class="ttdeci">

double kalman\_q\_process\_var

</div>

<div class="ttdoc">

Kalman parameter: process noise variance of the position.

</div>

<div class="ttdef">

**Definition** robot.hpp:88

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

<div id="autil_8hpp_html" class="ttc">

<div class="ttname">

[util.hpp](util_8hpp.md)

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
