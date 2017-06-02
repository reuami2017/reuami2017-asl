import xml.etree.ElementTree as ET
import os
import ranges

"""
AVG FUNCTION
"""


def avg_coord(filename, body_part, coord = 'x'):
    """

    :param file: the file in question
    :param body_part: The body part to be analysed (ex. HipRight)
    :param coord: the coord, automatically set to x for testing
    :return: the avg coord of the given body part in the file for the coord
    """
    root = ET.parse(filename).getroot()
    sum_of_bodypart = 0
    num_of_bodypart = 0
    # ok this is an meh solution because it works with the structure hard coded, but we shouldnt be changing much anyways if we change
    for sign in root:
        for frame in sign:
            for joint in frame:
                if joint.get('name') == body_part:
                    sum_of_bodypart += float(joint.get(coord))
                    num_of_bodypart += 1

    return str(sum_of_bodypart / num_of_bodypart)

print(avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight') + " " +
avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'x') + " " +
avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'y') + " " +
avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'z'))

"""
FRAME TIME!
"""
# for sign in root:
#     for frame in sign:
#         print(frame.tag) #should be frame


def seconds(filename):
    """
    this assumes that there is only 1 sign, will need to be modified if there are ever multiple signs in 1 file
    :param file: the file
    :return: the seconds in the file
    """
    root = ET.parse(filename).getroot()
    for sign in root:
        return len(sign) / 30.0


print(seconds('XML_ASL_Files\(D)DINOSAUR_716.xml'))

one_sec_signs = 0
two_sec_signs = 0
three_sec_signs = 0
four_sec_signs = 0

num_of_words = 0
sum_of_times = 0

for file in os.listdir("XML_ASL_Files"):
    try:
        sec = seconds("XML_ASL_Files\\" + file)
        if sec <= 0:
            continue  # whoopsies its broken
        elif sec < 1:
            one_sec_signs += 1
        elif sec < 2:
            two_sec_signs += 1
        elif sec < 3:
            three_sec_signs += 1
        elif sec < 4:
            four_sec_signs += 1
        num_of_words += 1
        sum_of_times += sec
    except ET.ParseError:  # some file derped on me and annoyed the hell out of me
        continue

print("There are: " + str(one_sec_signs) + " one second long signs in the database")
print("There are: " + str(two_sec_signs) + " two second long signs in the database")
print("There are: " + str(three_sec_signs) + " three second long signs in the database")
print("There are: " + str(four_sec_signs) + " four second long signs in the database")
print("Average time is: " + str(sum_of_times / num_of_words))
