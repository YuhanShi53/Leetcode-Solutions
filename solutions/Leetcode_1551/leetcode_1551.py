""" Leetcode 1551 - Minimum Operations to Make Array Equal

https://leetcode.com/problems/minimum-operations-to-make-array-equal/

"""


class Solution1:
    """ 1. MINE | Math """

    def min_operations(self, n: int) -> int:
        return n * n >> 2


if __name__ == '__main__':
    n = 2
    ans = Solution1().min_operations(n)
    print(ans)
