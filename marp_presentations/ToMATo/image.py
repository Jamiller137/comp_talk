import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import kneighbors_graph
from sklearn.cluster import KMeans

# 1. Create non-convex "two moons" dataset (18 points)
# Upper moon (cluster 1)
angles1 = np.linspace(0, np.pi, 9)
moon1 = np.column_stack([np.cos(angles1), np.sin(angles1)])

# Lower moon (cluster 2) - shifted and flipped
angles2 = np.linspace(0, np.pi, 9)
moon2 = np.column_stack([1 - np.cos(angles2), -np.sin(angles2) - 0.5])

X = np.vstack([moon1, moon2])
true_labels = np.array([0] * 9 + [1] * 9)

# 2. Build a symmetric binary adjacency matrix (k-nearest neighbors)
n_neighbors = 2
A = kneighbors_graph(
    X, n_neighbors=n_neighbors, mode="connectivity", include_self=False
)
# Make symmetric: if either i->j or j->i exists, then edge exists
A = (A + A.T) > 0
A = A.astype(float)
A_array = A.toarray()

# 3. Compute normalized graph Laplacian: L_sym = I - D^{-1/2} A D^{-1/2}
D = np.diag(A_array.sum(axis=1))
D_inv_sqrt = np.diag(1.0 / np.sqrt(np.maximum(np.diag(D), 1e-12)))
L = np.eye(A_array.shape[0]) - D_inv_sqrt @ A_array @ D_inv_sqrt

# 4. Eigen decomposition
eigvals, eigvecs = np.linalg.eigh(L)
idx = np.argsort(eigvals)
eigvals, eigvecs = eigvals[idx], eigvecs[:, idx]

# Find spectral gaps
gaps = np.diff(eigvals)
largest_gap_idx = 3  # Gap between 4th and 5th eigenvalue

print("Eigenvalues (smallest to largest):")
print(np.round(eigvals[:10], 4))
print("\nEigenvalue gaps:")
for i in range(min(10, len(gaps))):
    print(f"  Gap {i} (λ_{i+1} - λ_{i}): {gaps[i]:.4f}")
print(
    f"\nHighlighted spectral gap at index {largest_gap_idx}: "
    f"{gaps[largest_gap_idx]:.4f}"
)

# 5. Create embeddings
embedding_1_2 = eigvecs[:, 0:2]  # 1st and 2nd eigenvectors
embedding_2_3 = eigvecs[:, 1:3]  # 2nd and 3rd eigenvectors

# 6. K-Means clustering in spectral space
kmeans = KMeans(n_clusters=2, n_init=20, random_state=42)
labels = kmeans.fit_predict(embedding_1_2)

# 7. Visualization
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

# Plot 1: Original data (ground truth)
ax1 = fig.add_subplot(gs[0, 0])
scatter1 = ax1.scatter(
    X[:, 0], X[:, 1], c=true_labels, cmap="viridis", s=200, zorder=3
)
for i in range(len(X)):
    ax1.text(
        X[i, 0],
        X[i, 1],
        str(i),
        ha="center",
        va="center",
        fontsize=8,
        color="white",
        weight="bold",
    )
ax1.set_title("Original Non-Convex Data\n(True Labels)")
ax1.set_aspect("equal")
ax1.grid(True, alpha=0.3)

# Plot 2: KNN Graph
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(X[:, 0], X[:, 1], c="steelblue", s=200, zorder=3)
for i in range(len(X)):
    ax2.text(
        X[i, 0],
        X[i, 1],
        str(i),
        ha="center",
        va="center",
        fontsize=8,
        color="white",
        weight="bold",
    )
    for j in range(i + 1, len(X)):
        if A_array[i, j] > 0:
            ax2.plot(
                [X[i, 0], X[j, 0]],
                [X[i, 1], X[j, 1]],
                "k-",
                alpha=0.3,
                linewidth=1.5,
            )
            # Add edge weight label at midpoint
            mid_x = (X[i, 0] + X[j, 0]) / 2
            mid_y = (X[i, 1] + X[j, 1]) / 2
            ax2.text(
                mid_x,
                mid_y,
                f"{int(A_array[i, j])}",
                ha="center",
                va="center",
                fontsize=7,
                color="red",
                bbox=dict(
                    boxstyle="round,pad=0.3",
                    facecolor="white",
                    edgecolor="none",
                    alpha=0.7,
                ),
            )
