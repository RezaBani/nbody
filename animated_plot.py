"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation
from math import pi

df = pd.read_csv("nbody_py_5000_iter.csv")
#sun     = df[df["Body name"] == "sun"].reset_index(drop=True)
#jupiter = df[df["Body name"] == "jupiter"].reset_index(drop=True)
#saturn  = df[df["Body name"] == "saturn"].reset_index(drop=True)
#uranus  = df[df["Body name"] == "uranus"].reset_index(drop=True)
#neptune = df[df["Body name"] == "neptune"].reset_index(drop=True)
SOLAR_MASS = 4*pi*pi
jupiter_mass = 9.54791938424326609e-04 * SOLAR_MASS * 150
saturn_mass = 2.85885980666130812e-04 * SOLAR_MASS * 200
uranus_mass = 4.36624404335156298e-05 * SOLAR_MASS * 300
neptune_mass = 5.15138902046611451e-05 * SOLAR_MASS * 500
mass_ratio = [SOLAR_MASS, jupiter_mass, saturn_mass, uranus_mass, neptune_mass]
mass_ratio = [SOLAR_MASS, SOLAR_MASS, SOLAR_MASS, SOLAR_MASS, SOLAR_MASS]
colors = ["r", "b", "b", "b", "b"]

# First set up the figure, the axis, and the plot element we want to animate
plt.style.use("ggplot")
fig = plt.figure()
ax = fig.add_subplot(111)
scat = ax.scatter(df["X-Position"][0:5], df["Y-Position"][0:5], c = colors, s = mass_ratio)
ax.set_xlim(min(df["X-Position"])-2, max(df["X-Position"])+2)
ax.set_ylim(min(df["Y-Position"])-2, max(df["Y-Position"])+2)
ax.set_xlabel("X")
ax.set_ylabel("Y")

def update_plot(i):
    j = i * 5
    scat.set_offsets(df.iloc[j:j+5][["X-Position","Y-Position"]])
    return scat,

# call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim = animation.FuncAnimation(fig, update_plot, frames=5000, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
