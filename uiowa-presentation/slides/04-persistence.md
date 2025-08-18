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
- **Filtrations and Interleaving**: Measures stability between Mapper constructions
- **Multi-scale Approaches**: Use multiple parameter settings simultaneously


**Practical Guidelines**:
1. **Filter Function Selection**:
   - Density-based: $f(x) = \frac{1}{k} \sum_{i=1}^k d(x, x_i^{nn})$
   - Eccentricity: $f(x) = \sum_{y \in X} d(x,y)$
   - Coordinate projections: $f(x) = x_j$ for dimension $j$



