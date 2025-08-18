## Visualization Methods


### Persistence Diagrams
- **Points**: $(birth, death)$ coordinates
- **Diagonal**: $y = x$ represents noise threshold
- **Distance from Diagonal**: Measures feature persistence


### Barcodes
- **Intervals**: $[birth, death)$ as horizontal bars
- **Length**: Indicates feature persistence
- **Stacking**: Shows multiple features per dimension


### Mapper Networks
- **Nodes**: Clusters from pullback cover
- **Edges**: Non-empty cluster intersections
- **Node Size**: Proportional to cluster size
- **Node Color**: Based on filter function values


### Statistical Summaries
- **Persistence Landscapes**: $\lambda_k(t) = \max_i \max(0, \min(t - b_i, d_i - t))$
- **Persistence Images**: Gaussian smoothing of persistence diagrams
- **Persistence Curves**: $PC_p(t) = \left(\sum_{(b,d)} (d-b)^p \mathbf{1}_{[b,d)}(t)\right)^{1/p}$


### Interactive Exploration
- **Linked Views**: Coordinate multiple visualizations
- **Parameter Sweeps**: Animate across parameter ranges  
- **Feature Selection**: Isolate specific topological features
- **Data Integration**: Combine with original data visualization

