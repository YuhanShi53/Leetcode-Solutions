""" Leetcode 856 - Score of Parentheses

https://leetcode.com/problems/score-of-parentheses/

1. Time: O(n) Memory: O(n)
2. Time: O(n) Memory: O(1)

"""


class Solution1:
    """ 1. Stack

    Copy from: https://leetcode.com/problems/score-of-parentheses/discuss/1080516/C%2B%2B-Easy-Stack-Solution-0-ms-faster-than-100

    """

    def score_of_parentheses(self, S: str) -> int:
        score = 0
        stack = []
        for x in S:
            if x == '(':
                stack.append(score)
                score = 0
            else:
                prev = stack.pop()
                score += prev + max(score, 1)
        return score


class Solution2:
    """ 2. Level Count

    https://leetcode.com/problems/score-of-parentheses/discuss/1080518/Python-O(1)-space-solution-explained

    """

    def score_of_parentheses(self, S):
        score = 0
        depth = 0
        for i, x in enumerate(S):
            if x == '(':
                depth += 1
            else:
                depth -= 1
                if i > 0 and S[i-1:i+1] == '()':
                    score += 1 << depth
        return score


if __name__ == '__main__':
    s = '(((()))(()))'
    res = Solution2().score_of_parentheses(s)
    print(res)
