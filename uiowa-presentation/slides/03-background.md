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


## Mapper
<svg xmlns="http://www.w3.org/2000/svg" viewBox="100 100 300 300" style="max-width: 60%; height: auto;">
  <rect x="130.889" y="100" width="60.7" height="177.157" style="stroke: rgb(0, 0, 0); fill: rgba(255, 178, 178, 0.525);"></rect>
  <rect x="183.15" y="100.085" width="60.7" height="177.157" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgba(255, 238, 178, 0.525);"></rect>
  <rect x="233.793" y="100.085" width="63.215" height="177.157" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgba(191, 255, 178, 0.525);"></rect>
  <rect x="283.359" y="100.085" width="60.7" height="177.157" style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgba(178, 255, 236, 0.525);"></rect>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" cx="190.153" cy="133.744" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="212.78" cy="127.923" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="198.593" cy="119.74" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="184.945" cy="148.085" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="170.22" cy="139.424" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="169.501" cy="157.983" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 119.834px 185.69px 0px;" cx="119.834" cy="185.69" rx="2.024" ry="2.155" transform="matrix(0, -1, 1, 0, 37.574773, -8.922374)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 144.167px 179.027px 0px;" cx="144.167" cy="179.027" rx="2.024" ry="2.155" transform="matrix(0, -1, 1, 0, 7.045897, -23.517649)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 128.91px 169.66px 0px;" cx="128.91" cy="169.66" rx="2.024" ry="2.155" transform="matrix(0, -1, 1, 0, 13.592502, -0.821515)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 114.234px 202.105px 0px;" cx="114.234" cy="202.105" rx="2.024" ry="2.155" transform="matrix(0, -1, 1, 0, 28.627652, -10.659241)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 98.398px 192.191px 0px;" cx="98.398" cy="192.191" rx="2.024" ry="2.155" transform="matrix(0, -1, 1, 0, 55.71756, 14.439462)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 97.625px 213.435px 0px;" cx="97.625" cy="213.435" rx="2.024" ry="2.155" transform="matrix(0, -1, 1, 0, 67.625085, -18.614576)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -292.454px -245.718px 0px;" cx="-292.45" cy="-245.72" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 594.037367, 398.218823)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -268.121px -252.381px 0px;" cx="-268.12" cy="-252.38" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 575.90074, 426.139833)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -283.378px -261.748px 0px;" cx="-283.38" cy="-261.75" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 599.868363, 422.177967)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -298.053px -229.303px 0px;" cx="-298.05" cy="-229.3" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 584.373289, 376.911162)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -313.89px -239.217px 0px;" cx="-313.89" cy="-239.22" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 609.428726, 372.990988)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -314.663px -217.973px 0px;" cx="-314.66" cy="-217.97" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 590.446613, 351.070528)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 255.791px 121.739px 0px;" cx="255.791" cy="121.739" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 254.713px 138.527px 0px;" cx="254.713" cy="138.527" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 208.918px 142.153px 0px;" cx="208.918" cy="142.153" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 272.133px 112.796px 0px;" cx="272.133" cy="112.796" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 224.004px 118.645px 0px;" cx="224.004" cy="118.645" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 236.575px 129.106px 0px;" cx="236.575" cy="129.106" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -301.916px -218.692px 0px;" cx="-301.91" cy="-218.69" rx="2.155" ry="2.024" transform="matrix(-1, 0, 0, -1, 603.832036, 437.384712)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -279.29px -224.515px 0px;" cx="-279.29" cy="-224.51" rx="2.155" ry="2.024" transform="matrix(-1, 0, 0, -1, 558.579367, 449.029923)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -293.477px -232.697px 0px;" cx="-293.48" cy="-232.7" rx="2.155" ry="2.024" transform="matrix(-1, 0, 0, -1, 586.953964, 465.393947)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -307.123px -204.352px 0px;" cx="-307.12" cy="-204.35" rx="2.155" ry="2.024" transform="matrix(-1, 0, 0, -1, 614.246334, 408.704338)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -321.849px -213.014px 0px;" cx="-321.85" cy="-213.01" rx="2.155" ry="2.024" transform="matrix(-1, 0, 0, -1, 643.697631, 426.028712)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -309.28px -191.079px 0px;" cx="-309.27" cy="-191.08" rx="2.155" ry="2.024" transform="matrix(-1, 0, 0, -1, 618.559053, 382.158626)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 51.575029, -33.028619)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 294.128px 198.662px 0px;" cx="294.128" cy="198.662" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 33.437852, -5.107278)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 278.871px 189.295px 0px;" cx="278.871" cy="189.295" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 57.4053, -9.069491)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 331.531px 170.305px 0px;" cx="331.531" cy="170.305" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, -67.029948, 68.074271)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 325.931px 186.72px 0px;" cx="325.931" cy="186.72" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, -93.934632, 56.552769)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 310.095px 176.806px 0px;" cx="310.095" cy="176.806" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, -68.879551, 52.631807)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 309.322px 198.05px 0px;" cx="309.322" cy="198.05" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, -87.861429, 30.712599)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 201.467px 217.402px 0px;" cx="201.467" cy="217.402" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 260.371px 224.741px 0px;" cx="260.37" cy="224.741" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 205.238px 237.816px 0px;" cx="205.238" cy="237.816" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 185.844px 203.735px 0px;" cx="185.844" cy="203.735" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 169.681px 214.308px 0px;" cx="169.681" cy="214.308" rx="2.155" ry="2.024"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 182.251px 224.768px 0px;" cx="182.251" cy="224.768" rx="2.155" ry="2.024"></ellipse>
  <rect x="100" y="270.746" width="284.466" height="1.687" style="stroke: rgb(0, 0, 0);"></rect>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="387.022" y="291.683" transform="matrix(0.775986, 0, 0, 0.565405, 88.811531, 110.787735)">x</text>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(255, 0, 0);" cx="151.676" cy="350.564" rx="4.265" ry="4.007"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 177, 0);" cx="210.267" cy="304.462" rx="4.265" ry="4.007"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 177, 0);" cx="209.818" cy="395.993" rx="4.265" ry="4.007"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(51, 253, 0);" cx="261.224" cy="304.25" rx="4.265" ry="4.007"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(51, 253, 0);" cx="260.776" cy="395.781" rx="4.265" ry="4.007"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(0, 255, 247);" cx="317.57" cy="347.823" rx="4.265" ry="4.007"></ellipse>
  <path style="stroke: rgb(0, 0, 0); stroke-linecap: square; fill: rgb(255, 183, 0);" d="M 155.044 347.823 L 207.124 306.908"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" d="M 214.307 304.377 L 257.408 304.377"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" d="M 264.142 393.378 L 315.325 351.197"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" d="M 205.328 394.643 L 154.594 353.728"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" d="M 314.876 344.027 L 264.591 305.643"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" d="M 214.307 395.908 L 256.51 395.908"></path>
</svg>
