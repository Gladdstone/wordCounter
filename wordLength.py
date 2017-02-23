"""
Filename: wordLength.py
Author: Joseph Farrell
"""

from wordData import *


class WordLength(struct):
    _slots = ((str, 'word'), (int, 'length'), (int, 'count'))


def summaryFromWords(words, year):
    """
    Precon: Takes
                words-dictionary mapping words to lists of YearCount objects
                year-year for which data is to be found
    Postcon: Returns five-tuple containing the five number summary
    """
    lst = list()

    for key in words:
        for word in words[key]:
            if word.year == year and word.count >= 1000:
                lst.append(WordLength(key, len(key), word.count))
            else:
                pass

    sortedlst = sort(lst)

    min = find_min(sortedlst)
    max = find_max(sortedlst)
    med = find_med(sortedlst)
    q1 = find_q1(sortedlst)
    q2 = find_q2(sortedlst)

    return min, q1, med, q2, max


def find_min(lst):
    """
    Precon: Takes
                lst-list sorted by length
    Postcon: Returns smallest length
    """
    x = lst[0].length
    return x


def find_max(lst):
    """
    Precon: Takes
                lst-list sorted by length
    Postcon: Returns largest length
    """
    index = len(lst) - 1
    x = lst[index].length
    return x


def find_med(lst):
    """
    Precon: Takes
                lst-list sorted by length
    Postcon: Returns median length
    """
    wordTotal = 0
    find = 0
    temp = 0

    for word in lst:
        wordTotal += word.count

    for word in lst:
        if find < wordTotal / 2:
            temp = word.length
            find += word.count
        else:
            return temp


def find_q1(lst):
    """
    Precon: Takes
                lst-list sorted by length
    Postcon: Returns length at first quartile
    """
    wordTotal = 0
    find = 0
    temp = 0

    for word in lst:
        wordTotal += word.count

    for word in lst:
        if find < wordTotal / 4:
            temp = word.length
            find += word.count
        else:
            return temp


def find_q2(lst):
    """
    Precon: Takes
                lst-list sorted by length
    Postcon: Returns length at third quartile
    """
    wordTotal = 0
    find = 0
    temp = 0

    for word in lst:
        wordTotal += word.count

    for word in lst:
        if find < wordTotal * (3/4):
            temp = word.length
            find += word.count
        else:
            return temp

def sort(lst):
    """
    Precon: Takes
                lst-unsorted list
    Postcon: Returns list sorted by length
    """
    if lst == []:
        return []
    else:
        pivot = lst[0].length
        (l, s, m) = partition(pivot, lst)
        return sort(l) + s + sort(m)

def partition(pivot, lst):
    """
    Precon: Takes
                pivot-pivot point for quick sort
                lst-list to be partitioned
    Postcon: Returns partitions of given list based on pivot point
    """
    (l, s, m) = ([], [], [])
    for i in lst:
        if i.length > pivot:
            m.append(i)
        elif i.length == pivot:
            s.append(i)
        elif i.length < pivot:
            l.append(i)
    return l, s, m

def main():
    file = input('Enter file name: ')
    start = input('Enter year: ')

    words = readWordFile(file)
    solution = summaryFromWords(words, start)
    print(solution)

if __name__ == '__main__':
    main()