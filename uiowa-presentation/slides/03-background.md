## Topological Data Analysis

The use of tools from topology to extract and study data 'shape' across scales.

**Key Insight**: Topology provides robust features that persist across noise and different scales, revealing the intrinsic geometric structure of data.


## Three Themes

### 1. Data → Topological Spaces

### 2. Persistence and Stability

### 3. Visualization Methods


## Constructing Topological Spaces

**Problem**: Raw data typically lacks inherent topological structure.

**Solution**: Construct simplicial complexes from point-cloud data using proximity relationships.


## General Framework:
- Given point cloud $X = \{x_1, x_2, \ldots, x_n\} \subset \mathbb{R}^d$
- Define proximity criterion based on distance threshold $\epsilon$
- Build simplicial complex $K_\epsilon(X)$ where simplices represent local connectivity



## Vietoris-Rips Complex

**Definition**: For point cloud $X$ and radius $\epsilon > 0$:

$$VR_\epsilon(X) = \{\sigma \subseteq X : \text{diam}(\sigma) \leq 2\epsilon\}$$


**Construction**:
- Include $k$-simplex $\{(x_{i_0}, x_{i_1}, \ldots, x_{i_k})\}$ 
if all pairwise distances satisfy:
  $$d(x_{i_j}, x_{i_k}) \leq 2\epsilon \text{ for all } j, k$$


**Properties**:
- Easy to compute
- May include "hollow" simplices
- Commonly used for persistent homology



## Čech Complex

**Definition**: For point cloud $X$ and radius $\epsilon > 0$:

$$\\check{C}\_\\epsilon(X) = \{\sigma \subseteq X : \bigcap_{x \in \sigma} B(x, \epsilon) \neq \emptyset\}$$


**Construction**:
- Include simplex $\sigma$ if the intersection of all $\epsilon$-balls centered at vertices is non-empty
- Geometrically captures true "holes" in data

**Nerve Theorem**: $\check{C}_\epsilon(X)$ has same homotopy type as union of balls $\bigcup_{x \in X} B(x, \epsilon)$

**Trade-off**: More geometrically accurate but computationally expensive


## Witness Complex

**Definition**: Given landmarks $L \subset X$ and witnesses $W \subset X$:

A simplex $\sigma \subseteq L$ belongs to $W_\epsilon(L,W)$ if there exists $w \in W$ such that:
$$d(w, l) \leq d(w, L \setminus \sigma) + \epsilon$$
for all $l \in \sigma$

**Key Idea**:
- Witnesses "see" landmark configurations
- Reduces computational complexity
- Particularly useful for large datasets

**Parameters**:
- Number of landmarks $|L|$
- Witness threshold $\epsilon$


## Delaunay Complex

**Definition**: For point cloud $X \subset \mathbb{R}^d$:

Delaunay triangulation $Del(X)$ consists of simplices where the circumsphere contains no other points from $X$.

**Alpha Complex Connection**:
$$\alpha\text{-complex}_\alpha(X) = \{\sigma \in Del(X) : \text{circumradius}(\sigma) \leq \alpha\}$$

**Properties**:
- Dual to Voronoi diagram
- Captures natural geometric structure
- Well-defined for general position points


## Alpha Complex

**Definition**: Subcomplex of Delaunay triangulation where circumradius ≤ $\alpha$:

$$A_\alpha(X) = \{\sigma \in Del(X) : R(\sigma) \leq \alpha\}$$

where $R(\sigma)$ is the circumradius of simplex $\sigma$.

**Filtration**: $A_{\alpha_1} \subseteq A_{\alpha_2} \subseteq \cdots$ for $\alpha_1 \leq \alpha_2 \leq \cdots$

**Advantages**:
- Geometrically meaningful
- Fewer "artificial" simplices than Vietoris-Rips
- Efficient computation in low dimensions


## Mapper Complex

**Algorithm** (Singh, Mémoli, Carlsson):

1. **Cover**: Choose cover $\mathcal{U} = \{U_i\}$ of filter function range $f: X \to \mathbb{R}^k$
2. **Pullback**: Compute pullback cover $\{f^{-1}(U_i)\}$
3. **Cluster**: Apply clustering algorithm to each $f^{-1}(U_i)$
4. **Network**: Create graph where nodes = clusters, edges = non-empty intersections

**Mathematical Framework**:
- Filter function: $f: X \to \mathbb{R}^k$
- Cover overlap parameter: $p \in (0,1)$
- Resolution parameter: $r > 0$
- Clustering method: $C: 2^X \to 2^{2^X}$



## Persistence and Stability

**Persistence**: Topological features that survive across multiple scales in a filtration.

**Filtration**: Nested sequence of complexes:
$$K_0 \subseteq K_1 \subseteq K_2 \subseteq \cdots \subseteq K_n$$

**Birth-Death**: Feature appears at $K_i$ (birth) and disappears at $K_j$ (death) for $i < j$.

**Persistence**: $\text{pers}(\text{feature}) = j - i$ or $\text{death} - \text{birth}$

**Stability Theorem** (Cohen-Steiner, Edelsbrunner, Harer):
For filtrations $f, g: K \to \mathbb{R}$:
$$d_\infty(\text{dgm}(f), \text{dgm}(g)) \leq \|f - g\|_\infty$$


## Persistent Homology

**Definition**: For filtration $\emptyset = K_0 \subseteq K_1 \subseteq \cdots \subseteq K_n$, track:

$$H_k(K_0) \to H_k(K_1) \to \cdots \to H_k(K_n)$$

**$k$-th Persistent Betti Numbers**:
$$\beta_k^{i,j} = \text{rank}(H_k(K_i) \to H_k(K_j))$$

**Persistence Diagram**: Multiset of points $(b,d)$ where:
- $b$ = birth time
- $d$ = death time
- Points above diagonal $y = x$ represent persistent features

**Barcode**: Alternative visualization showing feature lifespans as intervals $[b,d)$

**Bottleneck Distance**: Stable metric between persistence diagrams:
$$d_B(D_1, D_2) = \inf_{\gamma} \sup_{p \in D_1} \|p - \gamma(p)\|_\infty$$


## Stability in Mapper Parameter Choices

**Parameter Sensitivity**:
- **Resolution**: Affects granularity of cover
- **Overlap**: Controls information flow between regions  
- **Filter Function**: Choice dramatically impacts results
- **Clustering Method**: Different algorithms yield different structures

**Theoretical Results**:
- **Interleaving Distance**: Measures stability between Mapper constructions
- **Multi-scale Approaches**: Use multiple parameter settings simultaneously

**Practical Guidelines**:
1. **Filter Function Selection**:
   - Density-based: $f(x) = \frac{1}{k} \sum_{i=1}^k d(x, x_i^{nn})$
   - Eccentricity: $f(x) = \sum_{y \in X} d(x,y)$
   - Coordinate projections: $f(x) = x_j$ for dimension $j$

2. **Parameter Ranges**:
   - Resolution: 10-50 intervals typically
   - Overlap: 20-50% overlap recommended
   - Cross-validation for optimal choices



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

