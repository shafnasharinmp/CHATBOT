'''To work with open3d'''
#pip install open3d

import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = np.load("3d_shape_points_data.npz")
print(data.files)

array = data['points']
print(array)

array.shape

import open3d as o3d
o3d.visualization.webrtc_server.enable_webrtc()

# Step 1: Load and Visualize the 3D Data
def load_and_visualize(filename):
    import numpy as np
    import open3d as o3d

    # Load .npz file
    data = np.load(filename)
    points = data["points"]  # Ensure the correct key

    # Convert to Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Visualize
    o3d.visualization.draw_geometries([pcd], window_name="Original 3D Point Cloud")
    return pcd

# Execute the function
pcd = load_and_visualize('3d_shape_points_data.npz')

# Load and visualize the 3D point cloud using matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data
data = np.load('3d_shape_points_data.npz')
points = data['points']

# Create 3D scatter plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot points
scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2],
                    c=points[:, 2],  # Color by z-coordinate
                    cmap='viridis',
                    s=1)  # Point size

# Add a color bar
plt.colorbar(scatter)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Point Cloud Visualization')

# Show the plot
plt.show()

# Print some basic statistics about the point cloud
print("\
Point Cloud Statistics:")
print(f"Number of points: {len(points)}")
print(f"Coordinate ranges:")
print(f"X: [{points[:, 0].min():.2f}, {points[:, 0].max():.2f}]")
print(f"Y: [{points[:, 1].min():.2f}, {points[:, 1].max():.2f}]")
print(f"Z: [{points[:, 2].min():.2f}, {points[:, 2].max():.2f}]")

import numpy as np
from sklearn.neighbors import LocalOutlierFactor
from scipy.spatial import cKDTree

def preprocess_point_cloud(points, n_neighbors=20, contamination=0.1, voxel_size=0.01):
    # Remove statistical outliers using Local Outlier Factor
    lof = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination)
    outlier_labels = lof.fit_predict(points)
    points_denoised = points[outlier_labels == 1]

    # Voxel grid downsampling
    # Create a grid of voxels
    voxel_coords = np.floor(points_denoised / voxel_size)
    # Dictionary to store points in each voxel
    voxel_dict = {}
    for i, coord in enumerate(voxel_coords):
        voxel_dict.setdefault(tuple(coord), []).append(points_denoised[i])
    # Calculate centroid for each voxel
    points_downsampled = np.array([np.mean(voxel_points, axis=0)
                                 for voxel_points in voxel_dict.values()])

    # Normalize to center
    centroid = np.mean(points_downsampled, axis=0)
    points_normalized = points_downsampled - centroid

    # Scale to unit cube
    scale = np.max(np.abs(points_normalized))
    points_normalized = points_normalized / scale

    return points_normalized

# Load the original data
data = np.load('3d_shape_points_data.npz')
points = data['points']

# Apply preprocessing
processed_points = preprocess_point_cloud(points)

# Visualize original vs processed points
fig = plt.figure(figsize=(15, 7))

# Original points
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(points[:, 0], points[:, 1], points[:, 2],
           c=points[:, 2], cmap='viridis', s=1)
ax1.set_title('Original Point Cloud')

# Processed points
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(processed_points[:, 0], processed_points[:, 1], processed_points[:, 2],
           c=processed_points[:, 2], cmap='viridis', s=1)
ax2.set_title('Preprocessed Point Cloud\
(Denoised, Downsampled, Normalized)')

plt.tight_layout()
plt.show()

