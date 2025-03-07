import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o', linestyle='--', color='r')

#Set the size of the markers to 20:
# plt.plot(x, y, marker='o', linestyle='--',  ms = 20 ,color='r')

# Adding labels
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")

# Adding title
plt.title("Basic Line Plot")

# Adding grid
plt.grid()

plt.show()




