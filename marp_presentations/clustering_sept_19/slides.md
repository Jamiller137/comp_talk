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
- Types of Clusters
- Feature Selection
- Types of Clustering
    - Partitioning Methods (K-Means)
    - Hierarchical Methods (Agglomerative / Divisive)
    - Density-based Methods (DBSCAN)
    - Probabilistic EM Methods (GMM)
    - Dimension Reduction (NMF)
    - Co-Clustering
- Cluster Evaluation

---

## What is Clustering?

Partitioning a dataset where points within each group are more *similar* to each other than to points in other groups.


**Unsupervised**: No ground truth labels to check clustering against.

---

## Visual Example of Clustering

**Intuition**: Clusters are dense subsets separated by sparse subsets.

---

## What is 'Similar'?

- Clustering is an optimization problem on partitions of data.

Given data points $X = \{x_1, \ldots, x_n\}$, find a partition $\{C_1, \ldots, C_K\}$ that (min)maximizes some (dis)similarity score (between) within clusters.

$$ \min_{\mathcal{C} \in \mathcal{Part}(X)} \sum_{C_i , C_j \in \mathcal{C}} \text{Sim}(C_i, C_j)$$


---

## Distance Example

$$\min_{\mathcal{C}} \sum_{k=1}^{|\mathcal{C}|} \sum_{x_i \in C_k} \text{dist}(x_i, \mu_k)$$

Where $\mu_k$ is a representative for cluster $C_k$

- Euclidean: $\|x_i - x_j\|_2$
- Manhattan: $\|x_i - x_j\|_1$
- Cosine: $1 - \frac{x_i \cdot x_j}{\|x_i\|\|x_j\|}$

---

## What would you want?

- Scale-invariance
- Richness
- Consistent


---

## Impossibility Theorem

There is no clustering scheme that satisfies all three.

---

## Types of Clusters

The choice of distance criterion and algorithm determines cluster shapes:

---

## **Spherical/Convex**
Circular or elliptical boundaries
- Example: K-means produces spherical clusters

---

## **Manifold/Non-Convex** 
Complex, curved boundaries
- Example: Two interlocking crescents

---

## **Varying vs. Uniform Density**
- Uniform: All clusters have similar point density
- Varying: Some clusters are dense, others sparse

---

## Types of Clusters (cont.)

**Overlapping vs. Separated**:
- **Hard clustering**: Each point belongs to exactly one cluster
- **Soft clustering**: Points have probabilities of belonging to multiple clusters

---

**Well-separated vs. Connected**:
- Clear gaps between clusters vs. gradual transitions

---

## Types of (hard) Clustering Algorithms

**Four main categories**:

1. **Partitioning**: Divide data into K clusters (K-means)
2. **Hierarchical**: Build tree of clusters (Agglomerative)  
3. **Density-based**: Find dense regions (DBSCAN)
4. **Model-based**: Fit probabilistic models (GMM)

Each has different assumptions about cluster structure!

---

## image
describes cluster assumptions

---

## Partitioning (distance) Methods: K-Means

**Algorithm**:
1. Choose number of clusters K
2. Initialize K cluster centroids randomly
3. Assign each point to nearest centroid
4. Update centroids to mean of assigned points
5. Repeat steps 3-4 until convergence or cutoff

**Objective**: Minimize within-cluster sum of squares (WCSS)

$$\text{WCSS} = \sum_{k=1}^{K} \sum_{x_i \in C_k} \|x_i - \mu_k\|^2$$

---

## Hierarchical Clustering

**Two types**:
1. **Agglomerative** (bottom-up): Start with individual points, merge clusters
2. **Divisive** (top-down): Start with all points, split clusters

---

**Output**: Dendrogram showing cluster hierarchy at all levels

**Key decision**: How to measure distance between clusters?

Cutting height?

---

## Linkage Criteria

**Single linkage**: Distance between closest points
$$d(C_i, C_j) = \min_{x \in C_i, y \in C_j} d(x,y)$$

