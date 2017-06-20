"""
A quick function for going through the directory and displaying a histogram
make_hist.py
@author: Kesavan Kushalnagar
"""
import re
import os
import matplotlib.pyplot as plt


def make_hist(directory):
    """
    makes the histogram
    :param: directory: the directory of the files
    :return: nothing, but it prints out a histogram of how often each rating appears
    """
    vals = []
    for file in os.listdir(directory):
        if re.match("CS_\d+_#\d\d_person\d+_\d+_\d+", file):  # ensure that the string is in the correct form
            vals.append(re.search("\d+").group(0))  # guaranteed to match from above, gets the first digit
    plt.hist(vals)
    plt.title("Distribution of Deaf Speech Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Deaf people")
