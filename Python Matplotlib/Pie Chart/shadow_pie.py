"""
Shadow
Add a shadow to the pie chart by setting the shadows parameter to True:

"""


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("Shadow Pie Chart ")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 