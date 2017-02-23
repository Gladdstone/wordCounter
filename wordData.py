"""
Filename: wordData.py
Author: Joseph Farrell
"""

from rit_lib import *


class YearCount(struct):
    _slots = ((int, 'year'), (int, 'count'))


class WordTrend(struct):
    _slots = ((str, 'word'), (float, 'trend'))


def readWordFile(fileName):
    """
    Precon: Takes file name of unigram data file
    Postcon: Returns dictionary mapping words to lists of YearCount objects
    """
    data = dict()

    for line in open(fileName):
        if line.strip().isalpha():
            data[line.strip()] = []
            temp = line.strip()
        else:
            line = line.replace(',', ' ')
            line = line.split()
            data[temp].append(YearCount(int(line[0]), int(line[1])))
    return data


def totalOccurrences(word, words):
    """
    Precon: Takes word for which to calculate count, and dictionary mapping words to lists of YearCount objects
    Postcon: Returns total number of times word has appeared in print
    """

    count = 0
    if word in words:
        for i in words[word]:
            count = count + i.count
        return count
    else:
        return count



def main():
    file = input('Enter file name: ')
    word = input('Enter word: ')

    data = readWordFile(file)
    print('Total: ' + str(totalOccurrences(word, data)))

if __name__ == '__main__':
    main()