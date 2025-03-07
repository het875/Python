import matplotlib.pyplot as plt
import mplcursors

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]




fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
plt.gcf().canvas.manager.set_window_title('mplcursors ')  # Corrected title

mplcursors.cursor()  # Enables interactive tooltips
plt.show()



"""
📌 What happens?

Hovering over points shows their values dynamically.



"""