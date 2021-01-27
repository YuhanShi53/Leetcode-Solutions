""" Leetcode 1680 - 

https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

1. Time: O(n) Memory: O(1)
2. Time: O(n) Memory: O(1)

"""


class Solution1:
    """ 1. MINE | Bit-Manipulation | Math """

    def concatenated_binary(self, n: int) -> int:
        res = 0
        for x in range(1, n+1):
            res = (res * (1 << (len(bin(x)) - 2)) + x) % 1000000007
        return res % 1000000007


class Solution2:
    """ 2. Improvement of 1 """

    def concatenated_binary(self, n):
        res, length = 0, 0
        for x in range(1, n+1):
            if x & (x - 1) == 0:
                length += 1
            res = (res * (1 << length) + x) % 1000000007
        return res % 1000000007


if __name__ == '__main__':
    n = 63556
    res = Solution2().concatenated_binary(n)
    print(res)
