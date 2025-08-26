## Topological Data Analysis
The use of topology to extract and study the shape of data.

Relies on the *Manifold Hypothesis*
- Naturally occuring datasets lie along manifolds inside the ambient space.


## Three Themes

1. Simplicial Approximation

2. Persistence and Stability

3. Visualization Methods


## Constructing Topological Spaces from Data

**Problem**: Raw data lacks inherent topological structure.

**Simplicial Approximation**: Methods for producing topological spaces from point-cloud data


## General Framework:
Given a point-cloud $X = \\{\vec{x}_1, \vec{x}_2, \ldots, \vec{x}_n\\} \subset M = \bigcup M_\{i\}^\{d_\{i\}\} \subset \mathbb{R}^d$

- Build a simplicial complex which approximates the topology of $M$.


## Simplicial Complex:
- A simplicial complex is a family of sets which is closed under taking subsets:

<div style="text-align: left;">
        $\text{Vertices} = \Delta^{0} = \{ 1\}, \{ 2\}, \{ 3\}, \{ 4\}, \{ 5\}$
        $\text{Edges} = \Delta^{1} = \{ 1, 2\}, \{ 2, 3\}, \{ 1, 3\}, \{ 1, 4\}$
        $\text{Faces} = \Delta^{2} =  \{ 1, 2, 3\}$
</div>

#### Geometric Realization
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -20 252.323 233.641" style="max-width: 30%; height: auto;">
  <text style="fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; white-space: pre; text-rendering: geometricprecision;" x="111.86" y="14.938">1</text>
  <text style="fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; white-space: pre; text-rendering: geometricprecision;" x="-10" y="74.03">2</text>
  <text style="fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; white-space: pre; text-rendering: geometricprecision;" x="47.062" y="143.046">3</text>
  <text style="fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; white-space: pre; text-rendering: geometricprecision;" x="153.87" y="145.633">4</text>
  <text style="fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; white-space: pre; text-rendering: geometricprecision;" x="199.802" y="60.786">5</text>
  <path style="stroke: rgb(0, 0, 0); fill: rgb(180, 230, 255); stroke-width: 2px; shape-rendering: geometricprecision;" d="M 101.579 13.408 L 19.122 69.575 L 39.294 126.338 L 101.579 13.408 Z"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; shape-rendering: geometricprecision;" d="M 100.981 15.201 L 148.185 128.131"></path>
  <ellipse style="stroke: rgb(0, 0, 0); shape-rendering: geometricprecision;" cx="37.465" cy="124.984" rx="5.941" ry="5.941"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; shape-rendering: geometricprecision;" cx="147.929" cy="124.984" rx="5.941" ry="5.941"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; shape-rendering: geometricprecision;" cx="189.081" cy="49.1" rx="5.941" ry="5.941"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; shape-rendering: geometricprecision;" cx="19.222" cy="69.814" rx="5.941" ry="5.941"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; shape-rendering: geometricprecision;" cx="100.329" cy="14.52" rx="5.941" ry="5.941"></ellipse>
</svg>


## Nerve Complex:
The nerve of a family of sets $\mathcal{U}$ is a simplicial complex
which records intersection information.

