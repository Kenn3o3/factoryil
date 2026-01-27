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

</div>

</div>

<div class="header">

<div class="headertitle">

<div class="title">

franky::ImpedanceMotion Member List

</div>

</div>

</div>

<div class="contents">

This is the complete list of members for [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md), including all inherited members.

|                                                                                                                                                                                                                                                                                         |                                                                    |                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448)(std::shared\_ptr\< Reaction\< franka::Torques \> \> reaction)                                                                                                                                              | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347)(std::shared\_ptr\< Reaction\< franka::Torques \> \> reaction)                                                                                                                                         | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) typedef                                                                                                                                                                                                   | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369)(const RobotState \&robot\_state, franka::Duration rel\_time, franka::Duration abs\_time)                                                                                                         | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [ImpedanceMotion](classfranky_1_1_impedance_motion.md#a60d55400835651bf37a1593f72e1a5cf)(Affine target, const Params \&params)                                                                                                                                                        | [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)   | <span class="mlabel">explicit</span>                                          |
| [init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6)(Robot \*robot, const RobotState \&robot\_state, const std::optional\< franka::Torques \> \&previous\_command)                                                                                                     | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [initImpl](classfranky_1_1_impedance_motion.md#a87fe10bf698cbc2b55db0a354fa9d250)(const RobotState \&robot\_state, const std::optional\< franka::Torques \> \&previous\_command) override                                                                                             | [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)   | <span class="mlabel">protected</span><span class="mlabel">virtual</span>      |
| [intermediate\_target](classfranky_1_1_impedance_motion.md#aabd59d6e0609d88130d71426324d12e2)() const                                                                                                                                                                                 | [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)   | <span class="mlabel">inline</span><span class="mlabel">protected</span>       |
| [Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4)()                                                                                                                                                                                                               | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) | <span class="mlabel">explicit</span><span class="mlabel">protected</span>     |
| [nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7)(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< franka::Torques \> \&previous\_command)                        | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [nextCommandImpl](classfranky_1_1_impedance_motion.md#a6594ab5628923b88cce26903ae02077c)(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration rel\_time, franka::Duration abs\_time, const std::optional\< franka::Torques \> \&previous\_command) override | [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)   | <span class="mlabel">protected</span><span class="mlabel">virtual</span>      |
| [reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d)()                                                                                                                                                                                                            | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2)(CallbackType callback)                                                                                                                                                                                | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) |                                                                               |
| [robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)() const                                                                                                                                                                                                          | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) | <span class="mlabel">inline</span><span class="mlabel">protected</span>       |
| [target](classfranky_1_1_impedance_motion.md#a1ce961ddf51cd792482fd5ca2b299d97)() const                                                                                                                                                                                               | [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)   | <span class="mlabel">inline</span><span class="mlabel">protected</span>       |
| [update](classfranky_1_1_impedance_motion.md#aee9a6e23b63db2ebc49c6615b461189c)(const RobotState \&robot\_state, franka::Duration time\_step, franka::Duration time)=0                                                                                                                | [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md)   | <span class="mlabel">protected</span><span class="mlabel">pure virtual</span> |
| [\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16)()=default                                                                                                                                                                                                     | [franky::Motion\< franka::Torques \>](classfranky_1_1_motion.md) | <span class="mlabel">virtual</span>                                           |

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
