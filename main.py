try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import os
import ranges
import music
import re
import matplotlib.pyplot as plt
from textblob import TextBlob
import sys
from itertools import *
import pickle  # this is being used, python just can't see it``
import urllib
from mutagen.mp3 import MP3
import pandas as pd
import xml


"""
Somehow create a database
Ideally it will have a format as such:

name, attrname

Later, more attributes such as sentiment can be added as they are understood.

"""


def get_word(file):
    """
    helper function that regexes the word out of the filename
    :param file: the filename
    :return: the word from the filename
    """
    temp = re.sub("_", "", file)
    temp = re.sub("xml", "", temp).lower()
    temp = re.sub(r"([a-z])\^([a-z])", r"\1 \2", temp, 0, re.IGNORECASE)
    temp = re.sub(r"([a-z])\-([a-z])", r"\1 \2", temp, 0, re.IGNORECASE)
    temp = re.sub(r"([a-z])\+\+([a-z])", r"\1 \2", temp, 0, re.IGNORECASE)
    temp = re.sub(r"([a-z])\+([a-z])", r"\1 \2", temp, 0, re.IGNORECASE)
    temp = re.sub("[^a-z ]", "", temp)
    return re.sub("xml", "", temp).lower()


def make_word_database():
    """
    makes the database
    :return: a dict with all the files. The dict relates each word to their type (noun, verb, etc)
    """
    new_dict = {}
    sentiment_dict = {}
    sound_len_dict = {}
    print("Making word database")
    sound_files = os.listdir("sound")
    for file in os.listdir("edited\XML_ASL_Files"):
        temp = get_word(file)
        # try:
        #     music.get_file(temp)  # store all of the different names of files. Should only be ran once
        # except urllib.error.HTTPError:
        #     pass
        if temp + ".mp3" in sound_files:
            sound_len_dict[temp] = MP3("sound/" + temp + ".mp3").info.length
        else:
            sound_len_dict[temp] = -1
        new_dict[temp] = TextBlob(temp).tags[0][1]  # get the type of word (noun, verb, etc)
        sentiment_dict[temp] = TextBlob(temp).sentiment.polarity  # add sentiment to the database
        if (len(new_dict) % 100) == 0:
            print(str(int(len(new_dict) / 30)) + "% done")
    return new_dict, sentiment_dict, sound_len_dict


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
    for sign in root:
        for frame in sign:
            for joint in frame:
                if joint.get('name') == body_part:
                    sum_of_bodypart += float(joint.get(coord))
                    num_of_bodypart += 1

    return str(sum_of_bodypart / num_of_bodypart)
#
# print(avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight') + " " +
# avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'x') + " " +
# avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'y') + " " +
# avg_coord('XML_ASL_Files\(D)DINOSAUR_716.xml', 'HipRight', 'z'))


def seconds(filename):
    """
    this assumes that there is only 1 sign, will need to be modified if there are ever multiple signs in 1 file
    :param filename: the file
    :return: the seconds in the file
    """
    root = ET.parse(filename).getroot()
    for sign in root:
        return len(sign) / 30.0
# print(seconds('XML_ASL_Files\(D)DINOSAUR_716.xml'))


