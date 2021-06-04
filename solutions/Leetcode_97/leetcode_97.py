class Solution1:
    def is_interleave(self, s1: str, s2: str, s3: str):
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s1_len + s2_len != s3_len:
            return False
        invalid = [[False] * (s2_len+1) for _ in range(s1_len+1)]
        def compare(i, j, k):
            if invalid[i][j]:
                return False
            if k == s3_len:
                return True
            is_valid = (i < s1_len and s1[i] == s3[k] and compare(i+1, j, k+1)
                        or j < s2_len and s2[j] == s3[k] and compare(i, j+1, k+1))
            if not is_valid:
                invalid[i][j] = True
            return is_valid
        return compare(0, 0, 0)


class Solution2:
    def is_interleave(self, s1, s2, s3):
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s1_len + s2_len != s3_len:
            return False
        dp = [True] * (s2_len+1)
        for j in range(1, s2_len+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, s1_len + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, s2_len + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]
                

