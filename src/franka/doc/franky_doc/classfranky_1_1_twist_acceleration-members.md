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

<div class="headertitle">

<div class="title">

franky::TwistAcceleration Member List

</div>

</div>

</div>

<div class="contents">

This is the complete list of members for [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md), including all inherited members.

|                                                                                                                                                                                                                             |                                                                      |                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [angular\_acceleration](classfranky_1_1_twist_acceleration.md#a6d6cabb998123f95bc7af53e428f7029)() const                                                                                                                  | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span>                                     |
| [fromVectorRepr](classfranky_1_1_twist_acceleration.md#a56735cb015ce872ba1857d7af6081d3a)(const Vector6d \&vector\_repr)                                                                                                  | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span><span class="mlabel">static</span>   |
| [linear\_acceleration](classfranky_1_1_twist_acceleration.md#a9d91f3165e9017533f063603aad7dc4e)() const                                                                                                                   | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span>                                     |
| [operator\<\<](classfranky_1_1_twist_acceleration.md#a85106207596cbe76f085e987a937b129)                                                                                                                                   | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">friend</span>                                     |
| [propagateThroughLink](classfranky_1_1_twist_acceleration.md#a0cb4b6497e1332cb717b6f3d132de65f)(const Eigen::Vector3d \&link\_translation, const Eigen::Vector3d \&base\_angular\_velocity) const                         | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span>                                     |
| [transformWith](classfranky_1_1_twist_acceleration.md#a0887f6ede60cbe7ce36dc0541af45a8b)(const Affine \&transformation) const                                                                                             | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span>                                     |
| [transformWith](classfranky_1_1_twist_acceleration.md#ad32f3d63877f1f0a679677fd4301fc0b)(const RotationMatrixType \&rotation) const                                                                                       | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span>                                     |
| [TwistAcceleration](classfranky_1_1_twist_acceleration.md#a99508b6c2741d8f18acca43e538beecb)(const TwistAcceleration \&twist\_acceleration\_acceleration)=default                                                         | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) |                                                                        |
| [TwistAcceleration](classfranky_1_1_twist_acceleration.md#a12807e75c0b6f39208d1822dbdf2eb28)(Eigen::Vector3d linear\_acceleration=Eigen::Vector3d::Zero(), Eigen::Vector3d angular\_acceleration=Eigen::Vector3d::Zero()) | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span><span class="mlabel">explicit</span> |
| [vector\_repr](classfranky_1_1_twist_acceleration.md#aae1e4fd8a259657bbad3082ca943d5ec)() const                                                                                                                           | [franky::TwistAcceleration](classfranky_1_1_twist_acceleration.md) | <span class="mlabel">inline</span>                                     |

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
