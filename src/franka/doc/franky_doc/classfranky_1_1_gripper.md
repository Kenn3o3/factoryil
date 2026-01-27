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
  - [Gripper](classfranky_1_1_gripper.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_gripper.md#pub-methods) | [List of all members](classfranky_1_1_gripper-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Gripper Class Reference

</div>

</div>

</div>

<div class="contents">

A wrapper around the franka::Gripper class that adds asynchronous functionality. [More...](classfranky_1_1_gripper.md#details)

`#include <gripper.hpp>`

<div class="dynheader">

Inheritance diagram for franky::Gripper:

</div>

<div class="dyncontent">

<div class="center">

![](classfranky_1_1_gripper.png)

</div>

</div>

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[Gripper](classfranky_1_1_gripper.md#ad496a52d3a7a01926c8fd6e679901a89) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::string &[franka\_address](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

 

[Gripper](classfranky_1_1_gripper.md#ac6996e448e7a780d67682743cd836da9) ([Gripper](classfranky_1_1_gripper.md) &&[gripper](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [noexcept](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[graspAsync](classfranky_1_1_gripper.md#a39998a7c1c4ea04403e9dc74e2459d5f) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [width](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [speed](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [force](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [epsilon\_inner](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=0.005, [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [epsilon\_outer](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)=0.005)

 

Asynchronous variant of the franka::Gripper::grasp function.  

 

std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[moveAsync](classfranky_1_1_gripper.md#a9e8dbe460f5b1cf277ad281906fe8ed7) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [width](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e), [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [speed](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Asynchronous variant of the franka::Gripper::move function.  

 

[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[open](classfranky_1_1_gripper.md#a6f9b3b3a14eefe618b480a4e932dce24) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [speed](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Opens the gripper fully.  

 

std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[openAsync](classfranky_1_1_gripper.md#aa1b54a5041bdc3c8161cd8da895388c6) ([double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [speed](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Asynchronous variant of the open function.  

 

std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[homingAsync](classfranky_1_1_gripper.md#af81ac0bf44132f338e43e64d8c10ea7e) ()

 

Asynchronous variant of the franka::Gripper::homing function.  

 

std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[stopAsync](classfranky_1_1_gripper.md#aa272b7106a9a5262a0bfc76ed36e002b) ()

 

Asynchronous variant of the franka::Gripper::stop function.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[width](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Current opening width of the gripper \[m\].  

 

[bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[is\_grasped](classfranky_1_1_gripper.md#a792b6d30ee087a4cddba5e3d2320d6e9) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Whether the gripper is grasping.  

 

[double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[max\_width](classfranky_1_1_gripper.md#a5ae2659a6edf6e117fc461f60191c9db) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Maximum width of the gripper \[m\].  

 

franka::GripperState 

[state](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Current gripper state.  

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

A wrapper around the franka::Gripper class that adds asynchronous functionality.

</div>

## Constructor & Destructor Documentation

<span id="ad496a52d3a7a01926c8fd6e679901a89"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#ad496a52d3a7a01926c8fd6e679901a89)</span>Gripper() <span class="overload">\[1/2\]</span>

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
<td>franky::Gripper::Gripper</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::string &amp; </td>
<td><em>franka_address</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">explicit</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="ac6996e448e7a780d67682743cd836da9"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#ac6996e448e7a780d67682743cd836da9)</span>Gripper() <span class="overload">\[2/2\]</span>

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
<td>franky::Gripper::Gripper</td>
<td>(</td>
<td><a href="classfranky_1_1_gripper.md" class="el">Gripper</a> &amp;&amp; </td>
<td><em>gripper</em></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">noexcept</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

## Member Function Documentation

<span id="a39998a7c1c4ea04403e9dc74e2459d5f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#a39998a7c1c4ea04403e9dc74e2459d5f)</span>graspAsync()

<div class="memitem">

<div class="memproto">

|                                                                                                                     |   |                                                                  |                             |
| ------------------------------------------------------------------------------------------------------------------- | - | ---------------------------------------------------------------- | --------------------------- |
| std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> franky::Gripper::graspAsync | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *width*,                    |
|                                                                                                                     |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *speed*,                    |
|                                                                                                                     |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *force*,                    |
|                                                                                                                     |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *epsilon\_inner* = `0.005`, |
|                                                                                                                     |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *epsilon\_outer* = `0.005`  |
|                                                                                                                     | ) |                                                                  |                             |

</div>

<div class="memdoc">

Asynchronous variant of the franka::Gripper::grasp function.

  - Parameters
    
    |                |                                                                                                      |
    | -------------- | ---------------------------------------------------------------------------------------------------- |
    | width          | Size of the object to grasp in \[m\].                                                                |
    | speed          | Closing speed in \[m/s\].                                                                            |
    | force          | Grasping force in \[N\].                                                                             |
    | epsilon\_inner | Maximum tolerated deviation when the actual grasped width is smaller than the commanded grasp width. |
    | epsilon\_outer | Maximum tolerated deviation when the actual grasped width is larger than the commanded grasp width.  |
    

<!-- end list -->

  - Returns  
    Future that becomes ready when the grasp is finished. Contains true if an object has been grasped, false otherwise.

</div>

</div>

<span id="af81ac0bf44132f338e43e64d8c10ea7e"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#af81ac0bf44132f338e43e64d8c10ea7e)</span>homingAsync()

<div class="memitem">

<div class="memproto">

|                                                                                                                      |   |  |   |  |
| -------------------------------------------------------------------------------------------------------------------- | - |  | - |  |
| std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> franky::Gripper::homingAsync | ( |  | ) |  |

</div>

<div class="memdoc">

Asynchronous variant of the franka::Gripper::homing function.

  - Returns  
    A future that becomes ready when the homing is finished. Contains true if the homing was successful.

</div>

</div>

<span id="a792b6d30ee087a4cddba5e3d2320d6e9"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#a792b6d30ee087a4cddba5e3d2320d6e9)</span>is\_grasped()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a> franky::Gripper::is_grasped</td>
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

Whether the gripper is grasping.

</div>

</div>

<span id="a5ae2659a6edf6e117fc461f60191c9db"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#a5ae2659a6edf6e117fc461f60191c9db)</span>max\_width()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> franky::Gripper::max_width</td>
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

Maximum width of the gripper \[m\].

</div>

</div>

<span id="a9e8dbe460f5b1cf277ad281906fe8ed7"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#a9e8dbe460f5b1cf277ad281906fe8ed7)</span>moveAsync()

<div class="memitem">

<div class="memproto">

|                                                                                                                    |   |                                                                  |          |
| ------------------------------------------------------------------------------------------------------------------ | - | ---------------------------------------------------------------- | -------- |
| std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> franky::Gripper::moveAsync | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *width*, |
|                                                                                                                    |   | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *speed*  |
|                                                                                                                    | ) |                                                                  |          |

</div>

<div class="memdoc">

Asynchronous variant of the franka::Gripper::move function.

  - Parameters
    
    |       |                                   |
    | ----- | --------------------------------- |
    | width | Intended opening width in \[m\].  |
    | speed | Speed of the movement in \[m/s\]. |
    

<!-- end list -->

  - Returns  
    Future that becomes ready when the movement is finished. Contains true if the movement was successful,

</div>

</div>

<span id="a6f9b3b3a14eefe618b480a4e932dce24"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#a6f9b3b3a14eefe618b480a4e932dce24)</span>open()

<div class="memitem">

<div class="memproto">

|                                                                                      |   |                                                                  |         |   |  |
| ------------------------------------------------------------------------------------ | - | ---------------------------------------------------------------- | ------- | - |  |
| [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franky::Gripper::open | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *speed* | ) |  |

</div>

<div class="memdoc">

Opens the gripper fully.

  - Parameters
    
    |       |                                   |
    | ----- | --------------------------------- |
    | speed | Speed of the movement in \[m/s\]. |
    

<!-- end list -->

  - Returns  
    True if the gripper was opened successfully.

</div>

</div>

<span id="aa1b54a5041bdc3c8161cd8da895388c6"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#aa1b54a5041bdc3c8161cd8da895388c6)</span>openAsync()

<div class="memitem">

<div class="memproto">

|                                                                                                                    |   |                                                                  |         |   |  |
| ------------------------------------------------------------------------------------------------------------------ | - | ---------------------------------------------------------------- | ------- | - |  |
| std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> franky::Gripper::openAsync | ( | [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) | *speed* | ) |  |

</div>

<div class="memdoc">

Asynchronous variant of the open function.

  - Parameters
    
    |       |                                   |
    | ----- | --------------------------------- |
    | speed | Speed of the movement in \[m/s\]. |
    

<!-- end list -->

  - Returns  
    Future that becomes ready when the gripper is fully opened. Contains true if the gripper was opened successfully.

</div>

</div>

<span id="abb8531bbdefc46cbd15f36a3ad40b1e8"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#abb8531bbdefc46cbd15f36a3ad40b1e8)</span>state()

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
<td>franka::GripperState franky::Gripper::state</td>
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

Current gripper state.

</div>

</div>

<span id="aa272b7106a9a5262a0bfc76ed36e002b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#aa272b7106a9a5262a0bfc76ed36e002b)</span>stopAsync()

<div class="memitem">

<div class="memproto">

|                                                                                                                    |   |  |   |  |
| ------------------------------------------------------------------------------------------------------------------ | - |  | - |  |
| std::shared\_future\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> franky::Gripper::stopAsync | ( |  | ) |  |

</div>

<div class="memdoc">

Asynchronous variant of the franka::Gripper::stop function.

  - Returns  
    A future that becomes ready when the stop is finished. Contains true if the stop was successful.

</div>

</div>

<span id="a176c18c2ca98694075eea1085dc65a7e"></span>

## <span class="permalink">[◆ ](classfranky_1_1_gripper.md#a176c18c2ca98694075eea1085dc65a7e)</span>width()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">double</a> franky::Gripper::width</td>
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

Current opening width of the gripper \[m\].

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/[gripper.hpp](gripper_8hpp_source.md)
  - /home/runner/work/franky/franky/src/[gripper.cpp](gripper_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
