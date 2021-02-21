""" Leetcode 13 - Roman to Integer

https://leetcode.com/problems/roman-to-integer/

1. Time: O(n) Memory: O(1) (n is length of string)

"""


class Solution1:
    """ 1. MINE | Hash Map """

    def roman_to_int(self, s: str) -> int:
        roman_int_pair = {'M': 1000,
                          'D': 500,
                          'C': 100,
                          'L': 50,
                          'X': 10,
                          'V': 5,
                          'I': 1}
        res = 0
        for i, x in enumerate(s):
            if i + 1 < len(s) and roman_int_pair[x] < roman_int_pair[s[i+1]]:
                res -= roman_int_pair[x]
            else:
                res += roman_int_pair[x]
        return res


if __name__ == '__main__':
    roman = ''
    res = Solution1().roman_to_int(roman)
    print(res)
