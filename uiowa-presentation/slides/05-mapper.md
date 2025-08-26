## Mapper

*"You're still trying to replace $\check{C}_{\epsilon}(X)$. I told you we can't do it. Now, what we might be able to do is re-create it in the aggregate."*

<div class="uiowa-logo">
    <img src="images/brad.jpg" alt="University of Iowa" style="height: 250px;">
</div>
<p style="font-size: 0.55em; margin: 0;">
  Welch, D. (n.d.). <em>We're going to recreate Toney in the aggregate.</em> Medium. 
  <a href="https://medium.com/@duncanwelch31/were-going-to-recreate-toney-in-the-aggregate-4a4dfe370b1c">https://medium.com/@duncanwelch31/were-going-to-recreate-toney-in-the-aggregate-4a4dfe370b1c</a>
</p>


## Mapper Ingredients

<p style="font-size: 0.55em; margin: 0;">
  Singh, G., Mémoli, F., &amp; Carlsson, G. E. (2007). <em>Topological methods for the analysis of high dimensional data sets and 3d object recognition</em>. In SPBG (pp. 91–100).
</p>

1. A **dataset** $X$ with a metric.
2. A **filter** (lens) function $f: X \to \mathbb{R}^m$
3. An **open cover** $\mathcal{U}$ of $f[X]$
4. A **clustering method** on $X$


## Mapper Diagram
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


## Mapper Construction
1. Apply the filter $f[X]$
2. Apply covering scheme on the image.
3. Pullback each cover element $$V_i = f^{-1}[U_i] \subseteq X$$
4. Apply the clustering method inside each $V_i$
5. Build the nerve from the set of all resulting clusters.


## Mapper filtration:
It has been shown that the mapper algorithm with certain parameter choices for the filter function, cover scheme, and clustering method will yield filtrations.

- DBSCAN with $\text{MinPts} \leq 2$ gives a filtration over $\epsilon$

<p style="font-size: 0.55em; margin: 0;">
  Bungula, W., &amp; Darcy, I. (2024). <em>Bi-Filtration and Stability of TDA Mapper for Point Cloud Data</em>. arXiv:2409.17360. 
  <a href="https://arxiv.org/abs/2409.17360">https://arxiv.org/abs/2409.17360</a>
</p>


## Pros:
1. For large high-dimensional data mapper is usually **faster** than using Cech, Rips, and Witness complexes.
2. **Flexible:** Can fine-tune parameters to suit analysis in a particular domain.


## Cons:
1. There are many parameter choices to consider:
    - Varying filter function, covering and clustering schemes can dramatically change the result.
2. There is no guarantee that the result from any given parameter selection is stable.


