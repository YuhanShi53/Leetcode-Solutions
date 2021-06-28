""" Leetcode 593 - Valid Square

https://leetcode.com/problems/valid-square/

1. MINE-Math: Time: O(nlogn) Space: O(n) (n is num_of_vectors)
2. Math: Time: O(nlogn) Space: O(n) (n is num_of_vectors)

"""

from typing import List


class Solution1:
    """ 1. MINE-Math """

    def valid_square(self,
                     p1: List[int],
                     p2: List[int],
                     p3: List[int],
                     p4: List[int]) -> bool:
        vectors = [(x[0] - p1[0], x[1] - p1[1]) for x in [p2, p3, p4]]
        vector_mods = [x[0]**2 + x[1]**2 for x in vectors]
        vectors, mods = list(
            zip(*sorted(zip(vectors, vector_mods), key=lambda x: x[1])))
        if (mods[0] + mods[1] == mods[2]
                and vectors[0][0] + vectors[1][0] == vectors[2][0]
                and vectors[0][1] + vectors[1][1] == vectors[2][1]
                and mods[0] == mods[1] > 0):
            return True
        return False


class Solution2:
    """ 2. Math """

    def valid_square(self, p1, p2, p3, p4):

        def d(x1, x2):
            return (x1[0] - x2[0])**2 + (x1[1]-x2[1])**2

        diffs = [d(p1, p2), d(p1, p3), d(p1, p4),
                 d(p2, p3), d(p2, p4), d(p3, p4)]
        diffs.sort()
        if diffs[0] != 0 and diffs[3] < diffs[4] and len(set(diffs)) == 2:
            return True
        return False


if __name__ == '__main__':
    p1 = [1, 0]
    p2 = [-1, 0]
    p3 = [0, 1]
    p4 = [0, -1]
    if Solution2().valid_square(p1, p2, p3, p4):
        print('yes')
