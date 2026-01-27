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

  - [franky](namespacefranky.md)
  - [RobotStateEstimator](classfranky_1_1_robot_state_estimator.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_robot_state_estimator.md#pub-methods) | [List of all members](classfranky_1_1_robot_state_estimator-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::RobotStateEstimator Class Reference

</div>

</div>

</div>

<div class="contents">

`#include <robot_state_estimator.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[RobotStateEstimator](classfranky_1_1_robot_state_estimator.md#a721e373a1b32f8ed2b7f07d7a756ce6e) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [q\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [dq\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ddq\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [control\_process\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [q\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [dq\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [q\_d\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [dq\_d\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ddq\_d\_obs\_var](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [control\_adaptation\_rate](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

 

[RobotStateEstimator](classfranky_1_1_robot_state_estimator.md#a69e0374844fe46ea58ae8c7e0db0c351) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotStateEstimator](classfranky_1_1_robot_state_estimator.md) &)=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[RobotState](structfranky_1_1_robot_state.md) 

[update](classfranky_1_1_robot_state_estimator.md#a7a1712e861d5790171fc0d9ec467687d) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::RobotState &[franka\_robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Model](classfranky_1_1_model.md) \&model)

 

[RobotState](structfranky_1_1_robot_state.md) 

[operator()](classfranky_1_1_robot_state_estimator.md#a832d262bc83ad2d21a5e8c9f63838cbb) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::RobotState &[franka\_robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Model](classfranky_1_1_model.md) \&model)

 

## Constructor & Destructor Documentation

<span id="a721e373a1b32f8ed2b7f07d7a756ce6e"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_state_estimator.md#a721e373a1b32f8ed2b7f07d7a756ce6e)</span>RobotStateEstimator() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                  |   |                                                                  |                             |
| ------------------------------------------------ | - | ---------------------------------------------------------------- | --------------------------- |
| franky::RobotStateEstimator::RobotStateEstimator | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *q\_process\_var*,          |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *dq\_process\_var*,         |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *ddq\_process\_var*,        |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *control\_process\_var*,    |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *q\_obs\_var*,              |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *dq\_obs\_var*,             |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *q\_d\_obs\_var*,           |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *dq\_d\_obs\_var*,          |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *ddq\_d\_obs\_var*,         |
|                                                  |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *control\_adaptation\_rate* |
|                                                  | ) |                                                                  |                             |

</div>

<div class="memdoc">

</div>

</div>

<span id="a69e0374844fe46ea58ae8c7e0db0c351"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_state_estimator.md#a69e0374844fe46ea58ae8c7e0db0c351)</span>RobotStateEstimator() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td>franky::RobotStateEstimator::RobotStateEstimator</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_robot_state_estimator.md" class="el">RobotStateEstimator</a> &amp; </td>
<td></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">default</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

## Member Function Documentation

<span id="a832d262bc83ad2d21a5e8c9f63838cbb"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_state_estimator.md#a832d262bc83ad2d21a5e8c9f63838cbb)</span>operator()()

<div class="memitem">

<div class="memproto">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<tbody>
<tr class="odd">
<td><a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> franky::RobotStateEstimator::operator()</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> franka::RobotState &amp; </td>
<td><em>franka_robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_model.md" class="el">Model</a> &amp; </td>
<td><em>model</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="a7a1712e861d5790171fc0d9ec467687d"></span>

## <span class="permalink">[◆ ](classfranky_1_1_robot_state_estimator.md#a7a1712e861d5790171fc0d9ec467687d)</span>update()

<div class="memitem">

<div class="memproto">

|                                                                                     |   |                                                                                                       |                         |
| ----------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------- | ----------------------- |
| [RobotState](structfranky_1_1_robot_state.md) franky::RobotStateEstimator::update | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::RobotState &                  | *franka\_robot\_state*, |
|                                                                                     |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Model](classfranky_1_1_model.md) & | *model*                 |
|                                                                                     | ) |                                                                                                       |                         |

</div>

<div class="memdoc">

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/[robot\_state\_estimator.hpp](robot__state__estimator_8hpp_source.md)
  - /home/runner/work/franky/franky/src/[robot\_state\_estimator.cpp](robot__state__estimator_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
