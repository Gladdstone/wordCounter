"""
Filename: letterFreq.py
Author: Joseph Farrell
"""

from wordData import *
from rit_lib import *
from operator import attrgetter


class Letter(struct):
    _slots = ((str, 'letter'), (int, 'count'))


def letterFreq(words):
    """
    Precon: Takes dictionary mapping words to lists of YearCount objects
    Postcon: Returns string containing 26 lowercase letters sorted in decreasing order by frequency
    """
    alphadict = createLst()

    for key in words:
        for char in key:
            use = totalOccurrences(key, words)
            alphadict[char] += use
    alphalst = to_string(alphadict)
    print(alphalst)
    return alphalst


def createLst():
    """
    Precon: Takes none
    Postcon: Returns dictionary of letters each mapped to 0
    """
    letter = dict()
    letter['a'] = 0
    letter['b'] = 0
    letter['c'] = 0
    letter['d'] = 0
    letter['e'] = 0
    letter['f'] = 0
    letter['g'] = 0
    letter['h'] = 0
    letter['i'] = 0
    letter['j'] = 0
    letter['k'] = 0
    letter['l'] = 0
    letter['m'] = 0
    letter['n'] = 0
    letter['o'] = 0
    letter['p'] = 0
    letter['q'] = 0
    letter['r'] = 0
    letter['s'] = 0
    letter['t'] = 0
    letter['u'] = 0
    letter['v'] = 0
    letter['w'] = 0
    letter['x'] = 0
    letter['y'] = 0
    letter['z'] = 0
    return letter


def to_string(x):
    """
    Precon: Takes
                dictionary-set of letters mapped to frequency of use
    Postcon: Returns list of keys sorted in decreasing order of frequency
    """
    lst = []

    for key in x:
        lst.append(Letter(key, x[key]))
    sortedlst = sorted(lst, key = attrgetter('count'))
    sortedlst = reversed(sortedlst)


    alphastring = ''
    for key in sortedlst:
        alphastring += str(key.letter)
    return alphastring


def main():
    file = input('Enter file name: ')
    lst = readWordFile(file)
    letterFreq(lst)

if __name__ == '__main__':
    main()