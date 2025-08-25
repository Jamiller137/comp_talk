## Visualization/Analysis Methods

1. Multi-scale summaries of homology

    - Persistence Diagrams

2. Fixed-scale nerve representations

    - Simplicial representations (Cech complex, etc.)
    - Mapper


## Current Tools:
- Ripser
- CeREEBrus
- Kepler Mapper
- Dionysus
- GHUDI
- Zen Mapper
- TDAView
- MappeR


## Natural Image Space Setup
Given a grid of grayscale pixels, a major focus of computer vision research is studying the subset of natural images.

<div class="uiowa-logo">
    <img src="images/01.png" alt="University of Iowa" style="height: 300px;">
</div>
<p style="font-size: 0.55em; margin: 0;">
    van Hateren, J. H., &amp; van der Schaaf, A. (1998). <em>Independent component filters of natural images compared with simple cells in primary visual cortex</em>. Proc. R. Soc. Lond. B, 265, 359–366.
</p>


## Major Problem
The space of such images globally has as many dimensions as there are pixels which makes analysis intractible.

To reduce this dimensionality problem, most analysis is done locally.


## Natural Images Analysis
<p style="font-size: 0.55em; margin: 0;">
  Carlsson, G., Ishkhanov, T., Silva, V., &amp; Zomorodian, A. (2008). <em>On the Local Behavior of Spaces of Natural Images</em>. International Journal of Computer Vision, 76, 1–12.
</p>

Considered the space of $3 \times 3$ *high-contrast* patches from natural images.

<div class="uiowa-logo">
    <img src="images/patch1.png" alt="University of Iowa" style="height: 200px;">
</div>


## Previous Results

Have shown evidence for a high-density manifold whose 1-skeleton follows the three circle model:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 459.791 317.343" style="max-width: 60%;">
  <rect x="8.652" y="39.069" width="24.706" height="24.706" style="stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.357" y="39.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(137, 137, 137);"></rect>
  <rect x="58.066" y="39.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.652" y="63.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.357" y="63.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(137, 137, 137);"></rect>
  <rect x="58.066" y="63.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.652" y="88.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.357" y="88.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(137, 137, 137);"></rect>
  <rect x="58.066" y="88.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.325" y="139.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(246, 246, 246); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="139.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="139.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="163.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(246, 246, 246); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="163.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="163.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="188.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="188.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="188.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="239.069" width="24.706" height="24.706" style="stroke: rgb(255, 255, 255); stroke-width: 1px;"></rect>
  <rect x="33.03" y="239.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="239.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.325" y="263.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="263.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="57.739" y="263.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="288.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="33.03" y="288.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="288.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <text style="fill: rgb(255, 0, 0); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; white-space: pre;" transform="matrix(0.771769, 0, 0, 0.756097, -78.941299, -17.978598)" x="122.055" y="57.487">Linear</text>
  <text style="fill: rgb(214, 0, 255); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; white-space: pre;" transform="matrix(0.610857, 0, 0, 0.637347, -87.939308, 67.890366)"><tspan x="155.659" y="259.367">Quadratic</tspan><tspan x="155.659" dy="1em">​</tspan></text>
  <text style="fill: rgb(7, 0, 255); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; white-space: pre;" transform="matrix(0.610857, 0, 0, 0.637347, -87.167091, -32.57262)"><tspan x="155.659" y="259.367">Quadratic</tspan><tspan x="155.659" dy="1em">​</tspan></text>
  <ellipse style="fill: rgba(216, 216, 216, 0); stroke-width: 3px; stroke: rgb(255, 0, 0);" cx="196.408" cy="174.488" rx="56.779" ry="56.779"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(30, 0, 255, 0); stroke: rgb(7, 0, 255);" cx="195.893" cy="174.032" rx="56.006" ry="9.084"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(216, 216, 216, 0); stroke: rgb(214, 0, 255);" cx="195.7" cy="173.845" rx="6.759" ry="56.006"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0);" cx="195.713" cy="118.418" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="196.279" cy="232.039" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="253.444" cy="174.103" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="140.659" cy="174.102" rx="4.442" ry="4.442"></ellipse>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="270.825" y="183.115">=</text>
  <ellipse style="fill: rgba(216, 216, 216, 0); stroke-width: 3px; stroke: rgb(255, 0, 0);" cx="377.173" cy="174.649" rx="56.779" ry="56.779"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(216, 216, 216, 0); stroke: rgb(214, 0, 255);" cx="376.465" cy="174.006" rx="6.759" ry="56.006"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="376.478" cy="118.579" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="377.044" cy="232.2" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="434.209" cy="174.264" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="321.424" cy="174.263" rx="4.442" ry="4.442"></ellipse>
  <path style="fill: rgba(216, 216, 216, 0); stroke-width: 3px; stroke: rgb(7, 0, 255);" d="M 321.81 175.003 C 321.81 175.003 266.963 68.399 375.885 66.467 C 484.807 64.535 434.982 174.617 434.982 174.617 C 434.982 174.617 478.628 283.54 380.521 283.153 C 282.414 282.766 321.81 176.548 321.81 175.003 Z"></path>
