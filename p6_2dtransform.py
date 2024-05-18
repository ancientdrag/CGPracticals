# for 2D-Translation

import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the original triangle
triangle = np.array([[0, 0], [0, 2], [2, 0], [0,0]])

# Define the translation vector
translation = np.array([2, 1])

# Translate the triangle by adding the translation vector to each vertex
new_triangle = triangle + translation

# Plot the original and translated triangles
plt.plot(triangle[:,0], triangle[:,1], 'bo-', label='Original Triangle')
plt.plot(new_triangle[:,0], new_triangle[:,1], 'go-', label='Translated Triangle')
plt.axis('equal')
plt.legend()
plt.show()


# for 2D-Rotation

import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the original triangle
triangle = np.array([[0, 0], [0, 2], [2, 0], [0,0]])

# Define the rotation angle in degrees
angle_deg = 45

# Convert the rotation angle to radians
angle_rad = np.deg2rad(angle_deg)

# Define the rotation matrix
rotation = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                     [np.sin(angle_rad), np.cos(angle_rad)]])

# Rotate the triangle by multiplying each vertex by the rotation matrix
new_triangle = np.dot(triangle, rotation)

# Plot the original and rotated triangles
plt.plot(triangle[:,0], triangle[:,1], 'yo-', label='Original Triangle')
plt.plot(new_triangle[:,0], new_triangle[:,1], 'go-', label='Rotated Triangle')
plt.axis('equal')
plt.legend()
plt.show()


# for 2D-Scaling

import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the original triangle
triangle = np.array([[0, 0], [0, 2], [2, 0], [0,0]])

# Define the scaling factor
scale_factor = 2

# Define the scaling matrix
scaling = np.array([[scale_factor, 0],
                    [0, scale_factor]])

# Scale the triangle by multiplying each vertex by the scaling matrix
new_triangle = np.dot(triangle, scaling)

# Plot the original and scaled triangles
plt.plot(triangle[:,0], triangle[:,1], 'ro-', label='Original Triangle')
plt.plot(new_triangle[:,0], new_triangle[:,1], 'go-', label='Scaled Triangle')
plt.axis('equal')
plt.legend()
plt.show()
 

# for 2D-Shearing

import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the original triangle
triangle = np.array([[0, 0], [0, 2], [2, 0], [0,0]])

# Define the shearing factor
shear_factor = 2

# Define the shearing matrix
shearing = np.array([[1, shear_factor],
                     [0, 1]])

# Shear the triangle by multiplying each vertex by the shearing matrix
new_triangle = np.dot(triangle, shearing)

# Plot the original and sheared triangles
plt.plot(triangle[:,0], triangle[:,1], 'bo-', label='Original Triangle')
plt.plot(new_triangle[:,0], new_triangle[:,1], 'go-', label='Sheared Triangle')
plt.axis('equal')
plt.legend()
plt.show()
 

# for 2D-Reflection

import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the original triangle
triangle = np.array([[0, 0], [0, 2], [2, 0], [0,0]])

# Define the reflection axis
reflection_axis = np.array([[1, 0], [0, -1]])

# Reflect the triangle by multiplying each vertex by the reflection axis
new_triangle = np.dot(triangle, reflection_axis)

# Plot the original and reflected triangles
plt.plot(triangle[:,0], triangle[:,1], 'bo-', label='Original Triangle')
plt.plot(new_triangle[:,0], new_triangle[:,1], 'go-', label='Reflected Triangle')
plt.axis('equal')
plt.legend()
plt.show()
