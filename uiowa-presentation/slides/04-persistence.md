## Persistence and Stability

Each method of obtaining a topological space from data typically has a set of parameters.

Different choices of parameters may yield different complexes.


## Filtrations:
A nested sequence of simplicial complexes:
$$\Delta_0 \subseteq \Delta_1 \subseteq \Delta_2 \subseteq \cdots \subseteq \Delta_n$$

- Required in order to compare complexes in the parameter space.


## Examples:

$ \check{C}\_\epsilon(X), VR_\epsilon(X), \text{and } \text{Wit}\_{\epsilon}(L, W)$ all are filtrations with respect to the parameter $\epsilon$.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" xmlns:bx="https://boxy-svg.com" style="max-width: 100%; height: auto; ">
  <defs>
    <bx:grid x="0" y="0" width="53.4" height="50.042"></bx:grid>
  </defs>
  <path style="stroke: rgb(0, 0, 0); fill: rgb(179, 255, 255); stroke-width: 3px;" d="M 730.43 150.713 L 740.925 72.628 L 676.099 49.202 L 730.43 150.713 Z"></path>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="614.19" y="102.015">⊆</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="453.005" y="103.064">⊆</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="293.475" y="103.274">⊆</text>
  <path style="stroke-width: 3px; stroke: rgb(0, 0, 0); fill: rgb(255, 171, 171);" d="M 678.002 50.797 L 731.318 151.805 L 694.2 151.805 L 678.002 50.797 Z"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 3px;" d="M 422.334 69.689 L 410.574 143.577"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 3px;" d="M 359.362 45.34 L 421.494 66.75"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 3px;" d="M 376.154 146.095 L 410.574 144.836"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 3px;" d="M 199.832 45.34 L 261.964 66.75"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 3px;" d="M 216.624 146.095 L 251.044 144.836"></path>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="144.583" y="102.435">⊆</text>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 3px;" d="M 71.367 146.095 L 105.787 144.836"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 3px; stroke-dasharray: 5px;" d="M 693.955 150.294 L 740.554 72.628"></path>
  <path style="stroke: rgb(0, 0, 0); stroke-width: 3px; fill: none;" d="M 535.684 144.416 L 583.123 67.17 L 520.151 45.76"></path>
  <path style="stroke-width: 3px; stroke: rgb(0, 0, 0); fill: rgb(100, 160, 100);" d="M 534.845 147.355 L 581.864 67.17 L 573.048 141.898 L 534.845 147.355 Z"></path>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="77.666" y="185.559">ε</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="227.596" y="184.299">ε</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="387.126" y="183.669">ε</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="547.915" y="182.62">ε</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px; stroke-width: 1px;" x="704.926" y="182.62">ε</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="91.225" y="193.871" transform="matrix(0.725144, 0, 0, 0.578402, 25.073778, 77.793785)">1</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="91.225" y="193.871" transform="matrix(0.809718, 0, 0, 0.588937, 167.296387, 76.017998)">2</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="91.225" y="193.871" transform="matrix(0.682869, 0, 0, 0.620187, 338.149719, 70.784882)">3</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="91.225" y="193.871" transform="matrix(0.682869, 0, 0, 0.578521, 497.820526, 77.806526)">4</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="91.225" y="193.871" transform="matrix(0.704011, 0, 0, 0.547271, 654.501831, 83.072762)">5</text>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="199.076" cy="45.467" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="252.015" cy="143.031" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="262.721" cy="66.331" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="215.072" cy="145.13" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="358.606" cy="45.467" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="411.545" cy="143.031" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="422.251" cy="66.331" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="374.602" cy="145.13" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="677.28" cy="50.504" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="730.219" cy="148.068" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="740.925" cy="71.368" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="693.276" cy="150.167" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="519.815" cy="45.467" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="572.754" cy="143.031" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="583.46" cy="66.331" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="535.811" cy="145.13" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="53.819" cy="45.467" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="106.758" cy="143.031" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="117.464" cy="66.331" rx="6.675" ry="6.675"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(130, 160, 255);" cx="69.815" cy="145.13" rx="6.675" ry="6.675"></ellipse>