$ \sigma = \\{ i_{0}, \dots, i_{k}\\} \in N(\mathcal{U}) \iff \bigcap_{n=0}^{n=k} U_{i_{n}} \neq \emptyset$
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 10 500 200" style="max-width: 95%; height: auto;">
  <g style="" transform="matrix(0.5408, 0, 0, 0.5408, 10.78545, -39.983433)">
    <path style="stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0.39);" d="M 143.165 277.127 L 110.899 277.725 C 110.899 277.725 89.484 133.723 244.742 133.126 C 400 132.529 388.743 300 377.39 286.687 C 366.037 273.374 344.527 286.09 344.527 286.09 C 350.984 121.612 141.373 136.114 143.165 277.127 Z"></path>
    <path style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgba(119, 255, 150, 0.39); transform-origin: 245.338px 311.186px 0px;" d="M 141.904 378.03 L 109.638 378.628 C 109.638 378.628 88.223 234.626 243.481 234.029 C 398.739 233.432 387.482 400.903 376.129 387.59 C 364.776 374.277 343.267 386.993 343.267 386.993 C 349.724 222.515 140.112 237.017 141.904 378.03 Z" transform="matrix(-1, 0, 0, -1, 0, 0)"></path>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="238.766" y="125.693">U1</text>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="239.412" y="416.647">U2</text>
    <ellipse style="stroke-width: 5px; stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0);" cx="247.132" cy="263.086" rx="120.1" ry="112.034"></ellipse>
  </g>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(255, 0, 0); transform-origin: 168.26px 258.604px 0px;" cx="168.26" cy="258.604" rx="3.555" ry="3.555" transform="matrix(0, 1, -1, 0, -25.065055, -200.041695)"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(0, 255, 0); transform-origin: 321.223px 258.803px 0px;" cx="321.223" cy="258.803" rx="3.554" ry="3.554" transform="matrix(0, 1, -1, 0, -178.135728, -117.518341)"></ellipse>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 142.926px 100.248px 0px;" d="M 104.796 100.086 L 181.055 100.409" transform="matrix(0, 1, -1, 0, 0, 0)"></path>
  <g transform="matrix(0.5408, 0, 0, 0.5408, 192.710846, -39.983376)" style="">
    <path style="stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0.39);" d="M 143.165 277.127 L 110.899 277.725 C 110.899 277.725 89.484 133.723 244.742 133.126 C 400 132.529 388.743 300 377.39 286.687 C 366.037 273.374 344.527 286.09 344.527 286.09 C 350.984 121.612 141.373 136.114 143.165 277.127 Z"></path>
    <path style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgba(119, 255, 150, 0.39);" d="M 141.904 378.03 L 109.638 378.628 C 109.638 378.628 105.726 299.755 144.891 262.112 C 184.056 224.469 293.617 238.379 294.214 240.004 C 294.811 241.629 269.773 269.88 269.773 269.88 C 295.35 253.585 127.077 235.224 141.904 378.03 Z" transform="matrix(-1, 0, 0, -1, 490.675995, 622.372009)"></path>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="238.766" y="125.693">U1</text>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="344.037" y="394.025">U2</text>
    <path style="stroke: rgb(0, 0, 0); fill: rgba(135, 95, 255, 0.467);" d="M 101.538 251.036 C 90.544 339.994 226.062 417.117 235.979 386.855 L 240.759 356.198 C 228.973 383.237 114.033 291.429 149.339 251.036 L 101.538 251.036 Z"></path>
    <ellipse style="stroke-width: 5px; stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0);" cx="247.132" cy="263.086" rx="120.1" ry="112.034"></ellipse>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="109.213" y="369.527">U3</text>
  </g>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 343.206px 99.472px 0px;" d="M 302.653 114.013 L 383.76 84.931" transform="matrix(0, 1, -1, 0, 0, 0)"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 307.274px 93.052px 0px;" d="M 272.537 73.502 L 342.012 112.602" transform="matrix(0, 1, -1, 0, 0, 0)"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 323.43px 134.575px 0px;" d="M 316.16 165.757 L 330.701 103.392" transform="matrix(0, -1, 1, 0, 0, 0)"></path>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(255, 0, 0); transform-origin: 506.573px 260.397px 0px;" cx="506.573" cy="260.397" rx="3.555" ry="3.555" transform="matrix(0, 1, -1, 0, -179.416838, -203.094782)"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(0, 255, 58); transform-origin: 659.536px 260.596px 0px;" cx="659.536" cy="260.596" rx="3.554" ry="3.554" transform="matrix(0, 1, -1, 0, -301.143116, -119.601878)"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(145, 107, 255); transform-origin: 573.574px 331.222px 0px;" cx="573.574" cy="331.222" rx="3.554" ry="3.554" transform="matrix(0, 1, -1, 0, -284.396952, -205.411367)"></ellipse>
