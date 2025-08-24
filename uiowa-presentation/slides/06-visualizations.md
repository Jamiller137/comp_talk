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
- Dataset of $4 \times 10^6$ high-contrast patches in $\mathbb{R}^{8}$

**Goal:** Study high-density subset of these high-contrast patches.


## Density Filter

Let $X(\nu, p)$ to be the $p\\%$ of points in $X$ with the smallest distance to their $\nu^\text{th}$-nearest neighbor. 


## Five Circles
<div class="uiowa-logo">
    <img src="images/natural_5_circles.png" alt="University of Iowa" style="max-width: 55%;">
</div>


## 2-Manifold

$\beta_{2} = 1$ in $\mathbb{Z}/2\mathbb{Z}$ coefficients is evidence that we have a 2-manifold.
<div class="uiowa-logo">
    <img src="images/natural_barcodes.png" alt="University of Iowa" style="max-width: 30%;">
</div>

- So this space is either a Torus or a Klein Bottle.


## The Klein Bottle:
After investigating patches they conclude you can parameterize the space of high-contrast $3 \times 3$ patches with high density 



### Goal: Obtain result using mapper analysis


### Zen-Sight


### Interactive Exploration
- **Filtrations**: Animate across parameter ranges  
- **Mapper Graph**: Manipulate and decompose simplicial complex
- **Data Integration**: Include with original data for analysis

