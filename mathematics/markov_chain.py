# -*- coding: utf-8 -*-
"""Functions related to Markov chains."""


import random


def random_walk(duration, start = 0, probability = 0.5):
    """Random walk based on a Markov chain.

    Args:
        duration (int)          -- how long to randomly walk
        start (int)             -- start value
        probability (float)     -- probability of increasing

    Returns:
        series (list of floats) -- the result of the random walk
    """

    series = []
    series.append(start)

    random.seed()

    for i in range(1, duration):
        if(random.random() >= probability):
            series.append(series[i-1] + 1)
        else:
            series.append(series[i-1] - 1)

    return series
