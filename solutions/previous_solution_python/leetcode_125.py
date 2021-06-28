""" Leetcode 125 - Valid Palindrome

https://leetcode.com/problems/valid-palindrome/


1. MINE Two-Pointer: Time: O(n) Space: O(n)
2. Simiplified Two-Pointer: Time: O(n) Space: O(1)

"""


class Solution1:
    """ 1. MINE Two-Pointer """

    def is_palindrome(self, s: str) -> bool:
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet_dict = {}
        for x, y in zip(lower_alphabet, upper_alphabet):
            alphabet_dict[y] = x
        for x in lower_alphabet + '0123456789':
            alphabet_dict[x] = x

        format_s = []
        for x in s:
            if alphabet_dict.get(x, 0):
                format_s.append(alphabet_dict[x])
        format_s = ''.join(format_s)

        low, high = 0, len(format_s) - 1
        while low < high:
            if format_s[low] != format_s[high]:
                return False
            low += 1
            high -= 1
        return True


class Solution2:
    """ 2. Simiplified Two-pointer """

    def is_palindrome(self, s):
        low, high = 0, len(s) - 1
        while low < high:
            while low < high and not s[low].isalnum():
                low += 1
            while low < high and not s[high].isalnum():
                high -= 1
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True


if __name__ == '__main__':
    s = "race a car"
    res = Solution2().is_palindrome(s)
    print(res)
