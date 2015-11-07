# -*- coding: utf-8 -*-

import math

def simpsons_rule(function, a, b, n):
    """Numerically integrate a function between a and b,
    using n subintervals, by Simpson's rule.

    Note:
        n has to be even.

    Arguments:
        function (lambda) -- the function to integrate over
        a        (float)  -- where to start integrating
        b        (float)  -- where to stop integrating
        n        (int)    -- subintervals
    """

    return ((b - a)/6.0) * (function(a) + 4 * function((a + b)/2.0) + function(b))


def main():
    print("Simpson's rule: ")
    print(simpsons_rule(lambda x:x**2, 0.0, 2.0, 10))


if __name__ == "__main__":
    main()
