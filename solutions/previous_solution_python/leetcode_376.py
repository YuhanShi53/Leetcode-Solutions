""" Leetcode 376 - Wiggle Subsequence

https://leetcode.com/problems/wiggle-subsequence/

1. Time: O(n) Memory: O(1)
2. TIme: O(n) Memory: O(1)

"""

from typing import List


class Solution1:
    """ 1. MINE | Greedy """

    def wiggle_max_length(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        length = 1
        prev = float('nan')
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if not (nums[i] - nums[i-1]) * prev >= 0:
                length += 1
                prev = nums[i] - nums[i-1]
        return length


class Solution2:
    """ 2. Dynamic Programming """

    def wiggle_max_length(self, nums):
        if len(nums) < 2:
            return len(nums)
        decrease, increase = 1, 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                increase = decrease + 1
            elif nums[i] - nums[i-1] < 0:
                decrease = increase + 1
        return max(decrease, increase)


if __name__ == '__main__':
    nums = [1, 1, 1, 2]
    res = Solution1().wiggle_max_length(nums)
    print(res)
