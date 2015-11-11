# -*- coding: utf-8 -*-
"""Various plotting functions."""

import numpy as np
import matplotlib.pyplot as plt
from differentiation import derivative


def plot_function(function, a, b, n=0.1):
    """Plot a function between a and b.

    Arguments:
        function (lambda) -- the function to plot
        a        (float)  -- where to start plotting
        b        (float)  -- where to stop plotting
        next     (int)    -- step size
    """

    x = np.arange(a, b, n)
    y = [function(x) for x in x]

    plt.plot(x, y)
    plt.show()


def plot_function_and_derivative(function, a, b, h, n=0.1):
    """Plot a function and its derivative between a and b.

    Arguments:
        function (lambda) -- the function to plot
        a        (float)  -- where to start plotting
        b        (float)  -- where to stop plotting
        h        (float)  -- limit
        next     (int)    -- step size
    """

    # The function itself.
    x = np.arange(a, b, n)
    y = [function(x) for x in x]
    plt.plot(x, y, 'b')

    # Calculate the derivative.
    y_diff = [derivative(function, i, h) for i in x]
    plt.plot(x, y_diff, 'r')

    plt.show()
