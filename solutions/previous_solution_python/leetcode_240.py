""" Leetcode 240 - Search A 2D Matrix II

https://leetcode.com/problems/search-a-2d-matrix-ii/

1. Time: O(m*logn) Memory: O(1) (m, n are height and width of matrix)
2. Time: O(m+n) Memory: O(1) (m, n are height and width of matrix)

"""

from typing import List


class Solution1:
    """ 1. MINE | Binary Search """

    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        threshold = len(matrix[0]) - 1
        for i in range(len(matrix)):
            left = 0
            right = threshold
            while left <= right:
                mid = (left+right)//2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    left = mid + 1
                else:
                    threshold = mid - 1
                    right = mid - 1
        return False


class Solution2:
    """ 2. Binary Search """

    def search_matrix(self, matrix, target):
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
target = 0
res = Solution2().search_matrix(matrix, target)
print(res)
