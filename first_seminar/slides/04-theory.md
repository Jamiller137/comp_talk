
**Uniform Manifold Approximation and Projection**

Three key theoretical components:
1. Manifold approximation with uniform data distribution
2. Fuzzy topological representation via simplicial sets  
3. Optimization of low-dimensional embeddings


## The Core Problem

**Given:** Data $X = \{x_1, \ldots, x_N\}$ assumed to lie on manifold $ M $

**Challenge:** Real data is rarely uniformly distributed on the manifold when viewed in the ambient space

**Solution:** Find a Riemannian metric such that data appears approximately uniform


## Motivation:

<div class="uiowa-logo">
    <img src="images/ellipse_rips_balls_comparison.png" alt="University of Iowa" style="max-width: 100%;">
</div>


## Geodesic Distance

- Let $(M, g)$ be a Riemannian manifold in $\mathbb{R}^n$.

If (locally) $g$ is a constant diagonal matrix in ambient coordinates, then in a ball $B \subseteq U$ centered at $p \in M$ with volume $\frac{\pi^{n/2}}{\Gamma(n/2+1)}$ w.r.t. $g$:

- The geodesic distance from $p$ to any $q \in B$ is $\frac{1}{r}d_{\mathbb{R}^n}(p,q)$

where $r$ is the radius in ambient space.


## Construct Local Metric

- For each datapoint $x_i$, define a local extended-pseudo-metric:
    - Use the distance to $k$-th nearest neighbor to normalize the unit ball about the datapoint
    - Ensures uniform distribution assumption locally


**Result:** Family of incompatible metric spaces $\{(X, d_i)\}_{i=1}^N$

**Next step:** Convert to fuzzy simplicial sets for merging


## Technical Details:


## Category Theory Prerequisites

**Definition:** The category $\Delta$ has:
- Objects: finite ordered sets $[n] = \{1, \ldots, n\}$
- Morphisms: order-preserving maps


## Simplicial Sets
A simplicial set is a functor $X: \Delta^{op} \to \textbf{Sets}$

Elements $X([n])$ are called $n$-simplices of $X$.


## Extended-Pseudo-Metric Spaces

**Definition:** An extended-pseudo-metric space $(X,d)$ has:
1. $d(x,y) \geq 0$, and $x = y \implies d(x,y) = 0$
2. $d(x,y) = d(y,x)$
3. $d(x,z) \leq d(x,y) + d(y,z)$ or $d(x,z) = \infty$

**$\textbf{FinEPMet}$:** Finite extended-pseudo-metric spaces with non-expansive maps (contractions).


## Fuzzy Sets
Let $I = (0,1] \subseteq \mathbb{R}$ with topology given by intervals $[0,a)$ for $a \in (0,1]$.

**Definition:** A fuzzy set is a presheaf $P$ on $I$ such that all maps $P(a \leq b)$ are injections.

**$\textbf{Fuzz}$:** Full subcategory of sheaves on $I$ spanned by fuzzy sets.


## Fuzzy Simplicial Sets

**Definition:** The category $\textbf{sFuzz}$ of fuzzy simplicial sets has:
- Objects: functors $\Delta^{op} \to \textbf{Fuzz}$  
- Morphisms: natural transformations

**Alternative view:** Fuzzy simplicial set = sheaf over $\Delta \times I$


## The Adjoint Functors

**FinReal: $\textbf{Fin-sFuzz} \to \textbf{FinEPMet}$**

$$\text{FinReal}(\Delta^n_{<a}) = (\{x_1, \ldots, x_n\}, d_a)$$

where $d_a(x_i, x_j) = \begin{cases} -\log(a) & \text{if } i \neq j \newline 0 & \text{otherwise} \end{cases}$


## The Adjunction

**Theorem 1:** The functors 
- $\text{FinReal}: \textbf{Fin-sFuzz} \to \textbf{FinEPMet}$
- $\text{FinSing}: \textbf{FinEPMet} \to \textbf{Fin-sFuzz}$

form an adjunction with FinReal as left adjoint.

**FinSing** defined by: $$([n], [0,a)) \mapsto \text{hom}\_{\textbf{FinEPMet}}(\text{FinReal}(\Delta^n_{<a}), Y)$$


## End Technical Details


## Fuzzy Topological Representation

$X = \{X_1, \ldots, X_N\}$, the fuzzy topological representation:

$$\bigcup_{i=1}^n \text{FinSing}((X, d_i))$$

where $$d_i(X_j, X_k) = \begin{cases} d_M(X_j, X_k) - \rho & \text{if } i = j \text{ or } i = k \newline \infty & \text{otherwise} \end{cases}$$

The fuzzy union merges incompatible local metric spaces into global structure.



## Optimizing Low-Dimensional Representation

### Cross Entropy

**Definition 10:** Cross entropy of fuzzy sets $(A, \mu)$ and $(A, \nu)$:

$$C((A,\mu), (A,\nu)) = \sum_{a \in A}  \mu(a) \log \frac{\mu(a)}{\nu(a)}$$ 
$$ + (1-\mu(a)) \log \frac{1-\mu(a)}{1-\nu(a)} $$


- **Objective:** Minimize cross entropy between:
    - High-dimensional fuzzy simplicial set representation
    - Low-dimensional fuzzy simplicial set representation (graph embedding)
- **Implementation:** Stochastic gradient descent with differentiable approximations
