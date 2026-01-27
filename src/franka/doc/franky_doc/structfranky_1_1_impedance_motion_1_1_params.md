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
  - [ImpedanceMotion](classfranky_1_1_impedance_motion.md)
  - [Params](structfranky_1_1_impedance_motion_1_1_params.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Attributes](structfranky_1_1_impedance_motion_1_1_params.md#pub-attribs) | [List of all members](structfranky_1_1_impedance_motion_1_1_params-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::ImpedanceMotion::Params Struct Reference

</div>

</div>

</div>

<div class="contents">

Parameters for the impedance motion. [More...](structfranky_1_1_impedance_motion_1_1_params.md#details)

`#include <impedance_motion.hpp>`

<div class="dynheader">

Inheritance diagram for franky::ImpedanceMotion::Params:

</div>

<div class="dyncontent">

<div class="center">

![](structfranky_1_1_impedance_motion_1_1_params.png)

</div>

</div>

## <span id="pub-attribs"></span> Public Attributes

</div>

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

Parameters for the impedance motion.

</div>

## Member Data Documentation

<span id="aa83f8133fcb021ce23b1e0bc998d4499"></span>

## <span class="permalink">[◆ ](structfranky_1_1_impedance_motion_1_1_params.md#aa83f8133fcb021ce23b1e0bc998d4499)</span>force\_constraints

<div class="memitem">

<div class="memproto">

|                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------- |
| Eigen::Vector\<[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 6\> franky::ImpedanceMotion::Params::force\_constraints |

</div>

<div class="memdoc">

The force constraints in \[N, Nm\] for each joint.

</div>

</div>

<span id="aaa14fc3684c6a91038cf13a86dd865f9"></span>

## <span class="permalink">[◆ ](structfranky_1_1_impedance_motion_1_1_params.md#aaa14fc3684c6a91038cf13a86dd865f9)</span>force\_constraints\_active

<div class="memitem">

<div class="memproto">

|                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Eigen::Vector\<[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 6\> franky::ImpedanceMotion::Params::force\_constraints\_active {Eigen::Vector\<[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 6\>[::Zero](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)()} |

</div>

<div class="memdoc">

Allows to enable or disable individual force constraints.

</div>

</div>

<span id="afddc6620238e8713fe4e9c3ad507a4cc"></span>

## <span class="permalink">[◆ ](structfranky_1_1_impedance_motion_1_1_params.md#afddc6620238e8713fe4e9c3ad507a4cc)</span>rotational\_stiffness

<div class="memitem">

<div class="memproto">

|                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::ImpedanceMotion::Params::rotational\_stiffness {200} |

</div>

<div class="memdoc">

The rotational stiffness in \[1, 300\] Nm/rad.

</div>

</div>

<span id="a38a921916482fa544b8f6583c8f6850f"></span>

## <span class="permalink">[◆ ](structfranky_1_1_impedance_motion_1_1_params.md#a38a921916482fa544b8f6583c8f6850f)</span>target\_type

<div class="memitem">

<div class="memproto">

|                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ReferenceType](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80e) franky::ImpedanceMotion::Params::target\_type {[ReferenceType::kAbsolute](namespacefranky.md#a2354a27cfe3100f07e0ad71513ded80eabab0767e88027de9944aa55c24c8387a)} |

</div>

<div class="memdoc">

The type of the target reference (relative or absolute).

</div>

</div>

<span id="a122b129596499ae590225f7b1fe3bfd0"></span>

## <span class="permalink">[◆ ](structfranky_1_1_impedance_motion_1_1_params.md#a122b129596499ae590225f7b1fe3bfd0)</span>translational\_stiffness

<div class="memitem">

<div class="memproto">

|                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------- |
| [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::ImpedanceMotion::Params::translational\_stiffness {2000} |

</div>

<div class="memdoc">

The translational stiffness in \[10, 3000\] N/m.

</div>

</div>

-----

The documentation for this struct was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/motion/[impedance\_motion.hpp](impedance__motion_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
