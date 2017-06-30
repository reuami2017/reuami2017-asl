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


def max_arm_distance(filename):
    """
    finds the max arm distance for the hands for the given file
    :param filename: the file
    :return: a tuple of the left, then the right max arm distance
    """
    root = ET.parse("XML_ASL_Files" + "\\" + filename).getroot()
    max_range_right = 0
    max_range_left = 0
    for sign in root:
        for frame in sign:
            for joint in frame:
                pointsum_right = [0, 0, 0]
                pointsum_left = [0, 0, 0]
                if joint.get('name') == "SpineMid":
                    spine = [float(joint.get("x"))
                             , float(joint.get("y"))
                             , float(joint.get("z"))]
                elif joint.get('name') in ['WristRightHand', 'HandRight', 'HandTipRight', 'ThumbRight']:
                    pointsum_right[0] += float(joint.get("x"))
                    pointsum_right[1] += float(joint.get("y"))
                    pointsum_right[2] += float(joint.get("z"))
                elif joint.get('name') in ['WristLeftHand', 'HandLeft', 'HandTipLeft', 'ThumbLeft']:
                    pointsum_left[0] += float(joint.get("x"))
                    pointsum_left[1] += float(joint.get("y"))
                    pointsum_left[2] += float(joint.get("z"))
            # if the max range is less than the current average range from the right hand to the spine, update it.
            new_range_right = math.sqrt(
                (pointsum_right[0] / 4 - spine[0]) ** 2 + (pointsum_right[1] / 4 - spine[1]) ** 2 + (
                    pointsum_right[2] / 4 - spine[2]) ** 2)
            new_range_left = math.sqrt(
                (pointsum_left[0] / 4 - spine[0]) ** 2 + (pointsum_left[1] / 4 - spine[1]) ** 2 + (
                    pointsum_left[2] / 4 - spine[2]) ** 2)
            if max_range_right < new_range_right:
                max_range_right = new_range_right
            if max_range_left < new_range_left:
                max_range_left = new_range_left
    return max_range_left, max_range_right

