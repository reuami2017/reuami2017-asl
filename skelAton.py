#import animation as am
import xml.etree.ElementTree as ET # fone home
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
def make_lines(filename):
    """
    looks at the file
    :return an array of arrays of 3 arrays of floats. The outer array represents all of the different joints.
    The inside frames contain 25 different arrays, which are each of the different body parts in the array.
    """
    lines = []
    d = {}
    signs = ET.parse(filename).getroot()
    for sign in signs:
        for frame in sign:
            for joint in frame:
                body_part = joint.get('name')
                if body_part not in d:
                    d[body_part] = [[], [], []]
                d[body_part][0].append(float(joint.get("x")))
                d[body_part][1].append(float(joint.get("y")))
                d[body_part][2].append(float(joint.get("z")))
    return d

def getxyzplot( body, frame):
        return [dict[body][0][frame],dict[body][1][frame],dict[body][2][frame]]

def bodypart(body, body2, frame):
    ax.plot([ getxyzplot(body,  frame)[0], getxyzplot(body2, frame)[0]],
             [getxyzplot(body,  frame)[1], getxyzplot(body2, frame)[1]]
            ,zs=[getxyzplot(body, frame)[2], getxyzplot(body2, frame)[2]]
             )
def makebody(frame):
    ax.clear()
    ## head
    bodypart("Head", "Neck", frame)
    bodypart("SpineShoulder", "Neck", frame)
    bodypart("SpineShoulder", "SpineMid", frame)
    bodypart("SpineBase", "SpineMid", frame)
    # leg left
    bodypart("SpineBase", "HipLeft", frame)
    bodypart("HipLeft", "KneeLeft", frame)
    bodypart("AnkleLeft", "KneeLeft", frame)
    bodypart("AnkleLeft", "FootLeft", frame)
    #arm left
    bodypart("SpineShoulder", "ShoulderLeft", frame)
    bodypart("ElbowLeft", "ShoulderLeft", frame)
    bodypart("ElbowLeft", "WristLeft", frame)
    bodypart("HandLeft", "WristLeft", frame)
    bodypart("HandLeft", "HandTipLeft", frame)
    bodypart("WristLeft", "ThumbLeft", frame)

    ## right arm
    bodypart("SpineShoulder", "ShoulderRight", frame)
    bodypart("ElbowRight", "ShoulderRight", frame)
    bodypart("ElbowRight", "WristRight", frame)
    bodypart("HandRight", "WristRight", frame)
    bodypart("WristRight", "ThumbRight", frame)
    bodypart("HandRight", "HandTipRight", frame)

    # leg right
    bodypart("SpineBase", "HipRight",  frame)
    bodypart("HipRight", "KneeRight", frame)
    bodypart("AnkleRight", "KneeRight", frame)
    bodypart("AnkleRight", "FootRight", frame)
# dict= make_lines("XML_ASL_Files/LATER_2890.xml")
# dict= make_lines("/DINOSAUR_716.xml")
# dict=make_lines("edited/XML_ASL_Files/MOTHER+_1611.xml")
# dict=make_lines("edited/XML_ASL_Files/MOTHER+FATHER_3213.xml")
dict=make_lines("edited/XML_ASL_Files/FATHER+_1613.xml")

fig = plt.figure()
ax = p3.Axes3D(fig)
ax.axis("off")  # comment this line and a later line to put back in the axis
ax.view_init(270,270)

def updatefig(i):
    makebody(i)
    #ax.canvas.draw_idle()
    # plt.pause(1000)
    ax.axis("off")  # comment this line out to put back in the axis and a previous line (ax.axis('off')



anim = animation.FuncAnimation(fig, updatefig,frames= len(dict["Head"][0]), interval=1000/30)
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
import threading

# ax.set_axis_off()


plt.show()
#def thread():
#    while True:
#        for i in range (len(dict["Head"][0])):
 #           updatefig(i)

#t = threading.Thread(target=thread)
#t.daemon = False
#t.start()

