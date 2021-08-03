from collections import defaultdict
from typing import List


class Solution1:
    def subsets_with_dup(self, nums):
        nums.sort()
        subsets = [[]]
        i = 0
        for i, x in enumerate(nums):
            if i == 0 or x != nums[i-1]:
                prev_len = len(subsets)
            for j in range(len(subsets) - prev_len, len(subsets)):
                subsets.append(subsets[j] + [x])
        return subsets


class SolutionMINE:
    def subsets_with_dup(self, nums: List[List[int]]) -> List[List[int]]:
        num_dict = defaultdict(int)
        for x in nums:
            num_dict[x] += 1
        subsets = [[]]
        for num, count in num_dict.items():
            append_items = [[num] * c for c in range(1, count+1)]
            for i in range(len(subsets)):
                for append_item in append_items:
                    subsets.append(subsets[i] + append_item)
        return subsets
