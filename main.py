import xml.etree.ElementTree as ET
import os
import ranges
import re
import matplotlib.pyplot as plt
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
    print("Making word database")
    for file in os.listdir("XML_ASL_Files"):
        temp = get_word(file)
        new_dict[temp] = TextBlob(temp).tags[0][1]
        if (len(new_dict) % 100) == 0:
            print(str(int(len(new_dict) / 35)) + "% done")
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


arm_dict = {}

#goes through all the files and gets various statistics
def details(directory):
    """
    gets random details from the xml directory and prints them out
    :param directory: the name of the directory with XML files in it
    :return: a dictionary of all signs mapped to all signs
    """
    time_dict = {}

    for file in os.listdir(directory):
        try:
            sec = seconds(directory + "\\" + file)
            name = get_word(file)
            time_dict[name] = sec
            arm_dict[name] = ranges.avg_hand_distance_right(file)
            if (len(time_dict) % 100) == 0:
                print(str(int(len(time_dict) / 34)) + "% done")

        except ET.ParseError: # some file appears to be broken and I'm not sure which one, so just catch with this.
            continue

    return time_dict


def details(directory):
    """
    gets random details from the xml directory and prints them out
    :param directory: the name of the directory with XML files in it
    :return: a dictionary of all signs mapped to all signs
    """
    time_dict = {}

    print("Creating arm length database")
    for file in os.listdir(directory):
        try:
            sec = seconds(directory + "\\" + file)
            name = get_word(file)
            time_dict[name] = sec
            arm_dict[name] = ranges.avg_hand_distance_right(file)
            if (len(time_dict) % 100) == 0:
                print(str(int(len(time_dict) / 34)) + "% done")

        except ET.ParseError: # some file appears to be broken and I'm not sure which one, so just catch with this.
            continue

    return time_dict


df = pd.DataFrame([word_types, details("XML_ASL_Files"), arm_dict], index=["type", "seconds", "arm"]).transpose()
df[['seconds', 'arm']] = df[['seconds', 'arm']].apply(pd.to_numeric)


one_sec = df[(1 > df['seconds']) | (df['seconds'] >= 0)]
two_sec = df[(2 > df['seconds']) | (df['seconds'] >= 1)]
three_sec = df[(3 > df['seconds']) | (df['seconds'] >= 2)]
four_sec = df[df['seconds'] >= 3]
nouns = df[(df['type'] == "NN") | (df['type'] == "NNS") | (df['type'] == "NNP") | (df['type'] == "NNPS")]  # all nouns start with NN
verbs = df[(df['type'] == "VB") | (df['type'] == "VBD") | (df['type'] == "VBG") | (df['type'] == "VBN") | (df['type'] == "VBP") | (df['type'] == "VBZ") ]  # all verbs start with VB
adjectives = df[(df['type'] == "JJ") | (df['type'] == "JJR") | (df['type'] == "JJS")]  # adjectives
adverbs = df[(df['type'] == "RB") | (df['type'] == "RBS") | (df['type'] == "RBR")]  # adverbs obviously
print("One sec: \n" + str(one_sec.describe()))
print("Two sec: \n" + str(two_sec.describe()))
print("Three sec: \n" + str(three_sec.describe()))
print("Four sec: \n" + str(four_sec.describe()))
print("Overall: \n" + str(df.describe()))
print("Type: \n" + str(df['type'].describe()))
print('Nouns: \n' + str(nouns.describe()))
print("Verbs: \n" + str(verbs.describe()))
print('Adjectives: \n' + str(adjectives.describe()))
print('Adverbs: \n' + str(adverbs.describe()))
"""
Run program here
"""
# details("XML_ASL_Files")
