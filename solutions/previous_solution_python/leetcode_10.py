""" Leetcode 10 - Regular Expression Matching

https://leetcode.com/problems/regular-expression-matching/


1. BackTracking: Time: 1476ms(13%) Memory: 14MB(35%)
2. DP: Time: 60ms(57%) 14MB(37%)

"""


class Solution1:
    """ 1. Backtracking """
    def is_match(self, s, p):
        if not s and not p:
            return True
        if s and not p:
            return False

        if len(p) > 1 and p[1] is '*':
            return self.is_match(s, p[2:]) or s and (
                p[0] == s[0] or p[0] == '.') and self.is_match(s[1:], p)
        else:
            return s and (p[0] == s[0] or p[0] == '.') and self.is_match(
                s[1:], p[1:])


class Solution2:
    """ 2. DP """
    def is_match(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        elif not p:
            return False

        s_len = len(s)
        p_len = len(p)
        status_mat = [[False for i in range(p_len + 1)]
                      for j in range(s_len + 1)]
        status_mat[0][0] = True
        for j in range(2, p_len + 1):
            if p[j - 1] == '*' and status_mat[0][j - 2]:
                status_mat[0][j] = True

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] == '*':
                    status_mat[i][j] = status_mat[i][j - 2] or (
                        s[i - 1] == p[j - 2]
                        or p[j - 2] == '.') and (status_mat[i - 1][j])
                else:
                    status_mat[i][j] = (s[i - 1] == p[j - 1] or p[j - 1]
                                        == '.') and status_mat[i - 1][j - 1]
        return status_mat[s_len][p_len]


if __name__ == '__main__':
    s = 'aa'
    p = 'a'
    is_match = Solution1().is_match(s, p)
    print(is_match)