</svg>


## Real Example:
<div class="uiowa-logo">
    <img src="images/filtration_visualization.png" alt="University of Iowa" style="max-width: 75%;">
</div>


## Homology
Homology measures topological features of a space $X$ by identifying a sequence of abelian groups:
<div style="text-align: left;">
    <ul>
      <li>$H_0(X)$ ~ Connected components (0-dim holes)</li>
      <li>$H_1(X)$ ~ Loops/circles (1-dim holes)
</li>
      <li>$H_2(X)$ ~ Voids/cavities of spheres (2-dim holes)</li>
      <li>$H_k(X)$ ~ $k$-dim holes</li>
    </ul>
  </div>


## Persistent Homology
Tracks how homological features evolve across a filtration of simplicial complexes.

- Computes the homology at each stage.
- Identifies topological features that persist.

**Persistence**: $$\text{P}(\text{f}) = \epsilon_\text{f-death} - \epsilon_\text{f-birth}$$


## Persistence Diagram
**Birth-Death**: Feature $f_i$ appears at $x_i$ (birth) and disappears at $y_i$ (death).
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300">
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" cx="71.97" cy="88.666" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="97.277" cy="82.155" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="81.409" cy="73.003" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="66.145" cy="104.705" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="49.676" cy="95.018" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="48.872" cy="115.776" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 119.834px 185.69px 0px;" cx="119.834" cy="185.69" rx="2.264" ry="2.41" transform="matrix(0, -1, 1, 0, -84.487218, -48.904353)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 144.167px 179.027px 0px;" cx="144.167" cy="179.027" rx="2.264" ry="2.41" transform="matrix(0, -1, 1, 0, -115.749724, -66.017382)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 128.91px 169.66px 0px;" cx="128.91" cy="169.66" rx="2.264" ry="2.41" transform="matrix(0, -1, 1, 0, -110.234894, -41.742546)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 114.234px 202.105px 0px;" cx="114.234" cy="202.105" rx="2.264" ry="2.41" transform="matrix(0, -1, 1, 0, -95.157135, -48.90286)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 98.398px 192.191px 0px;" cx="98.398" cy="192.191" rx="2.264" ry="2.41" transform="matrix(0, -1, 1, 0, -66.73443, -22.005783)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 97.625px 213.435px 0px;" cx="97.625" cy="213.435" rx="2.264" ry="2.41" transform="matrix(0, -1, 1, 0, -53.508146, -56.458392)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -292.454px -245.718px 0px;" cx="-292.45" cy="-245.72" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, 489.051288, 355.3625)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -268.121px -252.381px 0px;" cx="-268.12" cy="-252.38" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, 471.648312, 385.801814)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -283.378px -261.748px 0px;" cx="-283.38" cy="-261.75" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, 496.647515, 380.260831)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -298.053px -229.303px 0px;" cx="-298.05" cy="-229.3" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, 477.579404, 333.476193)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -313.89px -239.217px 0px;" cx="-313.89" cy="-239.22" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, 503.726384, 327.916633)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -314.663px -217.973px 0px;" cx="-314.66" cy="-217.97" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, 482.405195, 305.916521)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 145.382px 75.239px 0px;" cx="145.382" cy="75.239" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 144.176px 94.015px 0px;" cx="144.176" cy="94.015" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 92.957px 98.071px 0px;" cx="92.957" cy="98.071" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 163.659px 65.237px 0px;" cx="163.659" cy="65.237" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 109.83px 71.778px 0px;" cx="109.83" cy="71.778" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 123.89px 83.478px 0px;" cx="123.89" cy="83.478" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -196.968px -183.676px 0px;" cx="-196.97" cy="-183.67" rx="2.41" ry="2.264" transform="matrix(-1, 0, 0, -1, 393.936154, 367.351284)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -171.663px -190.188px 0px;" cx="-171.68" cy="-190.18" rx="2.41" ry="2.264" transform="matrix(-1, 0, 0, -1, 343.325374, 380.375021)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -187.53px -199.339px 0px;" cx="-187.54" cy="-199.34" rx="2.41" ry="2.264" transform="matrix(-1, 0, 0, -1, 375.060331, 398.67733)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -202.794px -167.638px 0px;" cx="-202.8" cy="-167.64" rx="2.41" ry="2.264" transform="matrix(-1, 0, 0, -1, 405.587374, 335.276311)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -219.261px -177.325px 0px;" cx="-219.28" cy="-177.32" rx="2.41" ry="2.264" transform="matrix(-1, 0, 0, -1, 438.522949, 354.649091)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: -205.204px -152.793px 0px;" cx="-205.21" cy="-152.8" rx="2.41" ry="2.264" transform="matrix(-1, 0, 0, -1, 410.407003, 305.585346)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, -51.067706, -73.540119)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 294.128px 198.662px 0px;" cx="294.128" cy="198.662" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, -68.471306, -43.101041)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 278.871px 189.295px 0px;" cx="278.871" cy="189.295" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, -43.472122, -48.64188)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 331.531px 170.305px 0px;" cx="331.531" cy="170.305" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, -176.408083, 35.3893)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 325.931px 186.72px 0px;" cx="325.931" cy="186.72" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, -207.162657, 24.447574)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 310.095px 176.806px 0px;" cx="310.095" cy="176.806" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, -181.015689, 18.887965)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 309.322px 198.05px 0px;" cx="309.322" cy="198.05" rx="2.264" ry="2.41" transform="matrix(0, 1, -1, 0, -202.337271, -3.111224)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 84.624px 182.232px 0px;" cx="84.624" cy="182.232" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 150.504px 190.44px 0px;" cx="150.503" cy="190.44" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 88.841px 205.064px 0px;" cx="88.841" cy="205.064" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 67.151px 166.946px 0px;" cx="67.151" cy="166.946" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 49.073px 178.771px 0px;" cx="49.073" cy="178.771" rx="2.41" ry="2.264"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 63.132px 190.47px 0px;" cx="63.132" cy="190.47" rx="2.41" ry="2.264"></ellipse>
  <rect x="329.451" y="229.707" width="254.532" height="1.204" style="stroke: rgb(0, 0, 0);"></rect>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="387.022" y="291.683" transform="matrix(0.775986, 0, 0, 0.565405, 136.127106, 92.923706)">birth</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Arial&quot;, sans-serif; font-size: 28px;" x="310.254" y="177.842" transform="matrix(0.73822, 0, 0, 0.742424, 31.488762, 43.561951)">death</text>
  <rect x="208.851" y="349.731" width="202.389" height="2.537" style="stroke: rgb(0, 0, 0); stroke-width: 1px; transform-origin: 310.051px 350.994px 0px;" transform="matrix(0, 1, 1, 0, 18.969913, -221.230031)"></rect>
  <path style="paint-order: fill; fill: rgb(116, 239, 247); stroke: rgb(128, 0, 255);" d="M 329.567 231.267 L 560.352 32.831"></path>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; transform-origin: 269.795px 205.325px 0px; stroke: rgb(255, 32, 32);" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 111.433354, -31.029986)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 110.467655, -22.822123)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 97.431845, -15.579976)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 121.089631, -34.409587)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 117.227091, -162.354717)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 146.195866, -56.618937)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 136.539564, -50.342324)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 151.506709, -65.309556)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 128.050009, -41.555318)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 72.325697, -3.300942)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 88.258314, -7.348946)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 79.084975, 2.76696)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 70.877023, 9.139966)"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke-width: 1px; stroke: rgb(255, 32, 32); transform-origin: 269.795px 205.325px 0px;" cx="269.795" cy="205.325" rx="2.024" ry="2.155" transform="matrix(0, 1, -1, 0, 81.981829, -3.301041)"></ellipse>
  <path style="fill: rgba(216, 216, 216, 0); stroke: rgba(255, 0, 0, 0.447);" d="M 148.996 198.114 C 145.143 200.04 135.798 198.759 133.063 201.493 C 132.65 201.906 129.925 201.009 129.683 201.493 C 128.466 203.927 107.264 204.936 106.025 202.459 C 105.512 201.432 99.658 203.333 98.783 202.459 C 93.27 196.946 83.465 196.314 77.54 190.389 C 69.31 182.16 58.481 169.272 47.605 163.834 C 42.619 161.341 40.473 155.199 35.535 152.729 C 31.422 150.673 30.567 141.967 27.81 139.211 C 25.873 137.274 29.213 131.094 29.741 130.037 C 31.888 125.744 31.816 120.72 35.052 117.484 C 39.683 112.853 46.314 107.671 50.502 103.483 C 53.084 100.901 59.542 101.202 62.572 98.172 C 72.787 87.956 96.104 87.067 112.302 87.067 C 118.027 87.067 132.352 85.873 135.477 88.998 C 136.254 89.775 141.774 88.073 142.236 88.998 C 143.647 91.819 156.162 90.371 158.652 92.861 C 159.29 93.499 162.62 92.914 163.48 93.344 C 168.161 95.684 176.14 94.899 179.413 98.172 C 182.921 101.68 190.19 109.489 193.897 110.725 C 196.048 111.442 196.287 115.299 198.725 116.519 C 203.92 119.116 205.232 128.946 210.313 131.486 C 210.952 131.805 210.893 134.963 211.278 135.348 C 216.167 140.236 215.29 154.363 212.727 159.489 C 206.534 171.875 193.642 176.16 183.275 186.526 C 180.111 189.691 173.917 188.642 170.239 192.32 C 167.25 195.31 162.208 193.68 159.135 195.217 C 155.119 197.225 148.894 199.562 145.133 199.562"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); paint-order: fill markers; stroke-dasharray: 5px, 10px;" d="M 200 118.45 L 382.677 44.096"></path>
