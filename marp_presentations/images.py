import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_samples, silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform
import seaborn as sns
from matplotlib.patches import Ellipse
import os
from sklearn.neighbors import NearestNeighbors

# Create output directory
os.makedirs('presentation_images', exist_ok=True)

# Set style for consistent appearance
plt.style.use('seaborn-v0_8')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

def save_figure(fig, filename, dpi=300):
    """Save figure with consistent settings"""
    fig.savefig(f'presentation_images/{filename}', 
                dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)

# 1. Visual Example of Clustering - Basic intuition (UPDATED)
def create_clustering_intuition():
    """Create basic clustering example showing dense regions"""
    np.random.seed(42)
    
    # Generate three well-separated clusters
    centers = [(-3, -3), (3, -3), (0, 3)]
    X, y = make_blobs(n_samples=300, centers=centers, 
                      cluster_std=0.8, random_state=42)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Raw data (UPDATED TITLE)
    ax1.scatter(X[:, 0], X[:, 1], c='gray', alpha=0.6, s=50)
    ax1.set_title('Raw Data', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    ax1.grid(True, alpha=0.3)
    
    # Clustered data
    ax2.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=50)
    ax2.set_title('Identified Clusters', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Feature 1')
    ax2.set_ylabel('Feature 2')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'clustering_intuition.png')

