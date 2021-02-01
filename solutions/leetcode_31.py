""" Leetcode 31 - Next Permutation

https://leetcode.com/problems/next-permutation/

1. Time: O(n) Memory: O(1) (n is length of nums)

"""

from typing import List


class Solution1:
    """ 1. Array """

    def next_permutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return
        pointer = len(nums) - 2

        while pointer >= 0:
            if nums[pointer] < nums[pointer+1]:
                target_i = self._find_smallest_larger_num(pointer, nums)
                nums[pointer], nums[target_i] = nums[target_i], nums[pointer]
                nums[pointer+1::] = nums[len(nums)-1:pointer:-1]
                return
            pointer -= 1
        nums[0:] = nums[-1::-1]

    def _find_smallest_larger_num(self, pointer, nums):
        target = len(nums) - 1
        for i in range(target, pointer, -1):
            if nums[i] > nums[pointer]:
                return i


if __name__ == "__main__":
    nums = [1, 2, 4, 3]
    Solution1().next_permutation(nums)
    print(nums)
