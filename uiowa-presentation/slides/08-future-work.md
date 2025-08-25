## Future Work

- Filtration Visualization
- Finish application to Natural Image Patches
- Apply on more datasets

- User-independent Parameter Selection
    - Use Data Assimilation


## WiP: Parameter Selection
*Joint with Dr. Ethan Rooke*
1. Use G-Mapper to construct cover over $f[X] \subset \mathbb{R}$.
2. Use a modfied Jacaard Index as a similarity score
$$ J(p, G, G') = \frac{N_G(p) \cap N_\{G'\}(p)}{N_G(p) \cup N_\{G'\}(p)} $$
3. Forecast Model: Locally quadratic (go to vertex)


## Intial Implementation Results:
Want to optimize DBSCAN $\epsilon$ parameter:
<div class="uiowa-logo">
    <img src="images/dataset.png" alt="University of Iowa" style="max-width: 55%;">
</div>


Ensemble ($n=30$) Traversing DBSCAN $\epsilon$-Filtration
<div class="uiowa-logo">
    <img src="images/optimization_path.png" alt="University of Iowa" style="max-width: 85%;">
</div>


<div class="uiowa-logo">
    <img src="images/graph3.png" alt="University of Iowa" style="max-width: 75%;">
</div>


<div class="uiowa-logo">
    <img src="images/graph2.png" alt="University of Iowa" style="max-width: 75%;">
</div>


<div class="uiowa-logo">
    <img src="images/graph1.png" alt="University of Iowa" style="max-width: 75%;">
</div>

