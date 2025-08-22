### Visualization Methods

Two main categories:

1. Multi-scale summaries of homology
2. Fixed-scale nerve representations


### Persistence Diagrams


### Barcodes


### Mapper Graphs


## Čech vs Vietoris–Rips (intuitive graphic)

- Čech at scale r: include a k-simplex when the k+1 balls of radius r have a non-empty common intersection.
- Vietoris–Rips at threshold t: include a k-simplex when all pairwise distances among its vertices are ≤ t (clique complex).


<div style="display:flex; gap: 2rem; align-items:flex-start; flex-wrap: wrap;">
  <!-- Čech panel -->
  <div style="flex: 1 1 360px;">
    <svg viewBox="0 0 220 180" width="auto" height="auto">
      <!-- balls of radius r (schematic) -->
      <circle cx="60" cy="120" r="55"  stroke="#4e79a7" stroke-width="2" opacity="0.9"/>
      <circle cx="160" cy="120" r="55"  stroke="#4e79a7" stroke-width="2" opacity="0.9"/>
      <circle cx="110" cy="35"  r="55"  stroke="#4e79a7" stroke-width="2" opacity="0.9"/>

      <!-- vertices (data points) -->
      <circle cx="60"  cy="120" r="4" fill="#000"/>
      <circle cx="160" cy="120" r="4" fill="#000"/>
      <circle cx="110" cy="35"  r="4" fill="#000"/>

      <!-- edges (1-simplices: pairwise overlaps exist) -->
      <line x1="60" y1="120" x2="160" y2="120" stroke="#777" stroke-width="2"/>
      <line x1="60" y1="120" x2="110" y2="35"  stroke="#777" stroke-width="2"/>
      <line x1="160" y1="120" x2="110" y2="35"  stroke="#777" stroke-width="2"/>

      <!-- no 2-simplex fill because there is no triple-overlap -->
      <text x="10" y="170" font-size="10" fill="#333">Balls overlap pairwise, but no common intersection of all three.</text>

      <!-- edges (threshold graph) -->
      <line x1="60" y1="120" x2="160" y2="120" stroke="#777" stroke-width="2"/>
      <line x1="60" y1="120" x2="110" y2="35"  stroke="#777" stroke-width="2"/>
      <line x1="160" y1="120" x2="110" y2="35"  stroke="#777" stroke-width="2"/>

      <!-- 2-simplex fill (clique) -->
      <polygon points="60,120 160,120 110,35" fill="#f28e2b" opacity="0.3" stroke="#f28e2b" stroke-width="2"/>

      <text x="10" y="170" font-size="10" fill="#333">All three edges present ⇒ filled 2-simplex in Rips.</text>
    </svg>
  </div>
</div>

Notes:
- Choose r so each pair of balls overlaps, but the triple-overlap is empty (as sketched).
- In Rips, pick a threshold t that makes all three edges present; the 2-simplex is then included by clique completion.


### Interactive Exploration
- **Filtrations**: Animate across parameter ranges  
- **Mapper Graph**: Manipulate and decompose simplicial complex
- **Data Integration**: Include with original data for analysis


### What this paper does

- The paper’s main objective is to **introduce a Mapper-based estimator for Reeb spaces and provide statistical guarantees in the stochastic filter setting** (when the filter is estimated from data).【1】
- It shows how to calibrate Mapper parameters to control risk and demonstrates applicability in several statistical and machine learning scenarios.【1】


### Background: Reeb spaces, Mapper, and filters

- Reeb spaces summarize how level sets of a function on data connect; Mapper is a practical construction approximating these structures from sampled data.【1】
- The paper considers **filter-based pseudometrics** to compare Mapper outputs and Reeb spaces.【1】
- With finite metric spaces and estimated filters, standard Mappers can have issues (e.g., instability, distortion), motivating a modified approach.【1】


### Core idea: Modified Mapper-based estimator

- The method first **refines the input point cloud** to reduce artifacts, then computes the Mapper on the refined structure.【1】
  - This targets “element-crossing edges,” which can distort topological recovery in standard pipelines.【1】
- The construction yields a more robust estimator of the underlying Reeb space, especially under noisy or estimated filters.【1】


### Stochastic filter setting

- In many applications, the filter function is **not known and must be estimated** (e.g., learned embedding, regression score, or summary of a conditional distribution).【1】
- The paper develops a **framework to statistically control Mapper quality when the filter is estimated**, addressing a core practical challenge.【1】


### Statistical guarantees and calibration

- Provides **risk bounds measured by the Gromov–Hausdorff distance** between the estimated and true Reeb spaces, e.g., $d_{GH}(\hat{\mathcal{R}}, \mathcal{R})$.【1】
- Details **how to calibrate Mapper parameters** (graph refinement and cover parameters such as resolution and overlap) to achieve these bounds.【1】
- These guarantees connect sampling, noise, and filter estimation error to the quality of topological recovery.【1】


### Why the refinement matters

- The refinement step alleviates topology-distorting artifacts from element-crossing edges, yielding **improved topological recovery** compared to standard Mapper in noisy or misspecified-filter regimes.【1】
- Especially beneficial when conditional distributions are high-variance or multimodal, where naive filters mislead the Mapper construction.【1】


### Applications and use cases

- Statistical machine learning with real-valued or multivariate filters:
  - Regression, classification, and dimension reduction tasks.【1】
- Conditional probability distributions:
  - Filters built from summaries (means, histograms) of conditional distributions, robust to noise.【1】
- Combinatorial graphs:
  - Mapper on graph spaces using graph edit distance as the metric.【1】


### Key findings

- The proposed estimator **recovers underlying topology more robustly** than standard Mapper when filters are estimated or data are noisy.【1】
- Provides **statistical risk bounds** and practical **parameter calibration** guidance.【1】
- **Effective in complex scenarios** (e.g., bimodal or high-variance conditionals) where standard approaches fail.【1】
- Establishes a principled way to **handle uncertainty in filter functions** for Mapper-based TDA.【1】


### Practical guidance (at a glance)

- Graph refinement:
  - Apply refinement to mitigate element-crossing edges before computing Mapper.【1】
- Cover construction:
  - Choose resolution and overlap informed by the risk bounds; adjust to balance sensitivity and stability.【1】
- Filter estimation:
  - Use filters compatible with the data’s noise/structure (e.g., stable summaries for conditional distributions).【1】


### Conclusions and impact

- The estimator is **statistically sound and practically useful** for TDA with estimated filters.【1】
- Advances TDA by bridging theoretical constructions and real-world data settings with uncertainty in filters.【1】


### Future directions

- Optimizing the estimator and its computational trade-offs.【1】
- Bootstrap methods for **confidence regions** on recovered structures.【1】
- Extending guarantees to other distances (e.g., **interleaving distance**).【1】


### Glossary (quick)

- Reeb space:
  - A quotient capturing connectivity of level sets of a function on a space.【1】
- Mapper:
  - A graph-based approximation built from a cover of the filter range and clustering of preimages.【1】
- Stochastic filter:
  - A filter function estimated from data rather than known exactly.【1】
- Gromov–Hausdorff distance:
  - A metric comparing shapes of metric spaces, used here for risk bounds.【1】


### Reference

- 1912.10742v2: Mapper-based estimator for Reeb spaces with stochastic filters; methodology, risk bounds, applications, and conclusions summarized above.【1】


