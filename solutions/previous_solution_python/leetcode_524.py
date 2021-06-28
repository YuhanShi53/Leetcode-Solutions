""" Leetcode 524 - Longest Word in Dictionary Through Deleting

https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

1. Time: O(m*n) Memory: O(n) (m is length of string, n is size of dict)
2. Time: O(m*n) Memory: O(n) (m is length of string, n is size of dict)

"""

from typing import List


class Solution1:
    """ 1. MINE | Brute-Force """

    def find_longest_word(self, s: str, d: List[str]) -> str:
        indices = [0 for i in range(len(d))]
        res = ''
        for x in s:
            for i in range(len(d)):
                if indices[i] < len(d[i]) and x == d[i][indices[i]]:
                    indices[i] += 1
                if indices[i] == len(d[i]):
                    res = min(d[i], res, key=lambda x: (-len(x), x))
        return res


class Solution2:
    """ 2. Accelerate Solution1 with Python built-in """

    def find_longest_word(self, s, d):
        res = ''
        for string in d:
            if len(string) >= len(res):
                if len(string) > len(res) or string < res:
                    idx = -1
                    try:
                        for x in string:
                            idx = s.index(x, idx+1)
                        res = string
                    except ValueError:
                        continue
        return res


if __name__ == '__main__':
    s = 'bab'
    d = ["ba", "ab", "a", "b"]
    res = Solution2().find_longest_word(s, d)
    print(res)
