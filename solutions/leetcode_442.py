""" Leetcode 442 - Find All Duplicates in An Array

https://leetcode.com/problems/find-all-duplicates-in-an-array/

1. Inplace-Hash: Time: O(n) Space: O(1)

"""

from typing import List


class Solution1:
    """ 1. Inplace-Hash """

    def find_duplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                duplicates.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return duplicates


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    duplicates = Solution1().find_duplicates(nums)
    print(duplicates)
