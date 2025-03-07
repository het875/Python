"""

Legend
To add a list of explanation for each wedge, use the legend() function:

"""


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("Legend Pie Chart ")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 