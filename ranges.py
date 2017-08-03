"""
file with all range functionality
"""

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import math
import numpy as np

def avg_hand_distance_right(filename):
    root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    return (avg_distance(root, "WristRight") +
            avg_distance(root, "HandRight") +
            avg_distance(root, "HandTipRight") +
            avg_distance(root, "ThumbRight")) / 4
def  getallbodypart(filename):
    """
    """
    name = []
    root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    for joint in root[0][0]:
        name.append(joint.get('name'))
    return name
#print(getallbodypart("#ALL_89.xml"))


def avg_distance(filename, body_part_from,  body_part_to="SpineMid"):
    """
    avg distance
    :param filename: filename
    :param body_part: body part
    :return: the avg distance float
    """
    if isinstance(filename, str):
        root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    else:
        root = filename
    total = 0.0
    count = 0.0
    try:
        for sign in root:
            for frame in sign:
                count += 1.0
                bp_x = -1
                spine_x = -1
                for joint in frame:
                    if joint.get('name') == body_part_to:
                        spine_x = float(joint.get("x"))
                        spine_y = float(joint.get("y"))
                        spine_z = float(joint.get("z"))
                    if joint.get('name') == body_part_from:
                        bp_x = float(joint.get("x"))
                        bp_y = float(joint.get("y"))
                        bp_z = float(joint.get("z"))
                    if (bp_x != -1 and spine_x != -1):
                        break
                total += math.sqrt(((bp_x - spine_x) ** 2) + ((bp_y - spine_y) ** 2) + ((bp_z - spine_z) ** 2))
    except ValueError:
        # print("negative infinity point")
        return total
    if total == 0.0:
        # print("no object found")
        return total

    return total/count


def distance_per_frame(filename, body_part_from, frame, body_part_to="SpineMid"):
    if isinstance(filename, str):
        root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    else:
        root = filename
    bp_x = -1
    spine_x=-1
    for joint in root[0][frame]:
        if joint.get('name') == body_part_to:
            spine_x = float(joint.get("x"))
            spine_y = float(joint.get("y"))
            spine_z = float(joint.get("z"))
        if joint.get('name') == body_part_from:
            bp_x = float(joint.get("x"))
            bp_y = float(joint.get("y"))
            bp_z = float(joint.get("z"))
        if(bp_x!=-1 and spine_x!=-1):
            break

    return math.sqrt(((bp_x - spine_x) ** 2) + ((bp_y - spine_y) ** 2) + ((bp_z - spine_z) ** 2))


def avg_distance_n_frames(filename, body_part, n, first_last, origin="SpineMid"):
    """
        avg distance between 2 body parts default origin is SpineMid, which is assumed to not move, for the first/last n frames
        :param filename: filename
        :param body_part: body part
        :param origin: SpineMid by default, the origin "body part"
        :param n: number of frames
        :param first_last: [first or last] n frames
        :return: the avg distance float
    """
    root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    total = 0.0
    frame_count = 0
    n_count = 0.0
    for sign in root:
        #there is only one sign in each "root"
        for frame in sign:
            frame_count += 1

        if first_last == "first":
            for frame in sign:
                flag = True
                n_count += 1
                if n_count >= n:
                    flag = False
                if flag:
                    bp_x = -1
                    spine_x = -1
                    for joint in frame:
                        if joint.get('name') == origin:
                            spine_x = float(joint.get("x"))
                            spine_y = float(joint.get("y"))
                            spine_z = float(joint.get("z"))
                        if joint.get('name') == body_part:
                            bp_x = float(joint.get("x"))
                            bp_y = float(joint.get("y"))
                            bp_z = float(joint.get("z"))
                        if (bp_x != -1 and spine_x != -1):
                            break
                    total += math.sqrt(((bp_x - spine_x) ** 2) + ((bp_y - spine_y) ** 2) + ((bp_z - spine_z) ** 2))
        else:
            for frame in sign:
                flag = True
                n_count += 1
                if frame_count - n_count >= n:
                    flag = False
                if flag:
                    bp_x = -1
                    spine_x = -1
                    for joint in frame:

                        if joint.get('name') == origin:
                            spine_x = float(joint.get("x"))
                            spine_y = float(joint.get("y"))
                            spine_z = float(joint.get("z"))
                        if joint.get('name') == body_part:
                            bp_x = float(joint.get("x"))
                            bp_y = float(joint.get("y"))
                            bp_z = float(joint.get("z"))
                        if (bp_x != -1 and spine_x != -1):
                            break
                    total += math.sqrt(((bp_x - spine_x) ** 2) + ((bp_y - spine_y) ** 2) + ((bp_z - spine_z) ** 2))

    if total == 0.0:
        print("no object found")
        return total

    return total / n


