""" Leetcode 121 - Bset Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

1. MINE DP & Kadane: Time: O(n) Space: O(1) (n is len_prices)
2. DP: Time: O(n) Space: O(1) (n is len_prices)

"""

from typing import List


class Solution1:
    """ 1. MINE DP & Kadane """

    def max_profit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maximum = 0
        local_maximum = 0
        for i in range(1, len(prices)):
            local_maximum = max(local_maximum+prices[i] - prices[i-1], 0)
            maximum = max(maximum, local_maximum)
        return maximum


class Solution2:
    """ 2. DP """

    def max_profit(self, prices):
        if len(prices) < 2:
            return 0

        buy = prices[0]
        sell = 0

        for x in prices:
            buy = min(x, buy)
            sell = max(x - buy, sell)
        return sell


if __name__ == '__main__':
    nums = [0, 6, -3, 7]
    res = Solution2().max_profit(nums)
    print(res)