# 3. Manifold/Non-Convex Clusters (UPDATED - removed swiss roll and spiral)
def create_manifold_clusters():
    """Create manifold/non-convex cluster examples"""
    np.random.seed(42)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Two moons
    X_moons, y_moons = make_moons(n_samples=300, noise=0.1, random_state=42)
    ax1.scatter(X_moons[:, 0], X_moons[:, 1], c=y_moons, cmap='viridis', s=50)
    ax1.set_title('Two Interlocking Crescents', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    
    # Concentric circles
    X_circles, y_circles = make_circles(n_samples=300, noise=0.05, 
                                       factor=0.5, random_state=42)
    ax2.scatter(X_circles[:, 0], X_circles[:, 1], c=y_circles, 
                cmap='viridis', s=50)
    ax2.set_title('Concentric Circles', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Feature 1')
    ax2.set_ylabel('Feature 2')
    
    plt.tight_layout()
    save_figure(fig, 'manifold_clusters.png')

# 6. Algorithm Comparison (UPDATED - using single linkage)
def create_algorithm_comparison():
    """Compare different clustering algorithms on the same dataset"""
    np.random.seed(42)
    
    # Create a complex dataset
    X_moons, _ = make_moons(n_samples=150, noise=0.1, random_state=42)
    X_blobs, _ = make_blobs(n_samples=150, centers=2, cluster_std=0.8,
                           center_box=(-8.0, 8.0), random_state=42)
    X = np.vstack([X_moons, X_blobs + [0, -6]])
    
    # Apply different algorithms
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    dbscan = DBSCAN(eps=0.8, min_samples=5)
    single_linkage = AgglomerativeClustering(n_clusters=4, linkage='single')  # UPDATED
    gmm = GaussianMixture(n_components=4, random_state=42)
    
    algorithms = [
        ('K-Means', kmeans),
        ('DBSCAN', dbscan),
        ('Single Linkage', single_linkage),  # UPDATED
        ('GMM', gmm)
    ]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.ravel()
    
    for i, (name, algorithm) in enumerate(algorithms):
        if name == 'GMM':
            labels = algorithm.fit_predict(X)
        else:
            labels = algorithm.fit_predict(X)
        
        scatter = axes[i].scatter(X[:, 0], X[:, 1], c=labels, 
                                 cmap='tab10', s=50, alpha=0.7)
        axes[i].set_title(f'{name} Clustering', fontsize=14, fontweight='bold')
        axes[i].grid(True, alpha=0.3)
        
        # Add cluster centers for K-means
        if name == 'K-Means':
            centers = algorithm.cluster_centers_
            axes[i].scatter(centers[:, 0], centers[:, 1], 
                           c='red', marker='x', s=200, linewidths=3)
    
    plt.tight_layout()
    save_figure(fig, 'algorithm_comparison.png')

# 7. K-Means Visualization (UPDATED - better random initialization)
def create_kmeans_visualization():
    """Show K-means clustering process with truly random initialization"""
    np.random.seed(42)
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.5, random_state=42)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.ravel()
    
    # Manual implementation to control initialization better
    k = 4
    # Random initialization - spread centers widely
    x_min, x_max = X[:, 0].min() - 2, X[:, 0].max() + 2
    y_min, y_max = X[:, 1].min() - 2, X[:, 1].max() + 2
    
    # Initial random centroids (widely spread)
    np.random.seed(123)  # Different seed for more random centers
    initial_centers = np.array([
        [np.random.uniform(x_min, x_max), np.random.uniform(y_min, y_max)]
        for _ in range(k)
    ])
    
    centers = initial_centers.copy()
    
    for iteration in range(4):
        if iteration == 0:
            # Initial state - no assignments yet
            axes[iteration].scatter(X[:, 0], X[:, 1], c='lightgray', s=50, alpha=0.6)
            axes[iteration].scatter(centers[:, 0], centers[:, 1], c='red', 
                                  marker='x', s=200, linewidths=3)
            axes[iteration].set_title('Initial Random Centroids', fontsize=12, fontweight='bold')
        else:
            # Assign points to nearest centroid
            distances = np.sqrt(((X - centers[:, np.newaxis])**2).sum(axis=2))
            labels = np.argmin(distances, axis=0)
            
            # Plot assignments
            axes[iteration].scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
            axes[iteration].scatter(centers[:, 0], centers[:, 1], c='red', 
                                  marker='x', s=200, linewidths=3)
            
            # Update centroids
            new_centers = np.array([X[labels == i].mean(axis=0) for i in range(k)])
            centers = new_centers
            
            axes[iteration].set_title(f'Iteration {iteration}', fontsize=12, fontweight='bold')
        
        axes[iteration].grid(True, alpha=0.3)
        axes[iteration].set_xlabel('Feature 1')
        axes[iteration].set_ylabel('Feature 2')
    
    plt.tight_layout()
    save_figure(fig, 'kmeans_process.png')

# 8. Hierarchical Clustering Dendrogram (UPDATED labels)
def create_dendrogram():
    """Create hierarchical clustering dendrogram"""
    np.random.seed(42)
    X, _ = make_blobs(n_samples=20, centers=3, cluster_std=1.0, random_state=42)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Data points (UPDATED TITLE)
    ax1.scatter(X[:, 0], X[:, 1], s=100, alpha=0.7)
    for i, (x, y) in enumerate(X):
        ax1.annotate(f'{i}', (x, y), xytext=(5, 5), 
                    textcoords='offset points', fontsize=10)
    ax1.set_title('Data', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Dendrogram (UPDATED XLABEL)
    Z = linkage(X, method='single')
    dendrogram(Z, ax=ax2, leaf_font_size=10, leaf_rotation=0)
    ax2.set_title('Single-Linkage Dendrogram', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Index')  # UPDATED
    ax2.set_ylabel('Distance')
    
    plt.tight_layout()
    save_figure(fig, 'dendrogram.png')

# 9. Single-Linkage Chaining Effect (UPDATED - more obvious chaining)
def create_chaining_effect():
    """Show single-linkage chaining effect"""
    np.random.seed(42)
    
    # Create more obvious elongated data with clear bridge
    cluster1 = np.random.multivariate_normal([-4, 0], [[0.3, 0], [0, 0.3]], 40)
    cluster2 = np.random.multivariate_normal([4, 0], [[0.3, 0], [0, 0.3]], 40)
    
    # Create a clear chain of bridge points
    bridge = np.array([[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]]) + \
             np.random.normal(0, 0.05, (5, 2))
    
    # Add some outlier points to make chaining more obvious
    outliers = np.array([[-1, 1], [0, -1], [1, 1]]) + np.random.normal(0, 0.1, (3, 2))
    
    X = np.vstack([cluster1, bridge, outliers, cluster2])
    
    # Apply only single linkage
    single_link = AgglomerativeClustering(n_clusters=2, linkage='single')
    single_labels = single_link.fit_predict(X)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    ax.scatter(X[:, 0], X[:, 1], c=single_labels, cmap='viridis', s=50)
    ax.set_title('Single Linkage (Chaining Effect)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    
    plt.tight_layout()
    save_figure(fig, 'chaining_effect.png')

# 10. DBSCAN Visualization (UPDATED - identify border points)
def create_dbscan_visualization():
    """Show DBSCAN with core, border, and noise points clearly identified"""
    np.random.seed(42)
    
    # Create data with noise
    X_blobs, _ = make_blobs(n_samples=200, centers=3, cluster_std=1.0, 
                           random_state=42)
    # Add noise points
    noise = np.random.uniform(-8, 8, (30, 2))
    X = np.vstack([X_blobs, noise])
    
    # Apply DBSCAN
    eps = 1.2
    min_samples = 5
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(X)
    
    # Identify core points
    nn = NearestNeighbors(radius=eps)
    nn.fit(X)
    core_samples = []
    for i in range(len(X)):
        neighbors = nn.radius_neighbors([X[i]], return_distance=False)[0]
        if len(neighbors) >= min_samples:
            core_samples.append(i)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot points with different markers for core, border, noise
    unique_labels = set(labels)
    colors_db = plt.cm.tab10(np.linspace(0, 1, len(unique_labels)))
    
    for label, color in zip(unique_labels, colors_db):
        if label == -1:  # Noise
            class_member_mask = (labels == label)
            xy = X[class_member_mask]
            ax.scatter(xy[:, 0], xy[:, 1], c='black', marker='x',
                      s=80, alpha=0.8, label='Noise')
        else:
            class_member_mask = (labels == label)
            xy = X[class_member_mask]
            
            # Separate core and border points within this cluster
            cluster_indices = np.where(class_member_mask)[0]
            core_in_cluster = [i for i in cluster_indices if i in core_samples]
            border_in_cluster = [i for i in cluster_indices if i not in core_samples]
            
            # Plot core points
            if core_in_cluster:
                core_xy = X[core_in_cluster]
                ax.scatter(core_xy[:, 0], core_xy[:, 1], c=[color], marker='o',
                          s=80, alpha=0.8, edgecolors='black', linewidth=1,
                          label=f'Cluster {label} (Core)' if len(core_in_cluster) > 0 else '')
            
            # Plot border points  
            if border_in_cluster:
                border_xy = X[border_in_cluster]
                ax.scatter(border_xy[:, 0], border_xy[:, 1], c=[color], marker='s',
                          s=60, alpha=0.6, edgecolors='black', linewidth=1,
                          label=f'Cluster {label} (Border)' if len(border_in_cluster) > 0 else '')
    
    ax.set_title('DBSCAN (eps = 1.2, MinPts = 5)', 
                fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    
    # Custom legend
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',
                             markersize=10, markeredgecolor='black', label='Core Points'),
                      Line2D([0], [0], marker='s', color='w', markerfacecolor='gray',
                             markersize=8, markeredgecolor='black', label='Border Points'),
                      Line2D([0], [0], marker='x', color='w', markerfacecolor='black',
                             markersize=10, label='Noise Points')]
    ax.legend(handles=legend_elements, loc='upper right')
    
    save_figure(fig, 'dbscan_clustering.png')

# 11. GMM Visualization (UPDATED - intensity highlighting instead of circles)
def create_gmm_visualization():
    """Show Gaussian Mixture Model clustering with intensity highlighting"""
    np.random.seed(42)
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.5, random_state=42)
    
    # Fit GMM
    gmm = GaussianMixture(n_components=3, random_state=42)
    labels = gmm.fit_predict(X)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create a grid for plotting intensity
    x_min, x_max = X[:, 0].min() - 2, X[:, 0].max() + 2
    y_min, y_max = X[:, 1].min() - 2, X[:, 1].max() + 2
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    
    # Calculate probability density for each component
    for i in range(3):
        # Get component parameters
        mean = gmm.means_[i]
        cov = gmm.covariances_[i]
        weight = gmm.weights_[i]
        
        # Calculate multivariate normal PDF
        from scipy.stats import multivariate_normal
        rv = multivariate_normal(mean, cov)
        density = rv.pdf(grid_points).reshape(xx.shape)
        
        # Plot contours with different colors
        colors_contour = ['Reds', 'Blues', 'Greens'][i]
        ax.contour(xx, yy, density, levels=5, alpha=0.6, cmap=colors_contour)
        ax.contourf(xx, yy, density, levels=10, alpha=0.2, cmap=colors_contour)
    
    # Plot data points
    scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', 
                        s=60, alpha=0.8, edgecolors='black', linewidth=0.5)
    
    # Plot means
    for i, mean in enumerate(gmm.means_):
        ax.plot(mean[0], mean[1], 'x', color='black', 
                markersize=15, markeredgewidth=4)
    
    ax.set_title('Gaussian Mixture Model with Density Contours', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    
    save_figure(fig, 'gmm_clustering.png')

# 12. Spectral Clustering Intuition (UPDATED - show graph Laplacian construction)
def create_spectral_clustering_steps():
    """Show complete spectral clustering process on two moons dataset"""
    np.random.seed(42)
    
    # Generate two moons data
    X, y_true = make_moons(n_samples=100, noise=0.1, random_state=42)
    
    fig = plt.figure(figsize=(20, 12))
    
    # Step 1: Original data
    ax1 = plt.subplot(2, 3, 1)
    ax1.scatter(X[:, 0], X[:, 1], c='gray', s=50, alpha=0.7)
    ax1.set_title('Step 1: Two Moons Dataset', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    
    # Step 2: Graph construction using RBF kernel
    from sklearn.metrics.pairwise import rbf_kernel
    gamma = 5.0  # RBF kernel parameter
    W = rbf_kernel(X, gamma=gamma)  # Similarity matrix
    
    ax2 = plt.subplot(2, 3, 2)
    im1 = ax2.imshow(W, cmap='viridis', interpolation='nearest')
    ax2.set_title('Step 2: Similarity Matrix W\n(RBF kernel)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Data point j')
    ax2.set_ylabel('Data point i')
    plt.colorbar(im1, ax=ax2, fraction=0.046, pad=0.04)
    
    # Step 3: Graph Laplacian (normalized) - computed manually
    # Compute degree matrix
    D = np.diag(np.sum(W, axis=1))
    D_sqrt_inv = np.diag(1.0 / np.sqrt(np.sum(W, axis=1)))
    
    # Normalized Laplacian: L = D^(-1/2) * (D - W) * D^(-1/2) = I - D^(-1/2) * W * D^(-1/2)
    L_norm = np.eye(len(X)) - D_sqrt_inv @ W @ D_sqrt_inv
    
    ax3 = plt.subplot(2, 3, 3)
    im2 = ax3.imshow(L_norm, cmap='RdBu', interpolation='nearest')
    ax3.set_title('Step 3: Normalized Laplacian\nL = I - D^(-1/2) * W * D^(-1/2)', 
                  fontsize=14, fontweight='bold')
    ax3.set_xlabel('Data point j')
    ax3.set_ylabel('Data point i')
    plt.colorbar(im2, ax=ax3, fraction=0.046, pad=0.04)
    
    # Step 4: Eigenvalue decomposition
    eigenvals, eigenvecs = np.linalg.eigh(L_norm)
    
    ax4 = plt.subplot(2, 3, 4)
    ax4.plot(range(1, 11), eigenvals[:10], 'bo-', linewidth=2, markersize=8)
    ax4.axhline(y=0, color='r', linestyle='--', alpha=0.7)
    ax4.set_title('Step 4: First 10 Eigenvalues', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Eigenvalue index')
    ax4.set_ylabel('Eigenvalue')
    ax4.grid(True, alpha=0.3)
    
    # Highlight the spectral gap
    if len(eigenvals) > 1:
        ax4.annotate('Spectral gap', xy=(2, eigenvals[1]), xytext=(4, eigenvals[1] + 0.3),
                    arrowprops=dict(arrowstyle='->', color='red', lw=2),
                    fontsize=12, color='red', fontweight='bold')
    
    # Step 5: Eigenvector embedding and K-means
    # Use the second smallest eigenvector (Fiedler vector) for 2-cluster case
    embedding = eigenvecs[:, 1].reshape(-1, 1)  # Second smallest eigenvector
    
    ax5 = plt.subplot(2, 3, 5)
    # Color points by the eigenvector values
    scatter = ax5.scatter(X[:, 0], X[:, 1], c=embedding.flatten(), 
                         cmap='RdYlBu', s=50, alpha=0.8)
    ax5.set_title('Step 5: Eigenvector Embedding\n(Fiedler vector values)', 
                  fontsize=14, fontweight='bold')
    ax5.set_xlabel('Feature 1')
    ax5.set_ylabel('Feature 2')
    ax5.grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=ax5, fraction=0.046, pad=0.04)
    
    # Step 6: Apply K-means to eigenvector
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    spectral_labels = kmeans.fit_predict(embedding)
    
    ax6 = plt.subplot(2, 3, 6)
    ax6.scatter(X[:, 0], X[:, 1], c=spectral_labels, cmap='viridis', s=50, alpha=0.8)
    ax6.set_title('Step 6: Final Spectral Clustering Result', 
                  fontsize=14, fontweight='bold')
    ax6.set_xlabel('Feature 1')
    ax6.set_ylabel('Feature 2')
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'spectral_clustering_steps.png')
    
    # Create an additional plot showing the 1D eigenvector values
    fig2, (ax_top, ax_bottom) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Top: 2D data colored by eigenvector values
    scatter = ax_top.scatter(X[:, 0], X[:, 1], c=embedding.flatten(), 
                            cmap='RdYlBu', s=80, alpha=0.8, edgecolors='black', linewidth=0.5)
    ax_top.set_title('Two Moons Data Colored by Fiedler Vector Values', 
                     fontsize=16, fontweight='bold')
    ax_top.set_xlabel('Feature 1')
    ax_top.set_ylabel('Feature 2')
    ax_top.grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=ax_top, fraction=0.046, pad=0.04, label='Eigenvector Value')
    
    # Bottom: 1D histogram of eigenvector values showing the clustering
    ax_bottom.hist(embedding.flatten(), bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    ax_bottom.axvline(x=0, color='red', linestyle='--', linewidth=2, 
                     label='K-means threshold (≈ 0)')
    ax_bottom.set_title('Distribution of Fiedler Vector Values\n(K-means separates around 0)', 
                       fontsize=16, fontweight='bold')
    ax_bottom.set_xlabel('Eigenvector Value')
    ax_bottom.set_ylabel('Frequency')
    ax_bottom.grid(True, alpha=0.3)
    ax_bottom.legend()
    
    plt.tight_layout()
    save_figure(fig2, 'spectral_embedding_analysis.png')


# 13. Silhouette Analysis (UPDATED - include dataset and clustering plots)
def create_silhouette_analysis():
    """Create silhouette analysis visualization with dataset plots"""
    np.random.seed(42)
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, 
                          random_state=42)
    
    fig = plt.figure(figsize=(20, 12))
    
    # Test different numbers of clusters
    n_clusters_range = [2, 3, 4, 5]
    
    for idx, n_clusters in enumerate(n_clusters_range):
        # Silhouette plot
        ax_silhouette = plt.subplot(2, 4, idx + 1)
        
        # Dataset plot
        ax_scatter = plt.subplot(2, 4, idx + 5)
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        cluster_labels = kmeans.fit_predict(X)
        
        # Calculate silhouette scores
        silhouette_avg = silhouette_score(X, cluster_labels)
        sample_silhouette_values = silhouette_samples(X, cluster_labels)
        
        # Silhouette plot
        y_lower = 10
        colors_sil = plt.cm.tab10(np.linspace(0, 1, n_clusters))
        
        for i in range(n_clusters):
            cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
            cluster_silhouette_values.sort()
            
            size_cluster_i = cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i
            
            ax_silhouette.fill_betweenx(np.arange(y_lower, y_upper),
                                       0, cluster_silhouette_values,
                                       facecolor=colors_sil[i], edgecolor=colors_sil[i], 
                                       alpha=0.7)
            
            y_lower = y_upper + 10
        
        ax_silhouette.axvline(x=silhouette_avg, color="red", linestyle="--", linewidth=2)
        ax_silhouette.set_title(f'k={n_clusters}\nSilhouette Score={silhouette_avg:.3f}', 
                               fontsize=12, fontweight='bold')
        ax_silhouette.set_xlabel('Silhouette Coefficient')
        ax_silhouette.set_ylabel('Cluster Label')
        ax_silhouette.set_xlim([-0.1, 1])
        
        # Dataset plot with clustering
        scatter = ax_scatter.scatter(X[:, 0], X[:, 1], c=cluster_labels, 
                                   cmap='tab10', s=50, alpha=0.7)
        
        # Plot centroids
        centers = kmeans.cluster_centers_
        ax_scatter.scatter(centers[:, 0], centers[:, 1], c='red', 
                          marker='x', s=200, linewidths=3)
        
        ax_scatter.set_title(f'K-Means Clustering (k={n_clusters})', 
                            fontsize=12, fontweight='bold')
        ax_scatter.set_xlabel('Feature 1')
        ax_scatter.set_ylabel('Feature 2')
        ax_scatter.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'silhouette_analysis.png')

