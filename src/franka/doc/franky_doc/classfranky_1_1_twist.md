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
  - [Twist](classfranky_1_1_twist.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Member Functions](classfranky_1_1_twist.md#pub-methods) | [Static Public Member Functions](classfranky_1_1_twist.md#pub-static-methods) | [Friends](classfranky_1_1_twist.md#friends) | [List of all members](classfranky_1_1_twist-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Twist Class Reference

</div>

</div>

</div>

<div class="contents">

[Twist](classfranky_1_1_twist.md "Twist of a frame.") of a frame. [More...](classfranky_1_1_twist.md#details)

`#include <twist.hpp>`

## <span id="pub-methods"></span> Public Member Functions

</div>

 

[Twist](classfranky_1_1_twist.md#acc5436a6628d7685aacf10d56e915126) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Twist](classfranky_1_1_twist.md) &[twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

 

[Twist](classfranky_1_1_twist.md#a9c27d104e1b1ede05906e1a4b8260aa2) (Eigen::Vector3d [linear\_velocity](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d)=Eigen::Vector3d::Zero(), Eigen::Vector3d [angular\_velocity](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4)=Eigen::Vector3d::Zero())

 

[Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) 

[vector\_repr](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the vector representation of the twist. It consists of the linear and angular velocities.  

 

[Twist](classfranky_1_1_twist.md) 

[transformWith](classfranky_1_1_twist.md#a3f75fc666b90701fb5b518ca44e7542a) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[transformation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform the frame of the twist by applying the given affine transform.  

 

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \>

[Twist](classfranky_1_1_twist.md) 

[transformWith](classfranky_1_1_twist.md#a8877c2da86231733a7ee309bd6378434) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RotationMatrixType](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) &[rotation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Transform the frame of the twist by applying the given rotation.  

 

[Twist](classfranky_1_1_twist.md) 

[propagateThroughLink](classfranky_1_1_twist.md#a896c0f6949127e1c37f5716b3f771bdb) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector3d &[link\_translation](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Propagate the twist through a link with the given translation. Hence, suppose this twist is the twist of a frame A, then this function computes the twist of a frame B that is rigidly attached to frame A by a link with the given translation: B = A + T, where T is the translation.  

 

Eigen::Vector3d 

[linear\_velocity](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the linear velocity.  

 

Eigen::Vector3d 

[angular\_velocity](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

Get the angular velocity.  

 

## <span id="pub-static-methods"></span> Static Public Member Functions

[static](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Twist](classfranky_1_1_twist.md) 

[fromVectorRepr](classfranky_1_1_twist.md#a39a4f6fc1cca31a7431618657d551f17) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Vector6d](namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb) &[vector\_repr](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e))

 

## <span id="friends"></span> Friends

std::ostream & 

[operator\<\<](classfranky_1_1_twist.md#ac0ce8d662af951bc5d7b3ab17a355790) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Twist](classfranky_1_1_twist.md) &[twist](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

[Twist](classfranky_1_1_twist.md "Twist of a frame.") of a frame.

</div>

## Constructor & Destructor Documentation

<span id="acc5436a6628d7685aacf10d56e915126"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#acc5436a6628d7685aacf10d56e915126)</span>Twist() <span class="overload">\[1/2\]</span>

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
<td>franky::Twist::Twist</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_twist.md" class="el">Twist</a> &amp; </td>
<td><em>twist</em></td>
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

<span id="a9c27d104e1b1ede05906e1a4b8260aa2"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#a9c27d104e1b1ede05906e1a4b8260aa2)</span>Twist() <span class="overload">\[2/2\]</span>

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
<td>franky::Twist::Twist</td>
<td>(</td>
<td>Eigen::Vector3d </td>
<td><em>linear_velocity</em> = <code>Eigen::Vector3d::Zero()</code>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Eigen::Vector3d </td>
<td><em>angular_velocity</em> = <code>Eigen::Vector3d::Zero()</code> </td>
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
    
    |                   |                                    |
    | ----------------- | ---------------------------------- |
    | linear\_velocity  | The linear velocity in \[m/s\].    |
    | angular\_velocity | The angular velocity in \[rad/s\]. |
    

</div>

</div>

## Member Function Documentation

<span id="af1199e9d3b8e06d11c519f99f5e2a4e4"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#af1199e9d3b8e06d11c519f99f5e2a4e4)</span>angular\_velocity()

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
<td>Eigen::Vector3d franky::Twist::angular_velocity</td>
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

Get the angular velocity.

  - Returns  
    The angular velocity \[rad/s\].

</div>

</div>

<span id="a39a4f6fc1cca31a7431618657d551f17"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#a39a4f6fc1cca31a7431618657d551f17)</span>fromVectorRepr()

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">static</a> <a href="classfranky_1_1_twist.md" class="el">Twist</a> franky::Twist::fromVectorRepr</td>
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
    
    |              |                                         |
    | ------------ | --------------------------------------- |
    | vector\_repr | The vector representation of the twist. |
    

</div>

</div>

<span id="a5c704065f92d12266fb0e16e2b2dd61d"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#a5c704065f92d12266fb0e16e2b2dd61d)</span>linear\_velocity()

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
<td>Eigen::Vector3d franky::Twist::linear_velocity</td>
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

Get the linear velocity.

  - Returns  
    The linear velocity \[m/s\].

</div>

</div>

<span id="a896c0f6949127e1c37f5716b3f771bdb"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#a896c0f6949127e1c37f5716b3f771bdb)</span>propagateThroughLink()

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
<td><a href="classfranky_1_1_twist.md" class="el">Twist</a> franky::Twist::propagateThroughLink</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> Eigen::Vector3d &amp; </td>
<td><em>link_translation</em></td>
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

Propagate the twist through a link with the given translation. Hence, suppose this twist is the twist of a frame A, then this function computes the twist of a frame B that is rigidly attached to frame A by a link with the given translation: B = A + T, where T is the translation.

  - Parameters
    
    |                   |                                                                                 |
    | ----------------- | ------------------------------------------------------------------------------- |
    | link\_translation | The translation of the link. Must be in the same reference frame as this twist. |
    

<!-- end list -->

  - Returns  
    The twist propagated through the link.

</div>

</div>

<span id="a3f75fc666b90701fb5b518ca44e7542a"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#a3f75fc666b90701fb5b518ca44e7542a)</span>transformWith() <span class="overload">\[1/2\]</span>

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
<td><a href="classfranky_1_1_twist.md" class="el">Twist</a> franky::Twist::transformWith</td>
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

Transform the frame of the twist by applying the given affine transform.

  - Parameters
    
    |                |                              |
    | -------------- | ---------------------------- |
    | transformation | The transformation to apply. |
    

<!-- end list -->

  - Returns  
    The twist after the transformation.

</div>

</div>

<span id="a8877c2da86231733a7ee309bd6378434"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#a8877c2da86231733a7ee309bd6378434)</span>transformWith() <span class="overload">\[2/2\]</span>

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
<td><a href="classfranky_1_1_twist.md" class="el">Twist</a> franky::Twist::transformWith</td>
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

Transform the frame of the twist by applying the given rotation.

  - Parameters
    
    |          |                        |
    | -------- | ---------------------- |
    | rotation | The rotation to apply. |
    

<!-- end list -->

  - Returns  
    The twist after the transformation.

</div>

</div>

<span id="a31a3a4886d8ef4ee37b4d12acec1162e"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#a31a3a4886d8ef4ee37b4d12acec1162e)</span>vector\_repr()

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
<td><a href="namespacefranky.md#a92a07a88df41e482914cf4f9f2dddecb" class="el">Vector6d</a> franky::Twist::vector_repr</td>
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

Get the vector representation of the twist. It consists of the linear and angular velocities.

  - Returns  
    The vector representation of the twist.

</div>

</div>

## Friends And Related Symbol Documentation

<span id="ac0ce8d662af951bc5d7b3ab17a355790"></span>

## <span class="permalink">[◆ ](classfranky_1_1_twist.md#ac0ce8d662af951bc5d7b3ab17a355790)</span>operator\<\<

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="classfranky_1_1_twist.md" class="el">Twist</a> &amp; </td>
<td><em>twist</em> </td>
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

  - /home/runner/work/franky/franky/include/franky/[twist.hpp](twist_8hpp_source.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
