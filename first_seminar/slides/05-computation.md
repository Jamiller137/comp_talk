## Practical Algorithm


## UMAP's Core Assumptions

1. **Manifold existence**: Data lies on a manifold where it would be uniformly distributed
2. **Local connectivity**: The underlying manifold is locally connected  
3. **Topological preservation**: Primary goal is preserving topological structure



## Phase 1: Graph Construction
- Build weighted $k$-neighbor graph
- Transform edge weights based on local distances
- Handle asymmetry (averaging)


## Phase 2: Graph Layout  
- Define objective function preserving graph characteristics
- Optimize low-dimensional representation via entropy
- Use force-directed layout with attractive/repulsive forces


## 3.1 Graph Construction

### Input
- Dataset: $X = \{x_1, ..., x_N}$
- Metric: $d: X×X \to \mathbb{R}_{\geq 0}$
- Hyperparameter: $k$ (number of neighbors)

### Step 1: Find k-Nearest Neighbors


## Local Parameters

### Distance to Nearest Neighbor ($\rho_i$)

**Purpose**: To ensure local connectivity (at least one edge with weight 1)

### Normalization Factor ($\sigma_i$)
Set $σᵢ$ such that: $\sum \exp(−max(0, d(x_i,x_j) − \rho_i)/\sigma_i) = \log_2 (k)$

**Purpose**: Defines local Riemannian metric normalization


## Directed Graph Construction

### Weighted Directed Graph Ḡ = (V, E, w)
- **Vertices**: $V = X$ (the dataset points)
- **Edges**: $E = {(xᵢ, xᵢⱼ) | 1 ≤ j ≤ k, 1 ≤ i ≤ N}$
- **Weights**: $w((xᵢ, xᵢⱼ)) = exp(−max(0, d(xᵢ,xᵢⱼ) − ρᵢ)/σᵢ)$

- Weight ≈ probability that edge exists


## Symmetrization Process

### Problem: 
Asymmetric k-neighbor graph


### Solution: 
Probabilistic t-conorm
$$B = A + Aᵀ − A ∘ Aᵀ$$

Where:
- $A =$ weighted adjacency matrix of Ḡ  
- $∘ =$ Hadamard (pointwise) product
- $Bᵢⱼ $= probability at least one directed edge exists


## 3.2 Graph Layout

- **Attractive forces**: Along existing edges
- **Repulsive forces**: Between all vertices
- **Optimization**: Non-convex, converges to local minima
- **Annealing**: Gradually decrease force magnitudes




## Algorithm Summary

1. **k-NN Search**: Find nearest neighbors for each point
2. **Local Metrics**: Compute ρᵢ and σᵢ for each point  
3. **Edge Weights**: Calculate using exponential kernel
4. **Symmetrization**: Apply probabilistic t-conorm
5. **Force Layout**: Optimize using attractive/repulsive forces
6. **Convergence**: Simulated annealing approach
