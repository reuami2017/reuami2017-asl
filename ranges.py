"""
file with all range functionality
"""

import xml.etree.ElementTree as ET
import math


def avg_arm_distance_right(filename):
    return (avg_distance(filename, "WristRight") + avg_distance(filename, "HandRight") + avg_distance(filename, "HandTipRight"), avg_distance(filename, "ThumbRight")) / 4


def avg_distance(filename, body_part):

    root = ET.parse(filename).getroot()

    total = 0.0
    count = 0.0

    for sign in root:
        for frame in sign:
            count += 1.0
            for joint in frame:
                if joint.get('name') == "SpineMid":
                    spine_x = float(joint.get("x"))
                    spine_y = float(joint.get("y"))
                    spine_z = float(joint.get("z"))
                if joint.get('name') == body_part:
                    bp_x = float(joint.get("x"))
                    bp_y = float(joint.get("y"))
                    bp_z = float(joint.get("z"))
                total += math.sqrt(((bp_x - spine_x) ** 2) + ((bp_y - spine_y) ** 2) + ((bp_z - spine_z) ** 2))

    print("The average distance from the SpineMid to " + body_part + " in the file " + filename + " is: " + str(total/count))
    return total/count


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
