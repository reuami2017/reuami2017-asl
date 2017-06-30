"""
A quick function for going through the directory and displaying a histogram
make_hist.py
@author: Kesavan Kushalnagar
"""
import re
import os
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def make_scatter():
    """
    makes the scatterplot
    :return:
    """
    good_scores = [41,41,44,47,47,50,50,50,50,50,50,50,50,50,50]
    fine_scores = [37,38,39,40,41,41,41,42,42,44,45,45,47,47,50]
    bad_scores = [19,30,34,39,48,14,14,17,20,21,23,23,24,25,30]
    wer_good = []  # fill this in with actual values later
    wer_fine = []
    wer_bad = []
    percent_total_good = []
    percent_correct_good = []
    percent_total_fine = [91.3, 86, 89.6, 75.3, 76.9, 91.3, 84.9, 83.5, 88.8, 86, 65.8, 100, 96.1, 100, 91.1]
    percent_correct_fine = [12.5, 15.1, 29.9, 34.1, 24.4, 18.8, 16.3, 17.6, 15, 24.4, 35.5, 13.9, 15.6, 0, 12.7]
    all_scores = good_scores + fine_scores + bad_scores
    all_wer = wer_good + wer_fine + wer_bad
    # plt.scatter(good_scores,wer_good)
    # time to make the trendline!
    z = np.polyfit(all_scores, all_wer, deg=1)
    p = np.poly1d(z)
    print(p)
    plt.scatter(all_scores, all_wer)
    plt.show()

make_scatter()

def make_hist(directory):
    """
    makes the histogram
    :param: directory: the directory of the files
    :return: nothing, but it prints out a histogram of how often each rating appears
    """
    vals = []
    for file in os.listdir(directory):
        # if re.match("CS_\d+_#\d+_person\d+_\d+_\d+", file):  # ensure that the string is in the correct form
        if re.match("CS_\d+_\w*", file):  # ensure that the string is in the correct form
            score = re.search("\d+", file).group(0)
            vals.append(int(score))
        else:
            print(file)
    print(vals)
    # bins=range(min(data), max(data) + binwidth, binwidth)
    # plt.hist(vals, bins = range(min(vals), max(vals) + 1, 1))
    plt.hist(vals)
    plt.title("Distribution of Deaf Speech Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Deaf people")
    plt.show()

# make_hist("converted audio files")
# make_hist("anonymous")