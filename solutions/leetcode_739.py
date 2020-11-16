""" Leetcode 739 - Daily Temperatures

https://leetcode.com/problems/daily-temperatures/

1. MINE Mono-Stack: Time: O(n) Space: O(n)

"""

from typing import List


class Solution1:
    """ 1. MINE Mono-Stack """

    def daliy_temperatures(self, T: List[int]) -> List[int]:
        mono_stack = []
        res = [0 for i in range(len(T))]
        for i, x in enumerate(T):
            while mono_stack and T[mono_stack[-1]] < x:
                day_idx = mono_stack.pop()
                res[day_idx] = i - day_idx
            mono_stack.append(i)
        return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = Solution1().daliy_temperatures(temperatures)
    print(res)
