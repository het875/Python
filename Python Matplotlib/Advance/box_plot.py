import matplotlib.pyplot as plt
import numpy as np

# Random data
data = np.random.randint(50, 100, size=(10, 5))

# Box plot
plt.figure("Box Plot Example")
plt.boxplot(data)

# Labels
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Box Plot Representation")

plt.show()

"""

Box Plot (Data Summary & Outliers)
A box plot shows the spread of data, including median, quartiles, and outliers.


🔹 Explanation
    Box plot parts:
    Middle line → Median (50% of data below this value).
    Box edges → 1st & 3rd quartile (Q1 & Q3).
    Whiskers → Data spread.
    Dots outside whiskers → Outliers.

"""