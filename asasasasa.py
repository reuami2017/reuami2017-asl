import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import ayyyylmaozedong as ayy

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.set_title('3D Test')

def init():
    x = np.linspace(0, 100, 100)
    y = np.linspace(0, 100, 100)
    data = ayy.get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "HandRight")
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