</svg>


## Nerve Theorem:

Given an open cover $\mathcal{U}$ of a manifold $M$ when is the topology of $N(\mathcal{U})$
equivalent to the topology of $M$?

The two are equivalent if each pairwise intersection $U_i \cap U_j$ is either empty or contractible.
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 10 500 200" style="max-width: 95%; height: auto;">
  <g style="" transform="matrix(0.5408, 0, 0, 0.5408, 10.78545, -39.983433)">
    <path style="stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0.39);" d="M 143.165 277.127 L 110.899 277.725 C 110.899 277.725 89.484 133.723 244.742 133.126 C 400 132.529 388.743 300 377.39 286.687 C 366.037 273.374 344.527 286.09 344.527 286.09 C 350.984 121.612 141.373 136.114 143.165 277.127 Z"></path>
    <path style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgba(119, 255, 150, 0.39); transform-origin: 245.338px 311.186px 0px;" d="M 141.904 378.03 L 109.638 378.628 C 109.638 378.628 88.223 234.626 243.481 234.029 C 398.739 233.432 387.482 400.903 376.129 387.59 C 364.776 374.277 343.267 386.993 343.267 386.993 C 349.724 222.515 140.112 237.017 141.904 378.03 Z" transform="matrix(-1, 0, 0, -1, 0, 0)"></path>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="238.766" y="125.693">U1</text>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="239.412" y="416.647">U2</text>
    <ellipse style="stroke-width: 5px; stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0);" cx="247.132" cy="263.086" rx="120.1" ry="112.034"></ellipse>
  </g>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(255, 0, 0); transform-origin: 168.26px 258.604px 0px;" cx="168.26" cy="258.604" rx="3.555" ry="3.555" transform="matrix(0, 1, -1, 0, -25.065055, -200.041695)"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(0, 255, 0); transform-origin: 321.223px 258.803px 0px;" cx="321.223" cy="258.803" rx="3.554" ry="3.554" transform="matrix(0, 1, -1, 0, -178.135728, -117.518341)"></ellipse>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 142.926px 100.248px 0px;" d="M 104.796 100.086 L 181.055 100.409" transform="matrix(0, 1, -1, 0, 0, 0)"></path>
  <g transform="matrix(0.5408, 0, 0, 0.5408, 192.710846, -39.983376)" style="">
    <path style="stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0.39);" d="M 143.165 277.127 L 110.899 277.725 C 110.899 277.725 89.484 133.723 244.742 133.126 C 400 132.529 388.743 300 377.39 286.687 C 366.037 273.374 344.527 286.09 344.527 286.09 C 350.984 121.612 141.373 136.114 143.165 277.127 Z"></path>
    <path style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgba(119, 255, 150, 0.39);" d="M 141.904 378.03 L 109.638 378.628 C 109.638 378.628 105.726 299.755 144.891 262.112 C 184.056 224.469 293.617 238.379 294.214 240.004 C 294.811 241.629 269.773 269.88 269.773 269.88 C 295.35 253.585 127.077 235.224 141.904 378.03 Z" transform="matrix(-1, 0, 0, -1, 490.675995, 622.372009)"></path>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="238.766" y="125.693">U1</text>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="344.037" y="394.025">U2</text>
    <path style="stroke: rgb(0, 0, 0); fill: rgba(135, 95, 255, 0.467);" d="M 101.538 251.036 C 90.544 339.994 226.062 417.117 235.979 386.855 L 240.759 356.198 C 228.973 383.237 114.033 291.429 149.339 251.036 L 101.538 251.036 Z"></path>
    <ellipse style="stroke-width: 5px; stroke: rgb(0, 0, 0); fill: rgba(255, 119, 119, 0);" cx="247.132" cy="263.086" rx="120.1" ry="112.034"></ellipse>
    <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="109.213" y="369.527">U3</text>
  </g>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 343.206px 99.472px 0px;" d="M 302.653 114.013 L 383.76 84.931" transform="matrix(0, 1, -1, 0, 0, 0)"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 307.274px 93.052px 0px;" d="M 272.537 73.502 L 342.012 112.602" transform="matrix(0, 1, -1, 0, 0, 0)"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px; transform-origin: 323.43px 134.575px 0px;" d="M 316.16 165.757 L 330.701 103.392" transform="matrix(0, -1, 1, 0, 0, 0)"></path>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(255, 0, 0); transform-origin: 506.573px 260.397px 0px;" cx="506.573" cy="260.397" rx="3.555" ry="3.555" transform="matrix(0, 1, -1, 0, -179.416838, -203.094782)"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(0, 255, 58); transform-origin: 659.536px 260.596px 0px;" cx="659.536" cy="260.596" rx="3.554" ry="3.554" transform="matrix(0, 1, -1, 0, -301.143116, -119.601878)"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(145, 107, 255); transform-origin: 573.574px 331.222px 0px;" cx="573.574" cy="331.222" rx="3.554" ry="3.554" transform="matrix(0, 1, -1, 0, -284.396952, -205.411367)"></ellipse>
