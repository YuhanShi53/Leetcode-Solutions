""" Leetcode 20 - Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

1. Time: O(n) Memory: O(n) (n is length of s)

"""


class Solution1:
    """ 1. MINE | Stack """

    def is_valid(self, s: str) -> bool:
        match_dict = {'}': '{', ')': '(', ']': '['}
        stack = []
        for x in s:
            if x not in match_dict:
                stack.append(x)
            elif not stack or stack.pop() != match_dict[x]:
                return False
        return not stack


if __name__ == '__main__':
    s = ']'
    res = Solution1().is_valid(s)
    print(res)
