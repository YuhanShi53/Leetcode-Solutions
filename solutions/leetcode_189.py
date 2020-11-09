""" Leetcode 189 - Rotate Array

https://leetcode.com/problems/rotate-array/


"""

from typing import List


class Solution1:
    """ 1. SM Recursive """

    def rotate(self, nums: List[int], k: int) -> None:

        def move_right():
            nums[0], nums[1:] = nums[-1], nums[:-1]

        for i in range(k):
            move_right()


class Solution2:
    """ 2. SM Index-Reverse """

    def rotate(self, nums, k):
        k %= len(nums)
        idx = len(nums) - k
        nums[:k], nums[k:] = nums[idx:], nums[:idx]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res = Solution2().rotate(nums, k)
    print(nums)
