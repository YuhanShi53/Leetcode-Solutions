""" Leetcode 139 - Word Break

https://leetcode.com/problems/word-break/


1. DP: Time: O(n^2) Space: O(n) (n is len_s)
2. Simplified-DP: Time: O(n^2) Space: O(n) (n is len_s)

"""


from typing import List


class Solution1:
    """ 1. DP """

    def word_break(self, s: str, wordDict: List[str]) -> bool:
        is_contain = [False for i in range(len(s)+1)]
        is_contain[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if is_contain[j] and s[j:i] in wordDict:
                    is_contain[i] = True
                    break
        return is_contain[-1]


class Solution2:
    """ 2. Simplified-DP """

    def word_break(self, s, wd):
        contain = [True]
        for i in range(1, len(s) + 1):
            contain += any(contain[j] and s[j:i] in wd for j in range(i)),
        return contain[-1]


if __name__ == '__main__':
    s = 'cat'
    word_dict = ["cats", "dog", "sand", "and", "catss"]
    res = Solution2().word_break(s, word_dict)
    print(res)
