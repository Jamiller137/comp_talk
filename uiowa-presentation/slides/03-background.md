## Topological Data Analysis
The use of topology to extract and study the shape of data.

Relies on the *Manifold Hypothesis*
- Naturally occuring datasets lie along manifolds inside the ambient space.


## Three Themes

1. Topologification*

2. Persistence and Stability

3. Visualization Methods



## Constructing Topological Spaces from Data

**Problem**: Raw data lacks inherent topological structure.

**Topologification**: Methods for producing topological spaces from point-cloud data


## General Framework:
Given a point-cloud $$X = \\{x_1, x_2, \ldots, x_n\\} \subset M^{\oplus \delta} \subset \mathbb{R}^d$$

Build simplicial complex which approximates the topology of $M$.


## Simplicial Complex:
A simplicial complex is a family of sets which is closed under taking subsets.
#### Geometric Realization
<div class="uiowa-logo">
    <img src="images/Simplicial_complex_example.svg.png" alt="University of Iowa" style="height: 250px;">
</div>


## Nerve Complex:
Given a family of sets (open cover) $\mathcal{U} = \\{U_{i} \\}_{i \in I}$. 

The nerve of $\mathcal{U}$ is a simplicial complex
which records intersection information.

$$ \sigma = \\{ i_{0}, \dots, i_{k}\\} \in N(\mathcal{U}) \iff \bigcap_{n=0}^{n=k} U_{i_{n}} \neq \emptyset$$


## Nerve Theorem:

Given an open cover $\mathcal{U}$ of a manifold $M$ when is the topology of $N(\mathcal{U})$
equivalent to the topology of $M$?

The two are equivalent if each pairwise intersection $U_i \cap U_j$ is either empty or contractible.


## Čech Complex

**Definition**: For point cloud $X$ and threshold $\epsilon \in \mathbb{R}$:

$$\\check{C}\_\\epsilon(X) = \left\\{\sigma \subseteq X : \bigcap_{x \in \sigma} B\left(x, \frac{\epsilon}{2}\right) \neq \emptyset \right\\}$$


**Construction**:
1. Create an open cover of our sampling $X$ with balls of radius $\frac{\epsilon}{2}$ centered at each $x \in X$.
2. $\\check{C}_\epsilon (X)$ is then the nerve of this open cover which approximates the nerve of $M$.

$$ \sigma \in \check{C}\_{\epsilon}(X) \iff \bigcap_{x_{k} \in \sigma} B(x_{k}, \frac{\epsilon}{2}) \neq \emptyset $$
**Note:** Accurate but computationally expensive


## Image of Cech Complex
<!-- Čech complex from three balls (nerve is the filled triangle) -->
<svg viewBox="0 0 600 450" xmlns="http://www.w3.org/2000/svg" style="max-width: 90%; height: auto;">
  <defs>
    <style>
      .label { font: 600 16px system-ui, -apple-system, Segoe UI, Roboto, sans-serif; fill: currentColor; }
      .point { fill: currentColor; }
      .edge { stroke: purple; stroke-width: 3; stroke-linecap: round; stroke-opacity: 0.7; }
    </style>
  </defs>

  <!-- Cover balls U1, U2, U3 -->
  <circle cx="200" cy="300" r="105" fill="#4e79a7" fill-opacity="0.18"/>
  <circle cx="400" cy="300" r="105" fill="#f28e2b" fill-opacity="0.18"/>
  <circle cx="300" cy="150" r="105" fill="#59a14f" fill-opacity="0.18"/>

  <!-- Čech complex (nerve): filled 2-simplex -->
  <polygon points="200,300 400,300 300,150" fill="none" opacity="1" stroke="gray" stroke-width="2" stroke-opacity="1"/>

  <!-- 0-simplices (centers) -->
  <circle cx="200" cy="300" r="5.5" class="point"/>
  <circle cx="400" cy="300" r="5.5" class="point"/>
  <circle cx="300" cy="150" r="5.5" class="point"/>

  <!-- Labels -->
  <text x="188" y="322" class="label">U1</text>
  <text x="408" y="322" class="label">U2</text>
  <text x="312" y="140" class="label">U3</text>
  <text x="308" y="260" class="label">Čech complex</text>
  <text x="308" y="278" class="label" style="font-weight: 400; opacity: 0.8;">(nerve of {U1, U2, U3})</text>
