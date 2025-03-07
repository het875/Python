import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create a new figure with a custom title
plt.figure()
plt.gcf().canvas.manager.set_window_title('Seaborn Plot')  # Corrected title

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

sns.set_style("darkgrid")  # Styles: white, darkgrid, whitegrid, ticks, dark

plt.plot(x, y, color='b')
plt.show()


"""
Advanced Styling with seaborn
Seaborn works on top of Matplotlib for beautiful plots.


📌 Why use this?

Seaborn improves visualization quality.
Provides built-in themes.


🔹 Explanation
sns.set_style("darkgrid") improves aesthetics.
plt.figure("Seaborn Styled Plot") names the window.

"""