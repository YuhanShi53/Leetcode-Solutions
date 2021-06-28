""" Leetcode 66 - Plus One

https://leetcode.com/problems/plus-one/

1. self-implement: Time: 40ms(21%) Memory: 14MB(6%)
"""

from typing import List

class Solution1:
    """ 1. self-implement """
    def plus_one(self, digits: List[int]) -> List[int]:
        flag = False
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
            flag = True
        if flag:
            digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    digits = [9, 9, 9]
    res = Solution1().plus_one(digits)
    print(res)
