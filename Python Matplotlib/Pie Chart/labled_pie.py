import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(" Labled Pie Chart ")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

"""
Labels
Add labels to the pie chart with the labels parameter.

The labels parameter must be an array with one label for each wedge:

"""