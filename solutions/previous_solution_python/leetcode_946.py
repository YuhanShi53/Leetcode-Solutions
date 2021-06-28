""" Leetcode 946 - Validate Stack Sequences

https://leetcode.com/problems/validate-stack-sequences/

1. Time: O(n) Memory: O(n) (n is length of pushed/popped)
2. Time: O(n) Memory: O(1) (n is length of pushed/popped)

"""

from typing import List


class Solution1:
    """ 1. MINE | Stack """

    def validate_stack_sequences(
            self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and popped[i] == stack[-1]:
                i += 1
                stack.pop()
        return False if stack else True


class Solution2:
    """ 2. O(1) Memory version of Solution1 """

    def validate_stack_sequence(self, pushed, popped):
        i, j = 0, 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1
            i += 1
        return i == 0


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    res = Solution1().validate_stack_sequences(pushed, popped)
    print(res)
