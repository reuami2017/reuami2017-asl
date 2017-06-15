"""
file with all range functionality
"""

import xml.etree.ElementTree as ET
import math


def avg_hand_distance_right(filename):
    return (avg_distance(filename, "WristRight") +
            avg_distance(filename, "HandRight") +
            avg_distance(filename, "HandTipRight") +
            avg_distance(filename, "ThumbRight")) / 4


def avg_distance(filename, body_part):
    """
    avg distance
    :param filename: filename
    :param body_part: body part
    :return: the avg distance int
    """
    root = ET.parse("XML_ASL_Files" + "\\" + filename).getroot()
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

    if total == 0.0:
        print("no object found")
        return total
    return total/count

