"""
Filename: boxAndWhisker.py
Author: Joseph Farrell
"""

import turtle


def boxAndWhisker(small, q1, med, q3, large):
    """
    Precon: Takes
                small: minimum value
                q1: first quartile
                med: median
                q3: third quartile
                large: maximum value
    Postcon: Draws box-and-whisker from data
    """
    #first vertical line
    up(20)
    down(40)
    up(20)
    #right horizontal
    right(q1 - small)
    #q1 vertical line
    up(20)
    down(40)
    #right horizontal to med
    right(med - q1)
    #med vertical line
    up(40)
    #reset left, right horizontal to q3
    left(med - q1)
    right(med - q1)
    right(q3 - med)
    #q3 vertical and reset
    down(40)
    left(q3 - med)
    right(q3 - med)
    up(20)
    #right horizontal to large
    right(large - q3)
    #large vertical line
    up(20)
    down(40)
    up(20)

    turtle.done()


def up(x):
    """
    Precon: Takes
                x-integer value representing distance
    Postcon: Moves turtle in correct direction for distance indicated by x
    """
    turtle.setheading(90)
    turtle.forward(x)

def down(x):
    """
    Precon: Takes
                x-integer value representing distance
    Postcon: Moves turtle in correct direction for distance indicated by x
    """
    turtle.setheading(270)
    turtle.forward(x)

def left(x):
    """
    Precon: Takes
                x-integer value representing distance
    Postcon: Moves turtle in correct direction for distance indicated by x
    """
    turtle.setheading(180)
    turtle.forward(x)

def right(x):
    """
    Precon: Takes
                x-integer value representing distance
    Postcon: Moves turtle in correct direction for distance indicated by x
    """
    turtle.setheading(0)
    turtle.forward(x)


def main():
    min = input('Enter the minimum: ')
    q1 = input('Enter the first quartile: ')
    med = input('Enter the median: ')
    q3 = input('Enter the third quartile: ')
    max = input('Enter the maximum: ')

    boxAndWhisker(int(min), int(q1), int(med), int(q3), int(max))

if __name__ == '__main__':
    main()