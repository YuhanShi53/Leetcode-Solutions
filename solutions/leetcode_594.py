""" Leetcode 594 - Longest Harmonious Subsequence

https://leetcode.com/problems/longest-harmonious-subsequence/

1. Time: O(n) Memory: O(m) (m is num of unique numbers, n is length of nums)

"""

from typing import List


class Solution1:
    """ 1. MINE | Hash Map """

    def find_lhs(self, nums: List[int]) -> int:
        num_count = {}
        length = 0
        for x in nums:
            num_count[x] = num_count.get(x, 0) + 1
        for x in num_count.keys():
            if x + 1 in num_count:
                length = max(length, num_count[x] + num_count[x+1])
        return length


if __name__ == '__main__':
    nums = [1, 0]
    res = Solution1().find_lhs(nums)
    print(res)
