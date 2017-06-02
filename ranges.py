"""
file with all range functionality
"""
import math


import xml.etree.ElementTree as ET


def avg_arm_distance(filename):
    """
    :param filename: the file of the sign
    :return: the average distance between the person's arm joints and hand joints to their chest for both hands (?)
    """
    return



def coord_range(filename, body_part, coord):
    """
    :param body_part: any body part such as HipRight
    :return: the x range of the given body part
    """
    root = ET.parse(filename).getroot()
    minval = 10000000000000000
    maxval = -1000000000000000
    for sign in root:
        for frame in sign:
            for joint in frame:
                if joint.get('name') == body_part:
                    if joint.get(coord) < minval:
                        minval = float(joint.get(coord))
                    if joint.get(coord) > maxval:
                        maxval = float(joint.get(coord))
    return maxval - minval

def average_of_ranges(filename, body_part):
    """
    :param body_part: the body part in question
    :return: the average of the x, y, and z ranges in a list
    """
    return [coord_range(filename, body_part, 'x'), coord_range(filename, body_part, 'y'), coord_range(filename, body_part, 'z')]