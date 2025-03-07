import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [30, 50, 20, 70]

plt.bar(categories, values, color=['red', 'blue', 'green', 'purple'])

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")

plt.show()