## Parameter Choice and Noise Matters:
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 873.667 536.365" style="max-width: 90%">
  <rect x="57.68" y="24.765" width="99.687" height="371.787" style="stroke: rgb(0, 0, 0); fill: rgba(169, 145, 255, 0.42);"></rect>
  <rect x="137.931" y="47.962" width="84.011" height="338.558" style="stroke: rgb(0, 0, 0); fill: rgba(255, 134, 134, 0.376);"></rect>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" cx="145.141" cy="171.787" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="162.382" cy="196.552" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="142.947" cy="147.022" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="188.715" cy="138.245" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="176.803" cy="165.831" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="141.692" cy="199.686" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="164.891" cy="223.511" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="143.574" cy="294.358" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="164.263" cy="270.533" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="132.916" cy="232.289" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="171.787" cy="312.539" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="188.715" cy="289.342" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="188.088" cy="331.975" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="221.944" cy="300.627" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="221.316" cy="328.057" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="267.085" cy="294.357" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="267.712" cy="327.586" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="309.718" cy="271.787" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="294.044" cy="308.15" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="344.828" cy="307.524" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="347.335" cy="246.708" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="344.2" cy="278.527" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="168.025" cy="111.912" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="211.912" cy="96.865" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="219.435" cy="123.041" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="247.649" cy="89.969" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="253.292" cy="111.912" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="290.282" cy="88.088" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="284.013" cy="107.524" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="324.765" cy="107.524" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="321.63" cy="79.31" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="359.875" cy="125.078" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="352.978" cy="181.505" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="386.207" cy="147.022" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="374.295" cy="194.044" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="379.937" cy="271.787" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="408.15" cy="182.132" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="378.683" cy="233.542" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 0, 0);" cx="116.616" cy="280.564" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(219, 209, 255);" cx="113.48" cy="429.99" rx="8.777" ry="8.777"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(219, 209, 255); stroke-width: 1px;" cx="113.479" cy="495.193" rx="8.777" ry="8.777"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 209, 209);" cx="194.985" cy="404.494" rx="8.777" ry="8.777"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 209, 209);" cx="194.357" cy="514.211" rx="8.777" ry="8.777"></ellipse>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px;" d="M 121.63 427.691 L 187.461 409.509"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px;" d="M 121.63 499.164 L 186.834 512.957"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-dasharray: 5px; stroke-width: 2px;" d="M 203.135 405.12 L 300.314 410.136"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-dasharray: 4px; stroke-width: 2px;" d="M 201.881 514.211 L 304.075 497.283"></path>
  <rect x="451.358" y="20.168" width="99.687" height="371.787" style="stroke: rgb(0, 0, 0); fill: rgba(169, 145, 255, 0.42); stroke-width: 1px;"></rect>
  <rect x="531.609" y="43.365" width="84.011" height="338.558" style="stroke: rgb(0, 0, 0); fill: rgba(255, 134, 134, 0.376); stroke-width: 1px;"></rect>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="538.819" cy="167.19" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="556.06" cy="191.955" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="536.625" cy="142.425" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="582.393" cy="133.648" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="570.481" cy="161.234" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="535.37" cy="195.089" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="558.569" cy="218.914" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="537.252" cy="289.761" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="557.941" cy="265.936" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="526.594" cy="227.692" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="565.465" cy="307.942" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="582.393" cy="284.745" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="581.766" cy="327.378" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="615.622" cy="296.03" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="614.994" cy="323.46" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="660.763" cy="289.76" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="661.39" cy="322.989" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="703.396" cy="267.19" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="687.722" cy="303.553" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="738.506" cy="302.927" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="741.013" cy="242.111" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="737.878" cy="273.93" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="561.703" cy="107.315" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="605.59" cy="92.268" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="613.113" cy="118.444" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="641.327" cy="85.372" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="646.97" cy="107.315" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="683.96" cy="83.491" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="677.691" cy="102.927" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="718.443" cy="102.927" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="715.308" cy="74.713" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="753.553" cy="120.481" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="746.656" cy="176.908" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="779.885" cy="142.425" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="767.973" cy="189.447" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="773.615" cy="267.19" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="801.828" cy="177.535" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 1px;" cx="772.361" cy="228.945" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="stroke-width: 1px; stroke: rgba(0, 0, 0, 0.275); fill: rgba(255, 0, 0, 0.21);" cx="510.294" cy="275.967" rx="6.583" ry="6.583"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); fill: rgb(219, 209, 255); stroke-width: 1px;" cx="502.142" cy="456.114" rx="8.777" ry="8.777"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 209, 209);" cx="588.663" cy="399.897" rx="8.777" ry="8.777"></ellipse>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 209, 209);" cx="588.035" cy="509.614" rx="8.777" ry="8.777"></ellipse>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px;" d="M 509.038 451.307 L 581.139 404.912"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 2px;" d="M 507.157 463.219 L 580.512 508.36"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-dasharray: 5px; stroke-width: 2px;" d="M 596.813 400.523 L 693.992 405.539"></path>
  <path style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-dasharray: 4px; stroke-width: 2px;" d="M 595.559 509.614 L 697.753 492.686"></path>
  <ellipse style="stroke: rgb(0, 0, 0); stroke-width: 1px; fill: rgb(255, 0, 0);" cx="524.765" cy="258.621" rx="6.583" ry="6.583"></ellipse>
</svg>


## Some Approaches to Parameter Selection:
- **G-Mapper** (Normal dist.-based Cover Selection)
<p style="font-size: 0.55em; margin: 0;">
  Alvarado, E., Belton, R., Fischer, E., Lee, K.-J., Palande, S., Percival, S., &amp; Purvine, E. (2025). <em>G-Mapper: Learning a Cover in the Mapper Construction</em>. arXiv:2309.06634. 
  <a href="https://arxiv.org/abs/2309.06634">https://arxiv.org/abs/2309.06634</a>
</p>

- **Ball Mapper** (Reduces to a single $\epsilon$ parameter)
<p style="font-size: 0.55em; margin: 0;">
  Dłotko, P. (2019). <em>Ball mapper: a shape summary for topological data analysis</em>. arXiv:1901.07410. 
  <a href="https://arxiv.org/abs/1901.07410">https://arxiv.org/abs/1901.07410</a>
</p>
