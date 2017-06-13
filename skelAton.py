import animation as am
import xml.etree.ElementTree as ET # fone home
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
    return d

def getxyzplot( body, frame):
        return [dict[body][0][frame],dict[body][1][frame],dict[body][2][frame]]

def bodypart(body, body2, frame):
    plt.plot([getxyzplot(body,  frame)[0], getxyzplot(body2, frame)[1]],
             [getxyzplot(body,  frame)[1], getxyzplot(body2, frame)[1]],
             [getxyzplot(body, frame)[2], getxyzplot(body2, frame)[2]])
dict= make_lines("DINOSAUR_716.xml")
## head
bodypart("Head",  "Neck", 0)
bodypart("SpineShoulder",  "Neck", 0)
bodypart( "SpineShoulder", "SpineMid", 0)
bodypart( "SpineBase","SpineMid", 0)
# leg left
bodypart( "SpineBase","HipLeft", 0)
bodypart( "HipLeft","KneeLeft", 0)
bodypart( "AnkleLeft","KneeLeft", 0)
bodypart( "AnkleLeft","FootLeft", 0)
# arm left
bodypart("SpineShoulder","ShoulderLeft", 0)
bodypart("ElbowLeft","ShoulderLeft", 0)
bodypart("ElbowLeft","WristLeft", 0)

bodypart("HandLeft","WristLeft", 0)
bodypart("HandLeft","HandTipLeft", 0)
bodypart("HandLeft","ThumbLeft", 0)

## right arm
bodypart("ElbowRight","ShoulderRight", 0)
bodypart("HandRight","WristRight", 0)
bodypart("HandRight","ThumbRight", 0)
bodypart("HandRight","HandTipRight", 0)
bodypart("ElbowRight","ShoulderRight", 0)
bodypart("SpineShoulder", "ShoulderRight", 0)
# leg right
bodypart( "SpineBase","HipRight", 0)
bodypart( "HipRight","KneeRight", 0)
bodypart( "AnkleRight","KneeRight", 0)
bodypart( "AnkleRight","FootRight", 0)

plt.show()
