# -*- coding: utf-8 -*-
"""Implementation of insertion sort."""

import random
import itertools


def insertion_sort(x):
    """Sort a list using insertion sort.

    Arguments:
        x (list)  -- the list to sort

    Return:
        x (list)  -- the list sorted
    """

    for i in range(1, len(x)):
        j = i
        while j > 0 and x[j] < x[j-1]:
            x[j], x[j-1] = x[j-1], x[j]
            j -= 1

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

    print("\nInsertion sort:")
    print(insertion_sort(x))


if __name__ == "__main__":
    main()