</svg>


## Pre-processing Flowchart:
<div style="text-align: left;">
  <ul>
    <li>Randomly sample 5000 patch vectors in $\mathbb{R}^9$ </li>
    <li>Take logarithm </li>
    <li>Subtract average of all coordinates from each coordinate</li>
    <li>Compute contrast or "D-norm" of the vector</li>
    <li>Keep the patch if it is among the top 20% of all patches</li>
    <li>Normalize by D-norm to place on a 7-dim ellipsoid</li>
    <li>Change coordinates so that the set lies on the 7-dimensional sphere in $\mathbb{R}^8$ </li>
  </ul>
</div>


## Final Analysis
- Dataset $X$ of $4 \times 10^6$ high-contrast patches in $\mathbb{R}^{8}$

**Goal:** Study high-density subset of these high-contrast patches.


## Density Filter

Let $X(\nu, p)$ to be the $p\\%$ of points in $X$ with the smallest distance to their $\nu^\text{th}$-nearest neighbor. 


## Five Circles
<div class="uiowa-logo">
    <img src="images/natural_5_circles.png" alt="University of Iowa" style="max-width: 55%;">
</div>


Recall:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 459.791 317.343" style="max-width: 70%;">
  <rect x="8.652" y="39.069" width="24.706" height="24.706" style="stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.357" y="39.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(137, 137, 137);"></rect>
  <rect x="58.066" y="39.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.652" y="63.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.357" y="63.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(137, 137, 137);"></rect>
  <rect x="58.066" y="63.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.652" y="88.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.357" y="88.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(137, 137, 137);"></rect>
  <rect x="58.066" y="88.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.325" y="139.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(246, 246, 246); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="139.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="139.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="163.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(246, 246, 246); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="163.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="163.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="188.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="188.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="188.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="239.069" width="24.706" height="24.706" style="stroke: rgb(255, 255, 255); stroke-width: 1px;"></rect>
  <rect x="33.03" y="239.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="239.069" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="8.325" y="263.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="33.03" y="263.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="57.739" y="263.775" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255); fill: rgb(233, 233, 233);"></rect>
  <rect x="8.325" y="288.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="33.03" y="288.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <rect x="57.739" y="288.484" width="24.706" height="24.706" style="stroke-width: 1px; stroke: rgb(255, 255, 255);"></rect>
  <text style="fill: rgb(255, 0, 0); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; white-space: pre;" transform="matrix(0.771769, 0, 0, 0.756097, -78.941299, -17.978598)" x="122.055" y="57.487">Linear</text>
  <text style="fill: rgb(214, 0, 255); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; white-space: pre;" transform="matrix(0.610857, 0, 0, 0.637347, -87.939308, 67.890366)"><tspan x="155.659" y="259.367">Quadratic</tspan><tspan x="155.659" dy="1em">​</tspan></text>
  <text style="fill: rgb(7, 0, 255); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; white-space: pre;" transform="matrix(0.610857, 0, 0, 0.637347, -87.167091, -32.57262)"><tspan x="155.659" y="259.367">Quadratic</tspan><tspan x="155.659" dy="1em">​</tspan></text>
  <ellipse style="fill: rgba(216, 216, 216, 0); stroke-width: 3px; stroke: rgb(255, 0, 0);" cx="196.408" cy="174.488" rx="56.779" ry="56.779"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(30, 0, 255, 0); stroke: rgb(7, 0, 255);" cx="195.893" cy="174.032" rx="56.006" ry="9.084"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(216, 216, 216, 0); stroke: rgb(214, 0, 255);" cx="195.7" cy="173.845" rx="6.759" ry="56.006"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0);" cx="195.713" cy="118.418" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="196.279" cy="232.039" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="253.444" cy="174.103" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="140.659" cy="174.102" rx="4.442" ry="4.442"></ellipse>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="270.825" y="183.115">=</text>
  <ellipse style="fill: rgba(216, 216, 216, 0); stroke-width: 3px; stroke: rgb(255, 0, 0);" cx="377.173" cy="174.649" rx="56.779" ry="56.779"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(216, 216, 216, 0); stroke: rgb(214, 0, 255);" cx="376.465" cy="174.006" rx="6.759" ry="56.006"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="376.478" cy="118.579" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="377.044" cy="232.2" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="434.209" cy="174.264" rx="4.442" ry="4.442"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="321.424" cy="174.263" rx="4.442" ry="4.442"></ellipse>
  <path style="fill: rgba(216, 216, 216, 0); stroke-width: 3px; stroke: rgb(7, 0, 255);" d="M 321.81 175.003 C 321.81 175.003 266.963 68.399 375.885 66.467 C 484.807 64.535 434.982 174.617 434.982 174.617 C 434.982 174.617 478.628 283.54 380.521 283.153 C 282.414 282.766 321.81 176.548 321.81 175.003 Z"></path>
