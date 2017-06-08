from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import xml.etree.ElementTree as ET


def get_x_y_z_values(filename, body_part):
    values = [[], [], []]
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


def graph(filename, body_part, color):
    vals = get_x_y_z_values(filename, body_part)

    ax.plot(vals[0], vals[1], vals[2], c=color)

# graph("UNEDITED_COPY_(D)DINOSAUR_716.xml", "WristRight", 'y')
# graph("UNEDITED_COPY_(D)DINOSAUR_716.xml", "HandRight", 'r')
# graph("UNEDITED_COPY_(D)DINOSAUR_716.xml", "ElbowRight", 'b')
#
# pyplot.show()