""" Leetcode 478 - Generate Random Point In A Circle

https://leetcode.com/problems/generate-random-point-in-a-circle/

"""

from typing import List

from math import sqrt, pi, cos, sin
from random import random


class Solution1:
    """ 1. Math

    Borrow from: https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/154037/Polar-Coordinates-10-lines
    For explanation, please head to: https://meyavuz.wordpress.com/2018/11/15/generate-uniform-random-points-within-a-circle/

    """

    def __init__(self, radius: float, x_center: float, y_center: float):
        self._radius = radius
        self._x_center = x_center
        self._y_center = y_center

    def rand_point(self) -> List[float]:
        r = sqrt(random()) * self._radius
        angle = random() * 2 * pi
        x = self._x_center + r * cos(angle)
        y = self._y_center + r * sin(angle)
        return [x, y]


if __name__ == '__main__':
    radius = 1.0
    x_center = 0.0
    y_center = 0.0
    x, y = Solution1(radius, x_center, y_center).rand_point()
    print(x, y)