</svg>


<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 313.345" style="max-width: 70%">
  <rect x="131.687" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);" y="15.75"></rect>
  <rect x="140.788" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0);" y="15.75"></rect>
  <rect x="149.891" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0);" y="15.75"></rect>
  <rect x="131.687" y="24.851" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="140.788" y="24.851" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0);"></rect>
  <rect x="149.891" y="24.851" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="131.687" y="33.954" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="140.788" y="33.954" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0);"></rect>
  <rect x="149.891" y="33.954" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <ellipse style="fill: rgba(216, 216, 216, 0); stroke-width: 3px; stroke: rgb(255, 0, 0);" cx="146.498" cy="158.201" rx="101.488" ry="101.488"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(30, 0, 255, 0); stroke: rgb(7, 0, 255);" cx="145.577" cy="160.704" rx="100.106" ry="56.421"></ellipse>
  <ellipse style="stroke-width: 3px; fill: rgba(216, 216, 216, 0); stroke: rgb(214, 0, 255);" cx="145.227" cy="157.517" rx="43.853" ry="100.106"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0);" cx="145.255" cy="57.98" rx="7.94" ry="7.94"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="146.266" cy="261.068" rx="7.94" ry="7.94"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="248.444" cy="157.512" rx="7.94" ry="7.94"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="46.85" cy="157.511" rx="7.94" ry="7.94"></ellipse>
  <rect x="132.885" y="91.01" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="141.786" y="91.01" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="150.69" y="91.01" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="132.885" y="99.912" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="141.786" y="99.912" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="150.69" y="99.912" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="132.885" y="108.814" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="141.786" y="108.814" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="150.69" y="108.814" width="8.902" height="8.902" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="177.246" y="142.212" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="186.147" y="142.212" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="195.05" y="142.212" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="177.246" y="151.113" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="186.147" y="151.113" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="195.05" y="151.113" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="177.246" y="160.016" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="186.147" y="160.016" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="195.05" y="160.016" width="8.901" height="8.901" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="394.958" y="183.715" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 255, 255); transform-origin: 399.51px 188.265px 0px;" transform="matrix(0, 1, -1, 0, -115.173621, -40.319651)"></rect>
  <rect x="404.058" y="183.715" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: 408.61px 188.265px 0px;" transform="matrix(0, 1, -1, 0, -124.274284, -31.219074)"></rect>
  <rect x="413.161" y="183.715" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 417.711px 188.264px 0px;" transform="matrix(0, 1, -1, 0, -133.374005, -22.117298)"></rect>
  <rect x="394.958" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 399.508px 197.368px 0px;" transform="matrix(0, 1, -1, 0, -124.275427, -49.423738)"></rect>
  <rect x="404.058" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: 408.609px 197.368px 0px;" transform="matrix(0, 1, -1, 0, -133.376091, -40.323227)"></rect>
  <rect x="413.161" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 417.71px 197.367px 0px;" transform="matrix(0, 1, -1, 0, -142.475699, -31.221146)"></rect>
  <rect x="394.958" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 399.508px 206.471px 0px;" transform="matrix(0, 1, -1, 0, -133.378475, -58.526705)"></rect>
  <rect x="404.058" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: 408.609px 206.471px 0px;" transform="matrix(0, 1, -1, 0, -142.479091, -49.426044)"></rect>
  <rect x="413.161" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 417.71px 206.47px 0px;" transform="matrix(0, 1, -1, 0, -151.578638, -40.324146)"></rect>
  <rect x="-160.65" y="-300" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 255, 255); transform-origin: -156.084px -295.452px 0px;" transform="matrix(-1, 0, 0, -1, 312.168744, 590.903505)"></rect>
  <rect x="-151.54" y="-300" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: -146.984px -295.452px 0px;" transform="matrix(-1, 0, 0, -1, 293.968088, 590.903505)"></rect>
  <rect x="-142.44" y="-300" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: -137.883px -295.452px 0px;" transform="matrix(-1, 0, 0, -1, 275.76602, 590.904)"></rect>
  <rect x="-160.65" y="-290.9" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: -156.086px -286.347px 0px;" transform="matrix(-1, 0, 0, -1, 312.171008, 572.694)"></rect>
  <rect x="-151.53" y="-290.9" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: -146.985px -286.347px 0px;" transform="matrix(-1, 0, 0, -1, 293.970267, 572.694532)"></rect>
  <rect x="-142.44" y="-290.9" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: -137.885px -286.349px 0px;" transform="matrix(-1, 0, 0, -1, 275.769958, 572.698)"></rect>
  <rect x="-160.65" y="-281.79" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: -156.086px -277.245px 0px;" transform="matrix(-1, 0, 0, -1, 312.171602, 554.49)"></rect>
  <rect x="-151.53" y="-281.8" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: -146.985px -277.246px 0px;" transform="matrix(-1, 0, 0, -1, 293.970267, 554.49122)"></rect>
  <rect x="-142.44" y="-281.8" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: -137.885px -277.246px 0px;" transform="matrix(-1, 0, 0, -1, 275.769958, 554.49278)"></rect>
  <rect x="-161.57" y="-191.84" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 255, 255); transform-origin: -157.009px -187.296px 0px;" transform="matrix(0, -1, 1, 0, 167.832121, 352.831102)"></rect>
  <rect x="-152.46" y="-191.84" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: -147.908px -187.296px 0px;" transform="matrix(0, -1, 1, 0, 158.731431, 343.73117)"></rect>
  <rect x="-143.37" y="-191.84" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: -138.808px -187.296px 0px;" transform="matrix(0, -1, 1, 0, 149.63082, 334.630432)"></rect>
  <rect x="-161.57" y="-182.75" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: -157.01px -178.191px 0px;" transform="matrix(0, -1, 1, 0, 176.938211, 343.726571)"></rect>
  <rect x="-152.46" y="-182.75" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: -147.91px -178.193px 0px;" transform="matrix(0, -1, 1, 0, 167.835846, 334.628881)"></rect>
  <rect x="-143.38" y="-182.75" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: -138.808px -178.193px 0px;" transform="matrix(0, -1, 1, 0, 158.734012, 325.528207)"></rect>
  <rect x="-161.57" y="-173.63" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: -157.01px -169.089px 0px;" transform="matrix(0, -1, 1, 0, 186.040344, 334.625422)"></rect>
  <rect x="-152.46" y="-173.64" width="9.101" height="9.101" style="stroke-width: 1px; fill: rgb(137, 137, 137); stroke: rgb(0, 0, 0); transform-origin: -147.91px -169.089px 0px;" transform="matrix(0, -1, 1, 0, 176.939406, 325.524763)"></rect>
  <rect x="-143.38" y="-173.64" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: -138.808px -169.092px 0px;" transform="matrix(0, -1, 1, 0, 167.835125, 316.427552)"></rect>
  <rect x="394.958" y="183.715" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 399.51px 188.265px 0px;" transform="matrix(0, 1, -1, 0, -288.859773, -41.790594)"></rect>
  <rect x="404.058" y="183.715" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 408.61px 188.265px 0px;" transform="matrix(0, 1, -1, 0, -297.960411, -32.689991)"></rect>
  <rect x="413.161" y="183.715" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 417.711px 188.264px 0px;" transform="matrix(0, 1, -1, 0, -307.060192, -23.588032)"></rect>
  <rect x="394.958" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 399.508px 197.368px 0px;" transform="matrix(0, 1, -1, 0, -297.961681, -50.894752)"></rect>
  <rect x="404.058" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 408.609px 197.368px 0px;" transform="matrix(0, 1, -1, 0, -307.062309, -41.794098)"></rect>
  <rect x="413.161" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 417.71px 197.367px 0px;" transform="matrix(0, 1, -1, 0, -316.16193, -32.692034)"></rect>
  <rect x="394.958" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 399.508px 206.471px 0px;" transform="matrix(0, 1, -1, 0, -307.064716, -59.997564)"></rect>
  <rect x="404.058" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 408.609px 206.471px 0px;" transform="matrix(0, 1, -1, 0, -316.165266, -50.896988)"></rect>
  <rect x="413.161" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 417.71px 206.47px 0px;" transform="matrix(0, 1, -1, 0, -325.264887, -41.79494)"></rect>
  <rect x="394.958" y="183.715" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(164, 164, 164); transform-origin: 399.51px 188.265px 0px;" transform="matrix(0, 1, -1, 0, -153.364696, -127.471426)"></rect>
  <rect x="404.058" y="183.715" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: 408.61px 188.265px 0px;" transform="matrix(0, 1, -1, 0, -162.465184, -118.371069)"></rect>
  <rect x="413.161" y="183.715" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 417.711px 188.264px 0px;" transform="matrix(0, 1, -1, 0, -171.565088, -109.269095)"></rect>
  <rect x="394.958" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: 399.508px 197.368px 0px;" transform="matrix(0, 1, -1, 0, -162.466454, -136.575698)"></rect>
  <rect x="404.058" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: 408.609px 197.368px 0px;" transform="matrix(0, 1, -1, 0, -171.567149, -127.475125)"></rect>
  <rect x="413.161" y="192.816" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: 417.71px 197.367px 0px;" transform="matrix(0, 1, -1, 0, -180.666727, -118.373039)"></rect>
  <rect x="394.958" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 399.508px 206.471px 0px;" transform="matrix(0, 1, -1, 0, -171.569607, -145.678637)"></rect>
  <rect x="404.058" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: 408.609px 206.471px 0px;" transform="matrix(0, 1, -1, 0, -180.670083, -136.577947)"></rect>
  <rect x="413.161" y="201.919" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: 417.71px 206.47px 0px;" transform="matrix(0, 1, -1, 0, -189.769661, -127.475973)"></rect>
  <rect x="38.048" y="54.933" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(164, 164, 164); transform-origin: 42.6px 59.483px 0px;"></rect>
  <rect x="47.153" y="54.933" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: 51.699px 59.483px 0px;"></rect>
  <rect x="56.249" y="54.934" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 60.8px 59.483px 0px;"></rect>
  <rect x="38.048" y="64.034" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: 42.599px 68.586px 0px;"></rect>
  <rect x="47.154" y="64.034" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: 51.699px 68.586px 0px;"></rect>
  <rect x="56.249" y="64.034" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: 60.8px 68.585px 0px;"></rect>
  <rect x="38.048" y="73.138" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 42.599px 77.69px 0px;"></rect>
  <rect x="47.154" y="73.137" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: 51.699px 77.689px 0px;"></rect>
  <rect x="56.249" y="73.137" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: 60.8px 77.688px 0px;"></rect>
  <rect x="167.335" y="257.156" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(164, 164, 164); transform-origin: 171.887px 261.706px 0px;" transform="matrix(0, -1, 1, 0, -127.984838, -3.541247)"></rect>
  <rect x="176.436" y="257.156" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: 180.987px 261.706px 0px;" transform="matrix(0, -1, 1, 0, -137.084345, -12.640815)"></rect>
  <rect x="185.539" y="257.156" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: 190.089px 261.705px 0px;" transform="matrix(0, -1, 1, 0, -146.187371, -21.741584)"></rect>
  <rect x="167.335" y="266.257" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: 171.886px 270.809px 0px;" transform="matrix(0, -1, 1, 0, -118.880787, -12.643059)"></rect>
  <rect x="176.436" y="266.257" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: 180.987px 270.809px 0px;" transform="matrix(0, -1, 1, 0, -127.981464, -21.743772)"></rect>
  <rect x="185.539" y="266.257" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: 190.088px 270.808px 0px;" transform="matrix(0, -1, 1, 0, -137.083177, -30.843296)"></rect>
  <rect x="167.335" y="275.36" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: 171.886px 279.912px 0px;" transform="matrix(0, -1, 1, 0, -109.777846, -21.746077)"></rect>
  <rect x="176.436" y="275.36" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: 180.987px 279.912px 0px;" transform="matrix(0, -1, 1, 0, -118.878525, -30.846772)"></rect>
  <rect x="185.539" y="275.36" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: 190.088px 279.911px 0px;" transform="matrix(0, -1, 1, 0, -127.980295, -39.946209)"></rect>
  <rect x="-256.9" y="-257.81" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(164, 164, 164); transform-origin: -252.352px -253.265px 0px;" transform="matrix(-1, 0, 0, -1, 504.704444, 506.529468)"></rect>
  <rect x="-247.81" y="-257.81" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: -243.253px -253.265px 0px;" transform="matrix(-1, 0, 0, -1, 486.505008, 506.529468)"></rect>
  <rect x="-238.7" y="-257.81" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); transform-origin: -234.151px -253.266px 0px;" transform="matrix(-1, 0, 0, -1, 468.301416, 506.531505)"></rect>
  <rect x="-256.9" y="-248.71" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: -252.354px -244.162px 0px;" transform="matrix(-1, 0, 0, -1, 504.708073, 488.323876)"></rect>
  <rect x="-247.81" y="-248.71" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: -243.253px -244.161px 0px;" transform="matrix(-1, 0, 0, -1, 486.506521, 488.322725)"></rect>
  <rect x="-238.7" y="-248.71" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(117, 117, 117); transform-origin: -234.153px -244.162px 0px;" transform="matrix(-1, 0, 0, -1, 468.306398, 488.323149)"></rect>
  <rect x="-256.91" y="-239.61" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255); transform-origin: -252.354px -235.059px 0px;" transform="matrix(-1, 0, 0, -1, 504.707911, 470.117945)"></rect>
  <rect x="-247.81" y="-239.6" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(220, 220, 220); transform-origin: -243.253px -235.058px 0px;" transform="matrix(-1, 0, 0, -1, 486.505379, 470.115257)"></rect>
  <rect x="-238.7" y="-239.6" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(164, 164, 164); transform-origin: -234.154px -235.059px 0px;" transform="matrix(-1, 0, 0, -1, 468.307255, 470.118601)"></rect>
  <rect x="132.865" width="9.101" height="9.101" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 255, 255);" y="201.457"></rect>
  <rect x="141.966" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);" y="201.457"></rect>
  <rect x="151.069" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);" y="201.457"></rect>
  <rect x="132.865" y="210.558" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="141.966" y="210.558" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="151.069" y="210.558" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0);"></rect>
  <rect x="132.865" y="219.661" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="141.966" y="219.661" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
  <rect x="151.069" y="219.661" width="9.101" height="9.101" style="stroke-width: 1px; stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);"></rect>
</svg>


## 2-Manifold

$\beta_{2} = 1$ is evidence that we have a surface.
<div class="uiowa-logo">
    <img src="images/natural_barcodes.png" alt="University of Iowa" style="max-width: 30%;">
</div>

- So this space is either a Torus or a Klein Bottle.


## The Klein Bottle:
They conclude you can parameterize this space with a Klein bottle:
<div style="display: flex; gap: 10px; justify-content: flex-start; align-items: center; max-width: 100%;">
    <img src="images/klein_bottle.png" alt="First image" style="max-width: 45%; height: auto;">
    <img src="images/klein_param.png" alt="Second image" style="max-width: 56%; height: auto;">
</div>
