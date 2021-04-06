""" Leetcode 775 - Global and Local Inversions

https://leetcode.com/problems/global-and-local-inversions/

1. Time: O(n) Memory: O(1)

"""

from typing import List


class Solution1:
    """ 1. MINE |  SPECIFIC """

    def is_ideal_permutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True


if __name__ == '__main__':
    A = [1, 2, 0]
    ans = Solution1().is_ideal_permutation(A)
    print(ans)
