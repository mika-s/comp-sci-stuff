# -*- coding: utf-8 -*-
"""Various numerical integration methods."""


def simpsons_rule(function, a, b):
    """Numerically integrate a function between a and b,
    by Simpson's rule.

    Arguments:
        function (lambda) -- the function to integrate over
        a        (float)  -- where to start integrating
        b        (float)  -- where to stop integrating
    """

    return ((b - a)/6.0) * \
        (function(a) + 4 * function((a + b)/2.0) + function(b))


def composite_simpsons_rule(function, a, b, n):
    """Numerically integrate a function between a and b,
    using n subintervals, by the composite Simpson's rule.

    Note:
        n has to be even.

    Arguments:
        function (lambda) -- the function to integrate over
        a        (float)  -- where to start integrating
        b        (float)  -- where to stop integrating
        n        (int)    -- subintervals
    """

    h = (b - a) / n
    s = function(a) + function(b)

    for j in range(1, n//2):
        s += 2 * function(2 * (a + j * h))

    for j in range(1, n//2 + 1):
        s += 4 * function(2 * (a + j * h) - h)

    return (h/3.0) * s


def uniform_trapezoidal_rule(function, a, b, n):
    """Numerically integrate a function between a and b,
    using n subintervals, by the Trapezoidal rule, using
    an uniform grid.

    Arguments:
        function (lambda) -- the function to integrate over
        a        (float)  -- where to start integrating
        b        (float)  -- where to stop integrating
        n        (int)    -- subintervals
    """

    h = (b - a) / n

    s = 0
    for j in range(1, n + 1):
        s += function(a + h * (j + 1))  + function(a + h * j)

    return (h/2.0) * s


def main():
    """The main function. Used to test the other functions."""

    print("Simpson's rule:")
    print(simpsons_rule(lambda x: x**2, 0.0, 2.0))

    print("\nComposite Simpson's rule:")
    print(composite_simpsons_rule(lambda x: x**2, 0.0, 2.0, 100))

    print("\nTrapezoidal rule (uniform grid):")
    print(uniform_trapezoidal_rule(lambda x: x**2, 0.0, 2.0, 100))


if __name__ == "__main__":
    main()