# Print statistics about the preprocessing
print("\
Preprocessing Statistics:")
print(f"Original number of points: {len(points)}")
print(f"Processed number of points: {len(processed_points)}")
print("\
Bounding box before preprocessing:")
print(f"X: [{points[:, 0].min():.2f}, {points[:, 0].max():.2f}]")
print(f"Y: [{points[:, 1].min():.2f}, {points[:, 1].max():.2f}]")
print(f"Z: [{points[:, 2].min():.2f}, {points[:, 2].max():.2f}]")
print("\
Bounding box after preprocessing (normalized):")
print(f"X: [{processed_points[:, 0].min():.2f}, {processed_points[:, 0].max():.2f}]")
print(f"Y: [{processed_points[:, 1].min():.2f}, {processed_points[:, 1].max():.2f}]")
print(f"Z: [{processed_points[:, 2].min():.2f}, {processed_points[:, 2].max():.2f}]")

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to analyze deformations using PCA
def analyze_deformations(points):
    # Perform PCA
    pca = PCA(n_components=3)
    pca.fit(points)
    explained_variance = pca.explained_variance_ratio_

    print("Explained Variance by Components:", explained_variance)

    # Calculate deformation magnitudes (distance from mean)
    mean_point = np.mean(points, axis=0)
    deformations = np.linalg.norm(points - mean_point, axis=1)

    # Normalize deformation magnitudes for color mapping
    colors = (deformations - deformations.min()) / (deformations.max() - deformations.min())

    return explained_variance, colors

# Load preprocessed points
data = np.load('shape_reconstruction.npz')
processed_points = data['reconstructed_points']

# Analyze deformations
explained_variance, colors = analyze_deformations(processed_points)

# Visualize deformation areas
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with color mapping based on deformations
scatter = ax.scatter(processed_points[:, 0], processed_points[:, 1], processed_points[:, 2],
                      c=colors, cmap='coolwarm', s=1)

# Add color bar
plt.colorbar(scatter, label='Deformation Magnitude')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Deformation Analysis using PCA')

plt.show()

# Print explained variance
print("Explained Variance by PCA Components:")
for i, var in enumerate(explained_variance):
    print(f"Component {i+1}: {var:.6f}")

from scipy.spatial import cKDTree

def reconstruct_shape(points, voxel_size=0.005, max_iterations=50):
    # Clone the original points as the target
    target_points = points.copy()

    # Initialize transformation matrix (identity)
    transformation = np.eye(4)

    for iteration in range(max_iterations):
        # Build KDTree for nearest neighbor search
        tree = cKDTree(target_points)
        distances, indices = tree.query(points)

        # Compute centroids
        source_centroid = np.mean(points, axis=0)
        target_centroid = np.mean(target_points[indices], axis=0)

        # Center the points
        source_centered = points - source_centroid
        target_centered = target_points[indices] - target_centroid

        # Compute covariance matrix
        H = np.dot(source_centered.T, target_centered)

        # Singular Value Decomposition (SVD)
        U, _, Vt = np.linalg.svd(H)
        R = np.dot(Vt.T, U.T)

        # Ensure a proper rotation matrix (det(R) = 1)
        if np.linalg.det(R) < 0:
            Vt[-1, :] *= -1
            R = np.dot(Vt.T, U.T)

        # Compute translation
        t = target_centroid - np.dot(R, source_centroid)

        # Update transformation matrix
        transformation[:3, :3] = R
        transformation[:3, 3] = t

        # Apply transformation
        points = np.dot(points, R.T) + t

        # Check convergence (if distances are small enough)
        if np.mean(distances) < voxel_size:
            break

    # Downsample using voxel grid
    voxel_coords = np.floor(points / voxel_size)
    voxel_dict = {}
    for i, coord in enumerate(voxel_coords):
        voxel_dict.setdefault(tuple(coord), []).append(points[i])
    points_downsampled = np.array([np.mean(voxel_points, axis=0) for voxel_points in voxel_dict.values()])

    return points_downsampled

# Load preprocessed points
data = np.load('shape_reconstruction.npz')
processed_points = data['reconstructed_points']

# Reconstruct the shape
reconstructed_points = reconstruct_shape(processed_points)

