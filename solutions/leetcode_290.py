""" Leetcode 290 - Word Pattern

https://leetcode.com/problems/word-pattern/

1. MINE Dict: Time: O(n) Space: O(2n) (n is len_str)

"""


class Solution1:
    """ 1. MINE Dict """

    def word_pattern(self, pattern: str, str: str) -> bool:
        exist_p = {}
        exist_s = {}
        str = str.split(' ')
        if len(pattern) != len(str):
            return False

        for i in range(len(pattern)):
            if (not exist_p.get(pattern[i], False)
                    and not exist_s.get(str[i], False)):
                exist_p[pattern[i]] = str[i]
                exist_s[str[i]] = pattern[i]
            elif (exist_p.get(pattern[i], str[i]) != str[i]
                    or exist_s.get(str[i], pattern[i]) != pattern[i]):
                return False
        return True


if __name__ == '__main__':
    pattern = 'aaaa'
    str = "dog dog dog dog"
    res = Solution1().word_pattern(pattern, str)
    print(res)
