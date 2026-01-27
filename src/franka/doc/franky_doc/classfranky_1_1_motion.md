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
  - [Motion](classfranky_1_1_motion.md)

</div>

</div>

<div class="header">

<div class="summary">

[Public Types](classfranky_1_1_motion.md#pub-types) | [Public Member Functions](classfranky_1_1_motion.md#pub-methods) | [Protected Member Functions](classfranky_1_1_motion.md#pro-methods) | [List of all members](classfranky_1_1_motion-members.md)

</div>

<div class="headertitle">

<div class="title">

franky::Motion\< ControlSignalType \> Class Template Reference<span class="mlabels"><span class="mlabel">abstract</span></span>

</div>

</div>

</div>

<div class="contents">

Base class for motions. [More...](classfranky_1_1_motion.md#details)

`#include <motion.hpp>`

<div class="dynheader">

Inheritance diagram for franky::Motion\< ControlSignalType \>:

</div>

<div class="dyncontent">

<div class="center">

![](classfranky_1_1_motion.png)

</div>

</div>

## <span id="pub-types"></span> Public Types

</div>

[using](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) = std::function\< [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration, franka::Duration, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) &)\>

 

## <span id="pub-methods"></span> Public Member Functions

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[\~Motion](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16) ()=[default](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[addReaction](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448) (std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [reaction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Add a reaction to the motion.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[addReactionFront](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347) (std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [reaction](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Add a reaction to the front of the reaction list.  

 

std::vector\< std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> \> 

[reactions](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d) ()

 

Currently registered reactions of the motion.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[registerCallback](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2) ([CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) [callback](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Register a callback that is called in every step of the motion.  

 

[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[init](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6) ([Robot](classfranky_1_1_robot.md) \*[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Initialize the motion.  

 

[ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) 

[nextCommand](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Get the next command of the motion.  

 

std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> 

[checkAndCallReactions](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

Check and call reactions.  

 

## <span id="pro-methods"></span> Protected Member Functions

 

[Motion](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4) ()

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) 

[initImpl](classfranky_1_1_motion.md#ad11b300fa7c37e18403af6a17bf663b8) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[virtual](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) 

[nextCommandImpl](classfranky_1_1_motion.md#ad2e6f47d30089ee335fecb671618a5f6) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &[robot\_state](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [time\_step](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [rel\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), franka::Duration [abs\_time](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> &[previous\_command](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))=0

 

[Robot](classfranky_1_1_robot.md) \* 

[robot](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f) () [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

 

<span id="details"></span>

## Detailed Description

<div class="textblock">

<div class="compoundTemplParams">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac)\>  
class franky::Motion\< ControlSignalType \>

</div>

Base class for motions.

  - Template Parameters
    
    |                   |                                                                                                                                                                   |
    | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ControlSignalType | Control signal type of the motion. Either franka::Torques, franka::JointVelocities, franka::CartesianVelocities, franka::JointPositions or franka::CartesianPose. |
    

</div>

## Member Typedef Documentation

<span id="aabc4cfc38ed77466ca94be5b1c38fc6c"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c)</span>CallbackType

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [using](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::CallbackType = std::function\<[void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)( [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &, franka::Duration, franka::Duration, franka::Duration, [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) &)\> |

</div>

<div class="memdoc">

</div>

</div>

## Constructor & Destructor Documentation

<span id="aa6d72b7a606055fc444bf2da0c463d16"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#aa6d72b7a606055fc444bf2da0c463d16)</span>\~Motion()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="classfranky_1_1_motion.md" class="el">franky::Motion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::~<a href="classfranky_1_1_motion.md" class="el">Motion</a></td>
<td>(</td>
<td></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">virtual</span><span class="mlabel">default</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

<span id="ab18f33f97f86e9fb838fb6d6d79915b4"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#ab18f33f97f86e9fb838fb6d6d79915b4)</span>Motion()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="classfranky_1_1_motion.md" class="el">franky::Motion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::Motion</td>
<td>(</td>
<td></td>
<td>)</td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">explicit</span><span class="mlabel">protected</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

## Member Function Documentation

<span id="a52f0efb3e6c876f480eceb75a18d7448"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#a52f0efb3e6c876f480eceb75a18d7448)</span>addReaction()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                            |   |                                                                                                                                                  |            |   |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::addReaction | ( | std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> | *reaction* | ) |  |

</div>

<div class="memdoc">

Add a reaction to the motion.

Reactions are evaluated in every step of the motion and can replace the current motion with a new motion.

  - Parameters
    
    |          |                      |
    | -------- | -------------------- |
    | reaction | The reaction to add. |
    

</div>

</div>

<span id="a8fdbf32e0808fb2f01514f83ee964347"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#a8fdbf32e0808fb2f01514f83ee964347)</span>addReactionFront()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                 |   |                                                                                                                                                  |            |   |  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::addReactionFront | ( | std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> | *reaction* | ) |  |

</div>

<div class="memdoc">

Add a reaction to the front of the reaction list.

Reactions are evaluated in every step of the motion and can replace the current motion with a new motion.

  - Parameters
    
    |          |                      |
    | -------- | -------------------- |
    | reaction | The reaction to add. |
    

</div>

</div>

<span id="a2a0e78863021c3c2116c8500c9386369"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#a2a0e78863021c3c2116c8500c9386369)</span>checkAndCallReactions()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                                                                                    |   |                                                                                                                   |                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| std::shared\_ptr\< [Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::checkAndCallReactions | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) & | *robot\_state*, |
|                                                                                                                                                                                                                                                                                                    |   | franka::Duration                                                                                                  | *rel\_time*,    |
|                                                                                                                                                                                                                                                                                                    |   | franka::Duration                                                                                                  | *abs\_time*     |
|                                                                                                                                                                                                                                                                                                    | ) |                                                                                                                   |                 |

</div>

<div class="memdoc">

Check and call reactions.

  - Parameters
    
    |              |                          |
    | ------------ | ------------------------ |
    | robot\_state | The current robot state. |
    | rel\_time    | The relative time.       |
    | abs\_time    | The absolute time \[s\]. |
    

<!-- end list -->

  - Returns  
    The new motion if a reaction was triggered, nullptr otherwise.

</div>

</div>

<span id="a3780f86a0c58bdfb959e4d9bb65179d6"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#a3780f86a0c58bdfb959e4d9bb65179d6)</span>init()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                     |   |                                                                                                                                                                  |                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::init | ( | [Robot](classfranky_1_1_robot.md) \*                                                                                                                           | *robot*,            |
|                                                                                                                                                                                                     |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &                                                | *robot\_state*,     |
|                                                                                                                                                                                                     |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> & | *previous\_command* |
|                                                                                                                                                                                                     | ) |                                                                                                                                                                  |                     |

</div>

<div class="memdoc">

Initialize the motion.

  - Parameters
    
    |                   |                          |
    | ----------------- | ------------------------ |
    | robot             | The robot instance.      |
    | robot\_state      | The current robot state. |
    | previous\_command | The previous command.    |
    

</div>

</div>

<span id="ad11b300fa7c37e18403af6a17bf663b8"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#ad11b300fa7c37e18403af6a17bf663b8)</span>initImpl()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">void</a> <a href="classfranky_1_1_motion.md" class="el">franky::Motion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::initImpl</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &amp; </td>
<td><em>previous_command</em> </td>
</tr>
<tr class="odd">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">protected</span><span class="mlabel">virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Reimplemented in [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69), [franky::WaypointMotion\< ControlSignalType, PositionWaypoint\< TargetType \>, TargetType \>](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69), [franky::WaypointMotion\< ControlSignalType, VelocityWaypoint\< TargetType \>, TargetType \>](classfranky_1_1_waypoint_motion.md#ada8edd9d849ee29244b6c2c1cfa30f69), [franky::CartesianImpedanceMotion](classfranky_1_1_cartesian_impedance_motion.md#a224f09b1b32ab145ff9db2c10220c51d), and [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md#a87fe10bf698cbc2b55db0a354fa9d250).

</div>

</div>

<span id="abc04c5fe350635cf36bc1e459736ddb7"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#abc04c5fe350635cf36bc1e459736ddb7)</span>nextCommand()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                         |   |                                                                                                                                                                  |                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::nextCommand | ( | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [RobotState](structfranky_1_1_robot_state.md) &                                                | *robot\_state*,     |
|                                                                                                                                                                                                                         |   | franka::Duration                                                                                                                                                 | *time\_step*,       |
|                                                                                                                                                                                                                         |   | franka::Duration                                                                                                                                                 | *rel\_time*,        |
|                                                                                                                                                                                                                         |   | franka::Duration                                                                                                                                                 | *abs\_time*,        |
|                                                                                                                                                                                                                         |   | [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::optional\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> & | *previous\_command* |
|                                                                                                                                                                                                                         | ) |                                                                                                                                                                  |                     |

</div>

<div class="memdoc">

Get the next command of the motion.

  - Parameters
    
    |                   |                          |
    | ----------------- | ------------------------ |
    | robot\_state      | The current robot state. |
    | time\_step        | The time step \[s\].     |
    | rel\_time         | The relative time.       |
    | abs\_time         | The absolute time \[s\]. |
    | previous\_command | The previous command.    |
    

<!-- end list -->

  - Returns  
    The next control signal for libfranka.

</div>

</div>

<span id="ad2e6f47d30089ee335fecb671618a5f6"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#ad2e6f47d30089ee335fecb671618a5f6)</span>nextCommandImpl()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">virtual</a> <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> <a href="classfranky_1_1_motion.md" class="el">franky::Motion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::nextCommandImpl</td>
<td>(</td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> <a href="structfranky_1_1_robot_state.md" class="el">RobotState</a> &amp; </td>
<td><em>robot_state</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>time_step</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>rel_time</em>,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>franka::Duration </td>
<td><em>abs_time</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0" class="el">const</a> std::optional&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt; &amp; </td>
<td><em>previous_command</em> </td>
</tr>
<tr class="even">
<td></td>
<td>)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">protected</span><span class="mlabel">pure virtual</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

Implemented in [franky::WaypointMotion\< ControlSignalType, WaypointType, TargetType \>](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b), [franky::WaypointMotion\< ControlSignalType, PositionWaypoint\< TargetType \>, TargetType \>](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b), [franky::WaypointMotion\< ControlSignalType, VelocityWaypoint\< TargetType \>, TargetType \>](classfranky_1_1_waypoint_motion.md#ade5d803c15b7f55e55258092788df21b), and [franky::ImpedanceMotion](classfranky_1_1_impedance_motion.md#a6594ab5628923b88cce26903ae02077c).

</div>

</div>

<span id="aed40663a195eb68318799d19451c5a0d"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#aed40663a195eb68318799d19451c5a0d)</span>reactions()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                                                                                                             |   |  |   |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |  | - |  |
| std::vector\< std::shared\_ptr\< [Reaction](classfranky_1_1_reaction.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \> \> \> [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::reactions | ( |  | ) |  |

</div>

<div class="memdoc">

Currently registered reactions of the motion.

</div>

</div>

<span id="a05ed2a4f6dbcd406f9298a7c8e4e76c2"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#a05ed2a4f6dbcd406f9298a7c8e4e76c2)</span>registerCallback()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

</div>

|                                                                                                                                                                                                                 |   |                                                                               |            |   |  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------- | ---------- | - |  |
| [void](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [franky::Motion](classfranky_1_1_motion.md)\< [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>::registerCallback | ( | [CallbackType](classfranky_1_1_motion.md#aabc4cfc38ed77466ca94be5b1c38fc6c) | *callback* | ) |  |

</div>

<div class="memdoc">

Register a callback that is called in every step of the motion.

  - Parameters
    
    |          |                                                                                                                                                                                          |
    | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | callback | The callback to register. Callbacks are called with the robot state, the time step \[s\], the relative time \[s\], the absolute time \[s\] and the control signal computed in this step. |
    

</div>

</div>

<span id="a4a279dafcbb7ae10605f58d27a3a368f"></span>

## <span class="permalink">[◆ ](classfranky_1_1_motion.md#a4a279dafcbb7ae10605f58d27a3a368f)</span>robot()

<div class="memitem">

<div class="memproto">

<div class="memtemplate">

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ControlSignalType](namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac) \>

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
<td><a href="classfranky_1_1_robot.md" class="el">Robot</a> * <a href="classfranky_1_1_motion.md" class="el">franky::Motion</a>&lt; <a href="namespacefranky.md#a9a12fea9c3341e3437af837efe8ebaac" class="el">ControlSignalType</a> &gt;::robot</td>
<td>(</td>
<td></td>
<td>)</td>
<td>const</td>
</tr>
</tbody>
</table></td>
<td><span class="mlabels"><span class="mlabel">inline</span><span class="mlabel">protected</span></span></td>
</tr>
</tbody>
</table>

</div>

<div class="memdoc">

</div>

</div>

-----

The documentation for this class was generated from the following files:

  - /home/runner/work/franky/franky/include/franky/motion/[motion.hpp](motion_8hpp_source.md)
  - /home/runner/work/franky/franky/src/motion/[motion.cpp](motion_8cpp.md)

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
