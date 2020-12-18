""" Leetcode 454 - 4 Sum II

https://leetcode.com/problems/4sum-ii/

"""

from collections import defaultdict
from typing import List


class Solution1:
    def four_sum_count(self,
                       A: List[int],
                       B: List[int],
                       C: List[int],
                       D: List[int]) -> int:
        num_dict = defaultdict(int)
        for x in D:
            num_dict[x] += 1
        count = 0
        for x in A:
            for y in B:
                for z in C:
                    count += num_dict[-x-y-z]
        return count


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    count = Solution1().four_sum_count(A, B, C, D)
    print(count)