# Generate all other functions that weren't updated...
def create_spherical_clusters():
    """Create spherical/convex cluster example"""
    np.random.seed(42)
    X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.2, 
                      center_box=(-8.0, 8.0), random_state=42)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='tab10', s=60, alpha=0.7)
    
    # Add circles to show spherical nature
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    centers = kmeans.fit(X).cluster_centers_
    
    for i, center in enumerate(centers):
        # Calculate radius as 2 standard deviations
        cluster_points = X[y == i]
        distances = np.linalg.norm(cluster_points - center, axis=1)
        radius = 2 * np.std(distances)
        
        circle = plt.Circle(center, radius, fill=False, 
                          color=colors[i % len(colors)], 
                          linewidth=2, linestyle='--', alpha=0.8)
        ax.add_patch(circle)
        ax.plot(center[0], center[1], 'x', color='black', 
                markersize=12, markeredgewidth=3)
    
    ax.set_title('Spherical/Convex Clusters', fontsize=16, fontweight='bold')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    save_figure(fig, 'spherical_clusters.png')

def create_density_clusters():
    """Create clusters with varying densities"""
    np.random.seed(42)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Uniform density
    X_uniform, y_uniform = make_blobs(n_samples=300, centers=3, 
                                     cluster_std=1.0, random_state=42)
    ax1.scatter(X_uniform[:, 0], X_uniform[:, 1], c=y_uniform, 
                cmap='viridis', s=50, alpha=0.7)
    ax1.set_title('Uniform Density Clusters', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Varying density
    # Dense cluster
    dense_cluster = np.random.multivariate_normal([0, 0], [[0.5, 0], [0, 0.5]], 150)
    # Medium cluster  
    medium_cluster = np.random.multivariate_normal([4, 0], [[2, 0], [0, 2]], 100)
    # Sparse cluster
    sparse_cluster = np.random.multivariate_normal([0, 4], [[4, 0], [0, 4]], 50)
    
    ax2.scatter(dense_cluster[:, 0], dense_cluster[:, 1], 
                c='red', s=50, alpha=0.7, label='Dense')
    ax2.scatter(medium_cluster[:, 0], medium_cluster[:, 1], 
                c='blue', s=50, alpha=0.7, label='Medium')
    ax2.scatter(sparse_cluster[:, 0], sparse_cluster[:, 1], 
                c='green', s=50, alpha=0.7, label='Sparse')
    ax2.set_title('Varying Density Clusters', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    save_figure(fig, 'density_clusters.png')

def create_separation_clusters():
    """Create well-separated and connected cluster examples"""
    np.random.seed(42)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Well-separated
    X_sep, y_sep = make_blobs(n_samples=300, centers=3, cluster_std=0.8,
                              center_box=(-10.0, 10.0), random_state=42)
    ax1.scatter(X_sep[:, 0], X_sep[:, 1], c=y_sep, cmap='viridis', s=50)
    ax1.set_title('Well-Separated Clusters', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Connected clusters (closer together)
    centers_conn = [(-1, 0), (1, 0), (0, 1.5)]
    X_conn, y_conn = make_blobs(n_samples=300, centers=centers_conn,
                               cluster_std=0.6, random_state=42)
    ax2.scatter(X_conn[:, 0], X_conn[:, 1], c=y_conn, cmap='viridis', s=50)
    ax2.set_title('Connected/Overlapping Clusters', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'separation_clusters.png')

# Main execution
if __name__ == "__main__":
    print("Generating updated clustering presentation images...")
    
    # Generate all images
    create_clustering_intuition()
    print("✓ Updated clustering intuition")
    
    create_spherical_clusters()
    print("✓ Created spherical clusters")
    
    create_manifold_clusters()
    print("✓ Updated manifold clusters (removed swiss roll and spiral)")
    
    create_density_clusters()
    print("✓ Created density variation clusters")
    
    create_separation_clusters()
    print("✓ Created separation clusters")
    
    create_algorithm_comparison()
    print("✓ Updated algorithm comparison (single linkage)")
    
    create_kmeans_visualization()
    print("✓ Updated K-means visualization (better random init)")
    
    create_dendrogram()
    print("✓ Updated dendrogram (fixed labels)")
    
    create_chaining_effect()
    print("✓ Updated chaining effect (more obvious)")
    
    create_dbscan_visualization()
    print("✓ Updated DBSCAN visualization (border points identified)")
    
    create_gmm_visualization()
    print("✓ Updated GMM visualization (intensity highlighting)")
    
    create_spectral_clustering_steps()
    print("✓ Updated spectral clustering (graph Laplacian construction)")
    
    create_silhouette_analysis()
    print("✓ Updated silhouette analysis (with dataset plots)")
    
    print(f"\nAll updated images saved to 'presentation_images/' directory!")
