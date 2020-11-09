""" Leetcode 152 - Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/

1. SM Dynamic-Programming: Time: O(n) Space: O(1) (n is len_nums)
2. Dynamic-Programming: Time: O(n) Space: O(1) (n is len_nums)

"""

from typing import List


class Solution1:
    """ 1. SM Dynamic-Programming """

    def max_product(self, nums: List[int]) -> int:
        positive = 1
        negative = 1
        maximum = -2**31 + 1

        for x in nums:
            if x == 0:
                positive = 0
                negative = 0
            elif x < 0:
                positive, negative = negative*x, min(positive*x, x)
            else:
                positive, negative = max(positive*x, x), negative*x
            maximum = max(maximum, positive)
        return maximum


class Solution2:
    """ 2. Dynamic-Programming """

    def max_product(self, nums: List[int]) -> int:
        prefix = 0
        suffix = 0
        maximum = -2**31 + 1
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            maximum = max(maximum, prefix, suffix)
        return maximum


if __name__ == '__main__':
    nums = [-4]
    res = Solution2().max_product(nums)
    print(res)
