#!/usr/bin/env python
""" Leetcode 441 - Arranging Coins

https://leetcode.com/problems/arranging-coins/

1. self-implement: Time: 9284ms Memory: 13.8MB
2. Binary Search: Time: 28ms(95%) Memory: 13.9MB(39.15%)

"""


class Solution1:
    """ self-implement """

    def arrange_coins(self, n: int) -> int:
        for x in range(2**32):
            if x + x**2 == 2 * n:
                return x
            elif x + x**2 > 2 * n:
                return x - 1


class Solution2:
    """ Binary search """

    def arrange_coins(self, n):
        start = 0
        end = n
        while start <= end:
            mid = start + ((end - start) >> 1)
            temp = mid * (mid+1) / 2

            if temp > n:
                end = mid - 1
            elif (mid+1) * (mid+2) / 2 > n:
                return mid
            else:
                start = mid + 1


if __name__ == '__main__':
    n = 12
    res = Solution2().arrange_coins(n)
    print(res)
