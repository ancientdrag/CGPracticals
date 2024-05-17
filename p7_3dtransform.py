import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the 3D cube vertices
cube_vertices = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
])


# Define the transformation matrices
scaling_matrix = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
])

rotation_matrix = np.array([
    [np.cos(np.pi/4), -np.sin(np.pi/4), 0],
    [np.sin(np.pi/4), np.cos(np.pi/4), 0],
    [0, 0, 1]
])

translation_matrix = np.array([
    [1, 0, 0, 4],
    [0, 1, 0, 3],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

# Apply the transformations to the cube vertices
transformed_cube_vertices = cube_vertices.dot(scaling_matrix).dot(rotation_matrix) + translation_matrix[:3,3]

# Perform parallel projection
parallel_projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0]
])
projected_cube_vertices = transformed_cube_vertices[:, :2].dot(parallel_projection_matrix)

# Perform perspective projection
focal_length = 5
perspective_projection_matrix = np.array([
    [focal_length, 0, 0],
    [0, focal_length, 0]
])
projected_cube_vertices_perspective = transformed_cube_vertices[:, :2].dot(perspective_projection_matrix) / transformed_cube_vertices[:, 2:]

# Plot the original and transformed 3D cube
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(cube_vertices[:, 0], cube_vertices[:, 1], cube_vertices[:, 2], color='blue')
ax.scatter(transformed_cube_vertices[:, 0], transformed_cube_vertices[:, 1], transformed_cube_vertices[:, 2], color='red')
plt.show()

# Plot the parallel projection
plt.scatter(projected_cube_vertices[:, 0], projected_cube_vertices[:, 1])
plt.title('Parallel Projection')
plt.show()

# Plot the perspective projection
plt.scatter(projected_cube_vertices_perspective[:, 0], projected_cube_vertices_perspective[:, 1])
plt.title('Perspective Projection')
plt.show()
