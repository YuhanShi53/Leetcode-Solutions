""" Leetcode 714 - Best Time To Buy and Sell Stock With Transcation Fee

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

1. Time: O(n) Memory: O(1) (n is length of prices)
2. Time: O(n) Memory: O(1) (n is length of prices)

"""

from typing import List


class Solution1:
    """ 1. MINE | Dynamic Programming """

    def max_profit(self, prices: List[int], fee: int) -> int:
        pre_buy, pre_sell = -5e4, 0
        for x in prices:
            pre_buy, pre_sell = max(
                pre_buy, pre_sell - x - fee), max(pre_sell, pre_buy + x)
        return pre_sell


class Solution2:
    """ 2. Greedy

    Borrow from: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/201603/Python.-Greedy-is-good.

    """

    def max_profit(self, prices, fee):
        profit, minimum = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                profit += prices[i] - minimum - fee
                minimum = prices[i] - fee
        return profit


if __name__ == '__main__':
    prices = [3, 1]
    fee = 3
    res = Solution1().max_profit(prices, fee)
    print(res)
