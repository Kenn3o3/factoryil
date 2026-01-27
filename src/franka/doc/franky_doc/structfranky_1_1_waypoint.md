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
  - [Waypoint](structfranky_1_1_waypoint.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Attributes](structfranky_1_1_waypoint.md#pub-attribs) | [List of all members](structfranky_1_1_waypoint-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Waypoint\< TargetType \> Struct Template Reference

</div>

</div>

</div>

<div class="contents">

A waypoint with a target and optional parameters. [More...](structfranky_1_1_waypoint.md#details)

`#include <waypoint_motion.hpp>`

<div class="dynheader">

Inheritance diagram for franky::Waypoint\< TargetType \>:

</div>

<div class="dyncontent">

<div class="center">

![](structfranky_1_1_waypoint.png)

</div>

</div>

## <span id="pub-attribs"></span> Public Attributes

</div>

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
struct franky::Waypoint\< TargetType \>

</div>

A waypoint with a target and optional parameters.

  - Template Parameters
    
    |            |                         |
    | ---------- | ----------------------- |
    | TargetType | The type of the target. |
    

<!-- end list -->

  - Parameters
    
    |                            |                                                                                                                                                                                                             |
    | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | target                     | The target of this waypoint.                                                                                                                                                                                |
    | reference\_type            | The reference type (absolute or relative).                                                                                                                                                                  |
    | relative\_dynamics\_factor | The relative dynamics factor for this waypoint. This factor will get multiplied with the robot's global dynamics factor and the motion dynamics factor to get the actual dynamics factor for this waypoint. |
    | minimum\_time              | The minimum time to get to the next waypoint.                                                                                                                                                               |
    | hold\_target\_duration     | For how long to hold the target of this waypoint after it has been reached.                                                                                                                                 |
    | max\_total\_duration       | The maximum time to try reaching this waypoint before moving on to the next waypoint. Default is infinite.                                                                                                  |
    

</div>

## Member Data Documentation

<span id="a2c1e5c63e3a7447b4699a546e49ed009"></span>

## <span class="permalink">[◆ ](structfranky_1_1_waypoint.md#a2c1e5c63e3a7447b4699a546e49ed009)</span>hold\_target\_duration

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| franka::Duration [franky::Waypoint](structfranky_1_1_waypoint.md)\< [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::hold\_target\_duration {0} |

</div>

<div class="memdoc">

</div>

</div>

<span id="a2a1eae68a4e9d3b9c54a0ff1fd6c9bb2"></span>

## <span class="permalink">[◆ ](structfranky_1_1_waypoint.md#a2a1eae68a4e9d3b9c54a0ff1fd6c9bb2)</span>max\_total\_duration

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| std::optional\<franka::Duration\> [franky::Waypoint](structfranky_1_1_waypoint.md)\< [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::max\_total\_duration {std::nullopt} |

</div>

<div class="memdoc">

</div>

</div>

<span id="ae1532c5f277153a041d626ce4666d382"></span>

## <span class="permalink">[◆ ](structfranky_1_1_waypoint.md#ae1532c5f277153a041d626ce4666d382)</span>minimum\_time

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| std::optional\<franka::Duration\> [franky::Waypoint](structfranky_1_1_waypoint.md)\< [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::minimum\_time {std::nullopt} |

</div>

<div class="memdoc">

</div>

</div>

<span id="a88afd539ed0caff485c32cf830e9e121"></span>

## <span class="permalink">[◆ ](structfranky_1_1_waypoint.md#a88afd539ed0caff485c32cf830e9e121)</span>relative\_dynamics\_factor

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) [franky::Waypoint](structfranky_1_1_waypoint.md)\< [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::relative\_dynamics\_factor {1.0} |

</div>

<div class="memdoc">

</div>

</div>

<span id="a857fb8417fc17ff5e171494b1d398355"></span>

## <span class="permalink">[◆ ](structfranky_1_1_waypoint.md#a857fb8417fc17ff5e171494b1d398355)</span>target

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Waypoint](structfranky_1_1_waypoint.md)\< [TargetType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::target |

</div>

<div class="memdoc">

</div>

</div>

-----

The documentation for this struct was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/motion/[waypoint\_motion.hpp](waypoint__motion_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
