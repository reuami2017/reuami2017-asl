"""
author - Kesavan Kushalngar
for hw 1 in CSCI 630
Develop a function that can solve Knuth's conjecture
"""

import queue
import math


class Node(object):
    def __init__(self, num, function):
        self.num = num
        self.parent = 0
        self.function = function


def get_successors(num):
    """
    succesors helper function for knuth AI BFS
    :param num: the num who's successors need to be found
    :return: a list of the successors
    """

    # later change the things being added to be just the operations themselves, so that they can be added to a dict
    succ = []
    succ.append(Node(math.sqrt(num), "sqrt of "))
    succ.append(Node(math.floor(num), "floor of "))
    if num % 1 == 0:  # else it is a float that needs to not be added
        if num < 198:  # I'd really rather not take factorials of enormous numbers if I can help it
            succ.append(Node(math.factorial(num), "factorial of "))
    return succ


def knuth(target):
    """
    solve's knuth conjecture
    :param target: the number trying to be reached
    :return: a sequence of expressions that will give the target number based on knuth's rules (square root, factorial, and floor)
    """
    #  create empty set S
    visited = []
    # create empty queue Q
    Q = queue.Queue()
    #
    # add root to S
    visited.append(4)  # 4 is the starting number for Knuth's Conjecture
    # Q.enqueue(root)
    Q.put(Node(4, "4"))
    #
    # while Q is not empty:
    #     current = Q.dequeue()
    #     if current is the goal:
    #         return current
    #     for each node n that is adjacent to current:
    #         if n is not in S:
    #             add n to S
    #             n.parent = current
    #             Q.enqueue(n)

    while not Q.empty():
        current = Q.get()
        if current.num == target:
            str = ""
            while current.parent != 0:
                str += current.function
                current = current.parent
            str += current.function  # to add the 4
            return str  # THIS NEEDS TO BE REPLACED BY A PATH FINDING THING LATER
        succ = get_successors(current.num)  # add successors to the queue
        for node in succ:
            # print("num is: " + str(node.num))
            if node.num not in visited:
                # print("num not in set is: " + str(node.num))
                visited.append(node.num)
                node.parent = current
                Q.put(node)
    return "Error: Queue was empty"


print("5 can be expressed as: " + knuth(5))
print("8 can be expressed as: " + knuth(8))
print("13 can be expressed as: " + knuth(13))
print("6 can be expressed as: " + knuth(6))