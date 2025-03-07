from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Set window title
fig = plt.figure("3D Surface Plot Example")
ax = fig.add_subplot(111, projection='3d')

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot surface
ax.plot_surface(X, Y, Z, cmap="viridis")

# Labels
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")
ax.set_title("3D Surface Plot")

plt.show()



"""
3D Plotting in Matplotlib
Matplotlib supports 3D visualizations using Axes3D.


🔹 Explanation
fig = plt.figure("3D Surface Plot Example") sets the window title.
ax = fig.add_subplot(111, projection='3d') creates a 3D plot.
ax.plot_surface(X, Y, Z, cmap="viridis") plots the surface using a color gradient.

"""

