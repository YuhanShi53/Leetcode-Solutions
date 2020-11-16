""" Leetcode 41 - First Missing Positive

https://leetcode.com/problems/first-missing-positive/

1. MINE Flag: Time: O(n) Space: O(1) (n is len_num)

"""


from typing import List


class Solution1:
    """ 1. MINE Flag """

    def fisrt_missing_postive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return i + 2


if __name__ == '__main__':
    nums = [1]
    res = Solution1().fisrt_missing_postive(nums)
    print(res)
