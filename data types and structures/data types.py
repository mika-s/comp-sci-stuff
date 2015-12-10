# -*- coding: utf-8 -*-
"""Implementation of basic data types in Python"""

from decimal import *


# Boolean data types

true_boolean = True
false_boolean = False

print("{0}, {1}".format(true_boolean, type(true_boolean)))
print("{0}, {1}".format(false_boolean, type(false_boolean)))

# Numeric data types

integer = 1
floating_point = 1.0
fixed_point = Decimal('1.0')
complex = 1 + 2j

print("{0}, {1}".format(integer, type(integer)))
print("{0}, {1}".format(floating_point, type(floating_point)))
print("{0}, {1}".format(fixed_point, type(fixed_point)))
print("{0}, {1}".format(complex, type(complex)))

# Composite data types

list = [1, 2, 3]		# "array"
tuple = (1, 2)

print("{0}, {1}".format(list, type(list)))
print("{0}, {1}".format(tuple, type(tuple)))

# String and text types

string = "this is a string"
character = 'c'			# basically a string

print("{0}, {1}".format(string, type(string)))
print("{0}, {1}".format(character, type(character)))
