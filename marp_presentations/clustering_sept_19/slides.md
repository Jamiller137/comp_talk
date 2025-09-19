---
marp: true
theme: uiowa
math: mathjax
paginate: true
footer: 'TDA/V Seminar: September 19th, 2025' 
---

<!-- _class: title-slide -->

# An Introduction to Clustering
##
**Jacob Miller**  
Department of Mathematics  
University of Iowa  

---

## Outline:

- What is Clustering?
- Theory
- Types of Clusters
- Some Clustering Algorithms
- Clustering Evaluation

---

## What is Clustering?

Partitioning a dataset where points within each group are more *similar* to each other than to points in other groups.

**Formally**: Given dataset $X = \{x_1, x_2, \ldots, x_n\} \subset \mathbb{R}^d$, find partition $\mathcal{C} = \{C_1, C_2, \ldots, C_k\}$ where $\bigcup_{i=1}^k C_i = X$ and $C_i \cap C_j = \emptyset$ for $i \neq j$.

**Unsupervised**: No ground truth labels to check clustering against.

---

## Visual Example of Clustering

**Intuition**: Clusters are dense subsets separated by sparse subsets.

---

## What is 'Similar'?

- Clustering is an optimization problem on partitions of data.

Given data points $X = \{x_1, \ldots, x_n\}$, find a partition $\{C_1, \ldots, C_K\}$ that (min)maximizes some (dis)similarity score (between) within clusters.

---

## Optimization Examples
$$\min_{\mathcal{C} \in \mathcal{Part}(X)} \sum_{k=1}^{|\mathcal{C}|} \sum_{x_i, x_j \in C_k} d(x_i, x_j)$$

$$\max_{\mathcal{C} \in \mathcal{Part}(X)} \sum_{k=1}^{|\mathcal{C}|} \sum_{x_i, x_j \in C_k} \text{sim}(x_i, x_j)$$

---

## Distance Example

$$\min_{\mathcal{C}} \sum_{k=1}^{|\mathcal{C}|} \sum_{x_i \in C_k} \text{dist}(x_i, \mu_k)$$

Where $\mu_k$ is a representative for cluster $C_k$

- Euclidean: $d(x_i, x_j) = \|x_i - x_j\|_2 = \sqrt{\sum_{d=1}^{D}(x_{id} - x_{jd})^2}$
- Manhattan: $d(x_i, x_j) = \|x_i - x_j\|_1 = \sum_{d=1}^{D}|x_{id} - x_{jd}|$
- Cosine: $d(x_i, x_j) = 1 - \frac{x_i \cdot x_j}{\|x_i\|_2\|x_j\|_2}$

---

## What would you want?

- **Scale-invariance**: $f(\alpha \cdot X) = f(X)$ for $\alpha > 0$
- **Richness**: For any partition of $X$, there exists a distance function such that the clustering function returns that partition
- **Consistency**: Shrinking intra-cluster distances and expanding inter-cluster distances doesn't change the clustering

---

## Impossibility Theorem

- **Scale-invariance**: $f(\alpha \cdot X) = f(X)$ for $\alpha > 0$
- **Richness**: For any partition of $X$, there exists a distance function such that the clustering function returns that partition
- **Consistency**: Shrinking intra-cluster distances and expanding inter-cluster distances doesn't change the clustering

**Kleinberg's Impossibility Theorem**: There is no clustering scheme that satisfies all three properties simultaneously.

---

## Types of Clusters

The choice of distance criterion and algorithm determines cluster shapes:

---

## Spherical/Convex
Circular or elliptical boundaries
- **Assumption**: $d(x, \mu) \leq r$ for cluster center $\mu$ and radius $r$
- Example: K-means produces spherical clusters with $L_2$ norm


Image

---

## Manifold/Non-Convex 
Complex, curved boundaries
- **Mathematical**: Clusters lie on low-dimensional manifolds $\mathcal{M} \subset \mathbb{R}^d$
- Example: Two interlocking crescents, Swiss roll