def create_database(directory):
    """
    gets random details from the xml directory and prints them out
    :param directory: the name of the directory with XML files in it
    :return: a dictionary of all signs mapped to all signs
    """
    time_dict = {}
    max_arm_range_right = {}
    max_arm_range_left = {}
    arm_dict = {}
    first_loc_wrist_right = {}
    first_loc_wrist_left = {}
    closest_body_part_to_right0 = {}
    closest_body_part_to_right1 = {}
    closest_body_part_to_left0 = {}
    closest_body_part_to_left1 = {}

    print("Creating arm length, time, and ranges databases")
    for file in os.listdir(directory):
        try:
            sec = seconds(directory + "\\" + file)
            name = get_word(file)
            time_dict[name] = sec
            arm_dict[name] = ranges.avg_hand_distance_right(file)
            first_loc_wrist_right[name] = ranges.avg_distance_n_frames(file, "WristRight", 5, "first")
            first_loc_wrist_left[name] = ranges.avg_distance_n_frames(file, "WristLeft", 5, "first")
            max_arm_range_right[name], max_arm_range_left[name] = ranges.max_arm_distance(file)
            # old version of the closest body part, new version coming up!
            # closest_body_part_to_right[name] = ranges.closest_body_part(file, ["HandRight", "WristRight"])[0][2]
            # closest_body_part_to_left[name] = ranges.closest_body_part(file, ["HandLeft", "WristLeft"])[0][2]
            closestright = ranges.closest_body_part(file, ["HandRight", "WristRight"])
            closestleft = ranges.closest_body_part(file, ["HandLeft", "WristLeft"])
            closest_body_part_to_right0[name] = closestright[0]  # should be a array?
            closest_body_part_to_right1[name] = closestright[1]
            closest_body_part_to_left0[name] = closestleft[0]
            closest_body_part_to_left1[name] = closestleft[1]

            if (len(time_dict) % 100) == 0:  # neato percentage tracking so that we can feel happy
                print(str(int(len(time_dict) / 30)) + "% done")

        except ET.ParseError: # some file appears to be broken and I'm not sure which one, so just catch with this.
            continue

    return time_dict, arm_dict, [max_arm_range_right, max_arm_range_left], \
           first_loc_wrist_left, first_loc_wrist_right, closest_body_part_to_right0, closest_body_part_to_right1,\
           closest_body_part_to_left0, closest_body_part_to_left1


def get_list_of_signs_right(df, body_part):
    """
    gets a list of all the body parts
    :param df: the dataframe
    :param body_part: the body part to look at
    :return:
    """
    return df[df['closest_body_right_hand0'] == body_part]


# TODO figure out how to narrow down with both body parts simultaneously, right now this does one.
# some issues are that the changes will only apply to one hand at a time, so it might be needed to do some weird
# check of both at once. Perhaps go online for some inspiration.
def narrow_list(candidates, body_part, position='right'):
    """
    narrows down the list of candidates
    :param candidates: the list of signs that matched the first time
    :param position: right or left
    :param body_part: the current body position of the right hand
    :return: the list of signs who are in candidates and match the body part right
    """
    if type(candidates) is not pd.DataFrame:
        return pd.DataFrame()  # should only be done for the first round
    bd = "closest_body_right_hand1"
    if position == "left":
        bd = "closest_body_left_hand1"  # change iff is left
    # print(candidates)
    # print(bd)
    # print(body_part)
    return candidates[candidates[bd] == body_part]


def get_list_of_signs_left(db, body_part):
    """
    gets a list of all the body parts on left
    :param db: the dataframe
    :param body_part: the interesting body part
    :return:
    """
    return db[db['closest_body_left_hand0'] == body_part]


def get_closest(filename):
    """
    gets the closest body part
    :param filename: the file (python.xml in this context)
    :return: the string of the smallest body part
    """
    while True:
        try:
            root = ET.parse(filename).getroot()
            break
        except xml.etree.ElementTree.ParseError:
            pass  # if there is a parse error, just try again until there is not a parse error
    frame = root[0][0]  # get the first frame or whatever
    low = 99999999
    current_closest = None
    for i in range(len(frame)):
        curr = float(frame[i].get("distance"))
        if curr < low:
            low = curr
            current_closest = frame[i].get("to")  # get the current.
    # print(current_closest)
    return current_closest


