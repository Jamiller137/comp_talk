## Topological Data Analysis

The use of tools from topology to extract and study data 'shape' across scales.



## Three Themes

1. Topologification

2. Persistence and Stability

3. Visualization Methods



## Constructing Topological Spaces from Data

**Problem**: Raw data lacks inherent topological structure.

**Manifold Hypothesis**: We assume dataset is sampled from a manifold $M$


## General Framework:
- Given point cloud $X = \\{x_1, x_2, \ldots, x_n\\} \subset \mathbb{R}^d$
with Manifold Hypothesis.

- Define a distance threshold $\epsilon$
- Build simplicial complex which approximates the nerve of $M$.


## Čech Complex

**Definition**: For point cloud $X$ and threshold $\epsilon \in \mathbb{R}$:

$$\\check{C}\_\\epsilon(X) = \left\\{\sigma \subseteq X : \bigcap_{x \in \sigma} B\left(x, \frac{\epsilon}{2}\right) \neq \emptyset \right\\}$$


**Construction**:
- Create an open cover of our sampling $X$ of the manifold $M$ with balls of radius $\frac{\epsilon}{2}$
- $\\check{C}_\epsilon (X)$ is then the nerve of this open cover which approximates the nerve of $M$.

**Trade-off**: Accurate but computationally expensive


## Vietoris-Rips Complex

**Definition**: For point cloud $X$ in a metric space and a given threshold $\epsilon \in \mathbb{R}^{\geq 0}$:

$$VR_\epsilon(X) = \\{\sigma \subseteq X : \text{diam}(\sigma) \leq \epsilon\\}$$


**Construction**:

$$\{(x_{i_0}, x_{i_1}, \ldots, x_{i_k})\} \in VR_\epsilon(X)$$
if all pairwise distances satisfy:
  $$d(x_{i_j}, x_{i_k}) \leq \epsilon$$



**Properties**:
- $VR_\epsilon(X)$ contains $\\check{C}_\epsilon (X)$ as a subcomplex and is easier to compute
- The elements of $X$ are the vertices of $VR_\epsilon(X)$
- 1-skeleton (vertices + edges) are the same for Rips and Cech complex.
- Compared to $\check{C}_\epsilon (X)$ may include additional "hollow" simplices: (reword this)

$$\sigma \in \check{C}{\epsilon}(X) \iff \bigcap_{x_{k} \in \sigma} B\left(x_{k}, \frac{\epsilon}{2}\right) \neq \emptyset $$


## Show triangle diagram Rips vs Cech


## Witness Complex

**Definition**: Given landmarks $L \subset X$ and witnesses $W \subset X$:

$\sigma \subseteq L$ is included as a simplex in $\text{Wit}(X, L, W)$ if it is 'witnessed' by some point $w \in W$.

$$d(w, l) \leq d(w, L \setminus \sigma) + \epsilon$$
for all $l \in \sigma$


**Idea**:

Witnesses "see" nearby landmark configurations 

- 'Strong' if $\epsilon = 0$

**Note**: Many other techniques can be derived from Witness Complexes (verify :)


## Add figure


## Curse of Dimensionality

Give dimension curse example and describe why mapper would be useful

- The witness complex is useful since it reduces the number of comparisons by just checking $L$ and $W$.
- Mapper is useful since it reduces dimension with filter and uses cluster intersection instead of pairwise distance comparisons across $X$

Remove the above bullet:

- Mapper uses a covering scheme. The filter function reduces computation for the cover_scheme.


## Money Ball joke

Billy Beane: Guys, you're still trying to replace Giambi [$\check{C}_{\epsilon}(X)$]. I told you we can't do it, and we can't do it. Now, what we might be able to do is re-create him. Re-create him in the aggregate [TDA-Mapper].

Grady Fuson: The what?


## Mapper Complex

**Mapper Algorithm** (Singh, Mémoli, Carlsson):

Given:
Dataset $X$ with a metric

A filter function $f:X \to \mathbb{R}^{m}$

A cover $U$ of $f[X]$

A clustering method on $X$


Make this slide better formatted (not centered or something)


## Construction
1. Pullback each cover element $U_i$ to $\bar{U}_i = f^{-1}[U_i] \subseteq X$
2. Cluster points in each $\bar{U}_i$
3. Build the nerve from the set of all resulting clusters.


## Add a picture with filter function

And more stuff
