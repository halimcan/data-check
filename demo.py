"""Module providing circle area calculation."""

import math

def circle_area(radius):
    """Return the area of a circle given its radius.

    Returns 0 if radius is negative.
    """
    if radius < 0:
        return 0
    return round(math.pi * radius ** 2, 2)
