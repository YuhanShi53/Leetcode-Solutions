""" Leetcode 5 - Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/

1. Time: O(n**2) Memory: O(1) (n is length of s)

"""


class Solution1:
    """ 1. Two-Pointers """

    def longest_palindrome(self, s: str) -> str:
        low, max_length = 0, 0
        if len(s) < 2:
            return s

        def extend_palindrome(left, right):
            nonlocal low, max_length
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > max_length:
                low = left + 1
                max_length = right - left - 1

        for i in range(len(s)):
            extend_palindrome(i, i)
            extend_palindrome(i, i+1)

        return s[low:low+max_length]


if __name__ == '__main__':
    s = 'babad'
    res = Solution1().longest_palindrome(s)
    print(res)
