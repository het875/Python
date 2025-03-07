import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set window title
fig = plt.figure("3D Scatter Plot")
ax = fig.add_subplot(111, projection='3d')

# Random data
np.random.seed(5)  # Ensures reproducibility
x = np.random.randint(1, 100, 50)
y = np.random.randint(1, 100, 50)
z = np.random.randint(1, 100, 50)

# Scatter plot
ax.scatter(x, y, z, c=z, cmap="coolwarm", marker="o")

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Scatter Plot")

plt.show()


"""

D Scatter Plot (Plotting Points in Space)
A scatter plot is useful for visualizing randomly distributed 3D points.



🔹 Explanation
ax.scatter(x, y, z, c=z, cmap="coolwarm", marker="o") creates a colored 3D scatter plot.
cmap="coolwarm" adds a gradient color effect.
np.random.randint(1, 100, 50) generates random 3D points.

"""
