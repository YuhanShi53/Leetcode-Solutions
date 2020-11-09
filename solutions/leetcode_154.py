""" Leetcode 154 - Find Minimum in Rotated Sorted Array II

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

1. SM Traversal: Time: O(n) Memory: O(1)
2. Binary-Search: Time: AVG-O(logn) WORST-O(n) Memory:O(1)

"""

from typing import List


class Solution1:
    """ 1. SM Traversal """

    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        for x in nums[1:]:
            if x < prev:
                return x
            prev = x
        return nums[0]


class Solution2:
    """ 2. Binary-Search """

    def find_min(self, nums):
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
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1
        return nums[low]


if __name__ == '__main__':
    nums = [2, 2, 2, 0, 1]
    res = Solution2().find_min(nums)
    print(res)
