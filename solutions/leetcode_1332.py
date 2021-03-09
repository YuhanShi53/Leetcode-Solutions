""" Leetcode 1332 - Remove Palindromic Subsequences

https://leetcode.com/problems/remove-palindromic-subsequences/

"""


class Solution1:
    """ 1. String """

    def remove_palindrome_sub(self, s: str) -> int:
        if s == "":
            return 0
        if s == s[::-1]:
            return 1
        return 2


if __name__ == '__main__':
    s = 'abb'
    res = Solution1().remove_palindrome_sub(s)
    print(res)
