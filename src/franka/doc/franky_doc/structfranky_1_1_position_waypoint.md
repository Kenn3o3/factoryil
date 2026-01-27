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
  - [PositionWaypoint](structfranky_1_1_position_waypoint.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Attributes](structfranky_1_1_position_waypoint.md#pub-attribs) | [List of all members](structfranky_1_1_position_waypoint-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::PositionWaypoint\< TargetType \> Struct Template Reference

</div>

</div>

</div>

<div class="contents">

A position waypoint with a target and optional parameters. [More...](structfranky_1_1_position_waypoint.md#details)

`#include <position_waypoint_motion.hpp>`

<div class="dynheader">

Inheritance diagram for franky::PositionWaypoint\< TargetType \>:

</div>

<div class="dyncontent">

<div class="center">

![](structfranky_1_1_position_waypoint.png)

</div>

</div>

## <span id="pub-attribs"></span> Public Attributes

</div>

[ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e) 

[reference\_type](structfranky_1_1_position_waypoint.md#ac5dee69cb4ee3ab71a80cd54244ad220) {[ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)}

 

![-](closed.png) Public Attributes inherited from [franky::Waypoint\< TargetType \>](structfranky_1_1_waypoint.md)

[TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[target](structfranky_1_1_waypoint.md#a857fb8417fc17ff5e171494b1d398355)

 

[RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) 

[relative\_dynamics\_factor](structfranky_1_1_waypoint.md#a88afd539ed0caff485c32cf830e9e121) {1.0}

 

std::optional\< franka::Duration \> 

[minimum\_time](structfranky_1_1_waypoint.md#ae1532c5f277153a041d626ce4666d382) {std::nullopt}

 

franka::Duration 

[hold\_target\_duration](structfranky_1_1_waypoint.md#a2c1e5c63e3a7447b4699a546e49ed009) {0}

 

std::optional\< franka::Duration \> 

[max\_total\_duration](structfranky_1_1_waypoint.md#a2a1eae68a4e9d3b9c54a0ff1fd6c9bb2) {std::nullopt}

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

<div class="compoundTemplParams">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>  
struct franky::PositionWaypoint\< TargetType \>

</div>

A position waypoint with a target and optional parameters.

  - Template Parameters
    
    |            |                         |
    | ---------- | ----------------------- |
    | TargetType | The type of the target. |
    

<!-- end list -->

  - Parameters
    
    |                 |                                            |
    | --------------- | ------------------------------------------ |
    | reference\_type | The reference type (absolute or relative). |
    

</div>

## Member Data Documentation

<span id="ac5dee69cb4ee3ab71a80cd54244ad220"></span>

## <span class="permalink">[◆ ](structfranky_1_1_position_waypoint.md#ac5dee69cb4ee3ab71a80cd54244ad220)</span>reference\_type

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e) [franky::PositionWaypoint](structfranky_1_1_position_waypoint.md)\< [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::reference\_type {[ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)} |

</div>

<div class="memdoc">

</div>

</div>

-----

The documentation for this struct was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/motion/[position\_waypoint\_motion.hpp](position__waypoint__motion_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
