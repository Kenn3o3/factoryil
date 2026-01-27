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

</div>

</div>

<div class="header">

<div class="summary">

[Namespaces](util_8hpp.md#namespaces) | [Functions](util_8hpp.md#func-members)

</div>

<div class="headertitle">

<div class="title">

util.hpp File Reference

</div>

</div>

</div>

<div class="contents">

<div class="textblock">

`#include <franka/duration.h>`  
`#include <Eigen/Core>`  
`#include <array>`  

</div>

[Go to the source code of this file.](util_8hpp_source.md)

## <span id="namespaces"></span> Namespaces

</div>

namespace  

[franky](namespacefranky.md)

 

## <span id="func-members"></span> Functions

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [T](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

std::array\< [T](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[franky::toStd](namespacefranky.md#a66970149b439291c4f95173b9e414161) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Matrix\< [T](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 1 \> &[vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<size\_t dims\>

std::array\< double, dims \> 

[franky::toStdD](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) (const Eigen::Matrix\< double, dims, 1 \> \&vector)

 

template\<[typename](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [T](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) , [size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

Eigen::Matrix\< [T](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 1 \> 

[franky::toEigen](namespacefranky.md#a246b8f841f3b7b07838f181539a5e35f) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::array\< [T](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

Eigen::Matrix\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 1 \> 

[franky::toEigenD](namespacefranky.md#aea642ac2353991b394de429b7932dccf) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) rows, [size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) cols\>

std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [rows](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \*[cols](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[franky::toStdDMatD](namespacefranky.md#a247f61893b0ba6dcf29b11453cf59564) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Matrix\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [rows](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [cols](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), Eigen::ColMajor \> &[matrix](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) rows, [size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) cols\>

Eigen::Matrix\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [rows](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [cols](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), Eigen::ColMajor \> 

[franky::toEigenMatD](namespacefranky.md#a44e848015229ff1e964fc5be35ee3d55) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [rows](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \*[cols](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[array](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

[Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) 

[franky::stdToAffine](namespacefranky.md#aded23761176a51276cdf6c8795d7891c) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), 16 \> &[array](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

Eigen::Vector\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[franky::ensureEigen](namespacefranky.md#a4af8de05472061175cee07678cddc6c3) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\< [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[franky::ensureStd](namespacefranky.md#acf0fc6eb90d96155c7700e17d783b101) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\< [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

std::array\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[franky::expand](namespacefranky.md#ae5cfa5596da548550897b01e9e1bd14b) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ScalarOrArray](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9)\< [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[size\_t](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

Eigen::Vector\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> 

[franky::expandEigen](namespacefranky.md#ad661aa664ba35fe438aec340c76bc913) ([const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [ScalarOrArray](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9)\< [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

template\<[int](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) dims\>

std::ostream & 

[franky::operator\<\<](namespacefranky.md#a58b50ccc87a970a8436dc3f1a87f69d6) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) Eigen::Vector\< [double](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \> &[vec](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

std::ostream & 

[franky::operator\<\<](namespacefranky.md#a13732434e1e955a423f850f682be8ad1) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

std::ostream & 

[franky::operator\<\<](namespacefranky.md#ac3fd06cc033b4b78ad59685214472e87) (std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), [const](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) franka::Duration &[duration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))

 

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
