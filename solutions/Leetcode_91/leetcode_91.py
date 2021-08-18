class Solution1:
    def num_decodings(self, s: str) -> int:
        valid_nums = {str(x): 1 for x in range(1, 27)}
        pprev = 1
        prev = 1 if s[0] in valid_nums else 0
        for i in range(1, len(s)):
            current = valid_nums.get(s[i], 0) * prev + valid_nums.get(s[i-1:i+1], 0) * pprev
            pprev, prev = prev, current
        return prev


class Solution2:
    def num_decodings(self, s):
        pprev = 1
        prev = 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            current = prev * (s[i] != '0') + pprev * (s[i-1] == '1' or s[i-1] == '2' and s[i] < '7')
            pprev, prev = prev, current
        return prev
