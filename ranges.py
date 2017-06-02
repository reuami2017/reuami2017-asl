"""
file with all range functionality
"""

import xml.etree.ElementTree as ET
import math

def AvgDistance(filename, body_part):

    root = ET.parse(filename).getroot()

    sum = 0.0
    count = 0.0

    for sign in root:
        for frame in sign:
            count += 1.0
            for joint in frame:
                if joint.get('name') == "SpineMid":
                    spineX = joint.get("x")
                    spineY = joint.get("y")
                    spineZ = joint.get("z")
                if joint.get('name') == body_part:
                    bpX = joint.get("x")
                    bpY = joint.get("y")
                    bpZ = joint.get("z")
                sum += math.sqrt(((bpX - spineX) ** 2) + ((bpY - spineY) ** 2) + ((bpZ - spineZ) ** 2))

    print("The average distance from the SpineMid to " + body_part + " in the file " + filename + " is: " + str(sum/count))
    return sum/count


def coord_ranges_and_avgs(filename, body_part):
    """
    :param body_part: any body part such as HipRight
    :return: the x range of the given body part
    """
    root = ET.parse(filename).getroot()
    Xmax, Ymax, Zmax = -999999999999999999
    Xmin, Ymin, Zmin = 999999999999999999
    Xsum, Ysum, Zsum = 0.0
    count = 0.0

    for sign in root:
        for frame in sign:
            count += 1.0
            for joint in frame:
                if joint.get('name') == body_part:
                    Xsum += joint.get("x")
                    Ysum += joint.get("y")
                    Zsum += joint.get("z")
                    if joint.get("x") < min:
                        min = float(joint.get("x"))
                    if joint.get("x") > max:
                        max = float(joint.get("x"))
                    if joint.get("y") < min:
                        min = float(joint.get("y"))
                    if joint.get("y") > max:
                        max = float(joint.get("y"))
                    if joint.get("z") < min:
                        min = float(joint.get("z"))
                    if joint.get("z") > max:
                        max = float(joint.get("z"))

    return Xmax-Xmin, Xsum/count, Ymax-Ymin, Ysum/count, Zmax-Zmin, Zsum/count

def average_of_ranges(filename, body_part):
    """
    :param body_part: the body part in question
    :return: the average of the x, y, and z ranges in a list
    """
    return [coord_range(filename, body_part, 'x'), coord_range(filename, body_part, 'y'), coord_range(filename, body_part, 'z')]
