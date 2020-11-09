""" Leetcode 140 - Word Break II

https://leetcode.com/problems/word-break-ii/


"""

from typing import List


class Solution1:
    """ 1. Recursive """

    def word_break(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict = {}
        max_word_len = 0
        for word in wordDict:
            word_dict[word] = 1
            max_word_len = max(max_word_len, len(word))

        idx = 0
        s_len = len(s)
        sentences = []

        def helper(idx, word, sentence):
            if idx == s_len and not word:
                sentences.append(" ".join(sentence))
                return
            elif idx == s_len:
                return

            word += s[idx]
            idx += 1
            if word_dict.get(word, 0):
                helper(idx, "", sentence + [word])
            if len(word) >= max_word_len:
                return
            helper(idx, word, sentence)

        helper(idx, "", [])
        return sentences


# class Solution2:
#     """ 2. Recursive """

#     def word_break(self, s, wordDict):

#         def bfs(s):


if __name__ == "__main__":
    s = (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaaaaaaaa"
    )
    word_dict = [
        "a",
        "aa",
        "aaa",
        "aaaa",
        "aaaaa",
        "aaaaaa",
        "aaaaaaa",
        "aaaaaaaa",
        "aaaaaaaaa",
        "aaaaaaaaaa",
    ]
    res = Solution1().word_break(s, word_dict)
    print(res)
