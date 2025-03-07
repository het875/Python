import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set window title
fig = plt.figure("3D Line Plot")
ax = fig.add_subplot(111, projection='3d')

# Data
t = np.linspace(0, 10, 100)  # Time steps
x = np.sin(t)
y = np.cos(t)
z = t  # Moving upward

# 3D Line
ax.plot(x, y, z, color="red", linewidth=2)

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Line Plot")

plt.show()




"""
D Line Plot (Connecting Points in 3D)
A line plot connects points in space, useful for tracking movement or trends.


🔹 Explanation
ax.plot(x, y, z, color="red") draws a line in 3D space.
(x, y, z) are calculated as a spiral movement.



"""