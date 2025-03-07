import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1", color='b', linestyle='-', marker='o')
plt.plot(x, y2, label="Line 2", color='g', linestyle='--', marker='s')

# Adding labels and title
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multiple Line Plot")

# Adding legend
plt.legend()

plt.show()
