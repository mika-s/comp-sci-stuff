# -*- coding: utf-8 -*-
"""Implementation of selection sort."""

import random
import itertools


def selection_sort(x):
    """Sort a list using selection sort.

    Arguments:
        x (list)  -- the list to sort

    Return:
        x (list)  -- the list sorted
    """

    for i in range(0, len(x)):
        k = i

        for j in range(i+1, len(x)):
            if x[j] < x[k]:
                k = j

        x[i], x[k] = x[k], x[i]

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

    print("\nSelection sort:")
    print(selection_sort(x))


if __name__ == "__main__":
    main()