# Visualize the reconstructed shape
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of reconstructed points
scatter = ax.scatter(reconstructed_points[:, 0], reconstructed_points[:, 1], reconstructed_points[:, 2],
                      c=reconstructed_points[:, 2], cmap='plasma', s=1)

# Add color bar
plt.colorbar(scatter, label='Z-coordinate')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Reconstructed Shape using ICP')

plt.show()

# Save the reconstructed points
np.savez('final_reconstructed_shape.npz', reconstructed_points=reconstructed_points)

# Print completion message
print("Reconstruction completed and saved to 'final_reconstructed_shape.npz'.")

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

def evaluate_reconstruction(original_points, reconstructed_points):
    """Evaluates the reconstruction accuracy using nearest-neighbor distances."""
    if original_points.shape[1] != reconstructed_points.shape[1]:
        raise ValueError("Original and reconstructed points must have the same dimensions!")

    # KDTree for nearest neighbor search
    tree = cKDTree(reconstructed_points)
    distances, _ = tree.query(original_points)

    # Compute error metrics
    mse = np.mean(distances ** 2)
    rmse = np.sqrt(mse)
    max_error = np.max(distances)
    median_error = np.median(distances)

    print("Reconstruction Evaluation Metrics:")
    print(f"Mean Squared Error (MSE): {mse:.5f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.5f}")
    print(f"Maximum Error: {max_error:.5f}")
    print(f"Median Error: {median_error:.5f}")

    return mse, rmse, max_error, median_error

# Load original and reconstructed points safely
try:
    original_data = np.load('3d_shape_points_data.npz')
    original_points = original_data.get('points', None)
    if original_points is None:
        raise KeyError("Key 'points' not found in 3d_shape_points_data.npz")

    reconstructed_data = np.load('final_reconstructed_shape.npz')
    reconstructed_points = reconstructed_data.get('reconstructed_points', None)
    if reconstructed_points is None:
        raise KeyError("Key 'reconstructed_points' not found in final_reconstructed_shape.npz")

except Exception as e:
    print(f"Error loading files: {e}")
    exit()

# Evaluate reconstruction
metrics = evaluate_reconstruction(original_points, reconstructed_points)

# Compute error distances using KDTree
tree = cKDTree(reconstructed_points)
distances, _ = tree.query(original_points)

# Plot error distribution
plt.figure(figsize=(10, 6))
plt.hist(distances, bins=50, density=True, alpha=0.7, color='blue')
plt.xlabel('Point-to-Point Distance')
plt.ylabel('Density')
plt.title('Distribution of Reconstruction Errors')
plt.grid(True, alpha=0.3)
plt.show()

# Function to save point clouds in PLY format
def save_point_cloud(points, filename):
    """Saves a point cloud to a PLY file."""
    header = "\n".join([
        "ply",
        "format ascii 1.0",
        f"element vertex {len(points)}",
        "property float x",
        "property float y",
        "property float z",
        "end_header"
    ])

    try:
        with open(filename, 'w') as f:
            f.write(header + "\n")
            np.savetxt(f, points, fmt="%.6f")
        print(f"Saved point cloud to {filename}")
    except Exception as e:
        print(f"Error saving {filename}: {e}")

# Save original and reconstructed point clouds
save_point_cloud(original_points, 'original_shape.ply')
save_point_cloud(reconstructed_points, 'reconstructed_shape.ply')

# Plot original and reconstructed shapes
fig = plt.figure(figsize=(15, 7))

# Original Shape
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(original_points[:, 0], original_points[:, 1], original_points[:, 2],
            c=original_points[:, 2], cmap='viridis', s=1)
ax1.set_title('Original Shape')

# Reconstructed Shape
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(reconstructed_points[:, 0], reconstructed_points[:, 1], reconstructed_points[:, 2],
            c=reconstructed_points[:, 2], cmap='viridis', s=1)
ax2.set_title('Reconstructed Shape')

plt.tight_layout()
plt.show()



