# -*- coding: utf-8 -*-
"""Implementation of bubble sort."""

import random
import itertools


def bubble_sort(x):
    """Sort a list using bubble sort.

    Arguments:
        x (list)  -- the list to sort

    Return:
        x (list)  -- the list sorted
    """

    sorted = False

    while not sorted:
        swapped = False

        for i in range(1, len(x)):
            if x[i] < x[i-1]:
                swapped = True
                x[i], x[i-1] = x[i-1], x[i]

        if not swapped:
            sorted = True

    return x


def main():
    """The main function. Used to test the other functions."""

    # Create an unsorted list.
    random.seed()
    x = []
    for _ in itertools.repeat(None, 20):
        x.append(int(100 * random.random()))

    print("\nUnsorted list")
    print(x)

    print("\nBubble sort:")
    print(bubble_sort(x))


if __name__ == "__main__":
    main()
