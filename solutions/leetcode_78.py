""" Leetcode 78 - Subsets

https://leetcode.com/problems/subsets/

1. self-implement Iterative: Time: 44ms(26%) Memory: 13.7MB(99%)


"""
from typing import List

class Solution1:
    """ 1. Self-implement Iterative """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for x in nums:
            for i in range(len(sets)):
                sets.append(sets[i] + [x])
        return sets

if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution1().subsets(nums)
    print(res)