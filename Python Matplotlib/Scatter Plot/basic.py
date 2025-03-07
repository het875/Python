import matplotlib.pyplot as plt

# Data
height = [160, 170, 165, 180, 175]
weight = [55, 70, 60, 75, 80]

# Create scatter plot
plt.scatter(height, weight)

# Add titles and labels
plt.title('Height vs Weight Scatter Plot')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

# Display plot
plt.show()
