""" Leetcode 123 - 

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


"""

from typing import List


class Solution1:

    INT_MIN = - 2**32 + 1

    def max_profit(self, prices: List[int]) -> int:

        first_buy = self.INT_MIN
        first_sell = self.INT_MIN
        sec_buy = self.INT_MIN
        sec_sell = self.INT_MIN
        for x in prices:
            sec_sell = max(sec_sell, sec_buy + x)
            sec_buy = max(sec_buy, first_sell-x)
            first_sell = max(first_sell, first_buy+x)
            first_buy = max(first_buy, -x)
        return max(first_sell, sec_sell)


if __name__ == '__main__':
    nums = [1, 2, 3, 0, 2]
    res = Solution1().max_profit(nums)
    print(res)
