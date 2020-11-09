""" Leetcode 409 - Longest Palindrome

https://leetcode.com/problems/longest-palindrome/


"""

from collections import defaultdict


class Solution1:
    """ 1. SM Hash-Table """

    def longest_palindrome(self, s: str) -> int:
        num_counts = defaultdict(int)
        for x in s:
            num_counts[x] += 1
        length = 0
        has_odd = 0
        for x in num_counts.values():
            length += x // 2 * 2
            has_odd = max(x % 2, has_odd)
        return length + has_odd


if __name__ == '__main__':
    s = 'abccccdd'
    res = Solution1().longest_palindrome(s)
    print(res)
