""" Leetcode 413 - Arithmetic Slices

https://leetcode.com/problems/arithmetic-slices/

1. Time: O(n) Memory: O(1) (n is length of A)
2. Time: O(n) Memory: O(1) (n is length of A)

"""

from typing import List


class Solution1:
    """ 1. MINE | Math """

    def number_of_arithmetic_slices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        left, diff, count = -1, None, 0
        for i in range(1, len(A)):
            if A[i] - A[i-1] != diff:
                n = i - left - 1
                count += max(0, n*(n-1)//2)
                left = i - 1
                diff = A[i] - A[i-1]
        n = len(A) - left - 1
        count += max(0, n*(n-1)//2)
        return count


class Solution2:
    """ 2. Dynamic Programming """

    def number_of_arithmetic_slices(self, A):
        if len(A) < 3:
            return 0
        count, local_count = 0, 0
        for i in range(2, len(A)):
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                local_count += 1
                count += local_count
            else:
                local_count = 0
        return count


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    res = Solution2().number_of_arithmetic_slices(nums)
    print(res)