</svg>


## Vietoris-Rips Complex

**Definition**: For point cloud $X$ in a metric space and a given threshold $\epsilon \in \mathbb{R}^{\geq 0}$:

$$VR_\epsilon(X) = \\{\sigma \subseteq X : \text{diam}(\sigma) \leq \epsilon\\}$$


**Construction**:

$$\sigma = \{(x_{i_0}, x_{i_1}, \ldots, x_{i_k})\} \in VR_\epsilon(X)$$
if all pairwise distances satisfy:
  $$d(x_{i_j}, x_{i_k}) \leq \epsilon$$


## Image of Rips Complex:
<svg viewBox="0 0 600 450" xmlns="http://www.w3.org/2000/svg" style="max-width: 90%; height: auto;">
  <defs>
    <style>
      .label { font: 600 16px system-ui, -apple-system, Segoe UI, Roboto, sans-serif; fill: currentColor; }
      .point { fill: currentColor; }
      .edge { stroke: purple; stroke-width: 3; stroke-linecap: round; stroke-opacity: 0.7; }
    </style>
  </defs>

  <!-- Cover balls U1, U2, U3 -->
  <circle cx="200" cy="300" r="105" fill="#4e79a7" fill-opacity="0.18"/>
  <circle cx="400" cy="300" r="105" fill="#f28e2b" fill-opacity="0.18"/>
  <circle cx="300" cy="150" r="105" fill="#59a14f" fill-opacity="0.18"/>

  <!-- Čech complex (nerve): filled 2-simplex -->
  <polygon points="200,300 400,300 300,150" fill="purple" opacity="0.7" stroke="gray" stroke-width="2" stroke-opacity="1"/>

  <!-- 0-simplices (centers) -->
  <circle cx="200" cy="300" r="5.5" class="point"/>
  <circle cx="400" cy="300" r="5.5" class="point"/>
  <circle cx="300" cy="150" r="5.5" class="point"/>

  <!-- Labels -->
  <text x="188" y="322" class="label">U1</text>
  <text x="408" y="322" class="label">U2</text>
  <text x="312" y="140" class="label">U3</text>
  <text x="308" y="260" class="label">Čech complex</text>
  <text x="308" y="278" class="label" style="font-weight: 400; opacity: 0.8;">(nerve of {U1, U2, U3})</text>
</svg>


**Properties**:
- $\\check{C}_\epsilon (X) \subseteq VR_\epsilon(X)$ as a subcomplex
- 1-skeleton (vertices + edges) are equal for Rips and Cech complex.
- The Rips Complex may include additional "hollow" simplices:


## Witness Complex

**Definition**: Given landmarks and witnesses $$L, W \subset X$$

$\sigma \subseteq L$ is included as a simplex in $\text{Wit}(L, W)$ if it is 'witnessed' by some point $w \in W$.


