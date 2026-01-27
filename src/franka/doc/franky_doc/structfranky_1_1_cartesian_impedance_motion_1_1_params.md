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
  - [CartesianImpedanceMotion](classfranky_1_1_cartesian_impedance_motion.md)
  - [Params](structfranky_1_1_cartesian_impedance_motion_1_1_params.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Attributes](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#pub-attribs) | [List of all members](structfranky_1_1_cartesian_impedance_motion_1_1_params-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::CartesianImpedanceMotion::Params Struct Reference

</div>

</div>

</div>

<div class="contents">

Parameters for the Cartesian impedance motion. [More...](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#details)

`#include <cartesian_impedance_motion.hpp>`

<div class="dynheader">

Inheritance diagram for franky::CartesianImpedanceMotion::Params:

</div>

<div class="dyncontent">

<div class="center">

![](structfranky_1_1_cartesian_impedance_motion_1_1_params.png)

</div>

</div>

## <span id="pub-attribs"></span> Public Attributes

</div>

[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[return\_when\_finished](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#a55fe8148f737b8ab7856d39cb5e1733d) {[true](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[finish\_wait\_factor](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#acc7d37d06d998daec4c4a7c8dcfcf3cb) {1.2}

 

![-](closed.png) Public Attributes inherited from [franky::ImpedanceMotion::Params](structfranky_1_1_impedance_motion_1_1_params.md)

[ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e) 

[target\_type](structfranky_1_1_impedance_motion_1_1_params.md#a38a921916482fa544b8f6583c8f6850f) {[ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[translational\_stiffness](structfranky_1_1_impedance_motion_1_1_params.md#a122b129596499ae590225f7b1fe3bfd0) {2000}

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[rotational\_stiffness](structfranky_1_1_impedance_motion_1_1_params.md#afddc6620238e8713fe4e9c3ad507a4cc) {200}

 

Eigen::Vector\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 6 \> 

[force\_constraints](structfranky_1_1_impedance_motion_1_1_params.md#aa83f8133fcb021ce23b1e0bc998d4499)

 

Eigen::Vector\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 6 \> 

[force\_constraints\_active](structfranky_1_1_impedance_motion_1_1_params.md#aaa14fc3684c6a91038cf13a86dd865f9) {Eigen::Vector\<[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 6\>[::Zero](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)()}

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Parameters for the Cartesian impedance motion.

  - See also  
    [ImpedanceMotion::Params](structfranky_1_1_impedance_motion_1_1_params.md "Parameters for the impedance motion.")

</div>

## Member Data Documentation

<span id="acc7d37d06d998daec4c4a7c8dcfcf3cb"></span>

## <span class="permalink">[◆ ](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#acc7d37d06d998daec4c4a7c8dcfcf3cb)</span>finish\_wait\_factor

<div class="memitem">

<div class="memproto">

|                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::CartesianImpedanceMotion::Params::finish\_wait\_factor {1.2} |

</div>

<div class="memdoc">

How long to wait after the motion has finished. This factor gets multiplied with the duration of the motion to obtain the total motion duration. After the motion duration has expired, the motion will hold the target until the total motion duration is reached. E.g. a factor of 1.2 will hold the target for 20% longer than the motion duration.

</div>

</div>

<span id="a55fe8148f737b8ab7856d39cb5e1733d"></span>

## <span class="permalink">[◆ ](structfranky_1_1_cartesian_impedance_motion_1_1_params.md#a55fe8148f737b8ab7856d39cb5e1733d)</span>return\_when\_finished

<div class="memitem">

<div class="memproto">

|                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::CartesianImpedanceMotion::Params::return\_when\_finished {[true](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)} |

</div>

<div class="memdoc">

Whether to end the motion when the target is reached or keep holding the last target.

</div>

</div>

-----

The documentation for this struct was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/motion/[cartesian\_impedance\_motion.hpp](cartesian__impedance__motion_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