</svg>


## Applying Nerve Theorem
We know how to construct the nerve from an open cover of a manifold.

**Question:** How do we use the nerve theorem when given a sampling from a manifold?


## Čech Complex

**Construction**:
1. Create an open cover of our sampling $X$ with balls of radius $\frac{\epsilon}{2}$ centered at each $\vec{x} \in X$.
2. $\\check{C}_\epsilon (X)$ is then the nerve of this open cover.

$$ \sigma \in \check{C}\_{\epsilon}(X) \iff \bigcap_{\vec{x}_{k} \in \sigma} B\left(\vec\{x\}_\{k\}, \frac{\epsilon}{2}\right) \neq \emptyset $$


## Image of Cech Complex
**Definition**: For point cloud $X$ and threshold $\epsilon \in \mathbb{R}$:

$\\check{C}\_\\epsilon(X) = \left\\{\sigma \subseteq X : \bigcap_{\vec{x} \in \sigma} B\left(\vec{x}, \frac{\epsilon}{2}\right) \neq \emptyset \right\\}$
<!-- Čech complex from three balls (nerve is the filled triangle) -->
<svg viewBox="0 0 600 450" xmlns="http://www.w3.org/2000/svg" style="max-width: 50%; height: auto;">
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

$\sigma = \{(x_{i_0}, x_{i_1}, \ldots, x_{i_k})\} \in VR_\epsilon(X)$
if all pairwise distances satisfy: $d(x_{i_j}, x_{i_k}) \leq \epsilon$

<svg viewBox="0 0 600 450" xmlns="http://www.w3.org/2000/svg" style="max-width: 50%; height: auto;">
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


## $VR_{\epsilon}$ Definition:
For point cloud $X$ in a metric space and a given threshold $\epsilon \in \mathbb{R}^{\geq 0}$:

$$VR_\epsilon(X) = \\{\sigma \subseteq X : \text{diam}(\sigma) \leq \epsilon\\}$$


## $VR_{\epsilon}$ Properties:
- $\\check{C}_\epsilon (X) \subseteq VR_\epsilon(X)$ as a subcomplex
- $1$-skeletons are identical
- The Rips Complex may include additional simplices:


## Complexity of $VR_\epsilon$ and $\check{C}_{\epsilon}$

- Cech complex $k$-skeleton in $O(n^{k+1})$ time.
- Rips Complex distance comparisons in $O(n^2)$ time. 
    - The number of cliques grows exponentially so the enumeration step will dominate.

<p style="font-size: 0.55em; margin: 0;">
  Zomorodian, A. (2010). <em>Fast construction of the Vietoris-Rips complex</em>. Computers & Graphics, 34(3), 263–271.
</p>


## The (Strict) Witness Complex: $\text{Wit}_\infty(L, W)$