Image

---

## Varying vs. Uniform Density
- **Uniform**: $\rho(C_i) \approx \rho(C_j)$ for all clusters $i, j$
- **Varying**: $\frac{|C_i|/\text{vol}(C_i)}{|C_j|/\text{vol}(C_j)} \gg 1$ for some clusters

Image

---

## Well-separated vs. Connected:
- **Separated**: $\min_{x \in C_i, y \in C_j} d(x,y) > \max_{x,y \in C_k} d(x,y)$ for $k \in \{i,j\}$
- **Connected**: Clusters connected by low-density regions

Image

---

## Types of Clustering Algorithms

**Four main categories**:

1. **Partitioning**: Minimize $\sum_{k} \sum_{x \in C_k} d(x, \mu_k)^2$
2. **Hierarchical**: Build tree with linkage $d(C_i, C_j)$
3. **Density-based**: Find $\{x : \rho(x) > \theta\}$ for density $\rho$
4. **Model-based**: Maximize $\prod_{i} \sum_{k} \pi_k p(x_i | \theta_k)$

Each has different assumptions about cluster structure!

---

## image
Describe these cluster assumptions

---

## Partitioning (distance) Methods: K-Means

**Algorithm**:
1. Choose number of clusters K
2. Initialize K cluster centroids $\mu_1^{(0)}, \ldots, \mu_K^{(0)}$ randomly
3. Assign: $C_k^{(t)} = \{x_i : k = \arg\min_j \|x_i - \mu_j^{(t-1)}\|^2\}$
4. Update: $\mu_k^{(t)} = \frac{1}{|C_k^{(t)}|} \sum_{x_i \in C_k^{(t)}} x_i$
5. Repeat steps 3-4 until $\|\mu_k^{(t)} - \mu_k^{(t-1)}\| < \epsilon$

---

## K-Means / Medoids

Image for this

---

## Hierarchical Clustering

**Two types**:
1. **Agglomerative** (bottom-up): Start with $n$ clusters $\{x_i\}$, merge until $k$ clusters
2. **Divisive** (top-down): Start with 1 cluster $X$, split until $k$ clusters

**Output**: Dendrogram showing cluster hierarchy at all levels

---

## Reading Dendrograms

Image

**Horizontal lines**: Represent clusters at that level
**Vertical lines**: Show merge operations with cost $d(C_i, C_j)$
**Height**: Distance at which clusters merge

---

## Linkage Criteria

**Single linkage**: Distance between closest points
$$d(C_i, C_j) = \min_{x \in C_i, y \in C_j} d(x,y)$$

**Complete linkage**: Distance between farthest points  
$$d(C_i, C_j) = \max_{x \in C_i, y \in C_j} d(x,y)$$

**Average linkage**: Average distance between all pairs

---

## Single-Linkage Clustering

1. **Initialize**: Start with $n$ clusters, each containing one point
   $$\mathcal{C}^{(0)} = \{\{x_1\}, \{x_2\}, \ldots, \{x_n\}\}$$

2. **Compute distance matrix**: Calculate all pairwise cluster distances
   $$D^{(0)}_{ij} = d(x_i, x_j) \text{ for all } i \neq j$$

3. **Find minimum**: Identify closest pair of clusters
   $$(i^*, j^*) = \arg\min_{i,j: i \neq j} D^{(t)}_{ij}$$

---

4. **Merge**: Combine clusters $C_{i^*}$ and $C_{j^*}$
   $$C_{\text{new}} = C_{i^*} \cup C_{j^*}$$

5. **Update distances**: For all remaining clusters $C_k$:
   $$D_{\text{new},k} = \min(D_{i^*,k}, D_{j^*,k})$$

6. **Repeat**: Until desired number of clusters or single cluster remains

---

## Single-Linkage

