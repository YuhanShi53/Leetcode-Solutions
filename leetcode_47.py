""" Leetcode 47 - Permutation II 

https://leetcode.com/problems/permutations-ii

1. SM-DFS: Time: O(n^2) Space: O(n^2)

"""

from collections import defaultdict
from typing import List


class Solution1:
    """ 1. SM-DFS """

    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        num_dict = defaultdict(int)
        max_len = len(nums)
        permutations = []
        for x in nums:
            num_dict[x] += 1

        def helper(permutation):
            if len(permutation) == max_len:
                permutations.append(permutation)
                return
            for x, count in num_dict.items():
                if count > 0:
                    num_dict[x] -= 1
                    helper(permutation + [x])
                    num_dict[x] += 1

        helper([])
        return permutations


if __name__ == '__main__':
    nums = [1]
    res = Solution1().permute_unique(nums)
    print(res)
