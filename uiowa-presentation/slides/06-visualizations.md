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


## Three Circle Model:
Evidence supports the following:

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


## 2-Manifold

$\beta_{2} = 1$ in $\mathbb{Z}/2\mathbb{Z}$ is evidence that we have a surface.
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



### Goal: Obtain result using mapper analysis


### Zen-Sight


### Interactive Exploration
- **Filtrations**: Animate across parameter ranges  
- **Mapper Graph**: Manipulate and decompose simplicial complex
- **Data Integration**: Include with original data for analysis

