import xml.etree.ElementTree as ET

"""
AVG FUNCTION
"""
def avg_coord(file, body_part, coord = 'x'):
    """

    :param file: the file in question
    :param body_part: The body part to be analysed (ex. HipRight)
    :param coord: the coord, automatically set to x for testing
    :return: the avg coord of the given body part in the file for the coord
    """
    root = ET.parse(file).getroot()
    sum_of_bodypart = 0
    num_of_bodypart = 0
    # ok this is an meh solution because it works with the structure hard coded, but we shouldnt be changing much anyways if we change
    for child in root:
        for children in child:
            for joint in children:
                if joint.get('name') == body_part:
                    sum_of_bodypart += float(joint.get(coord))
                    num_of_bodypart += 1

    return sum_of_bodypart / num_of_bodypart

print(avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight'))
avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'x')
avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'y')
avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'z')




"""
FRAME TIME!
"""
# for sign in root:
#     for frame in sign:
#         print(frame.tag) #should be frame

def seconds(file):
    """
    this assumes that there is only 1 sign, will need to be modified
    :param file: the file
    :return: the seconds in the file
    """
    num_of_frames = 0
    root = ET.parse(file).getroot()
    for sign in root:
        len(sign)
        # for frame in sign:
        #     num_of_frames += 1

seconds('XML_ASL_Files\(D)DINOSAUR_716.xml')