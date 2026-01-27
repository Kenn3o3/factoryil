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

  - [src](dir_68267d1309a1af8e8297ef4c3efbcdba.md)
  - [motion](dir_ca2de2e9d8437914a4a3713259582ff6.md)

</div>

</div>

<div class="header">

<div class="summary">

[Namespaces](measure_8cpp.md#namespaces) | [Macros](measure_8cpp.md#define-members) | [Functions](measure_8cpp.md#func-members)

</div>

<div class="headertitle">

<div class="title">

measure.cpp File Reference

</div>

</div>

</div>

<div class="contents">

<div class="textblock">

`#include "franky/motion/measure.hpp"`  
`#include <franka/robot_state.h>`  
`#include <sstream>`  
`#include <utility>`  

</div>

## <span id="namespaces"></span> Namespaces

</div>

namespace  

[franky](namespacefranky.md)

 

## <span id="define-members"></span> Macros

\#define 

[MEASURE\_CMP\_DEF](measure_8cpp.md#ab03e1c9d729a553b46b39e8058a88f7d)(OP)

 

\#define 

[MEASURE\_OP\_DEF](measure_8cpp.md#af634d01b3a700d675d997bbaa2412d2a)(OP)

 

## <span id="func-members"></span> Functions

[Measure](classfranky_1_1_measure.md) 

[franky::measure\_pow](namespacefranky.md#a0a18805109d5f09280f8830ce2970d3e) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[base](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[exponent](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Measure](classfranky_1_1_measure.md) 

[franky::operator-](namespacefranky.md#ae1c89933ac509cfab2c71192d55b4176) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Measure](classfranky_1_1_measure.md) &[m](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

## Macro Definition Documentation

<span id="ab03e1c9d729a553b46b39e8058a88f7d"></span>

## <span class="permalink">[◆ ](measure_8cpp.md#ab03e1c9d729a553b46b39e8058a88f7d)</span>MEASURE\_CMP\_DEF

<div class="memitem">

<div class="memproto">

|                            |   |  |    |   |  |
| -------------------------- | - |  | -- | - |  |
| \#define MEASURE\_CMP\_DEF | ( |  | OP | ) |  |

</div>

<div class="memdoc">

**Value:**

<div class="fragment">

<div class="line">

Condition <span class="keyword">operator</span> OP(<span class="keyword">const</span> Measure \&m1, <span class="keyword">const</span> Measure \&m2) { \\

</div>

<div class="line">

std::stringstream ss; \\

</div>

<div class="line">

ss \<\< m1.repr() \<\< <span class="stringliteral">" "</span> \<\< \#OP \<\< <span class="stringliteral">" "</span> \<\< m2.repr(); \\

</div>

<div class="line">

<span class="keywordflow">return</span> Condition( \\

</div>

<div class="line">

\[m1, m2\](<span class="keyword">const</span> RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time) { \\

</div>

<div class="line">

<span class="keywordflow">return</span> m1(robot\_state, rel\_time, abs\_time) OP m2(robot\_state, rel\_time, abs\_time); \\

</div>

<div class="line">

}, \\

</div>

<div class="line">

ss.str()); \\

</div>

<div class="line">

}

</div>

</div>

</div>

</div>

<span id="af634d01b3a700d675d997bbaa2412d2a"></span>

## <span class="permalink">[◆ ](measure_8cpp.md#af634d01b3a700d675d997bbaa2412d2a)</span>MEASURE\_OP\_DEF

<div class="memitem">

<div class="memproto">

|                           |   |  |    |   |  |
| ------------------------- | - |  | -- | - |  |
| \#define MEASURE\_OP\_DEF | ( |  | OP | ) |  |

</div>

<div class="memdoc">

**Value:**

<div class="fragment">

<div class="line">

Measure <span class="keyword">operator</span> OP(<span class="keyword">const</span> Measure \&m1, <span class="keyword">const</span> Measure \&m2) { \\

</div>

<div class="line">

std::stringstream ss; \\

</div>

<div class="line">

ss \<\< <span class="stringliteral">"("</span> \<\< m1.repr() \<\< <span class="stringliteral">") "</span> \<\< \#OP \<\< <span class="stringliteral">" ("</span> \<\< m2.repr() \<\< <span class="stringliteral">")"</span>; \\

</div>

<div class="line">

<span class="keywordflow">return</span> Measure( \\

</div>

<div class="line">

\[m1, m2\](<span class="keyword">const</span> RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time) { \\

</div>

<div class="line">

<span class="keywordflow">return</span> m1(robot\_state, rel\_time, abs\_time) OP m2(robot\_state, rel\_time, abs\_time); \\

</div>

<div class="line">

}, \\

</div>

<div class="line">

ss.str()); \\

</div>

<div class="line">

}

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
