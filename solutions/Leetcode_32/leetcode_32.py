class Solution1:
    def longest_valid_parentheses(self, s: str) -> int:
        stack = []
        prev = 0
        max_length = 0
        for x in s:
            if x == '(':
                stack.append(prev)
                prev = 0
            elif len(stack) > 0:
                prev = prev + stack.pop() + 2
                max_length = max(max_length, prev)
            else:
                prev = 0
        return max_length


class Solution2:
    def longest_valid_parentheses(self, s):
        dp = [0] * (len(s)+1)
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i-2 >= 0 else 2
                elif i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[max(i-dp[i-1]-2, 0)]
                max_len = max(max_len, dp[i])
        return max_len


if __name__ == '__main__':
    s = ")()())()()("
    ans = Solution2().longest_valid_parentheses(s)
    print(ans)
