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

<div class="headertitle">

<div class="title">

util.hpp

</div>

</div>

</div>

<div class="contents">

[Go to the documentation of this file.](util_8hpp.md)

<div class="fragment">

<div class="line">

<span id="l00001"></span><span class="lineno"> 1</span><span class="preprocessor">\#pragma once</span>

</div>

<div class="line">

<span id="l00002"></span><span class="lineno"> 2</span>

</div>

<div class="line">

<span id="l00003"></span><span class="lineno"> 3</span><span class="preprocessor">\#include \<franka/duration.h\></span>

</div>

<div class="line">

<span id="l00004"></span><span class="lineno"> 4</span>

</div>

<div class="line">

<span id="l00005"></span><span class="lineno"> 5</span><span class="preprocessor">\#include \<Eigen/Core\></span>

</div>

<div class="line">

<span id="l00006"></span><span class="lineno"> 6</span><span class="preprocessor">\#include \<array\></span>

</div>

<div class="line">

<span id="l00007"></span><span class="lineno"> 7</span>

</div>

<div class="line">

<span id="l00008"></span><span class="lineno"> 8</span><span class="keyword">namespace </span>[franky](namespacefranky.md) {

</div>

<div class="line">

<span id="l00009"></span><span class="lineno"> 9</span>

</div>

<div class="line">

<span id="l00010"></span><span class="lineno"> 10</span><span class="keyword">template</span> \<<span class="keyword">typename</span> T, <span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00011" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00011"></span><span class="lineno"> [11](namespacefranky.md#a66970149b439291c4f95173b9e414161)</span>std::array\<T, dims\> [toStd](namespacefranky.md#a66970149b439291c4f95173b9e414161)(<span class="keyword">const</span> Eigen::Matrix\<T, dims, 1\> &[vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00012"></span><span class="lineno"> 12</span> std::array\<T, dims\> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00013"></span><span class="lineno"> 13</span> Eigen::Matrix\<T, dims, 1\>::Map([result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).data()) = [vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00014"></span><span class="lineno"> 14</span> <span class="keywordflow">return</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00015"></span><span class="lineno"> 15</span>}

</div>

</div>

<div class="line">

<span id="l00016"></span><span class="lineno"> 16</span>

</div>

<div class="line">

<span id="l00017"></span><span class="lineno"> 17</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00018" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00018"></span><span class="lineno"> [18](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)</span>std::array\<double, dims\> [toStdD](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(<span class="keyword">const</span> Eigen::Matrix\<double, dims, 1\> &[vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00019"></span><span class="lineno"> 19</span> <span class="keywordflow">return</span> [toStd\<double, dims\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00020"></span><span class="lineno"> 20</span>}

</div>

</div>

<div class="line">

<span id="l00021"></span><span class="lineno"> 21</span>

</div>

<div class="line">

<span id="l00022"></span><span class="lineno"> 22</span><span class="keyword">template</span> \<<span class="keyword">typename</span> T, <span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00023" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00023"></span><span class="lineno"> [23](namespacefranky.md#a246b8f841f3b7b07838f181539a5e35f)</span>Eigen::Matrix\<T, dims, 1\> [toEigen](namespacefranky.md#a246b8f841f3b7b07838f181539a5e35f)(<span class="keyword">const</span> std::array\<T, dims\> &[vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00024"></span><span class="lineno"> 24</span> <span class="keywordflow">return</span> Eigen::Matrix\<T, dims, 1\>::Map([vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).data());

</div>

<div class="line">

<span id="l00025"></span><span class="lineno"> 25</span>}

</div>

</div>

<div class="line">

<span id="l00026"></span><span class="lineno"> 26</span>

</div>

<div class="line">

<span id="l00027"></span><span class="lineno"> 27</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00028" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00028"></span><span class="lineno"> [28](namespacefranky.md#aea642ac2353991b394de429b7932dccf)</span>Eigen::Matrix\<double, dims, 1\> [toEigenD](namespacefranky.md#aea642ac2353991b394de429b7932dccf)(<span class="keyword">const</span> std::array\<double, dims\> &[vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00029"></span><span class="lineno"> 29</span> <span class="keywordflow">return</span> [toEigen\<double, dims\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([vector](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00030"></span><span class="lineno"> 30</span>}

</div>

</div>

<div class="line">

<span id="l00031"></span><span class="lineno"> 31</span>

</div>

<div class="line">

<span id="l00032"></span><span class="lineno"> 32</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> rows, <span class="keywordtype">size\_t</span> cols\>

</div>

<div id="foldopen00033" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00033"></span><span class="lineno"> [33](namespacefranky.md#a247f61893b0ba6dcf29b11453cf59564)</span>std::array\<double, rows \* cols\> [toStdDMatD](namespacefranky.md#a247f61893b0ba6dcf29b11453cf59564)(<span class="keyword">const</span> Eigen::Matrix\<double, rows, cols, Eigen::ColMajor\> &[matrix](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00034"></span><span class="lineno"> 34</span> std::array\<double, rows \* cols\> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00035"></span><span class="lineno"> 35</span> Eigen::Map\<Eigen::Matrix\<double, rows, cols, Eigen::ColMajor\>\>([result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).data()) = [matrix](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00036"></span><span class="lineno"> 36</span> <span class="keywordflow">return</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00037"></span><span class="lineno"> 37</span>}

</div>

</div>

<div class="line">

<span id="l00038"></span><span class="lineno"> 38</span>

</div>

<div class="line">

<span id="l00039"></span><span class="lineno"> 39</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> rows, <span class="keywordtype">size\_t</span> cols\>

</div>

<div id="foldopen00040" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00040"></span><span class="lineno"> [40](namespacefranky.md#a44e848015229ff1e964fc5be35ee3d55)</span>Eigen::Matrix\<double, rows, cols, Eigen::ColMajor\> [toEigenMatD](namespacefranky.md#a44e848015229ff1e964fc5be35ee3d55)(<span class="keyword">const</span> std::array\<double, rows \* cols\> &[array](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00041"></span><span class="lineno"> 41</span> <span class="keywordflow">return</span> Eigen::Map\<const Eigen::Matrix\<double, rows, cols, Eigen::ColMajor\>\>([array](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).data());

</div>

<div class="line">

<span id="l00042"></span><span class="lineno"> 42</span>}

</div>

</div>

<div class="line">

<span id="l00043"></span><span class="lineno"> 43</span>

</div>

<div id="foldopen00044" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00044"></span><span class="lineno"> [44](namespacefranky.md#aded23761176a51276cdf6c8795d7891c)</span><span class="keyword">inline</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [stdToAffine](namespacefranky.md#aded23761176a51276cdf6c8795d7891c)(<span class="keyword">const</span> std::array\<double, 16\> &[array](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00045"></span><span class="lineno"> 45</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00046"></span><span class="lineno"> 46</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).matrix() = [toEigenMatD\<4, 4\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)([array](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00047"></span><span class="lineno"> 47</span> <span class="keywordflow">return</span> [result](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00048"></span><span class="lineno"> 48</span>}

</div>

</div>

<div class="line">

<span id="l00049"></span><span class="lineno"> 49</span>

</div>

<div class="line">

<span id="l00050"></span><span class="lineno"> 50</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00051" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00051"></span><span class="lineno"> [51](namespacefranky.md#a4af8de05472061175cee07678cddc6c3)</span>Eigen::Vector\<double, dims\> [ensureEigen](namespacefranky.md#a4af8de05472061175cee07678cddc6c3)(<span class="keyword">const</span> [Array\<dims\>](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66) &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00052"></span><span class="lineno"> 52</span> <span class="keywordflow">if</span> (std::holds\_alternative\<Eigen::Vector\<double, dims\>\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))) <span class="keywordflow">return</span> std::get\<Eigen::Vector\<double, dims\>\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00053"></span><span class="lineno"> 53</span> <span class="keywordflow">return</span> [toEigenD\<dims\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(std::get\<std::array\<double, dims\>\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)));

</div>

<div class="line">

<span id="l00054"></span><span class="lineno"> 54</span>}

</div>

</div>

<div class="line">

<span id="l00055"></span><span class="lineno"> 55</span>

</div>

<div class="line">

<span id="l00056"></span><span class="lineno"> 56</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00057" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00057"></span><span class="lineno"> [57](namespacefranky.md#acf0fc6eb90d96155c7700e17d783b101)</span>std::array\<double, dims\> [ensureStd](namespacefranky.md#acf0fc6eb90d96155c7700e17d783b101)(<span class="keyword">const</span> [Array\<dims\>](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66) &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00058"></span><span class="lineno"> 58</span> <span class="keywordflow">if</span> (std::holds\_alternative\<std::array\<double, dims\>\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))) <span class="keywordflow">return</span> std::get\<std::array\<double, dims\>\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0));

</div>

<div class="line">

<span id="l00059"></span><span class="lineno"> 59</span> <span class="keywordflow">return</span> [toStdD\<dims\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(std::get\<Eigen::Vector\<double, dims\>\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)));

</div>

<div class="line">

<span id="l00060"></span><span class="lineno"> 60</span>}

</div>

</div>

<div class="line">

<span id="l00061"></span><span class="lineno"> 61</span>

</div>

<div class="line">

<span id="l00062"></span><span class="lineno"> 62</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00063" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00063"></span><span class="lineno"> [63](namespacefranky.md#ae5cfa5596da548550897b01e9e1bd14b)</span>std::array\<double, dims\> [expand](namespacefranky.md#ae5cfa5596da548550897b01e9e1bd14b)(<span class="keyword">const</span> [ScalarOrArray\<dims\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00064"></span><span class="lineno"> 64</span> <span class="keywordflow">if</span> (std::holds\_alternative\<[Array\<dims\>](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))) {

</div>

<div class="line">

<span id="l00065"></span><span class="lineno"> 65</span> <span class="keywordflow">return</span> [ensureStd\<dims\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(std::get\<[Array\<dims\>](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)));

</div>

<div class="line">

<span id="l00066"></span><span class="lineno"> 66</span> }

</div>

<div class="line">

<span id="l00067"></span><span class="lineno"> 67</span> std::array\<double, dims\> [output](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00068"></span><span class="lineno"> 68</span> std::fill([output](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).begin(), [output](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).end(), std::get\<double\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)));

</div>

<div class="line">

<span id="l00069"></span><span class="lineno"> 69</span> <span class="keywordflow">return</span> [output](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00070"></span><span class="lineno"> 70</span>}

</div>

</div>

<div class="line">

<span id="l00071"></span><span class="lineno"> 71</span>

</div>

<div class="line">

<span id="l00072"></span><span class="lineno"> 72</span><span class="keyword">template</span> \<<span class="keywordtype">size\_t</span> dims\>

</div>

<div id="foldopen00073" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00073"></span><span class="lineno"> [73](namespacefranky.md#ad661aa664ba35fe438aec340c76bc913)</span>Eigen::Vector\<double, dims\> [expandEigen](namespacefranky.md#ad661aa664ba35fe438aec340c76bc913)(<span class="keyword">const</span> [ScalarOrArray\<dims\>](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9) &[input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00074"></span><span class="lineno"> 74</span> <span class="keywordflow">if</span> (std::holds\_alternative\<[Array\<dims\>](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0))) {

</div>

<div class="line">

<span id="l00075"></span><span class="lineno"> 75</span> <span class="keywordflow">return</span> [ensureEigen\<dims\>](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)(std::get\<[Array\<dims\>](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)));

</div>

<div class="line">

<span id="l00076"></span><span class="lineno"> 76</span> }

</div>

<div class="line">

<span id="l00077"></span><span class="lineno"> 77</span> Eigen::Vector\<double, dims\> [output](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00078"></span><span class="lineno"> 78</span> [output](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).fill(std::get\<double\>([input](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)));

</div>

<div class="line">

<span id="l00079"></span><span class="lineno"> 79</span> <span class="keywordflow">return</span> [output](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00080"></span><span class="lineno"> 80</span>}

</div>

</div>

<div class="line">

<span id="l00081"></span><span class="lineno"> 81</span>

</div>

<div class="line">

<span id="l00082"></span><span class="lineno"> 82</span><span class="keyword">template</span> \<<span class="keywordtype">int</span> dims\>

</div>

<div id="foldopen00083" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00083"></span><span class="lineno"> [83](namespacefranky.md#a58b50ccc87a970a8436dc3f1a87f69d6)</span>std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> Eigen::Vector\<double, dims\> &[vec](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00084"></span><span class="lineno"> 84</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< <span class="stringliteral">"\["</span>;

</div>

<div class="line">

<span id="l00085"></span><span class="lineno"> 85</span> <span class="keywordflow">for</span> (<span class="keywordtype">size\_t</span> [i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) = 0; [i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \< [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0); [i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)++) {

</div>

<div class="line">

<span id="l00086"></span><span class="lineno"> 86</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< [vec](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\[[i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)\];

</div>

<div class="line">

<span id="l00087"></span><span class="lineno"> 87</span> <span class="keywordflow">if</span> ([i](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \!= [dims](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) - 1) [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< <span class="stringliteral">" "</span>;

</div>

<div class="line">

<span id="l00088"></span><span class="lineno"> 88</span> }

</div>

<div class="line">

<span id="l00089"></span><span class="lineno"> 89</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< <span class="stringliteral">"\]"</span>;

</div>

<div class="line">

<span id="l00090"></span><span class="lineno"> 90</span> <span class="keywordflow">return</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00091"></span><span class="lineno"> 91</span>}

</div>

</div>

<div class="line">

<span id="l00092"></span><span class="lineno"> 92</span>

</div>

<div id="foldopen00093" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00093"></span><span class="lineno"> [93](namespacefranky.md#a13732434e1e955a423f850f682be8ad1)</span><span class="keyword">inline</span> std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> [Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f) &[affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00094"></span><span class="lineno"> 94</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< <span class="stringliteral">"Affine(t="</span> \<\< [affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).translation().eval() \<\< <span class="stringliteral">", q="</span> \<\< Eigen::Quaterniond([affine](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).rotation()).coeffs() \<\< <span class="stringliteral">")"</span>;

</div>

<div class="line">

<span id="l00095"></span><span class="lineno"> 95</span> <span class="keywordflow">return</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00096"></span><span class="lineno"> 96</span>}

</div>

</div>

<div class="line">

<span id="l00097"></span><span class="lineno"> 97</span>

</div>

<div id="foldopen00098" class="foldopen" data-start="{" data-end="}">

<div class="line">

<span id="l00098"></span><span class="lineno"> [98](namespacefranky.md#ac3fd06cc033b4b78ad59685214472e87)</span><span class="keyword">inline</span> std::ostream &[operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)(std::ostream &[os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0), <span class="keyword">const</span> franka::Duration &[duration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)) {

</div>

<div class="line">

<span id="l00099"></span><span class="lineno"> 99</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0) \<\< <span class="stringliteral">"Duration("</span> \<\< [duration](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0).toMSec() \<\< <span class="stringliteral">")"</span>;

</div>

<div class="line">

<span id="l00100"></span><span class="lineno"> 100</span> <span class="keywordflow">return</span> [os](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0);

</div>

<div class="line">

<span id="l00101"></span><span class="lineno"> 101</span>}

</div>

</div>

<div class="line">

<span id="l00102"></span><span class="lineno"> 102</span>

</div>

<div class="line">

<span id="l00103"></span><span class="lineno"> 103</span>} <span class="comment">// namespace franky</span>

</div>

<div id="anamespacefranky_html" class="ttc">

<div class="ttname">

[franky](namespacefranky.md)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:8

</div>

</div>

<div id="anamespacefranky_html_a054ba89edc6e3948f2dfb5721aaa8bb4" class="ttc">

<div class="ttname">

[franky::operator\<\<](namespacefranky.md#a054ba89edc6e3948f2dfb5721aaa8bb4)

</div>

<div class="ttdeci">

std::ostream & operator\<\<(std::ostream \&os, const DynamicsLimit\< Vector7d \> \&limit)

</div>

<div class="ttdef">

**Definition** dynamics\_limit.cpp:47

</div>

</div>

<div id="anamespacefranky_html_a0b6bfc825c262ae89d9b0adcccd97ab0" class="ttc">

<div class="ttname">

[franky::toStdD](namespacefranky.md#a0b6bfc825c262ae89d9b0adcccd97ab0)

</div>

<div class="ttdeci">

std::array\< double, dims \> toStdD(const Eigen::Matrix\< double, dims, 1 \> \&vector)

</div>

<div class="ttdef">

**Definition** util.hpp:18

</div>

</div>

<div id="anamespacefranky_html_a246b8f841f3b7b07838f181539a5e35f" class="ttc">

<div class="ttname">

[franky::toEigen](namespacefranky.md#a246b8f841f3b7b07838f181539a5e35f)

</div>

<div class="ttdeci">

Eigen::Matrix\< T, dims, 1 \> toEigen(const std::array\< T, dims \> \&vector)

</div>

<div class="ttdef">

**Definition** util.hpp:23

</div>

</div>

<div id="anamespacefranky_html_a247f61893b0ba6dcf29b11453cf59564" class="ttc">

<div class="ttname">

[franky::toStdDMatD](namespacefranky.md#a247f61893b0ba6dcf29b11453cf59564)

</div>

<div class="ttdeci">

std::array\< double, rows \*cols \> toStdDMatD(const Eigen::Matrix\< double, rows, cols, Eigen::ColMajor \> \&matrix)

</div>

<div class="ttdef">

**Definition** util.hpp:33

</div>

</div>

<div id="anamespacefranky_html_a44e848015229ff1e964fc5be35ee3d55" class="ttc">

<div class="ttname">

[franky::toEigenMatD](namespacefranky.md#a44e848015229ff1e964fc5be35ee3d55)

</div>

<div class="ttdeci">

Eigen::Matrix\< double, rows, cols, Eigen::ColMajor \> toEigenMatD(const std::array\< double, rows \*cols \> \&array)

</div>

<div class="ttdef">

**Definition** util.hpp:40

</div>

</div>

<div id="anamespacefranky_html_a4af8de05472061175cee07678cddc6c3" class="ttc">

<div class="ttname">

[franky::ensureEigen](namespacefranky.md#a4af8de05472061175cee07678cddc6c3)

</div>

<div class="ttdeci">

Eigen::Vector\< double, dims \> ensureEigen(const Array\< dims \> \&input)

</div>

<div class="ttdef">

**Definition** util.hpp:51

</div>

</div>

<div id="anamespacefranky_html_a66970149b439291c4f95173b9e414161" class="ttc">

<div class="ttname">

[franky::toStd](namespacefranky.md#a66970149b439291c4f95173b9e414161)

</div>

<div class="ttdeci">

std::array\< T, dims \> toStd(const Eigen::Matrix\< T, dims, 1 \> \&vector)

</div>

<div class="ttdef">

**Definition** util.hpp:11

</div>

</div>

<div id="anamespacefranky_html_acf0fc6eb90d96155c7700e17d783b101" class="ttc">

<div class="ttname">

[franky::ensureStd](namespacefranky.md#acf0fc6eb90d96155c7700e17d783b101)

</div>

<div class="ttdeci">

std::array\< double, dims \> ensureStd(const Array\< dims \> \&input)

</div>

<div class="ttdef">

**Definition** util.hpp:57

</div>

</div>

<div id="anamespacefranky_html_ad661aa664ba35fe438aec340c76bc913" class="ttc">

<div class="ttname">

[franky::expandEigen](namespacefranky.md#ad661aa664ba35fe438aec340c76bc913)

</div>

<div class="ttdeci">

Eigen::Vector\< double, dims \> expandEigen(const ScalarOrArray\< dims \> \&input)

</div>

<div class="ttdef">

**Definition** util.hpp:73

</div>

</div>

<div id="anamespacefranky_html_aded23761176a51276cdf6c8795d7891c" class="ttc">

<div class="ttname">

[franky::stdToAffine](namespacefranky.md#aded23761176a51276cdf6c8795d7891c)

</div>

<div class="ttdeci">

Affine stdToAffine(const std::array\< double, 16 \> \&array)

</div>

<div class="ttdef">

**Definition** util.hpp:44

</div>

</div>

<div id="anamespacefranky_html_ae5cfa5596da548550897b01e9e1bd14b" class="ttc">

<div class="ttname">

[franky::expand](namespacefranky.md#ae5cfa5596da548550897b01e9e1bd14b)

</div>

<div class="ttdeci">

std::array\< double, dims \> expand(const ScalarOrArray\< dims \> \&input)

</div>

<div class="ttdef">

**Definition** util.hpp:63

</div>

</div>

<div id="anamespacefranky_html_ae77a95d5f13271457b8c8fb645da3bd9" class="ttc">

<div class="ttname">

[franky::ScalarOrArray](namespacefranky.md#ae77a95d5f13271457b8c8fb645da3bd9)

</div>

<div class="ttdeci">

std::variant\< double, Array\< dims \> \> ScalarOrArray

</div>

<div class="ttdef">

**Definition** types.hpp:21

</div>

</div>

<div id="anamespacefranky_html_ae9a820b03821a3e69e1e2eb1db33ea66" class="ttc">

<div class="ttname">

[franky::Array](namespacefranky.md#ae9a820b03821a3e69e1e2eb1db33ea66)

</div>

<div class="ttdeci">

std::variant\< std::array\< double, dims \>, Eigen::Vector\< double, dims \> \> Array

</div>

<div class="ttdef">

**Definition** types.hpp:18

</div>

</div>

<div id="anamespacefranky_html_aea642ac2353991b394de429b7932dccf" class="ttc">

<div class="ttname">

[franky::toEigenD](namespacefranky.md#aea642ac2353991b394de429b7932dccf)

</div>

<div class="ttdeci">

Eigen::Matrix\< double, dims, 1 \> toEigenD(const std::array\< double, dims \> \&vector)

</div>

<div class="ttdef">

**Definition** util.hpp:28

</div>

</div>

<div id="anamespacefranky_html_afab9faf133666ada543b15236a8c4b5f" class="ttc">

<div class="ttname">

[franky::Affine](namespacefranky.md#afab9faf133666ada543b15236a8c4b5f)

</div>

<div class="ttdeci">

Eigen::Affine3d Affine

</div>

<div class="ttdef">

**Definition** types.hpp:15

</div>

</div>

</div>

</div>

-----

<span class="small">Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.md) 1.9.8</span>
