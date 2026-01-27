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
  - [TwistAcceleration](classfranky_1_1_twist_acceleration.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_twist_acceleration.md#pub-methods) | [Static Public Member Functions](classfranky_1_1_twist_acceleration.md#pub-static-methods) | [Friends](classfranky_1_1_twist_acceleration.md#friends) | [List of all members](classfranky_1_1_twist_acceleration-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::TwistAcceleration Class Reference

</div>

</div>

</div>

<div class="contents">

[TwistAcceleration](classfranky_1_1_twist_acceleration.md "TwistAcceleration acceleration of a frame (2nd derivative of a pose).") acceleration of a frame (2nd derivative of a pose). [More...](classfranky_1_1_twist_acceleration.md#details)

`#include <twist_acceleration.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[TwistAcceleration](classfranky_1_1_twist_acceleration.md#a99508b6c2741d8f18acca43e538beecb) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TwistAcceleration](classfranky_1_1_twist_acceleration.md) &[twist\_acceleration\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

 

[TwistAcceleration](classfranky_1_1_twist_acceleration.md#a12807e75c0b6f39208d1822dbdf2eb28) (Eigen::Vector3d [linear\_acceleration](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e)=Eigen::Vector3d::Zero(), Eigen::Vector3d [angular\_acceleration](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029)=Eigen::Vector3d::Zero())

 

[Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) 

[vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the vector representation of the twist acceleration. It consists of the linear and angular velocities.  

 

[TwistAcceleration](classfranky_1_1_twist_acceleration.md) 

[transformWith](classfranky_1_1_twist_acceleration.md#a0887f6ede60cbe7ce36dc0541af45a8b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[transformation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform the frame of the twist acceleration by applying the given affine transform.  

 

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

[TwistAcceleration](classfranky_1_1_twist_acceleration.md) 

[transformWith](classfranky_1_1_twist_acceleration.md#ad32f3d63877f1f0a679677fd4301fc0b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform the frame of the twist acceleration by applying the given rotation.  

 

[TwistAcceleration](classfranky_1_1_twist_acceleration.md) 

[propagateThroughLink](classfranky_1_1_twist_acceleration.md#a0cb4b6497e1332cb717b6f3d132de65f) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &[link\_translation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &[base\_angular\_velocity](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Propagate the twist acceleration through a link with the given translation. Hence, suppose this twist acceleration is the twist acceleration of a frame A, then this function computes the twist acceleration of a frame B that is rigidly attached to frame A by a link with the given translation: B = A + T, where T is the translation.  

 

Eigen::Vector3d 

[linear\_acceleration](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the linear acceleration.  

 

Eigen::Vector3d 

[angular\_acceleration](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the angular acceleration.  

 

## <span id="pub-static-methods"></span> Static Public Member Functions

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TwistAcceleration](classfranky_1_1_twist_acceleration.md) 

[fromVectorRepr](classfranky_1_1_twist_acceleration.md#a56735cb015ce872ba1857d7af6081d3a) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec))

 

## <span id="friends"></span> Friends

std::ostream & 

[operator\<\<](classfranky_1_1_twist_acceleration.md#a85106207596cbe76f085e987a937b129) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [TwistAcceleration](classfranky_1_1_twist_acceleration.md) &[twist\_acceleration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

[TwistAcceleration](classfranky_1_1_twist_acceleration.md "TwistAcceleration acceleration of a frame (2nd derivative of a pose).") acceleration of a frame (2nd derivative of a pose).

</div>

## Constructor & Destructor Documentation

<span id="a99508b6c2741d8f18acca43e538beecb"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a99508b6c2741d8f18acca43e538beecb)</span>TwistAcceleration() <span class="overload">\[1/2\]</span>

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
<td>franky::TwistAcceleration::TwistAcceleration</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_twist_acceleration.md" class="el">TwistAcceleration</a> &amp; </td>
<td><em>twist_acceleration_acceleration</em></td>
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

<span id="a12807e75c0b6f39208d1822dbdf2eb28"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a12807e75c0b6f39208d1822dbdf2eb28)</span>TwistAcceleration() <span class="overload">\[2/2\]</span>

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
<td>franky::TwistAcceleration::TwistAcceleration</td>
<td>(</td>
<td>Eigen::Vector3d </td>
<td><em>linear_acceleration</em> = <code>Eigen::Vector3d::Zero()</code>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Eigen::Vector3d </td>
<td><em>angular_acceleration</em> = <code>Eigen::Vector3d::Zero()</code> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
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

  - Parameters
    
    |                       |                                          |
    | --------------------- | ---------------------------------------- |
    | linear\_acceleration  | The linear acceleration in \[m/s^2\].    |
    | angular\_acceleration | The angular acceleration in \[rad/s^2\]. |
    

</div>

</div>

## Member Function Documentation

<span id="a6d6cabb998123f95bc7af53e428f7029"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029)</span>angular\_acceleration()

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
<td>Eigen::Vector3d franky::TwistAcceleration::angular_acceleration</td>
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

Get the angular acceleration.

  - Returns  
    The angular acceleration \[rad/s^2\].

</div>

</div>

<span id="a56735cb015ce872ba1857d7af6081d3a"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a56735cb015ce872ba1857d7af6081d3a)</span>fromVectorRepr()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">static</a> <a href="classfranky_1_1_twist_acceleration.md" class="el">TwistAcceleration</a> franky::TwistAcceleration::fromVectorRepr</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb" class="el">Vector6d</a> &amp; </td>
<td><em>vector_repr</em></td>
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

  - Parameters
    
    |              |                                                      |
    | ------------ | ---------------------------------------------------- |
    | vector\_repr | The vector representation of the twist acceleration. |
    

</div>

</div>

<span id="a9d91f3165e9017533f063603aad7dc4e"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e)</span>linear\_acceleration()

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
<td>Eigen::Vector3d franky::TwistAcceleration::linear_acceleration</td>
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

Get the linear acceleration.

  - Returns  
    The linear acceleration \[m/s^2\].

</div>

</div>

<span id="a0cb4b6497e1332cb717b6f3d132de65f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a0cb4b6497e1332cb717b6f3d132de65f)</span>propagateThroughLink()

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
<td><a href="classfranky_1_1_twist_acceleration.md" class="el">TwistAcceleration</a> franky::TwistAcceleration::propagateThroughLink</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> Eigen::Vector3d &amp; </td>
<td><em>link_translation</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> Eigen::Vector3d &amp; </td>
<td><em>base_angular_velocity</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
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

Propagate the twist acceleration through a link with the given translation. Hence, suppose this twist acceleration is the twist acceleration of a frame A, then this function computes the twist acceleration of a frame B that is rigidly attached to frame A by a link with the given translation: B = A + T, where T is the translation.

  - Parameters
    
    |                         |                                                                                                                   |
    | ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
    | link\_translation       | The translation of the link (A to B). Must be in the same reference frame as this twist acceleration.             |
    | base\_angular\_velocity | Angular velocity of the base frame (A) \[rad/s\]. Must be in the same reference frame as this twist acceleration. |
    

<!-- end list -->

  - Returns  
    The twist acceleration propagated through the link.

</div>

</div>

<span id="a0887f6ede60cbe7ce36dc0541af45a8b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a0887f6ede60cbe7ce36dc0541af45a8b)</span>transformWith() <span class="overload">\[1/2\]</span>

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
<td><a href="classfranky_1_1_twist_acceleration.md" class="el">TwistAcceleration</a> franky::TwistAcceleration::transformWith</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#afab9faf133666ada543b15236a8c4b5f" class="el">Affine</a> &amp; </td>
<td><em>transformation</em></td>
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

Transform the frame of the twist acceleration by applying the given affine transform.

  - Parameters
    
    |                |                              |
    | -------------- | ---------------------------- |
    | transformation | The transformation to apply. |
    

<!-- end list -->

  - Returns  
    The twist acceleration after the transformation.

</div>

</div>

<span id="ad32f3d63877f1f0a679677fd4301fc0b"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#ad32f3d63877f1f0a679677fd4301fc0b)</span>transformWith() <span class="overload">\[2/2\]</span>

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

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
<td><a href="classfranky_1_1_twist_acceleration.md" class="el">TwistAcceleration</a> franky::TwistAcceleration::transformWith</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">RotationMatrixType</a> &amp; </td>
<td><em>rotation</em></td>
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

Transform the frame of the twist acceleration by applying the given rotation.

  - Parameters
    
    |          |                        |
    | -------- | ---------------------- |
    | rotation | The rotation to apply. |
    

<!-- end list -->

  - Returns  
    The twist acceleration after the transformation.

</div>

</div>

<span id="aae1e4fd8a259657bbad3082ca943d5ec"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec)</span>vector\_repr()

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
<td><a href="namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb" class="el">Vector6d</a> franky::TwistAcceleration::vector_repr</td>
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

Get the vector representation of the twist acceleration. It consists of the linear and angular velocities.

  - Returns  
    The vector representation of the twist acceleration.

</div>

</div>

## Friends And Related Symbol Documentation

<span id="a85106207596cbe76f085e987a937b129"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist_acceleration.md#a85106207596cbe76f085e987a937b129)</span>operator\<\<

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
<td>std::ostream &amp; <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">operator</a>&lt;&lt;</td>
<td>(</td>
<td>std::ostream &amp; </td>
<td><em>os</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_twist_acceleration.md" class="el">TwistAcceleration</a> &amp; </td>
<td><em>twist_acceleration</em> </td>
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

-----

The documentation for this class was generated from the following file:

  - /home/runner/work/franky/franky/include/franky/[twist\_acceleration.hpp](twist__acceleration_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
