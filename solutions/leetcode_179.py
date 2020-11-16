""" Leetcode 179 - Largest Number

https://leetcode.com/problems/largest-number/


"""

from typing import List


class Solution1:
    """ 1. MINE """

    def largest_number(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return '0'
        nums = list(map(lambda x: str(x), nums))

        for i in range(len(nums)):
            is_change = False
            for j in range(len(nums) - i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    is_change = True
            if not is_change:
                break
        return ''.join(nums)


if __name__ == '__main__':
    nums = [121, 12]
    res = Solution1().largest_number(nums)
    print(res)
