"""
A quick function for going through the directory and displaying a histogram
make_hist.py
@author: Kesavan Kushalnagar
"""
import re
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches

def make_scatter():
    """
    makes the scatterplot
    :return:
    """
    good_scores = [41,41,44,47,47,50,50,50,50,50,50,50,50,50,50]
    fine_scores = [37,38,39,40,41,41,41,42,42,44,45,45,47,47,50]
    bad_scores = [19,30,34,39,48,14,14,17,20,21,23,23,24,25]
    percent_total_bad = [98.7, 97.5, 93.5, 93.7, 100, 94.9, 91.6, 97.4, 97.7, 91.1, 98.8, 96.2, 93.7, 86.1]
    percent_correct_bad = [1.3, 11.3, 13.0, 6.3, 0, 5.1, 8.4, 2.6, 2.3, 8.9, 1.2, 5.1, 12.7, 16.5]
    percent_total_good = [72.7, 61, 31.6, 48.8, 82.4, 41.5, 60.5, 16.5, 65, 85.2, 13, 24, 50.7, 70.4, 57]
    percent_correct_good = [29.9, 43.9, 72.2, 54.9, 21.6, 81.7, 40.7, 83.5,48.8,  14.8, 88.3, 77.3, 54.7, 30.9, 44.3]
    percent_total_fine = [91.3, 86, 89.6, 75.3, 76.9, 91.3, 84.9, 83.5, 88.8, 86, 65.8, 100, 96.1, 100, 91.1]
    percent_correct_fine = [12.5, 15.1, 29.9, 34.1, 24.4, 18.8, 16.3, 17.6, 15, 24.4, 35.5, 13.9, 15.6, 0, 12.7]
    all_scores = good_scores + fine_scores + bad_scores
    all_total = percent_total_good + percent_total_fine + percent_total_bad
    all_correct = percent_correct_good + percent_correct_fine + percent_correct_bad
    print(np.mean(percent_total_bad))
    print(np.mean(percent_correct_bad))
    print(np.mean(percent_total_fine))
    print(np.mean(percent_correct_fine))
    print(np.mean(percent_correct_good))
    print(np.mean(percent_total_good))

    print(np.mean(all_total))
    print(np.mean(all_correct))

    z = np.polyfit(all_scores, all_total, deg=1)
    p = np.poly1d(z)
    plt.scatter(all_scores, all_total)
    plt.scatter(good_scores, percent_total_good, color="blue")
    plt.scatter(fine_scores, percent_total_fine, color="orange")
    plt.scatter(bad_scores, percent_total_bad, color="green")
    plt.plot(all_scores, p(all_scores), color="red")
    plt.title("Score vs Word Error Rate")
    blue_patch = mpatches.Patch(color='blue', label='Good Deaf Speech')
    orange_patch = mpatches.Patch(color='orange', label='Mediocre Deaf Speech')
    green_patch = mpatches.Patch(color='green', label = 'Bad Deaf Speech')
    plt.legend(handles=[blue_patch, orange_patch, green_patch])
    plt.xlabel("Score")
    plt.ylabel("Word Error Rate")
    plt.show()

    # z = np.polyfit(all_scores, all_correct, deg=1)
    # p = np.poly1d(z)
    # plt.scatter(good_scores, percent_correct_good, color="blue")
    # plt.scatter(fine_scores, percent_correct_fine, color="orange")
    # plt.scatter(bad_scores, percent_correct_bad, color="green")
    # plt.plot(all_scores, p(all_scores), color="red")
    # plt.title("Score vs Percent Correct")
    # plt.xlabel("Score")
    # plt.ylabel("Percent Correct")
    # blue_patch = mpatches.Patch(color='blue', label='Good Deaf Speech')
    # orange_patch = mpatches.Patch(color='orange', label='Mediocre Deaf Speech')
    # green_patch = mpatches.Patch(color='green', label = 'Bad Deaf Speech')
    # plt.legend(handles=[blue_patch, orange_patch, green_patch])
    # plt.show()

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