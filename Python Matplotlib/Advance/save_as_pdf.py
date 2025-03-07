import matplotlib.pyplot as plt

# Set window title
plt.figure("Save Figure Example")  

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Plot
plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Line")

# Labels and title
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Saving Figures in High Resolution")

# Save as PNG (300 DPI)
plt.savefig("high_res_plot.png", dpi=300, bbox_inches='tight')

# Save as PDF
plt.savefig("plot.pdf")

plt.legend()
plt.show()




"""
Sometimes, you need publication-quality plots.


🔹 Explanation
plt.savefig("high_res_plot.png", dpi=300, bbox_inches='tight')
dpi=300 ensures high resolution.
bbox_inches='tight' removes extra whitespace.
plt.savefig("plot.pdf") saves the plot as a PDF file.

"""