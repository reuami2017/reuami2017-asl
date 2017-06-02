import xml.etree.ElementTree as ET

root = ET.parse('XML_ASL_Files\(D)DINOSAUR_716.xml').getroot()

print(root.tag) #check that it's on the right file, should be signs

# for child in root:
#     print(child.tag) #this should be "sign" as output
#     for children in child:
#         print(children.tag) #this should be frame
#         for joint in children:
#             print(joint.tag) #should be joint

root.findall()
for joint in root.findall('joint'):
    print(1)
    print(joint.get('name'))
