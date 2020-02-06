"""This program creates a randomly generated integer(0-499) and string(500-999) dictionary
    and counts number of duplicates in both of them.
    date- 1/2/19
    -Surjashish
"""

import random


def randNum():
    newDict = dict.fromkeys(range(1000), [])
    for i in range(500):
        newDict[i] = random.randrange(1000, 9999)
        newDict[i + 500] = str(random.randrange(1000, 9999))

    numSet = set()
    stringSet = set()
    for x in range(len(newDict)):
        if x < 500:
            numSet.add(newDict[x])
        else:
            stringSet.add(newDict[x])
    print("Length of num set ", len(numSet), " length of string set ", len(stringSet), end=". ")

    print("And hence, total duplicate random integers are ", 500 - len(numSet),
          " and total duplicate random strings are ", 500 - len(stringSet))


randNum()
