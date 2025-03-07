"""
For dynamic charts, use Matplotlib’s FuncAnimation.




📌 Why use this?

Creates dynamic, real-time plots.

"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
plt.gcf().canvas.manager.set_window_title('Animated Plot ')  # Corrected title
x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))

def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
