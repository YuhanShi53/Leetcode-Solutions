""" Leetcode 991 - Broken Calculator

https://leetcode.com/problems/broken-calculator/

1. Time: O(logY) Memory: O(1)

"""


class Solution1:
    """ 1. MINE | Greedy """

    def broken_calc(self, X: int, Y: int) -> int:
        count = 0
        while X < Y:
            if Y % 2:
                Y += 1
            else:
                Y //= 2
            count += 1
        return count + X - Y


if __name__ == '__main__':
    X = 16
    Y = 30
    res = Solution1().broken_calc(X, Y)
    print(res)
