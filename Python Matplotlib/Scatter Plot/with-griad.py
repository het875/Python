import matplotlib.pyplot as plt

# Data
height = [160, 170, 165, 180, 175]
weight = [55, 70, 60, 75, 80]

# Create scatter plot with customizations
plt.scatter(height, weight, color='blue', s=100)

# Add labels and title
plt.title('Height vs Weight Scatter Plot')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

# Add gridlines
plt.grid(True)

# Annotate a point
plt.annotate('Person B', (170, 70), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()
