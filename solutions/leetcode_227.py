""" Leetcode 227 - Basic Calculator II

https://leetcode.com/problems/basic-calculator-ii/

"""


class Solution1:
    """ 1. MINE-Stack """

    def calculate(self, s: str) -> int:
        s += ')'
        temp = {'+': 0, '-': 0, '*': 1, '/': 1}

        nums = []
        ops = []
        for x in s:
            if x in temp and ops and temp[x] < temp[ops[-1]]:
                nums.append(nums.pop())
