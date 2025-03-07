import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set window title
fig = plt.figure("3D Wireframe Plot")
ax = fig.add_subplot(111, projection='3d')

# Meshgrid data
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Wireframe plot
ax.plot_wireframe(X, Y, Z, color="black")

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Wireframe Plot")

plt.show()




"""
 3D Wireframe Plot (Mesh Representation)
A wireframe plot represents surfaces using mesh lines.


🔹 Explanation
np.meshgrid(x, y) creates a grid of points.
ax.plot_wireframe(X, Y, Z, color="black") connects these points with wireframes.

"""