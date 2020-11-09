""" Leetcode 119 - Pascals Triangle II

https://leetcode.com/problems/pascals-triangle-ii/

1. SM Array: Time: O(k**2) Space: O(k) (k is row index)

"""

from typing import List


class Solution1:
    """ 1. SM Array """

    def get_row(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res.append(0)
            for i in range(len(res) - 1, 0, -1):
                res[i] += res[i - 1]
        return res


if __name__ == '__main__':
    row_index = 3
    res = Solution1().get_row(row_index)
    print(res)
