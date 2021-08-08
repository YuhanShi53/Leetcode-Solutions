class Solution1:
    def min_cut(self, s):
        dp = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            # Odd palindrome
            d = 0
            while d < min(i+1, (len(s)-i)) and s[i-d] == s[i+d]:
                dp[i+d+1] = min(dp[i+d+1], 1 + dp[i-d])
                d += 1
            # Even palindrome
            d = 0
            while d < min(i+1, (len(s)-i-1)) and s[i-d] == s[i+d+1]:
                dp[i+d+2] = min(dp[i+d+2], 1 + dp[i-d])
                d += 1
        return dp[-1]


class SolutionMINE:
    def min_cut(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = -1
        for i in range(len(s)):
            i_dp = i + 1
            dp[i_dp] = dp[i_dp-1] + 1
            for d in range(i+1):
                if s[d:i+1] == s[d:i+1][::-1]:
                    dp[i_dp] = min(dp[i_dp], dp[d] + 1)
        return dp[-1]
