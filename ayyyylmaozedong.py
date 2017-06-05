from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
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

fig = pyplot.figure()
ax = Axes3D(fig)

x_vals = get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "WristRight")[0]
y_vals = get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "WristRight")[1]
z_vals = get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "WristRight")[2]

x_vals2 = get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "HandRight")[0]
y_vals2 = get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "HandRight")[1]
z_vals2 = get_x_y_z_values("UNEDITED_COPY_(D)DINOSAUR_716.xml", "HandRight")[2]


ax.plot(x_vals, y_vals, z_vals)
ax.plot(x_vals2, y_vals2, z_vals2, c='y')

pyplot.show()