**Complete linkage**: Distance between farthest points  
$$d(C_i, C_j) = \max_{x \in C_i, y \in C_j} d(x,y)$$

**Average linkage**: Average distance between all pairs

---

## Agglomerative Clustering Example

---

## Reading Dendrograms

**Horizontal lines**: Represent clusters at that level
**Vertical lines**: Show merge operations  
**Height**: Distance at which clusters merge

Image / Example

---

## Density-Based Clustering: DBSCAN

**Core idea**: Clusters are dense regions separated by sparse regions

**Key parameters**:
- $\epsilon$: Neighborhood radius
- $\text{minPts}$: Minimum points to form cluster

---

**Point types**:
- **Core point**: Has $\geq$ minPts neighbors within $\epsilon$
- **Border point**: In neighborhood of core point
- **Noise point**: Neither core nor border

---

## DBSCAN Algorithm

1. For each point $p$:
   - Find all points within distance $\epsilon$
   - If $\geq$ minPts neighbors, mark as core point

2. For each core point:
   - Create cluster with all density-reachable points

3. Assign border points to nearby clusters

4. Mark remaining points as noise

---

## Probabilistic Methods: Overview

**Core idea**: Model data as generated from mixture of probability distributions

1. Assume each cluster follows a probability distribution
2. Use Maximum Likelihood Estimation (MLE)
3. Apply Expectation-Maximization (EM) algorithm

---

## Gaussian Mixture Models (GMM)

**Assumption**: Data generated from K Gaussian distributions

$$p(x) = \sum_{k=1}^{K} \pi_k \mathcal{N}(x; \mu_k, \Sigma_k)$$

---

## EM Algorithm for GMM

**E-step**: Compute responsibility of component k for point i
$$r_{ik} = \frac{\pi_k \mathcal{N}(x_i; \mu_k, \Sigma_k)}{\sum_{j=1}^{K} \pi_j \mathcal{N}(x_i; \mu_j, \Sigma_j)}$$

**M-step**: Update parameters
$$\mu_k = \frac{\sum_{i=1}^{n} r_{ik} x_i}{\sum_{i=1}^{n} r_{ik}}, \quad \pi_k = \frac{1}{n}\sum_{i=1}^{n} r_{ik}$$

**Iterate**: Until log-likelihood converges

---

## Dimension Reduction Methods

1. **Reduce dimensions first, then cluster**
2. **Simultaneous dimension reduction and clustering**

**Example methods**:
- Principal Component Analysis (PCA) + K-means
- Non-negative Matrix Factorization (NMF)
- Spectral clustering

---

## Non-negative Matrix Factorization (NMF)

---

## NMF Algorithm

**Objective**: Minimize reconstruction error
$$\min_{W,H \geq 0} \|X - WH\|_F^2$$


**Clustering**: Assign point i to cluster $\arg\max_k W_{ik}$

---

## Spectral Clustering

**Core idea**: Transform clustering into graph cut problem

---

## Spectral Clustering Properties


---

## High-Dimensions

---

## Co-Clustering

**Motivation**: Cluster both rows (samples) and columns (features) simultaneously

**Algorithms**:
- Spectral co-clustering
- Block diagonal co-clustering  
- Information-theoretic co-clustering

---

## Cluster Evaluation

1. **External validation**: Compare against ground truth labels
   - Adjusted Rand Index (ARI)
   - Normalized Mutual Information (NMI)
   - F-measure

2. **Internal validation**: Evaluate using data structure only
   - Silhouette score
   - Calinski-Harabasz index
   - Davies-Bouldin index

---

## Silhouette Score

**For each point i**: Compute silhouette coefficient
$$s_i = \frac{b_i - a_i}{\max(a_i, b_i)}$$

- $a_i$: Average distance to points in same cluster
- $b_i$: Average distance to points in nearest different cluster

$$\text{Silhouette} = \frac{1}{n}\sum_{i=1}^{n} s_i$$

---


