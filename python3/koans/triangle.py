#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if (any (x<=0 for x in [a,b,c])): # all sides greater than 0
        raise TriangleError
    elif (a+b<c or b+c<a or a+c<b): # The sum of any two sides should be greater than the third one
        raise TriangleError

    if (a==b and b==c):
        return "equilateral"
    elif (a==b or b==c or a==c):
        return "isosceles"
    else:
        return "scalene"

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