**Definition**: Given landmarks and witnesses $$L, W \subset X$$

$\sigma \subseteq L$ is included as a simplex in $\text{Wit}_\infty(L, W)$ if it is 'witnessed' by some point $w \in W$.

<p style="font-size: 0.55em; margin: 0;">
  Silva, V., &amp; Carlsson, G. (2004). <em>Topological estimation using witness complexes</em>. Proc. Sympos. Point-Based Graphics.
</p>


## A Witness Complex:
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
  <circle cx="230" cy="120" r="7" class="witness"/>
  <text x="312" y="244" class="label" style="font-weight: 500;">w</text>
  <text x="242" y="124" class="label" style="font-weight: 500;">w'</text>

  <!-- Dotted blue circle centered at the witness; radius chosen to include only L1, L2, L3 -->
  <!-- Distances from w(300,240): L1≈116.6, L2≈116.6, L3=90; others below are >120 -->
  <circle cx="300" cy="240" r="120" class="w-circle"/>
  <circle cx="230" cy="120" r="100" class="w-circle"/>

  <!-- Landmarks (three inside the witness circle forming the face) -->
  <circle cx="200" cy="300" r="6" class="landmark"/>
  <circle cx="400" cy="300" r="6" class="landmark"/>
  <circle cx="300" cy="124" r="6" class="landmark"/>
  <text x="188" y="322" class="label">L1</text>
  <text x="408" y="322" class="label">L2</text>
  <text x="312" y="140" class="label">L3</text>

  <!-- Additional landmarks (all outside the witness circle) -->
  <circle cx="460" cy="120" r="6" class="landmark"/>
  <circle cx="180" cy="180" r="6" class="landmark"/>
  <text x="468" y="116" class="label">L5</text>
  <text x="168" y="170" class="label">L4</text>

  <!-- Witness complex edges for {L1, L2, L3}; face is invisible (fill: none) -->
  <polygon points="200,300 400,300 300,124" class="edge"/>

  <line x1="180" y1="180" x2="300" y2="124" class="edge"/>    

  <!-- Caption -->
  <text x="308" y="300" class="label" style="font-weight: 500;">Witness complex</text>
  <text x="308" y="319" class="label" style="font-weight: 400; opacity: 0.8;">Dotted circle includes only {L1, L2, L3}</text>
</svg>


## $\text{Wit}_\infty (L, W)$ Construction:

1. The vertex set is $L$.

2. Add an edge $(l_i , l_j)$ if they are the two closest landmarks to some witness (ties allowed)

3. Add the $k$-simplex $(l_{i_0} , \dots, l_{i_{k}} )$ if all of its faces exist and it is the ($k+1$)-nearest neighbors to some witness (ties allowed)


## The (Lazy) Witness Complex: $\text{Wit}(L, W)$

*Lazy is to Strict as Rips is to Cech*

- Same 1-skeleton as $\text{Wit}_\infty(L, W)$

- Include the simplex $\sigma$ if all of its edges are included.

*Lazy* because it avoids re-checking nearest neighbor condition for higher dimensions


## The Parameterized Version: $ \text{Wit}_{\epsilon}(L, W; \nu)$ 
where $\epsilon \in \mathbb{R}^{+}$ and $\nu \in \mathbb{N}$

1. The edge $(l_i, l_j)$ is included if there is a witness $w_i$ whose $(d^{\nu}(w_i) + \epsilon)$-neighborhood contains $(l_i, l_j)$ 
2. Then fill in all possible higher dimensional simplices.


## Parameterized Witness Properties:
- $\nu = 0$ is closely related to $VR_\epsilon$

- When $\nu = 2$ and $\epsilon = 0$ we have:
$$\text{Wit}_{0}(L, W; 2) = \text{Wit}(L, W)$$

<p style="font-size: 0.55em; margin: 0;">
  Silva, V., &amp; Carlsson, G. (2004). <em>Topological estimation using witness complexes</em>. Proc. Sympos. Point-Based Graphics.
</p>
