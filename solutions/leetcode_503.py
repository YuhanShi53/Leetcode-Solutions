""" Leetcode 503 - Next Greater Element II

https://leetcode.com/problems/next-greater-element-ii/

1. Mono Stack: Time: 224ms(89%) Memory: 15.2MB(83%)

"""

from typing import List


class Solution1:
    """ 1. Mono Stack """

    def next_greater_elements(self, nums: List[int]) -> List[int]:
        monostack = []
        greater_elements = [-1 for i in range(len(nums))]
        for i in range(len(nums)*2):
            actual_i = i % len(nums)

            while monostack and nums[actual_i] > nums[monostack[-1]]:
                j = monostack.pop()
                greater_elements[j] = nums[actual_i]

            if i == actual_i:
                monostack.append(actual_i)
        return greater_elements


if __name__ == '__main__':
    nums = [1, 2, 1]
    res = Solution1().next_greater_elements(nums)
    print(res)
