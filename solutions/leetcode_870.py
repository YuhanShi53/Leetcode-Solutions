""" Leetcode 870 - Advantage Shuffle

https://leetcode.com/problems/advantage-shuffle/

"""

from typing import List


class Solution1:
    """ 1. MINE """

    def advantage_count(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        advantgage = []
        for x in B:
            if A[-1] <= x:
                advantgage.append(A[0])
                A.remove(A[0])
            else:
                i, j = 0, len(A) - 1
                while i < j:
                    mid = (i + j) // 2
                    if A[mid] > x:
                        j = mid
                    else:
                        i = mid + 1
                advantgage.append(A[i])
                A.remove(A[i])
        return advantgage


if __name__ == '__main__':
    A = [2, 7, 11, 15]
    B = [1, 10, 4, 11]
    ans = Solution1().advantage_count(A, B)
    print(ans)
