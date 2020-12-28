""" Leetcode 754 - Reach a Number

https://leetcode.com/problems/reach-a-number/

1. Time: O(1) Memory: O(1)

"""

from math import sqrt, ceil


class Solution1:
    """ 1. Math """

    def reach_number(self, target: int) -> int:
        target = abs(target)
        min_x = ceil((sqrt(1 + 8 * target) - 1) / 2)
        summation = (1+min_x) * min_x / 2
        if (summation - target) % 2:
            return min_x + 2 ** ((min_x + 1) % 2 == 0)
        else:
            return min_x


if __name__ == '__main__':
    target = 2
    res = Solution1().reach_number(target)
    print(res)
