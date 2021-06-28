""" Leetcode 268 - Missing Number

https://leetcode.com/problems/missing-number/

1. Time: O(n) Memory: O(1) (n is length of nums)
2. Time: O(n) Memory: O(1) (n is length of nums)

"""

from typing import List


class Solution1:
    """ 1. MINE | Array """

    def missing_number(self, nums: List[int]) -> int:
        n = len(nums)
        return (1+n)*n//2 - sum(nums)


class Solution2:
    """ 2. Bit-Manipulation """

    def missing_number(self, nums):
        res = 0
        for i in range(len(nums)):
            res ^= nums[i] ^ i
        return res ^ (i+1)


if __name__ == '__main__':
    nums = [0, 1]
    res = Solution1().missing_number(nums)
    print(res)
