""" Leetcode 309 - Best Time to Buy and Sell Stock with Cooldown

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

1. DP: Time: O(n) Space: O(1)

"""

from typing import List

INT_MIN = - 2**32 + 1


class Solution1:
    """ 1. DP """

    def max_profit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        b1, s1, s2 = INT_MIN, 0, 0
        for price in prices:
            b0 = max(b1, s2-price)
            s0 = max(s1, b1+price)
            b1, s1, s2 = b0, s0, s1
        return s0


if __name__ == '__main__':
    prices = [1, 2]
    res = Solution1().max_profit(prices)
    print(res)