## A Partial Witness Complex:
<!-- Witness complex with one witness and a dotted blue witness ball -->
<svg viewBox="0 0 600 450" xmlns="http://www.w3.org/2000/svg" style="max-width: 90%; height: auto;">
  <defs>
    <style>
      .label { font: 600 16px system-ui, -apple-system, Segoe UI, Roboto, sans-serif; fill: currentColor; }
      .landmark { fill: black; }
      .witness { fill: #f28e2b; stroke: black; stroke-width: 1.5; }
      .edge { fill: green; stroke: black; opacity: 0.3; stroke-width: 5; stroke-linejoin: round; vector-effect: non-scaling-stroke; }
      .w-circle { fill: none; stroke: #1f77b4; stroke-width: 3; stroke-dasharray: 8 8; vector-effect: non-scaling-stroke; stroke-opacity: 0.5; }
    </style>
  </defs>

  <!-- One witness -->
  <circle cx="300" cy="240" r="7" class="witness"/>
  <text x="312" y="244" class="label" style="font-weight: 500;">w</text>
  <circle cx="230" cy="120" r="7" class="witness"/>
  <text x="242" y="124" class="label" style="font-weight: 500;">w'</text>

  <!-- Dotted blue circle centered at the witness; radius chosen to include only L1, L2, L3 -->
  <!-- Distances from w(300,240): L1≈116.6, L2≈116.6, L3=90; others below are >120 -->
  <circle cx="300" cy="240" r="120" class="w-circle"/>
  <circle cx="230" cy="120" r="100" class="w-circle"/>

  <!-- Landmarks (three inside the witness circle forming the face) -->
  <circle cx="200" cy="300" r="6" class="landmark"/>
  <circle cx="400" cy="300" r="6" class="landmark"/>
  <circle cx="300" cy="150" r="6" class="landmark"/>
  <text x="188" y="322" class="label">L1</text>
  <text x="408" y="322" class="label">L2</text>
  <text x="312" y="150" class="label">L3</text>

  <!-- Additional landmarks (all outside the witness circle) -->
  <circle cx="450" cy="340" r="6" class="landmark"/>
  <circle cx="460" cy="120" r="6" class="landmark"/>
  <circle cx="180" cy="180" r="6" class="landmark"/>
  <text x="458" y="356" class="label">L6</text>
  <text x="468" y="116" class="label">L5</text>
  <text x="168" y="170" class="label">L4</text>

  <!-- Witness complex edges for {L1, L2, L3}; face is invisible (fill: none) -->
  <polygon points="200,300 400,300 300,150" class="edge"/>

  <line x1="180" y1="180" x2="300" y2="150" class="edge"/>    

  <!-- Caption -->
  <text x="308" y="300" class="label" style="font-weight: 500;">Witness complex</text>
  <text x="308" y="319" class="label" style="font-weight: 400; opacity: 0.8;">Dotted circle includes only {L1, L2, L3}</text>
</svg>


## $\sigma \subset L$ witnessed by $w$ if:

$$d(w, l) \leq d(w, L \setminus \sigma) + \epsilon$$
for all $l \in \sigma$


## Curse of Dimensionality
In high dimensions, geometric intuition breaks down 
and common computations are exponentially more expensive.

$$\frac{V_\text{hypersphere}}{V_\text{hypercube}} = \frac{\pi^{d/2}}{d2^{d-1}\Gamma(d/2)} \to 0 \text{ as } d \to \infty $$


## Mapper

*"You're still trying to replace $\check{C}_{\epsilon}(X)$. I told you we can't do it. Now, what we might be able to do is re-create it in the aggregate."*

<div class="uiowa-logo">
    <img src="images/brad.jpg" alt="University of Iowa" style="height: 250px;">
</div>

*(Singh, Mémoli, Carlsson)*


## Mapper Ingredients

<div style="text-align: left;">
    <ol>
      <li>A dataset $X$ with a metric</li>
        <br></br>
      <li>A filter function $f:X \to \mathbb{R}^{m}$</li>
        <br></br>
      <li>An open cover $\mathcal{U}$ of $f[X]$</li>
        <br></br>
      <li>A clustering method on $X$</li>
    </ol>
  </div>


## Construction
Pullback each cover element $$\bar{U}_i = f^{-1}[U_i] \subseteq X$$
$$\downarrow$$

Cluster points in each $\bar{U}_i$
$$\downarrow$$
Build the nerve from the set of all resulting clusters.


## Add a picture with filter function

And more stuff