**Note**: Creates elongated clusters due to **chaining effect** - clusters connected by single close points will merge.

Image Here

---

## Density-Based Clustering: DBSCAN

Clusters are dense regions separated by sparse regions

**Key parameters**:
- $\epsilon$: Neighborhood radius
- $\text{minPts}$: Minimum points to form cluster

**Density**: $\rho_{\epsilon}(x) = |\{y \in X : d(x,y) \leq \epsilon\}|$

---
## DBSCAN

- **Core point**: $\rho_{\epsilon}(x) \geq \text{minPts}$
- **Border point**: $\rho_{\epsilon}(x) < \text{minPts}$ but $\exists$ core point $y$ with $d(x,y) \leq \epsilon$
- **Noise point**: Neither core nor border

**Density-reachable**: $x$ is density-reachable from $y$ if $\exists$ chain of core points connecting them.

---

## DBSCAN Algorithm

1. For each point $p$:
   - Find $N_{\epsilon}(p) = \{q \in X : d(p,q) \leq \epsilon\}$
   - If $|N_{\epsilon}(p)| \geq \text{minPts}$, mark as core point

2. For each core point $p$:
   - Create cluster $C = \{p\} \cup \{q : q \text{ density-reachable from } p\}$

3. Assign border points to nearby clusters

4. Mark remaining points as noise

---

## Image of DBSCAN clusters:

---

## Probabilistic Methods: Overview

**Core idea**: Model data as generated from mixture of probability distributions

1. Assume each cluster follows a probability distribution $p(x | \theta_k)$
2. Use Maximum Likelihood Estimation: $\max_{\theta} \prod_{i=1}^n p(x_i | \theta)$
3. Apply Expectation-Maximization (EM) algorithm

**Log-likelihood**: $\ell(\theta) = \sum_{i=1}^n \log \sum_{k=1}^K \pi_k p(x_i | \theta_k)$

---

## Expectation-Maximization (EM) Algorithm

**Problem**: Maximize likelihood with latent (hidden) variables

**Setup**: 
- Observed data: $X = \{x_1, \ldots, x_n\}$
- Latent variables: $Z = \{z_1, \ldots, z_n\}$ 
- Parameters: $\theta$

**Objective**: $\max_{\theta} \ell(\theta) = \max_{\theta} \sum_{i=1}^n \log p(x_i | \theta)$


---

## EM alternates between:

**E-step**: Compute posterior distribution of latent variables
$$Q(\theta | \theta^{(t)}) = \sum_{i=1}^n \sum_{z_i} p(z_i | x_i, \theta^{(t)}) \log p(x_i, z_i | \theta)$$

**M-step**: Maximize expected complete log-likelihood
$$\theta^{(t+1)} = \arg\max_{\theta} Q(\theta | \theta^{(t)})$$

---

## Gaussian Mixture Models (GMM)

**Assumption**: Data generated from $K$ Gaussian distributions

$$p(x) = \sum_{k=1}^{K} \pi_k \mathcal{N}(x; \mu_k, \Sigma_k)$$

where $\mathcal{N}(x; \mu, \Sigma) = \frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\right)$

**Parameters**: $\theta = \{(\pi_k, \mu_k, \Sigma_k)\}_{k=1}^K$ with $\sum_{k=1}^K \pi_k = 1$

---

## EM Algorithm for GMM

**E-step**: Compute responsibility of component $k$ for point $i$
$$r_{ik} = \frac{\pi_k \mathcal{N}(x_i; \mu_k, \Sigma_k)}{\sum_{j=1}^{K} \pi_j \mathcal{N}(x_i; \mu_j, \Sigma_j)}$$

**M-step**: Update parameters
$\mu_k = \frac{\sum_{i=1}^{n} r_{ik} x_i}{\sum_{i=1}^{n} r_{ik}}, \quad \pi_k = \frac{1}{n}\sum_{i=1}^{n} r_{ik}$
$\Sigma_k = \frac{\sum_{i=1}^n r_{ik}(x_i - \mu_k)(x_i - \mu_k)^T}{\sum_{i=1}^n r_{ik}}$

