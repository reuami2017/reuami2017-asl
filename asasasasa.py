
"""
============
3D animation
============

A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import xml.etree.ElementTree as ET

def get_x_y_z_values(filename, body_part):
    values = [[],[],[]]
    root = ET.parse(filename).getroot()
    for sign in root:
        for frame in sign:
            for joint in frame:
                if joint.get('name') == body_part:
                    values[0].append(float(joint.get("x")))
                    values[1].append(float(joint.get("y")))
                    values[2].append(float(joint.get("z")))
    return values



def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data()
        line.set_3d_properties(data[2, :num])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines

# Creating fifty line objects.

ax.set_title('3D Test')
def init():
    x = np.linspace(0, 100, 100)
    y = np.linspace(0, 100, 100)
    data = get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "HandRight")

    ax.scatter(data[0], data[1],data[2] , marker='o', s=20, c="goldenrod", alpha=0.6)
    return ()
def animate(i):
    ax.view_init(elev=10., azim=i)
    return ()
# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)


anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()