ax2.set_title(f"KNN Graph (k={n_neighbors})\nBinary Adjacency Matrix")
ax2.set_aspect("equal")
ax2.grid(True, alpha=0.3)

# Plot 3: Eigenvalue spectrum with gaps
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(range(10), eigvals[:10], "o-", markersize=8, linewidth=2)
ax3.axhline(y=0, color="k", linestyle="--", alpha=0.3)
ax3.set_title("Eigenvalue Spectrum")
ax3.set_xlabel("Index")
ax3.set_ylabel("Eigenvalue")
ax3.grid(True, alpha=0.3)
# Highlight the spectral gap between 4th and 5th eigenvalue
ax3.axvspan(
    largest_gap_idx - 0.3,
    largest_gap_idx + 1.3,
    alpha=0.2,
    color="red",
    label=f"Gap at idx {largest_gap_idx}",
)
ax3.legend()

# Plot 4: Laplacian matrix
ax4 = fig.add_subplot(gs[1, 0])
im2 = ax4.imshow(L, cmap="RdBu_r", vmin=-1, vmax=1)
ax4.set_title("Normalized Laplacian L")
ax4.set_xlabel("Node")
ax4.set_ylabel("Node")
fig.colorbar(im2, ax=ax4, fraction=0.046, pad=0.04)

# Plot 5: Spectral embedding (1st & 2nd eigenvectors)
ax5 = fig.add_subplot(gs[1, 1])
scatter5 = ax5.scatter(
    embedding_1_2[:, 0],
    embedding_1_2[:, 1],
    c=labels,
    cmap="viridis",
    s=200,
    zorder=3,
)
for i in range(len(X)):
    ax5.text(
        embedding_1_2[i, 0],
        embedding_1_2[i, 1],
        str(i),
        ha="center",
        va="center",
        fontsize=8,
        color="white",
        weight="bold",
    )
ax5.set_title("Spectral Embedding\n(1st & 2nd eigenvectors)")
ax5.set_xlabel("1st Eigenvector")
ax5.set_ylabel("2nd Eigenvector")
ax5.axhline(y=0, color="k", linestyle="--", alpha=0.3)
ax5.axvline(x=0, color="k", linestyle="--", alpha=0.3)
ax5.grid(True, alpha=0.3)

# Plot 6: Spectral embedding (2nd & 3rd eigenvectors)
ax6 = fig.add_subplot(gs[1, 2])
scatter6 = ax6.scatter(
    embedding_2_3[:, 0],
    embedding_2_3[:, 1],
    c=labels,
    cmap="viridis",
    s=200,
    zorder=3,
)
for i in range(len(X)):
    ax6.text(
        embedding_2_3[i, 0],
        embedding_2_3[i, 1],
        str(i),
        ha="center",
        va="center",
        fontsize=8,
        color="white",
        weight="bold",
    )
ax6.set_title("Spectral Embedding\n(2nd & 3rd eigenvectors)")
ax6.set_xlabel("2nd Eigenvector")
ax6.set_ylabel("3rd Eigenvector")
ax6.axhline(y=0, color="k", linestyle="--", alpha=0.3)
ax6.axvline(x=0, color="k", linestyle="--", alpha=0.3)
ax6.grid(True, alpha=0.3)

plt.savefig("spectral_clustering_nonconvex.png", dpi=300, bbox_inches="tight")
print("\nFigure saved as 'spectral_clustering_nonconvex.png'")
print(f"\nCluster assignments: {labels}")
print(
    f"Accuracy: {max(np.mean(labels == true_labels), np.mean(labels != true_labels)):.2%}"
)
