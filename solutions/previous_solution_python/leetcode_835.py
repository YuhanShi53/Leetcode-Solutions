""" Leetcode 835 - Image Overlap

https://leetcode.com/problems/image-overlap/


1. Brute-Force: Time: (N**4) Space: O(1)

"""

from typing import List


class Solution1:
    """ 1. Brute-Force """

    def largest_overlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        max_overlap = 0

        def conv(a, b):
            max_overlap = 0
            num = len(a)
            for i in range(num):
                for j in range(num):
                    overlap = 0
                    for ii in range(num):
                        for jj in range(num):
                            if i + ii < num and j + jj < num:
                                overlap += a[ii][jj] and b[i + ii][j + jj]
                    max_overlap = max(max_overlap, overlap)

            return max_overlap

        max_overlap = max(max_overlap, conv(A, B))
        max_overlap = max(max_overlap, conv(B, A))
        return max_overlap


if __name__ == '__main__':
    A = [[1]]
    B = [[0]]
    res = Solution1().largest_overlap(A, B)
    print(res)
