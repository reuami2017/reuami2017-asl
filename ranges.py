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
                    spineX = float(joint.get("x"))
                    spineY = float(joint.get("y"))
                    spineZ = float(joint.get("z"))
                if joint.get('name') == body_part:
                    bpX = float(joint.get("x"))
                    bpY = float(joint.get("y"))
                    bpZ = float(joint.get("z"))
                sum += math.sqrt(((bpX - spineX) ** 2) + ((bpY - spineY) ** 2) + ((bpZ - spineZ) ** 2))

    print("The average distance from the SpineMid to " + body_part + " in the file " + filename + " is: " + str(sum/count))
    return sum/count


def coord_ranges_and_avgs(filename, body_part):
    """
    :param body_part: any body part such as HipRight
    :return: the x, y, and z ranges and average values for that body part
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
                    Xsum += float(joint.get("x"))
                    Ysum += float(joint.get("y"))
                    Zsum += float(joint.get("z"))
                    if joint.get("x") < min:
                        Xmin = float(joint.get("x"))
                    if joint.get("x") > max:
                        Xmax = float(joint.get("x"))
                    if joint.get("y") < min:
                        Ymin = float(joint.get("y"))
                    if joint.get("y") > max:
                        Ymax = float(joint.get("y"))
                    if joint.get("z") < min:
                        Zmin = float(joint.get("z"))
                    if joint.get("z") > max:
                        Zmax = float(joint.get("z"))

    return Xmax-Xmin, Xsum/count, Ymax-Ymin, Ysum/count, Zmax-Zmin, Zsum/count

def average_of_ranges(filename, body_part):
    """
    :param body_part: the body part in question
    :return: the average of the x, y, and z ranges in a list
    """
    return [coord_range(filename, body_part, 'x'), coord_range(filename, body_part, 'y'), coord_range(filename, body_part, 'z')]
