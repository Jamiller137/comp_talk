import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles, make_moons, make_swiss_roll
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_samples, silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform
import seaborn as sns
from matplotlib.patches import Ellipse
import os

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

# 1. Visual Example of Clustering - Basic intuition
def create_clustering_intuition():
    """Create basic clustering example showing dense regions"""
    np.random.seed(42)
    
    # Generate three well-separated clusters
    centers = [(-3, -3), (3, -3), (0, 3)]
    X, y = make_blobs(n_samples=300, centers=centers, 
                      cluster_std=0.8, random_state=42)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Raw data
    ax1.scatter(X[:, 0], X[:, 1], c='gray', alpha=0.6, s=50)
    ax1.set_title('Raw Data Points', fontsize=14, fontweight='bold')
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

# 2. Types of Clusters - Spherical/Convex
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

# 3. Manifold/Non-Convex Clusters
def create_manifold_clusters():
    """Create manifold/non-convex cluster examples"""
    np.random.seed(42)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 12))
    
    # Two moons
    X_moons, y_moons = make_moons(n_samples=300, noise=0.1, random_state=42)
    ax1.scatter(X_moons[:, 0], X_moons[:, 1], c=y_moons, cmap='viridis', s=50)
    ax1.set_title('Two Interlocking Crescents', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Concentric circles
    X_circles, y_circles = make_circles(n_samples=300, noise=0.05, 
                                       factor=0.5, random_state=42)
    ax2.scatter(X_circles[:, 0], X_circles[:, 1], c=y_circles, 
                cmap='viridis', s=50)
    ax2.set_title('Concentric Circles', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Swiss roll (3D to 2D projection)
    X_swiss, color_swiss = make_swiss_roll(n_samples=300, noise=0.1, 
                                          random_state=42)
    ax3.scatter(X_swiss[:, 0], X_swiss[:, 2], c=color_swiss, 
                cmap='viridis', s=50)
    ax3.set_title('Swiss Roll (2D Projection)', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # Spiral clusters
    theta = np.linspace(0, 4*np.pi, 150)
    r1 = theta + np.random.normal(0, 0.3, 150)
    r2 = theta + np.pi + np.random.normal(0, 0.3, 150)
    
    x1 = r1 * np.cos(theta)
    y1 = r1 * np.sin(theta)
    x2 = r2 * np.cos(theta + np.pi)
    y2 = r2 * np.sin(theta + np.pi)
    
    ax4.scatter(x1, y1, c='red', s=50, alpha=0.7, label='Spiral 1')
    ax4.scatter(x2, y2, c='blue', s=50, alpha=0.7, label='Spiral 2')
    ax4.set_title('Spiral Clusters', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.tight_layout()
    save_figure(fig, 'manifold_clusters.png')

# 4. Density Variations
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

# 5. Well-separated vs Connected
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

# 6. Algorithm Comparison
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
    hierarchical = AgglomerativeClustering(n_clusters=4, linkage='single')
    gmm = GaussianMixture(n_components=4, random_state=42)
    
    algorithms = [
        ('K-Means', kmeans),
        ('DBSCAN', dbscan),
        ('Hierarchical', hierarchical),
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

# 7. K-Means Visualization
def create_kmeans_visualization():
    """Show K-means clustering process"""
    np.random.seed(42)
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.5, random_state=42)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.ravel()
    
    # Show iterations
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=1, max_iter=1)
    
    for i in range(4):
        if i == 0:
            # Initial random centroids
            centers = kmeans.fit(X).cluster_centers_
            labels = np.zeros(len(X))  # No assignment yet
            axes[i].scatter(X[:, 0], X[:, 1], c='gray', s=50, alpha=0.6)
        else:
            kmeans.max_iter = i
            labels = kmeans.fit_predict(X)
            centers = kmeans.cluster_centers_
            axes[i].scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
        
        axes[i].scatter(centers[:, 0], centers[:, 1], c='red', 
                       marker='x', s=200, linewidths=3)
        axes[i].set_title(f'K-Means: {"Initial" if i==0 else f"Iteration {i}"}', 
                         fontsize=14, fontweight='bold')
        axes[i].grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'kmeans_process.png')

# 8. Hierarchical Clustering Dendrogram
def create_dendrogram():
    """Create hierarchical clustering dendrogram"""
    np.random.seed(42)
    X, _ = make_blobs(n_samples=20, centers=3, cluster_std=1.0, random_state=42)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Data points
    ax1.scatter(X[:, 0], X[:, 1], s=100, alpha=0.7)
    for i, (x, y) in enumerate(X):
        ax1.annotate(f'{i}', (x, y), xytext=(5, 5), 
                    textcoords='offset points', fontsize=10)
    ax1.set_title('Data Points with Labels', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Dendrogram
    Z = linkage(X, method='single')
    dendrogram(Z, ax=ax2, leaf_font_size=10, leaf_rotation=0)
    ax2.set_title('Single-Linkage Dendrogram', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Sample Index')
    ax2.set_ylabel('Distance')
    
    plt.tight_layout()
    save_figure(fig, 'dendrogram.png')

# 9. Single-Linkage Chaining Effect
def create_chaining_effect():
    """Show single-linkage chaining effect"""
    np.random.seed(42)
    
    # Create elongated data
    cluster1 = np.random.multivariate_normal([0, 0], [[0.5, 0], [0, 0.1]], 50)
    cluster2 = np.random.multivariate_normal([4, 0], [[0.1, 0], [0, 0.5]], 50)
    # Add connecting points
    bridge = np.array([[1, 0], [2, 0], [3, 0]]) + np.random.normal(0, 0.1, (3, 2))
    X = np.vstack([cluster1, bridge, cluster2])
    
    # Compare single vs complete linkage
    single_link = AgglomerativeClustering(n_clusters=2, linkage='single')
    complete_link = AgglomerativeClustering(n_clusters=2, linkage='complete')
    
    single_labels = single_link.fit_predict(X)
    complete_labels = complete_link.fit_predict(X)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.scatter(X[:, 0], X[:, 1], c=single_labels, cmap='viridis', s=50)
    ax1.set_title('Single Linkage (Chaining Effect)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    ax2.scatter(X[:, 0], X[:, 1], c=complete_labels, cmap='viridis', s=50)
    ax2.set_title('Complete Linkage', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'chaining_effect.png')

# 10. DBSCAN Visualization
def create_dbscan_visualization():
    """Show DBSCAN with core, border, and noise points"""
    np.random.seed(42)
    
    # Create data with noise
    X_blobs, _ = make_blobs(n_samples=200, centers=3, cluster_std=1.0, 
                           random_state=42)
    # Add noise points
    noise = np.random.uniform(-8, 8, (30, 2))
    X = np.vstack([X_blobs, noise])
    
    # Apply DBSCAN
    dbscan = DBSCAN(eps=1.2, min_samples=5)
    labels = dbscan.fit_predict(X)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot points
    unique_labels = set(labels)
    colors_db = plt.cm.tab10(np.linspace(0, 1, len(unique_labels)))
    
    for label, color in zip(unique_labels, colors_db):
        if label == -1:  # Noise
            color = 'black'
            marker = 'x'
            size = 50
            alpha = 0.5
            label_name = 'Noise'
        else:
            marker = 'o'
            size = 60
            alpha = 0.8
            label_name = f'Cluster {label}'
        
        class_member_mask = (labels == label)
        xy = X[class_member_mask]
        ax.scatter(xy[:, 0], xy[:, 1], c=[color], marker=marker,
                  s=size, alpha=alpha, label=label_name if label != -1 or 
                  sum(labels == -1) > 0 else '')
    
    ax.set_title('DBSCAN: Core, Border, and Noise Points', 
                fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    save_figure(fig, 'dbscan_clustering.png')

# 11. GMM Visualization
def create_gmm_visualization():
    """Show Gaussian Mixture Model clustering"""
    np.random.seed(42)
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.5, random_state=42)
    
    # Fit GMM
    gmm = GaussianMixture(n_components=3, random_state=42)
    labels = gmm.fit_predict(X)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', 
                        s=50, alpha=0.7)
    
    # Plot Gaussian ellipses
    for i in range(3):
        mean = gmm.means_[i]
        cov = gmm.covariances_[i]
        
        # Eigenvalues and eigenvectors for ellipse
        eigenvals, eigenvecs = np.linalg.eigh(cov)
        angle = np.degrees(np.arctan2(eigenvecs[1, 0], eigenvecs[0, 0]))
        
        # 2-sigma ellipse
        width, height = 2 * 2 * np.sqrt(eigenvals)
        ellipse = Ellipse(mean, width, height, angle=angle,
                         fill=False, color=colors[i], linewidth=2, 
                         linestyle='--', alpha=0.8)
        ax.add_patch(ellipse)
        
        ax.plot(mean[0], mean[1], 'x', color='black', 
                markersize=12, markeredgewidth=3)
    
    ax.set_title('Gaussian Mixture Model', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    save_figure(fig, 'gmm_clustering.png')

# 12. Spectral Clustering Intuition
def create_spectral_intuition():
    """Show spectral clustering intuition with graph representation"""
    np.random.seed(42)
    
    # Create two moons
    X, y_true = make_moons(n_samples=100, noise=0.1, random_state=42)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 12))
    
    # Original data
    ax1.scatter(X[:, 0], X[:, 1], c='gray', s=50)
    ax1.set_title('Original Data', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # K-means result (fails)
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X)
    ax2.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', s=50)
    ax2.set_title('K-Means Result (Poor)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Spectral clustering
    from sklearn.cluster import SpectralClustering
    spectral = SpectralClustering(n_clusters=2, random_state=42)
    spectral_labels = spectral.fit_predict(X)
    ax3.scatter(X[:, 0], X[:, 1], c=spectral_labels, cmap='viridis', s=50)
    ax3.set_title('Spectral Clustering Result', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # True clustering
    ax4.scatter(X[:, 0], X[:, 1], c=y_true, cmap='viridis', s=50)
    ax4.set_title('True Clusters', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'spectral_intuition.png')

# 13. Silhouette Analysis
def create_silhouette_analysis():
    """Create silhouette analysis visualization"""
    np.random.seed(42)
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, 
                          random_state=42)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Test different numbers of clusters
    n_clusters_range = [2, 3, 4, 5]
    
    for i, n_clusters in enumerate(n_clusters_range):
        ax = [ax1, ax2, ax3, ax4][i]
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        cluster_labels = kmeans.fit_predict(X)
        
        # Calculate silhouette scores
        silhouette_avg = silhouette_score(X, cluster_labels)
        sample_silhouette_values = silhouette_samples(X, cluster_labels)
        
        y_lower = 10
        for j in range(n_clusters):
            cluster_silhouette_values = sample_silhouette_values[cluster_labels == j]
            cluster_silhouette_values.sort()
            
            size_cluster_j = cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_j
            
            color = plt.cm.tab10(j / n_clusters)
            ax.fill_betweenx(np.arange(y_lower, y_upper),
                           0, cluster_silhouette_values,
                           facecolor=color, edgecolor=color, alpha=0.7)
            
            y_lower = y_upper + 10
        
        ax.axvline(x=silhouette_avg, color="red", linestyle="--", linewidth=2)
        ax.set_title(f'k={n_clusters}, Silhouette Score={silhouette_avg:.3f}', 
                    fontsize=12, fontweight='bold')
        ax.set_xlabel('Silhouette Coefficient Values')
        ax.set_ylabel('Cluster Label')
    
    plt.tight_layout()
    save_figure(fig, 'silhouette_analysis.png')

# Main execution
if __name__ == "__main__":
    print("Generating clustering presentation images...")
    
    # Generate all images
    create_clustering_intuition()
    print("✓ Created clustering intuition")
    
    create_spherical_clusters()
    print("✓ Created spherical clusters")
    
    create_manifold_clusters()
    print("✓ Created manifold clusters")
    
    create_density_clusters()
    print("✓ Created density variation clusters")
    
    create_separation_clusters()
    print("✓ Created separation clusters")
    
    create_algorithm_comparison()
    print("✓ Created algorithm comparison")
    
    create_kmeans_visualization()
    print("✓ Created K-means visualization")
    
    create_dendrogram()
    print("✓ Created dendrogram")
    
    create_chaining_effect()
    print("✓ Created chaining effect visualization")
    
    create_dbscan_visualization()
    print("✓ Created DBSCAN visualization")
    
    create_gmm_visualization()
    print("✓ Created GMM visualization")
    
    create_spectral_intuition()
    print("✓ Created spectral clustering intuition")
    
    create_silhouette_analysis()
    print("✓ Created silhouette analysis")
    
    print(f"\nAll images saved to 'presentation_images/' directory!")
    print("Images created:")
    print("- clustering_intuition.png")
    print("- spherical_clusters.png") 
    print("- manifold_clusters.png")
    print("- density_clusters.png")
    print("- separation_clusters.png")
    print("- algorithm_comparison.png")
    print("- kmeans_process.png")
    print("- dendrogram.png")
    print("- chaining_effect.png")
    print("- dbscan_clustering.png")
    print("- gmm_clustering.png")
    print("- spectral_intuition.png")
    print("- silhouette_analysis.png")
