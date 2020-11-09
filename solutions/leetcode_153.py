""" Leetcode 153 - Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

1. Binary Search: Time: O(logn) Memory: O(1)

"""

from typing import List


class Solution1:
    """ 1. Binary-Search """

    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[high]


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    res = Solution1().find_min(nums)
    print(res)
