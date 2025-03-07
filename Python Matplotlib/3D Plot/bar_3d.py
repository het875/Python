import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set window title
fig = plt.figure("3D Bar Chart")
ax = fig.add_subplot(111, projection='3d')

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
z = np.zeros(5)
dx = dy = np.ones(5)
dz = np.random.randint(1, 10, 5)  # Random heights

# 3D Bar plot
ax.bar3d(x, y, z, dx, dy, dz, color="purple")

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Bar Chart")

plt.show()


"""
3D Bar Plot
A bar plot in 3D is useful for categorical data.



🔹 Explanation
ax.bar3d(x, y, z, dx, dy, dz, color="purple") creates 3D bars.
dx and dy define bar width.
dz controls bar height.


"""