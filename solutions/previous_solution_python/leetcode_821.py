""" Leetcode 821 - Shortest Distance to a Chararcter

https://leetcode.com/problems/shortest-distance-to-a-character/


1. Time: O(n) Memory: O(n) (n is length of s)
2. Time: O(n) Memory: O(n) (n is length of s)

"""

from typing import List


class Solution1:
    """ 1. MINE | Dynamic Programming """

    def shortest_to_char(self, s: str, c: str) -> List[int]:
        c_positions = [i for i, x in enumerate(s) if x == c]
        distances = [None for i in range(len(s))]
        for i in c_positions:
            distances[i] = 0
        count = len(s) - len(c_positions)
        length = 1
        while count:
            for i in range(len(c_positions)):
                temp = c_positions.pop()
                if temp - 1 >= 0 and distances[temp-1] is None:
                    distances[temp - 1] = length
                    c_positions.insert(0, temp-1)
                    count -= 1
                if temp + 1 < len(s) and distances[temp+1] is None:
                    distances[temp + 1] = length
                    c_positions.insert(0, temp+1)
                    count -= 1
            length += 1
        return distances


class Solution2:
    """ 2. Bi-Pass | Dynamic Programming """

    def shortest_to_char(self, s, c):
        n = len(s)
        distances = [0 if x == c else n for x in s]
        for i in range(1, n):
            distances[i] = min(distances[i], distances[i-1] + 1)
        for i in range(n-2, -1, -1):
            distances[i] = min(distances[i], distances[i+1] + 1)
        return distances


if __name__ == '__main__':
    s = 'loveleetcode'
    c = 'e'
    res = Solution2().shortest_to_char(s, c)
    print(res)