</svg>


## Persistence Barcodes:

An alternative representation of persistent homology:
- Each feature becomes a horizontal bar 
- Bar length = $\epsilon_\text{birth} - \epsilon_\text{death}$
- Bar position = birth time 


## Real Example: 
<div class="uiowa-logo">
    <img src="images/noisy_circle_h1.png" alt="University of Iowa" style="max-width: 100%;">
</div>


## Approximating Cech Complex Persistence
Given a point-cloud $X \subset \mathbb{R}^{d}$ then there is a chain of inclusions

$$ \check{C}_{\epsilon'} (X) \subseteq VR_\epsilon (X) \subseteq \check{C}_\{\epsilon\}(X) $$

Whenever $\frac{\epsilon}{\epsilon'} \geq \sqrt{\frac{2d}{d + 1}}$

<p style="font-size: 0.55em; margin: 0;">
  Silva, V., &amp; Ghrist, R. (2007). <em>Coverage in sensor networks via persistent homology</em>. Algebraic & Geometric Topology, 7.
</p>


## Approximating via Witnesses
If $L$ is an $\epsilon$-net landmark set of $X \subset \mathbb{R}^{d}$ for $\epsilon > 0$, then

$$ VR_{\alpha / 3}(L) \subseteq \text{Wit}_{\alpha}(L, X \setminus L; \nu = 1) \subseteq VR\_{3 \alpha}(L)$$
for $\alpha \geq 2\epsilon $
<p style="font-size: 0.55em; margin: 0;">
  Arafat, N. A., Basu, D., &amp; Bressan, S. (2019). <em>Topological Data Analysis with ε-net Induced Lazy Witness Complex</em>. arXiv preprint arXiv:1906.06122.
</p>


## Stitching Together

So in theory with a representative landmark set satisfying the $\epsilon$-net condition you can approximate the
persistence in the Cech complex filtration via a laziest witness complex filtration.  


**Problem:** May still require a large high-dimensional Landmark set for it to be representative.


**Problem:** Curse of dimensionality makes it so that nearest neighbors is not stable under noise.

