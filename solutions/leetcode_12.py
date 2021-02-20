""" Leetcode 12 - Interger to Roman

https://leetcode.com/problems/integer-to-roman/

1. Time: O(1) Memory: O(1)

"""


class Solution1:
    """ 1. MINE | Straight-Forward """

    def int_to_roman(self, num):
        if num is None or num == 0:
            return ''
        int_roman_pairs = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                           (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                           (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        res = ''
        for value, roman in int_roman_pairs:
            if num >= value:
                res += num // value * roman
                num -= num // value * value
            elif num == 0:
                return res
        return res


if __name__ == '__main__':
    num = 300
    res = Solution1().int_to_roman(num)
    print(res)
