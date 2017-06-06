"""
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
def Gen_RandLine(length, dims=2) :
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.array( get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "HandRight"))


    print(lineData)
    return lineData

def update_lines(num, dataLines, lines) :
    for line, data in zip(lines, dataLines) :
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2,:num])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines
data = [Gen_RandLine(30, 3) for index in range(1)]

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0], dat[1], dat[2])[0] for dat in data]


ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 30, fargs=(data, lines),
                              interval=30, blit=False)

plt.show()