---

## Image of GMM cluster:

---

## Spectral Clustering

1. **Graph construction**: $A_{ij} = \exp(-\|x_i - x_j\|^2 / 2\sigma^2)$ if $\|x_i - x_j\| < \epsilon$
2. **Graph Laplacian**: $L = D - A$ where $D_{ii} = \sum_j A_{ij}$
3. **Eigendecomposition**: Find eigenvectors $v_1, \ldots, v_k$ of smallest eigenvalues
4. **Embedding**: Let $Y = [v_1 | \cdots | v_k] \in \mathbb{R}^{n \times k}$
5. **Clustering**: Apply K-means to rows of $Y$

---

## Spectral Clustering Properties

Transforms clustering into graph cut problem.

**Normalized cut**: $\text{Ncut}(A,B) = \frac{\text{cut}(A,B)}{\text{vol}(A)} + \frac{\text{cut}(A,B)}{\text{vol}(B)}$

where $\text{cut}(A,B) = \sum_{i \in A, j \in B} A_{ij}$ and $\text{vol}(A) = \sum_{i \in A} d_i$

**Theorem**: Minimizing normalized cut is equivalent to finding eigenvectors of normalized Laplacian $\mathcal{L} = D^{-1/2}LD^{-1/2}$.

---

## Image for Spectral intuition:

---

## High-Dimensions

**Curse of dimensionality**: In high dimensions ($d \gg n$):
- All pairwise distances become similar: $\frac{\text{dist}_{\max} - \text{dist}_{\min}}{\text{dist}_{\min}} \to 0$
- Volume concentrates in high-dimensional shells
- Need dimension reduction or feature selection

**Concentration**: For Gaussian data, $\frac{\|x\|^2 - d}{\sqrt{2d}} \to \mathcal{N}(0,1)$

---

## Co-Clustering

**Motivation**: Cluster both rows (samples) and columns (features) simultaneously

**Matrix**: $X \in \mathbb{R}^{n \times d}$ → row clusters $\mathcal{R} = \{R_1, \ldots, R_k\}$, column clusters $\mathcal{C} = \{C_1, \ldots, C_\ell\}$

- **Spectral co-clustering**: SVD of $D_r^{-1/2} X D_c^{-1/2}$
- **Block diagonal**: Minimize $\|X - \sum_{i,j} A_{ij} R_i C_j^T\|_F^2$  
- **Information-theoretic**: Maximize mutual information $I(\mathcal{R}; \mathcal{C})$

---

## Cluster Evaluation

1. **External validation**: Compare against ground truth labels
2. **Internal validation**: Evaluates clustering using the same data
   - Silhouette score, Calinski-Harabasz index, Davies-Bouldin index

---

## Silhouette Score

**For each point $i$**: Compute silhouette coefficient
$$s_i = \frac{b_i - a_i}{\max(a_i, b_i)}$$

where:
- $a_i = \frac{1}{|C(i)|-1} \sum_{j \in C(i), j \neq i} d(i,j)$: avg distance within cluster
- $b_i = \min_{k \neq C(i)} \frac{1}{|C_k|} \sum_{j \in C_k} d(i,j)$: avg distance to nearest cluster

---

## Silhouette Score 

Overall score is given by the average of these coefficients

$$\text{Silhouette} = \frac{1}{n}\sum_{i=1}^{n} s_i \in [-1,1]$$

- $s_i \to 1$ (well-clustered)
- $s_i \to 0$ (boundary) 
- $s_i \to -1$ (misclassified)

---

## Image for Silhouette Score

---

# FIN

Notes:

- Update with pictures
- Update Spectral, Probabilistic, Co-Clustering and Curse of Dimensionality
