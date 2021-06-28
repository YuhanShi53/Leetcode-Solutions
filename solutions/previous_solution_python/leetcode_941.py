""" Leetcode 941 - Valid Mountain Array

https://leetcode.com/problems/valid-mountain-array/

1. Time: O(N) Memory: O(1) (N is length of arr)
2. Time: O(N) Memory: O(1) (N is length of arr)

"""

from typing import List


class Solution1:
    """ 1. MIME | Straight-Forward """

    def valid_mountain_array(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        prev_grad = 0
        for i in range(len(arr) - 1):
            grad = arr[i+1] - arr[i]
            if (grad == 0
                    or grad > 0 and prev_grad < 0
                    or grad < 0 and prev_grad == 0):
                return False
            prev_grad = grad
        return grad < 0


class Solution2:
    """ 2. Two-Pointer """

    def valid_mountain_array(self, arr):
        if len(arr) < 3:
            return False
        start, end, length = 0, len(arr) - 1, len(arr)
        while start < length - 1 and arr[start+1] > arr[start]:
            start += 1
        while end > 0 and arr[end-1] > arr[end]:
            end -= 1
        return 0 < start == end < length - 1


if __name__ == '__main__':
    nums = [0, 3, 3, 2, 1]
    is_valid = Solution1().valid_mountain_array(nums)
    print(f'Is valid mountain: {is_valid}')
