""" Leetcode 171 - Excel Sheet Column Number

https://leetcode.com/problems/excel-sheet-column-number/

1. Math: Time: O(n) Space: O(n) (n is length of string)

"""

from functools import reduce


class Solution1:
    """ 1. Math """

    def title_to_number(self, s: str) -> int:
        return reduce(lambda x, y: x * 26 + y, [ord(x) - 64 for x in s])


if __name__ == '__main__':
    s = 'AB'
    res = Solution1().title_to_number(s)
    print(res)
