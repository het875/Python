import matplotlib.pyplot as plt
import numpy as np

# Random data
data = [np.random.normal(60, 10, 100), np.random.normal(70, 15, 100), np.random.normal(50, 20, 100)]

# Violin plot
plt.figure("Violin Plot Example")
plt.violinplot(data, showmeans=True)

# Labels
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Violin Plot Representation")

plt.show()



"""

 Violin Plot (Advanced Data Spread)
A violin plot combines a box plot and a density plot.



🔹 Explanation
    np.random.normal(mean, std, size) → Creates normal distribution.
    Violin shape represents data density.

"""