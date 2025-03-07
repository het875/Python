import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")

plt.show()



"""

Explanation:

np.random.randn(1000): Generates random numbers.
plt.hist(data, bins=30): Creates a histogram with 30 bins.



"""