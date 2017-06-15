import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import xml.etree.ElementTree as ET # fone home


def make_lines(filename):
    """
    looks at the file
    :return an array of arrays of 3 arrays of floats. The outer array represents all of the different joints.
    The inside frames contain 25 different arrays, which are each of the different body parts in the array.
    """
    lines = []
    d = {}
    signs = ET.parse(filename).getroot()
    for sign in signs:
        for frame in sign:
            for joint in frame:
                body_part = joint.get('name')
                if body_part not in d:
                    d[body_part] = [[], [], []]
                d[body_part][0].append(float(joint.get("x")))
                d[body_part][1].append(float(joint.get("y")))
                d[body_part][2].append(float(joint.get("z")))
        for key in d:
            lines.append(d[key])
    return lines

def update_lines(num, datalines, lines):
    for line, data in zip(lines, datalines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


def make_graph(filename):
    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    ax.set_title('3D animation of body part paths')
    temp = []  # things must be assigned to something or the graph will statically display everything
    for data in make_lines(filename):
        data = [np.array(data)]                                  ##
        temp.append(animation.FuncAnimation(fig, update_lines,len(ET.parse(filename).getroot()[0][0]),
                                fargs=(data, [ax.plot(dat[0], dat[1], dat[2])[0] for dat in data]),
                                interval=1000.0/30, blit=False))
#test1

    plt.show()

#make_graph("UNEDITED_COPY_(D)DINOSAUR_716.xml")
#make_graph("THROW_2256.xml")