def predict(db):
    old_closest = None  # initial, should never match again
    old_list_right = []
    old_list_left = []
    while True:
        current_closest = get_closest("python.xml")

        # TODO Can we get the current closest for the right and left hand y any chance?
        if current_closest == old_closest:
            continue  # don't do any printing unless something changed
        # else they differ! Neato!
        right_list2 = narrow_list(old_list_right, current_closest, "right")
        left_list2 = narrow_list(old_list_left, current_closest, "left")
        right_list1 = get_list_of_signs_right(db, current_closest)
        old_list_right = right_list1
        left_list1 = get_list_of_signs_left(db, current_closest)
        old_list_left = left_list1

        # Output all of the predictions live! Neato!

        rlist = right_list1.index.tolist()
        if rlist:
            print("Right list!")
            print(rlist)
        else:
            print("There is no predictions for this right hand position")
        llist = left_list1.index.tolist()
        if llist:
            print("Left list!")
            print(llist)
        else:
            print("There is no predictions for this left hand position")
        rlist1 = right_list2.index.tolist()
        if rlist1:
            print("Right list. predict 1!")
            print(rlist1)
        else:
            print("There is no predictions for this right hand position and predict 1")
        llist1 = left_list2.index.tolist()
        if llist1:
            print("Left list. predict 1!")
            print(llist1)
        else:
            print("There are no predictions for this left hand position and predict 1")

        old_closest = current_closest


"""
Run the program here
"""

check = input("Should the database be loaded from the database.pkl file? (Y/N)   ")
if check in ["Y", "y"]:
    df = pd.read_pickle("database.pkl")
else:
    #Make databases
    word_types, sentiment, sound = make_word_database()
    time, arm, arm_ranges, first_wrist_left, first_wrist_right, closest_body_right_hand0, closest_body_right_hand1,\
        closest_body_left_hand0, closest_body_left_hand1 = create_database("edited\XML_ASL_Files")
    #make dataframe
    df = pd.DataFrame([word_types, sentiment, time, arm, arm_ranges[0], arm_ranges[1], sound,
                       first_wrist_left, first_wrist_right, closest_body_right_hand0, closest_body_right_hand1,
                       closest_body_left_hand0, closest_body_left_hand1],
                      index=["type", "sentiment", "seconds", "arm", "right", "left", "sound_len",
                             "first_wrist_left", "first_wrist_right",
                             "closest_body_right_hand0", "closest_body_right_hand1",
                             "closest_body_left_hand0", "closest_body_left_hand1"]).transpose()
    df.to_pickle("database.pkl")


# turn each variable listed to numeric
df[['seconds', 'sentiment', 'arm', 'right', 'left',
    "sound_len", "first_wrist_left", "first_wrist_right"]] = df[['seconds', 'sentiment', 'arm', 'right', 'left',
                                                                 "sound_len", "first_wrist_left",
                                                                 "first_wrist_right"]].apply(pd.to_numeric)

predict(df)

google_words = df[df.sound_len != -1.00000]  # the google words data set, words that don't exist have len -1
one_sec = df[(1 > df['seconds']) & (df['seconds'] >= 0)]
two_sec = df[(2 > df['seconds']) & (df['seconds'] >= 1)]
three_sec = df[(3 > df['seconds']) & (df['seconds'] >= 2)]
four_sec = df[df['seconds'] >= 3]
nouns = df[(df['type'] == "NN") | (df['type'] == "NNS") | (df['type'] == "NNP") | (df['type'] == "NNPS")]  # all nouns start with NN
verbs = df[(df['type'] == "VB") | (df['type'] == "VBD") | (df['type'] == "VBG") | (df['type'] == "VBN") | (df['type'] == "VBP") | (df['type'] == "VBZ") ]  # all verbs start with VB
adjectives = df[(df['type'] == "JJ") | (df['type'] == "JJR") | (df['type'] == "JJS")]  # adjectives
adverbs = df[(df['type'] == "RB") | (df['type'] == "RBS") | (df['type'] == "RBR")]  # adverbs obviously
print("One sec: \n" + str(one_sec.describe()))
print("One sec nouns: \n" + str(nouns[(1 > nouns['seconds']) & (nouns['seconds'] >= 0)].describe()))

print("Two sec: \n" + str(two_sec.describe()))
print("Three sec: \n" + str(three_sec.describe()))
print("Four sec: \n" + str(four_sec.describe()))
print("Overall: \n" + str(df.describe()))
print("Type: \n" + str(df['type'].describe()))
print('Nouns: \n' + str(nouns.describe()))
print("Verbs: \n" + str(verbs.describe()))
print('Adjectives: \n' + str(adjectives.describe()))
print('Adverbs: \n' + str(adverbs.describe()))
