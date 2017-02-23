"""
Filename: trending.py
Author: Joseph Farrell
"""

from wordData import *

from rit_lib import *


class WordTrend(struct):
    _slots = ((str, 'word'), (float, 'trend'))


def trending(words, startYr, endYr):
    """
    Precon: Takes
                words-dictionary mapping words to lists of YearCount objects
                startYr-starting year
                endYr-ending year
    Postcon: Returns list of trending words sorted by decreasing trend value
    """
    startlst = dict()
    endlst = dict()
    lst = list()

    for word in words:
        for obj in words[word]:
            if obj.count >= 1000:
                if obj.year == startYr:
                    if word in startlst:
                        startlst[word] += obj.count
                    else:
                        startlst[word] = obj.count
                if obj.year == endYr:
                    if word in endlst:
                        endlst[word] += obj.count
                    else:
                        endlst[word] = obj.count

    index = 0
    for word in startlst:
        if word in endlst:
            trendval = endlst[word] / startlst[word]
            lst.append(WordTrend(word, trendval))
            index += 1

    sortedlst = sort(lst)
    return sortedlst


def sort(lst):
    """
    Precon: Takes
                lst-unsorted list
    Postcon: Returns list sorted by length
    """
    if lst == []:
        return []
    else:
        pivot = lst[0].trend
        (m, s, l) = partition(pivot, lst)
        return sort(m) + s + sort(l)

def partition(pivot, lst):
    """
    Precon: Takes
                pivot-pivot point for quick sort
                lst-list to be partitioned
    Postcon: Returns partitions of given list based on pivot point
    """
    (m, s, l) = ([], [], [])
    for i in lst:
        if i.trend > pivot:
            m.append(i)
        elif i.trend == pivot:
            s.append(i)
        elif i.trend < pivot:
            l.append(i)
    return m, s, l

def find_top(lst):
    """
    Precon: Takes
                lst-list of WordTrend objects sorted in descending order by trend value
    Postcon: Returns top ten words
    """
    i = len(lst)
    top = list()
    for word in lst:
        while i >= len(lst) - 10:
            top.append(word)
    return top

def find_bottom(lst):
    """
    Precon: Takes
                lst-list of WordTrend objects sorted in descending order by trend value
    Postcon: Returns bottom ten words
    """
    i = 0
    bottom = list()
    for word in lst:
        if i <= len(lst) - 10:
            i += 1
        else:
            bottom.append(word)
    return bottom


def main():
    file = input('Enter file name: ')
    start = input('Enter starting year: ')
    end = input('Enter ending year: ')

    words =readWordFile(file)
    trend = trending(words, start, end)
    top = find_top(trend)
    bottom = find_bottom(trend)

    print('The top 10 trending words from ' + start + ' to ' + end + ':')
    for x in top:
        print(x.word)
    print('')
    print('The bottom 10 trending words from ' + start + ' to ' + end + ':')
    for x in bottom:
        print(x.word)

if __name__ == '__main__':
    main()