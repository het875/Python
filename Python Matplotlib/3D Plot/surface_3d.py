import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set window title
fig = plt.figure("3D Surface Plot")
ax = fig.add_subplot(111, projection='3d')

# Generate data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Surface plot
surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", edgecolor="k")

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Surface Plot")

plt.show()


"""
3D Surface Plot (Smooth Surface)
A surface plot shows a smooth 3D shape with color mapping.



3D Surface Plot (Smooth Surface)
A surface plot shows a smooth 3D shape with color mapping.
"""