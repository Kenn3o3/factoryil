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
  - [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_relative_dynamics_factor.md#pub-methods) | [Static Public Member Functions](classfranky_1_1_relative_dynamics_factor.md#pub-static-methods) | [List of all members](classfranky_1_1_relative_dynamics_factor-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::RelativeDynamicsFactor Class Reference

</div>

</div>

</div>

<div class="contents">

Relative dynamics factors. [More...](classfranky_1_1_relative_dynamics_factor.md#details)

`#include <relative_dynamics_factor.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a7e43b12bb5d338ac74ef57c4fd791a6e) ()

 

Default constructor which initializes all values to 1.0.  

 

 

[RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a1e9ca6a5cc1d3663171e303f0b8eb3da) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [value](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Constructor which initializes all values to the given value.  

 

 

[RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md#a27eeb2985fbdf34e048942d63cc48e63) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [velocity](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [acceleration](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [jerk](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be))

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[velocity](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Velocity factor.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[acceleration](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Acceleration factor.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[jerk](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Jerk factor.  

 

[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[max\_dynamics](classfranky_1_1_relative_dynamics_factor.md#a7dbf4dc92014c7533ee0090581308b90) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Whether the maximum dynamics should be used.  

 

[RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) 

[operator\*](classfranky_1_1_relative_dynamics_factor.md#ab5a59d78758ae5fc747cce2df95022f1) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) &[other](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

## <span id="pub-static-methods"></span> Static Public Member Functions

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) 

[MAX\_DYNAMICS](classfranky_1_1_relative_dynamics_factor.md#aafb78c44330199e27db6b3f662307c14) ()

 

Special factor which causes the maximum dynamics to be used, independent of other factors applied elsewhere.  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

Relative dynamics factors.

This class encapsulates the relative dynamics factors, which are used to scale the maximum velocity, acceleration, and jerk of a trajectory.

</div>

## Constructor & Destructor Documentation

<span id="a7e43b12bb5d338ac74ef57c4fd791a6e"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#a7e43b12bb5d338ac74ef57c4fd791a6e)</span>RelativeDynamicsFactor() <span class="overload">\[1/3\]</span>

<div class="memitem">

<div class="memproto">

|                                                        |   |  |   |  |
| ------------------------------------------------------ | - |  | - |  |
| franky::RelativeDynamicsFactor::RelativeDynamicsFactor | ( |  | ) |  |

</div>

<div class="memdoc">

Default constructor which initializes all values to 1.0.

</div>

</div>

<span id="a1e9ca6a5cc1d3663171e303f0b8eb3da"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#a1e9ca6a5cc1d3663171e303f0b8eb3da)</span>RelativeDynamicsFactor() <span class="overload">\[2/3\]</span>

<div class="memitem">

<div class="memproto">

|                                                        |   |                                                                  |         |   |  |
| ------------------------------------------------------ | - | ---------------------------------------------------------------- | ------- | - |  |
| franky::RelativeDynamicsFactor::RelativeDynamicsFactor | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *value* | ) |  |

</div>

<div class="memdoc">

Constructor which initializes all values to the given value.

  - Parameters
    
    |       |                                                                         |
    | ----- | ----------------------------------------------------------------------- |
    | value | The value to initialize all factors with. Must be in the range (0, 1\]. |
    

</div>

</div>

<span id="a27eeb2985fbdf34e048942d63cc48e63"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#a27eeb2985fbdf34e048942d63cc48e63)</span>RelativeDynamicsFactor() <span class="overload">\[3/3\]</span>

<div class="memitem">

<div class="memproto">

|                                                        |   |                                                                  |                 |
| ------------------------------------------------------ | - | ---------------------------------------------------------------- | --------------- |
| franky::RelativeDynamicsFactor::RelativeDynamicsFactor | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *velocity*,     |
|                                                        |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *acceleration*, |
|                                                        |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *jerk*          |
|                                                        | ) |                                                                  |                 |

</div>

<div class="memdoc">

  - Parameters
    
    |              |                                                                |
    | ------------ | -------------------------------------------------------------- |
    | velocity     | The factor for the velocity. Must be in the range (0, 1\].     |
    | acceleration | The factor for the acceleration. Must be in the range (0, 1\]. |
    | jerk         | The factor for the jerk. Must be in the range (0, 1\].         |
    

</div>

</div>

## Member Function Documentation

<span id="a34da6e78cb104a1628a7dfb25038cd30"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#a34da6e78cb104a1628a7dfb25038cd30)</span>acceleration()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> franky::RelativeDynamicsFactor::acceleration</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Acceleration factor.

</div>

</div>

<span id="a1d7f32132b99026d50ad3f683552a4be"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#a1d7f32132b99026d50ad3f683552a4be)</span>jerk()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> franky::RelativeDynamicsFactor::jerk</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Jerk factor.

</div>

</div>

<span id="aafb78c44330199e27db6b3f662307c14"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#aafb78c44330199e27db6b3f662307c14)</span>MAX\_DYNAMICS()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">static</a> <a href="classfranky_1_1_relative_dynamics_factor.md" class="el">RelativeDynamicsFactor</a> franky::RelativeDynamicsFactor::MAX_DYNAMICS</td>
<td>(</td>
<td></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">static</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Special factor which causes the maximum dynamics to be used, independent of other factors applied elsewhere.

</div>

</div>

<span id="a7dbf4dc92014c7533ee0090581308b90"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#a7dbf4dc92014c7533ee0090581308b90)</span>max\_dynamics()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> franky::RelativeDynamicsFactor::max_dynamics</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Whether the maximum dynamics should be used.

</div>

</div>

<span id="ab5a59d78758ae5fc747cce2df95022f1"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#ab5a59d78758ae5fc747cce2df95022f1)</span>operator\*()

<div class="memitem">

<div class="memproto">

|                                                                                                                    |   |                                                                                                                                           |         |   |       |
| ------------------------------------------------------------------------------------------------------------------ | - | ----------------------------------------------------------------------------------------------------------------------------------------- | ------- | - | ----- |
| [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) franky::RelativeDynamicsFactor::operator\* | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RelativeDynamicsFactor](classfranky_1_1_relative_dynamics_factor.md) & | *other* | ) | const |

</div>

<div class="memdoc">

</div>

</div>

<span id="afd6505e3977f86efea0cae6bd3dca074"></span>

## <span class="permalink">[◆ ](classfranky_1_1_relative_dynamics_factor.md#afd6505e3977f86efea0cae6bd3dca074)</span>velocity()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> franky::RelativeDynamicsFactor::velocity</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Velocity factor.

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/[relative\_dynamics\_factor.hpp](relative__dynamics__factor_8hpp_source.md)
  - /home/runner/work/franky/franky/src/[relative\_dynamics\_factor.cpp](relative__dynamics__factor_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
