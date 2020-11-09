""" Leetcode 459 - Repeated Substring Pattern

https://leetcode.com/problems/repeated-substring-pattern/


1. SM

"""


class Solution1:
    """ 1. SM """

    def repeated_substring_pattern(self, s: str) -> bool:
        s_len = len(s)

        for i in range(1, s_len//2+1):
            if s_len % i == 0:
                flag = True
                for j in range(0, s_len-i, i):
                    if s[j:j+i] != s[j+i:j+i+i]:
                        flag = False
                if flag:
                    return True
        return False


if __name__ == '__main__':
    s = 'a'
    res = Solution1().repeated_substring_pattern(s)
    print(res)