def max_arm_distance(filename):
    """
    finds the max arm distance for the hands for the given file
    :param filename: the file
    :return: a tuple of the left, then the right max arm distance
    """
    root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
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


def getbodypart():
    bodypart ={}
    bodypartneedtoscan = ['SpineBase', 'SpineMid', 'Neck', 'Head', 'ShoulderLeft',
                          'ShoulderRight', 'HipLeft',  'SpineShoulder', 'HipRight']
    bodypart["HandRight"] = bodypartneedtoscan + ["HandLeft", "ElbowLeft", "WristLeft"]
    bodypart["HandLeft"] = bodypartneedtoscan + ["HandRight", "ElbowRight", "WristRight"]

    bodypart["WristRight"] = bodypart["HandRight"]
    bodypart["WristLeft"] = bodypart["HandLeft"]
    return bodypart


def closest_body_part(filename,  hands=["HandRight", "WristRight"], sensitivity=1.5, num_parts=2):
    """
    returns the closest body part (SpineMid, etc) by going through each and calculating the average.
    It might be a good idea to combine this with the above function so that runtime is reduced
    :param filename: the name of the file
    :param sensitivity: the sensitivity (radius multiplier) of the closeness
    :return: a string of the closest body part
    """
    root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    bodypart = getbodypart()
    lowest = lowestpoint(root,  bodypart, hands) * sensitivity
    bodydef = []
    # for i in hands:
    #     for j in bodypart[i]:
    #             avg = avg_distance(root, i, j)
    #             if lowest >= avg:
    #                bodydef.append([avg, i, j])
    for i in hands:
        for j in bodypart[i]:
            avg = avg_distance(root, i, j)
            if lowest >= avg:
                if j not in bodydef:
                    bodydef.append(j)
                if len(bodydef) >= num_parts:
                    break
        if len(bodydef) >= num_parts:
            break
    while len(bodydef) < 2:  # ensure that the database can be created properly, otherwise a index error will occur
        bodydef.append(np.nan)
    return bodydef


def closest_body_part_per_frame(filename,  hands=["HandRight", "WristRight"], sensitivity=1.5):
    """
    returns the closest body part (SpineMid, etc) by going through each and calculating the average.
    It might be a good idea to combine this with the above function so that runtime is reduced
    :param filename: the name of the file
    :param sensitivity: the sensitivity
    :return: a string of the closest body part
    """
    root=ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    count = len(root[0])
    framebuff = []
    bodypart = getbodypart()
    for frame in range(count):
        bodydef = []
        lowest = lowestpoint_per_frame(root, bodypart, frame,  hands) * sensitivity
        for i in hands:
            for j in bodypart[i]:
                    avg = distance_per_frame(root, i, frame, j)
                    if lowest > avg :
                        bodydef.append([avg, i, j])
        framebuff.append(bodydef)
    return framebuff


def lowestpoint(filename, bodypart, hands=["HandRight", "WristRight"]):
    """
    returns the closest body part (SpineMid, etc) by going through each and calculating the average.
    It might be a good idea to combine this with the above function so that runtime is reduced
    :param filename: the name of the file
    :return: a string of the closest body part
    """
    if isinstance(filename, str):
        root = ET.parse("edited/XML_ASL_Files" + "/" + filename).getroot()
    else:
        root = filename
    lowest =9999999999

    for i in hands:
        for j in bodypart[i]:
                avg = avg_distance(root, i, j)
                if lowest > avg:
                    lowest = avg
    return lowest


def lowestpoint_per_frame(filename, bodypart, frame,  hands=["HandRight", "WristRight"]):
    """
    returns the closest body part (SpineMid, etc) by going through each and calculating the average.
    It might be a good idea to combine this with the above function so that runtime is reduced
    :param filename: the name of the file
    :return: a string of the closest body part
    """
    lowest = 9999999999
    for i in hands:
        for j in bodypart[i]:
                avg = distance_per_frame(filename, i, frame, j)
                if lowest > avg:
                    lowest = avg
    return lowest


if __name__ == "__main__":
    print(closest_body_part_per_frame("MOTHER+FATHER_3213.xml"))  # testing




