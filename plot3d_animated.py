import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation
from math import pi

df = pd.read_csv("nbody_py_5000_iter.csv")
sun     = df[df["Body name"] == "sun"].reset_index(drop=True)
jupiter = df[df["Body name"] == "jupiter"].reset_index(drop=True)
saturn  = df[df["Body name"] == "saturn"].reset_index(drop=True)
uranus  = df[df["Body name"] == "uranus"].reset_index(drop=True)
neptune = df[df["Body name"] == "neptune"].reset_index(drop=True)
SOLAR_MASS = 4*pi*pi
# jupiter_mass = 9.54791938424326609e-04 * SOLAR_MASS * 150
# saturn_mass = 2.85885980666130812e-04 * SOLAR_MASS * 200
# uranus_mass = 4.36624404335156298e-05 * SOLAR_MASS * 300
# neptune_mass = 5.15138902046611451e-05 * SOLAR_MASS * 500
# mass_ratio = [SOLAR_MASS, jupiter_mass, saturn_mass, uranus_mass, neptune_mass]
mass_ratio = [SOLAR_MASS, SOLAR_MASS, SOLAR_MASS, SOLAR_MASS, SOLAR_MASS]
colors = ["r", "b", "b", "b", "b"]

# First set up the figure, the axis, and the plot element we want to animate
plt.style.use("ggplot")
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
# marker = "o" for scatter
line1, = ax.plot(df["X-Position"][0], df["Y-Position"][0], df["Z-Position"][0], marker = "o", lw=2, c = colors[0])
line2, = ax.plot(df["X-Position"][1], df["Y-Position"][1], df["Z-Position"][1], lw=2, c = colors[1])
line3, = ax.plot(df["X-Position"][2], df["Y-Position"][2], df["Z-Position"][2], lw=2, c = colors[2])
line4, = ax.plot(df["X-Position"][3], df["Y-Position"][3], df["Z-Position"][3], lw=2, c = colors[3])
line5, = ax.plot(df["X-Position"][4], df["Y-Position"][4], df["Z-Position"][4], lw=2, c = colors[4])
curr2, = ax.plot(df["X-Position"][1], df["Y-Position"][1], df["Z-Position"][1], marker = "o", ms = 5, mfc = "g", mec = "g")
curr3, = ax.plot(df["X-Position"][2], df["Y-Position"][2], df["Z-Position"][2], marker = "o", ms = 5, mfc = "g", mec = "g")
curr4, = ax.plot(df["X-Position"][3], df["Y-Position"][3], df["Z-Position"][3], marker = "o", ms = 5, mfc = "g", mec = "g")
curr5, = ax.plot(df["X-Position"][4], df["Y-Position"][4], df["Z-Position"][4], marker = "o", ms = 5, mfc = "g", mec = "g")
ax.set_xlim3d(min(df["X-Position"])-2, max(df["X-Position"])+2)
ax.set_ylim3d(min(df["Y-Position"])-2, max(df["Y-Position"])+2)
ax.set_zlim3d(min(df["Z-Position"])-2, max(df["Z-Position"])+2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

def update_plot(i):
    j = i * 5
    curr2.set_data(df.iloc[j+1][["X-Position","Y-Position"]].values.T)
    curr2.set_3d_properties(df.iloc[j+1]["Z-Position"])
    curr3.set_data(df.iloc[j+2][["X-Position","Y-Position"]].values.T)
    curr3.set_3d_properties(df.iloc[j+2]["Z-Position"])
    curr4.set_data(df.iloc[j+3][["X-Position","Y-Position"]].values.T)
    curr4.set_3d_properties(df.iloc[j+3]["Z-Position"])
    curr5.set_data(df.iloc[j+4][["X-Position","Y-Position"]].values.T)
    curr5.set_3d_properties(df.iloc[j+4]["Z-Position"])

    i = i + 1
    line1.set_data(sun.iloc[:i][["X-Position","Y-Position"]].values.T)
    line1.set_3d_properties(sun.iloc[:i]["Z-Position"])
    line2.set_data(jupiter.iloc[:i][["X-Position","Y-Position"]].values.T)
    line2.set_3d_properties(jupiter.iloc[:i]["Z-Position"])
    line3.set_data(saturn.iloc[:i][["X-Position","Y-Position"]].values.T)
    line3.set_3d_properties(saturn.iloc[:i]["Z-Position"])
    line4.set_data(uranus.iloc[:i][["X-Position","Y-Position"]].values.T)
    line4.set_3d_properties(uranus.iloc[:i]["Z-Position"])
    line5.set_data(neptune.iloc[:i][["X-Position","Y-Position"]].values.T)
    line5.set_3d_properties(neptune.iloc[:i]["Z-Position"])
    
    # return line1, line2, line3, line4, line5

# call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim = animation.FuncAnimation(fig, update_plot, frames=5000, interval=0, blit=False)
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()