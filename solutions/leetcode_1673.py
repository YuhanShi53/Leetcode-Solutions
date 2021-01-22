""" Leetcode 1673 - Find the Most Competitive Subsequence

https://leetcode.com/problems/find-the-most-competitive-subsequence/

"""

from typing import List


class Solution1:
    """ 1. MINE | Stack """

    def most_competitive(self, nums: List[int], k: int) -> List[int]:
        competitive = []
        for i, x in enumerate(nums):
            while len(competitive) + len(nums) - i > k and competitive and x < competitive[-1]:
                competitive.pop()
            competitive.append(x)
        return competitive[:k]


if __name__ == '__main__':
    nums = [2, 4, 3, 3, 5, 4, 9, 6]
    k = 4
    res = Solution1().most_competitive(nums, k)
    print(res)
