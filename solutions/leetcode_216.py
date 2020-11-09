""" Leetcode 216 - Combination Sum III

https://leetcode.com/problems/combination-sum-iii/

1. SM Backtracking & DFS

"""

from typing import List


class Solution1:
    """ 1. SM Backtracking & DFS """

    def combination_sum_3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 or n == 0:
            return []

        def combination(k, n, threshold):
            if k == 1:
                if threshold <= n < 10:
                    return [[n]]
                else:
                    return []

            candidates = []
            for x in range(threshold, min(n+1, 10)):
                temp = combination(k-1, n-x, x+1)
                if temp:
                    for y in temp:
                        candidates.append([x] + y)
            return candidates

        combinations = combination(k, n, 1)
        return combinations


if __name__ == '__main__':
    k = 1
    n = 10
    res = Solution1().combination_sum_3(k, n)
    print(res)
