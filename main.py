import xml.etree.ElementTree as ET
import os
import ranges
import re
from textblob import TextBlob
from itertools import *
    
import pandas as pd
import numpy as np
# import nltk


"""
Somehow create a database
Ideally it will have a format as such:

name,attrname

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


def make_database():
    """
    makes the database
    :return: a dict with all the files. The dict relates each word to their type (noun, verb, etc)
    """
    new_dict = {}
    for file in os.listdir("XML_ASL_Files"):
        temp = get_word(file)
        new_dict[temp] = TextBlob(temp).tags[0][1]
    return new_dict

word_types = make_database()



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


#goes through all the files and gets various statistics
def details(directory):
    """
    gets random details from the xml directory and prints them out
    :param directory: the name of the directory with XML files in it
    :return: a dictionary of all signs mapped to all signs
    """
    time_dict = {}
    # one_sec_signs = 0
    # two_sec_signs = 0
    # three_sec_signs = 0
    # four_sec_signs = 0

    one_sec_arm_distances = 0
    two_sec_arm_distances = 0
    three_sec_arm_distances = 0
    four_sec_arm_distances = 0

    num_of_words = 0  # might be able to replace with len(time_dict)
    sum_of_times = 0
    sum_of_arm_distances = 0

    for file in os.listdir(directory):
        try:
            sec = seconds(directory + "\\" + file)
            name = get_word(file)
            if sec <= 0:
                continue  # whoopsies its broken
            elif sec < 1:
                time_dict[name] = 1
                # one_sec_signs += 1
                one_sec_arm_distances += ranges.avg_hand_distance_right(file)
            elif sec < 2:
                # two_sec_signs += 1
                time_dict[name] = 2
                two_sec_arm_distances += ranges.avg_hand_distance_right(file)
            elif sec < 3:
                # three_sec_signs += 1
                time_dict[name] = 3
                three_sec_arm_distances += ranges.avg_hand_distance_right(file)
            else:  # technically the signs could be longer than 4 seconds, maybe we should remove them altogether
                time_dict[name] = 4
                # print(file)
                # four_sec_signs += 1
                four_sec_arm_distances += ranges.avg_hand_distance_right(file)

            num_of_words += 1
            if (num_of_words % 100) == 0:
                print(str(num_of_words / 35) + "% done")
            sum_of_times += sec
            sum_of_arm_distances += ranges.avg_hand_distance_right(file)

        except ET.ParseError:  # some file derped on me and annoyed the hell out of me
            continue

    # print("There are: " + str(one_sec_signs) + " one second long signs in the database")
    # print("There are: " + str(two_sec_signs) + " two second long signs in the database")
    # print("There are: " + str(three_sec_signs) + " three second long signs in the database")
    # print("There are: " + str(four_sec_signs) + " four second long signs in the database")
    # print("Average time is: " + str(sum_of_times / num_of_words))
    # print("Average distance is: " + str(sum_of_arm_distances / num_of_words))
    # print("Average one second distance is: " + str(one_sec_arm_distances / one_sec_arm_distances))
    # print("Average two second distance is: " + str(two_sec_arm_distances / one_sec_arm_distances))
    # print("Average three second distance is: " + str(three_sec_arm_distances / one_sec_arm_distances))
    # print("Average four second distance is: " + str(four_sec_arm_distances / one_sec_arm_distances))
    return time_dict
df = pd.DataFrame([word_types, details("XML_ASL_Files")], index=["type", "seconds"]).transpose()
print(df[df['seconds'] > 0])


"""
Run program here
"""
# details("XML_ASL_Files")
