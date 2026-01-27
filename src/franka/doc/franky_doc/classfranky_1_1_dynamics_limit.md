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
  - [DynamicsLimit](classfranky_1_1_dynamics_limit.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_dynamics_limit.md#pub-methods) | [Public Attributes](classfranky_1_1_dynamics_limit.md#pub-attribs) | [Friends](classfranky_1_1_dynamics_limit.md#friends) | [List of all members](classfranky_1_1_dynamics_limit-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::DynamicsLimit\< LimitType \> Class Template Reference

</div>

</div>

</div>

<div class="contents">

A template class representing a dynamics limit with a maximum value. [More...](classfranky_1_1_dynamics_limit.md#details)

`#include <dynamics_limit.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[DynamicsLimit](classfranky_1_1_dynamics_limit.md#a344e2c223138ec679d26af30e5fdd9e5) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::string &[desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[max\_val](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::shared\_ptr\< std::mutex \> &[write\_mutex](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::function\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)()\> &[can\_write\_condition](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Constructor for [DynamicsLimit](classfranky_1_1_dynamics_limit.md "A template class representing a dynamics limit with a maximum value.").  

 

 

[DynamicsLimit](classfranky_1_1_dynamics_limit.md#addd366f6d40b581abd6463ca61cfd2c5) (std::string [desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[max\_val](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::shared\_ptr\< std::mutex \> &[write\_mutex](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::function\< [bool](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)()\> &[can\_write\_condition](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[default\_val](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Constructor for [DynamicsLimit](classfranky_1_1_dynamics_limit.md "A template class representing a dynamics limit with a maximum value.").  

 

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [AlternativeType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[setFrom](classfranky_1_1_dynamics_limit.md#adbb6e9b426e82b05272e2fe3939e8eb5) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [AlternativeType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[value](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Set a new value for the limit with a different type.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[set](classfranky_1_1_dynamics_limit.md#a13c429626a61ddf6b37ad38e8b7ee9ec) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[value](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Set a new value for the limit.  

 

[LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[get](classfranky_1_1_dynamics_limit.md#a39d85438237067ffa3b3829500b01f14) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the current value of the limit.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[setFrom](classfranky_1_1_dynamics_limit.md#a8183726a4540729a377615e0e207f154) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\< 7 \> &[value](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

## <span id="pub-attribs"></span> Public Attributes

[const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[max](classfranky_1_1_dynamics_limit.md#a8ad7788915e12262221aa983c0588d62)

 

The maximum value this limit can take as defined by Franka.  

 

[const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::string 

[desc](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad)

 

Description of this limit.  

 

## <span id="friends"></span> Friends

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitTypeStream](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

std::ostream & 

[operator\<\<](classfranky_1_1_dynamics_limit.md#a1909095817a8e86989d8c822e3ea2fb3) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [DynamicsLimit](classfranky_1_1_dynamics_limit.md)\< [LimitTypeStream](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[dynamics\_limit](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

<div class="compoundTemplParams">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\>  
class franky::DynamicsLimit\< LimitType \>

</div>

A template class representing a dynamics limit with a maximum value.

This class provides functionality to store and manage a dynamic limit, including setting and getting the value of the limit while ensuring that it cannot be written while the robot is in control.

  - Template Parameters
    
    |           |                                                  |
    | --------- | ------------------------------------------------ |
    | LimitType | The type of the limit value (e.g., double, int). |
    

</div>

## Constructor & Destructor Documentation

<span id="a344e2c223138ec679d26af30e5fdd9e5"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#a344e2c223138ec679d26af30e5fdd9e5)</span>DynamicsLimit() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

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
<td><a href="classfranky_1_1_dynamics_limit.md" class="el">franky::DynamicsLimit</a>&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &gt;::DynamicsLimit</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::string &amp; </td>
<td><em>desc</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &amp; </td>
<td><em>max_val</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::shared_ptr&lt; std::mutex &gt; &amp; </td>
<td><em>write_mutex</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::function&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a>()&gt; &amp; </td>
<td><em>can_write_condition</em> </td>
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

Constructor for [DynamicsLimit](classfranky_1_1_dynamics_limit.md "A template class representing a dynamics limit with a maximum value.").

Initializes a new instance of the [DynamicsLimit](classfranky_1_1_dynamics_limit.md "A template class representing a dynamics limit with a maximum value.") class with the provided values. The maximum value is used as default value by this constructor.

  - Parameters
    
    |                       |                                                                           |
    | --------------------- | ------------------------------------------------------------------------- |
    | desc                  | A string description of the limit (e.g., "joint velocity").               |
    | max\_val              | The maximum allowable value for this limit.                               |
    | write\_mutex          | A shared pointer to the mutex used for synchronizing writes to the limit. |
    | can\_write\_condition | A function that returns true if the limit can be written to.              |
    

</div>

</div>

<span id="addd366f6d40b581abd6463ca61cfd2c5"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#addd366f6d40b581abd6463ca61cfd2c5)</span>DynamicsLimit() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

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
<td><a href="classfranky_1_1_dynamics_limit.md" class="el">franky::DynamicsLimit</a>&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &gt;::DynamicsLimit</td>
<td>(</td>
<td>std::string </td>
<td><em>desc</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &amp; </td>
<td><em>max_val</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::shared_ptr&lt; std::mutex &gt; &amp; </td>
<td><em>write_mutex</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::function&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">bool</a>()&gt; &amp; </td>
<td><em>can_write_condition</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &amp; </td>
<td><em>default_val</em> </td>
</tr>
<tr class="even">
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

Constructor for [DynamicsLimit](classfranky_1_1_dynamics_limit.md "A template class representing a dynamics limit with a maximum value.").

Initializes a new instance of the [DynamicsLimit](classfranky_1_1_dynamics_limit.md "A template class representing a dynamics limit with a maximum value.") class with the provided values.

  - Parameters
    
    |                       |                                                                           |
    | --------------------- | ------------------------------------------------------------------------- |
    | desc                  | A string description of the limit (e.g., "joint velocity").               |
    | max\_val              | The maximum allowable value for this limit.                               |
    | write\_mutex          | A shared pointer to the mutex used for synchronizing writes to the limit. |
    | can\_write\_condition | A function that returns true if the limit can be written to.              |
    | default\_val          | The default value for this limit.                                         |
    

</div>

</div>

## Member Function Documentation

<span id="a39d85438237067ffa3b3829500b01f14"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#a39d85438237067ffa3b3829500b01f14)</span>get()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> <a href="classfranky_1_1_dynamics_limit.md" class="el">franky::DynamicsLimit</a>&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &gt;::get</td>
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

Get the current value of the limit.

Retrieves the current value stored in this limit.

  - Returns  
    The current value of the limit.

</div>

</div>

<span id="a13c429626a61ddf6b37ad38e8b7ee9ec"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#a13c429626a61ddf6b37ad38e8b7ee9ec)</span>set()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_dynamics_limit.md" class="el">franky::DynamicsLimit</a>&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &gt;::set</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitType</a> &amp; </td>
<td><em>value</em></td>
<td>)</td>
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

Set a new value for the limit.

Sets the value of the limit, but only if the robot is not in control. Throws a runtime\_error if the condition for writing to the limit is not met.

  - Parameters
    
    |       |                                     |
    | ----- | ----------------------------------- |
    | value | The new value to set for the limit. |
    

<!-- end list -->

  - Exceptions
    
    |                     |                                                               |
    | ------------------- | ------------------------------------------------------------- |
    | std::runtime\_error | if the limit cannot be set due to the robot being in control. |
    

</div>

</div>

<span id="adbb6e9b426e82b05272e2fe3939e8eb5"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#adbb6e9b426e82b05272e2fe3939e8eb5)</span>setFrom() <span class="overload">\[1/2\]</span>

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [AlternativeType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                                               |   |                                                                                                                                             |         |   |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::DynamicsLimit](classfranky_1_1_dynamics_limit.md)\< [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::setFrom | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [AlternativeType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) & | *value* | ) |  |

</div>

<div class="memdoc">

Set a new value for the limit with a different type.

This version of `set` allows setting the value with a different type, with appropriate type conversions.

  - Template Parameters
    
    |                 |                                           |
    | --------------- | ----------------------------------------- |
    | AlternativeType | The type of the alternative value to set. |
    

<!-- end list -->

  - Parameters
    
    |       |                                     |
    | ----- | ----------------------------------- |
    | value | The new value to set for the limit. |
    

</div>

</div>

<span id="a8183726a4540729a377615e0e207f154"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#a8183726a4540729a377615e0e207f154)</span>setFrom() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

|                                                                                                                                                                                                                                                                                          |   |                                                                                                                                          |         |   |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ---------------------------------------------------------------------------------------------------------------------------------------- | ------- | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::DynamicsLimit](classfranky_1_1_dynamics_limit.md)\< [Vector7d](namespacefranky.md#a4c36e6539a78f808bf759142dec935c4) \>::setFrom\< [Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\< 7 \> \> | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\< 7 \> & | *value* | ) |  |

</div>

<div class="memdoc">

</div>

</div>

## Friends And Related Symbol Documentation

<span id="a1909095817a8e86989d8c822e3ea2fb3"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#a1909095817a8e86989d8c822e3ea2fb3)</span>operator\<\<

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitTypeStream](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

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
<td>std::ostream &amp; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">operator</a>&lt;&lt;</td>
<td>(</td>
<td>std::ostream &amp; </td>
<td><em>os</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_dynamics_limit.md" class="el">DynamicsLimit</a>&lt; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">LimitTypeStream</a> &gt; &amp; </td>
<td><em>dynamics_limit</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">friend</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

## Member Data Documentation

<span id="a771e6607930b05b1807b3f891a28c5ad"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#a771e6607930b05b1807b3f891a28c5ad)</span>desc

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::string [franky::DynamicsLimit](classfranky_1_1_dynamics_limit.md)\< [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::desc |

</div>

<div class="memdoc">

Description of this limit.

This string provides a human-readable description of the limit, such as "joint velocity" or "maximum load".

</div>

</div>

<span id="a8ad7788915e12262221aa983c0588d62"></span>

## <span class="permalink">[◆ ](classfranky_1_1_dynamics_limit.md#a8ad7788915e12262221aa983c0588d62)</span>max

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

</div>

|                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::DynamicsLimit](classfranky_1_1_dynamics_limit.md)\< [LimitType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>::max |

</div>

<div class="memdoc">

The maximum value this limit can take as defined by Franka.

This value represents the maximum boundary for the limit, beyond which the value cannot be set.

</div>

</div>

-----

The documentation for this class was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/[dynamics\_limit.hpp](dynamics__limit_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
