import xml.etree.ElementTree as ET

root = ET.parse('XML_ASL_Files\(D)DINOSAUR_716.xml').getroot()

print(root.tag) #check that it's on the right file, should be signs

for sign in root.findall('sign'):
    print(sign.tag)


"""
AVERAGE X POSITION OF A HIPRIGHT, MODIFY THIS SLIGHTLY FOR OTHER LIMBS, ETC.
"""
#TODO TURN THIS INTO A FUNCTION!!!!
sum_of_hiprights = 0
num_of_hiprights = 0
# ok this is an meh solution because it works with the structure hard coded, but we shouldnt be changing much anyways if we change
for child in root:
    for children in child:
        for joint in children:
            if joint.get('name') == 'HipRight':
                sum_of_hiprights += float(joint.get('x'))
                num_of_hiprights += 1

print("average hipright is: " + str(sum_of_hiprights / num_of_hiprights))

"""
FRAME TIME!
"""
# for sign in root:
#     for frame in sign:
#         print(frame.tag) #should be frame



for joint in root.findall('joint'):
    print(1)
    print(joint.get('name'))
