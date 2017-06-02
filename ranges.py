"""
file with all range functionality
"""



import xml.etree.ElementTree as ET


def coord_range(filename, body_part, coord):
    """
    :param body_part: any body part such as HipRight
    :return: the x range of the given body part
    """
    root = ET.parse(filename).getroot()
    min = 10000000000000000
    max = -1000000000000000
    for sign in root:
        for frame in sign:
            for joint in frame:
                if joint.get('name') == body_part:
                    if joint.get(coord) < min:
                        min = float(joint.get(coord))
                    if joint.get(coord) > max:
                        max = float(joint.get(coord))
    return max - min