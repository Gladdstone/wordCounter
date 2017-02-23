"""
Filename: printedWords.py
Author: Joseph Farrell
"""

from wordData import *

import simplePlot


def printedWords(words):
    """
    Precon: Take dictionary mapping words to lists of YearCount objects
    Postcon: Returns list containing YearCount entry for each year for which data exists sorted in ascending
             order by year
    """
    lst = []
    dic = dict()

    for key in words:
        for obj in words[key]:
            if obj.year in dic:
                dic[obj.year] += obj.count
            else:
                dic[obj.year] = obj.count

    for obj in dic:
        lst.append(YearCount(obj, dic[obj]))
    return lst


def wordsForYear(year, yearList):
    """
    Precon: Takes:
                year-integer representing year being queried
                yearList-list of YearCount objects
    Postcon: Returns integer count representing  the total printed words for queried year
    """
    x = 0

    for i in yearList:
        if str(i.year) == str(year):
            x += i.count
        else:
            pass
    return x


def main():

    file = input('Enter word file: ')
    year = input('Enter year: ')

    words = readWordFile(file)
    wordsByYearList = printedWords(words)
    total = wordsForYear(year, wordsByYearList)

    print('Total printed words in ' + year + ': ' + str(total) + '')
    """
    words = readWordFile('z.txt')
    wordsByYearList = printedWords(words)
    """
    labels = 'Year', 'Total Words'
    plot = simplePlot.plot2D('Number of printed words over time', labels)
    for yc in wordsByYearList:
        point = yc.year, yc.count
        plot.addPoint(point)
    plot.display()


if __name__ == '__main__':
    main()
