import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(0.02,100,0.02)
y = np.sin(x) + np.log(x)
marginx = 0.05*np.abs(np.max(x)-np.min(x))
marginy = 0.05*np.abs(np.max(y)-np.min(y))

plt.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x[0], y[0], c = "b")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_xlim(np.min(x)-marginx, np.max(x)+marginx)
ax.set_ylim(np.min(y)-marginy, np.max(y)+marginy)

def update_plot(i):
    line.set_data(x[:i+1], y[:i+1])
    return line,

anim = FuncAnimation(fig, update_plot, frames=x.shape[0]-1, interval=0, blit=True)
plt.show()
