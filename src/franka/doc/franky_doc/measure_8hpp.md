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

<div class="summary">

[Classes](measure_8hpp.md#nested-classes) | [Namespaces](measure_8hpp.md#namespaces) | [Functions](measure_8hpp.md#func-members)

</div>

<div class="headertitle">

<div class="title">

measure.hpp File Reference

</div>

</div>

</div>

<div class="contents">

<div class="textblock">

`#include <franka/robot_state.h>`  
`#include <functional>`  
`#include <iostream>`  
`#include "franky/motion/condition.hpp"`  

</div>

[Go to the source code of this file.](measure_8hpp_source.md)

## <span id="nested-classes"></span> Classes

</div>

class  

[franky::Measure](classfranky_1_1_measure.md)

 

A measure on the robot state. [More...](classfranky_1_1_measure.md#details)  

 

## <span id="namespaces"></span> Namespaces

namespace  

[franky](namespacefranky.md)

 

## <span id="func-members"></span> Functions

[Condition](classfranky_1_1_condition.md) 

[franky::operator==](namespacefranky.md#aec1faf1176412ec30ace8d9360cd2219) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Condition](classfranky_1_1_condition.md) 

[franky::operator\!=](namespacefranky.md#ad0fd48f95175ccff51a008422b0c79d3) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Condition](classfranky_1_1_condition.md) 

[franky::operator\<=](namespacefranky.md#a5bf2ceb580fd8b51d8423d17fb9e07c8) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Condition](classfranky_1_1_condition.md) 

[franky::operator\>=](namespacefranky.md#ac292d7f5a4917cd61c4fe03d39122cbb) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Condition](classfranky_1_1_condition.md) 

[franky::operator\<](namespacefranky.md#a64f30e1c601485d8fc082abd272481ba) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Condition](classfranky_1_1_condition.md) 

[franky::operator\>](namespacefranky.md#ab8f28e1eb83ddefdf341ea8644dc0392) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Measure](classfranky_1_1_measure.md) 

[franky::operator+](namespacefranky.md#a3154ceacb8374282106cf479a8efb47b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Measure](classfranky_1_1_measure.md) 

[franky::operator-](namespacefranky.md#ade53467cfbd74e6684940c1e2e98bfe9) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Measure](classfranky_1_1_measure.md) 

[franky::operator\*](namespacefranky.md#ada1326a1aed3004af977c08461d30169) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Measure](classfranky_1_1_measure.md) 

[franky::operator/](namespacefranky.md#affb71a7e2efda9caca54bdf81cc56d68) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m1](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m2](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Measure](classfranky_1_1_measure.md) 

[franky::operator-](namespacefranky.md#ae1c89933ac509cfab2c71192d55b4176) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Measure](classfranky_1_1_measure.md) 

[franky::measure\_pow](namespacefranky.md#a0a18805109d5f09280f8830ce2970d3e) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[base](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[exponent](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
