import xml.etree.ElementTree as ET

"""
AVERAGE X POSITION OF A HIPRIGHT, MODIFY THIS SLIGHTLY FOR OTHER LIMBS, ETC.
"""

def average_val(file, body_part, coord = 'x'):
    """
    body_part = the body part in question: HipRight is one example
    coord: the coordinate in question. x, y, z are valid
    """
    root = ET.parse(file).getroot()
    sum_of_hiprights = 0
    num_of_hiprights = 0
    # ok this is an meh solution because it works with the structure hard coded, but we shouldnt be changing much anyways if we change
    for child in root:
        for children in child:
            for joint in children:
                if joint.get('name') == body_part:
                    sum_of_hiprights += float(joint.get(coord))
                    num_of_hiprights += 1

    print("average " + body_part + " is: " + str(sum_of_hiprights / num_of_hiprights))

average_val('XML_ASL_Files\(D)DINOSAUR_716.xml', "HipRight")
average_val('XML_ASL_Files\(D)DINOSAUR_716.xml', "HipRight", "x")

"""
FRAME TIME!
"""

def frames(file):
    root = ET.parse(file).getroot()
    num_of_frames = 0
    for sign in root:
        for frame in sign:
            num_of_frames += 1
    print("seconds is: " + str(num_of_frames / 30.0))

#TODO Figure out how to loop over all files in the XML directory and pass them to frames

frames('XML_ASL_Files\(D)DINOSAUR_716.xml')
