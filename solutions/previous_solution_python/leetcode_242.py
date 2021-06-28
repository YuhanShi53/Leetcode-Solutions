""" Leetcode 242 - Valid Anagram

https://leetcode.com/problems/valid-anagram/

1. Time: O(n) Memory: O(m) (m is size of alphabet, n is length of string)
2. Time: O(n) Memory: O(m) (m is size of alphabet, n is length of string)

"""


class Solution1:
    """ 1. MINE | Hash Map """
    def is_anagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for x in s:
            s_count[x] += 1
        for x in t:
            t_count[x] += 1
        return s_count.items() == t_count.items()


class Solution2:
    """ 2. Hash Map | Use Python Counter """
    def is_anagram(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    s = "cat"
    t = "car"
    res = Solution1().is_anagram(s, t)
    print(res)
