# -*- coding: utf-8 -*-
"""Various numerical differentiation methods."""

from plotting import *


def derivative(function, x, h):
    """Numerically differentiate a function in point x,
    by the definition of the derivative, using a constant h.

    Arguments:
        function (lambda) -- the function to differentiate
        x        (float)  -- where to differentiate
        h        (float)  -- limit
    """

    return (function(x + h) - function(x)) / h


def main():
    """The main function. Used to test the other functions."""

    print("\nDerivative by formula:")
    print(derivative(lambda x: x**2, 2.0, 0.0001))

    #plot_function(lambda x: x**2, 0, 10)
    plot_function_and_derivative(lambda x: x**2, 0, 10, h = 0.0001)


if __name__ == "__main__":
    main()
