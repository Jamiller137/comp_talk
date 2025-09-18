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
```Given a set of data points, partition them into a set of groups which are as similar as possible.```

- Insert Image Here:

--- 

## What is 'similar'?

Given data points $X = \{x_1 , \dots, x_n \} \subset \mathbb{R}^d$ find a partition $\{C_1 , \dots, C_K \}$ that optimizes

$$
\min_{C_k} \sum_{k=1}^{K} \sum_{x_i \in C_k} \text{dist}(x_i, \mu_k)^2
$$
Where $\mu_k$ is a representative for cluster $C_k$

---

## Types of Clusters:
The type of distance criterion used will determine the types of clusters in the output:
- Convex / Spherical
- Manifold / Non-Convex
- Varying density or uniform density
- Overlapping vs. Separated clusters

---

## Feature Selection
Not all features of our data are meaningful for clustering

- Closely related to dimension reduction
    - picks subsets of dimensions instead of linear combinations.

- balancing act of interpretability vs less dimensions needed.

- Can be worked into clustering algorithms since some clusters may depend on certain features.

Clustering methods which incorporate feature selection are Co-Clusterers

---

## Probabilistic Models

- Core idea: model data from a generative process which exposes clusters
- Maximum Likelihood Fit
- GMM with Anderson-Darling test.
- EM (expectation maximization) approach to generative models
    - GMM with Numerical data
    - Bernoulli model for categorical
    - Hidden Markov Model (HMM) for sequence data
- Soft K-Means example

---

## Example: Gaussian Mixture Models:
Explain EM update process

---

## Distance-based Algorithms:
- *can* be related to generative algorithms since the probability distributions typically use a distance metric.
    - GMM roughly K-MEANS: many distance-based algorithms can be viewed as reductions/simplifications of generative algorithms.

---


## Distance-based cont...:
Can be broadly categorized into two types:
- **Flat:** Data divided into clusters in one shot
    - K-MEANS, K-MEDIANS, and K-MEDIODS
- **Hierarchical:** Clusters expressed hierarchically typically via a dendrogram at varying levels of granularity
    - Agglomerative: Bottom-Up
    - Divisive: Top-Down

---

## Example: K-Means

Show how K-Means / Medians works

---

## Example: Agglomerative / Single-linkage

Show how it works and dendrogram to prep for George's talk

---

## Density/Grid-based Methods:
- Explore the *space* of the data at varying granularity.
- DBSCAN
- Only natural on continuous continuous space
- Struggle with high dimension density calculations

--- 

## Dimension Reduction:
Can be viewed as a form of vertical clustering (clustering columns in our data matrix)
- Attempts to do clustering and dimension reduction in one step exist (co-clustering):
    - matrix factorization, spectral clustering, etc.

---

## Non-negative Matrix Factorization

Description and interpretation

--- 

## Spectral Methods:
- Graph-based
- Converts data into a graph with edge weights
    - clustering becomes finding optimal cuts 

Should expand on this for better interpretation

---

## High-dimensional stuff

- leads to problems in distance-based algorithms 

--- 

## Evaluation Metrics

- External
- Internal

---

## Silhouette Score:
- An internal evaluation metric commonly used
    - referenced in a couple mapper papers.
