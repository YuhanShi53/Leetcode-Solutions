""" Leetcode 1657 - Determine if Two Strings are Closed

https://leetcode.com/problems/determine-if-two-strings-are-close/



"""


class Solution1:
    """ 1. MINE | Hash """

    def close_strings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word_dict1, word_dict2 = {}, {}
        for (x, y) in zip(word1, word2):
            if x not in word_dict1:
                word_dict1[x] = 0
            if y not in word_dict2:
                word_dict2[y] = 0
            word_dict1[x] += 1
            word_dict2[y] += 1
        if word_dict1.keys() != word_dict2.keys():
            return False
        if sorted(word_dict1.values()) == sorted(word_dict2.values()):
            return True
        return False


class Solution2:
    """ 2. Simiplified of 1 """

    def close_strings(self, word1, word2):
        from collections import Counter
        if len(word1) != len(word2):
            return False
        return (set(word1) == set(word2)
                and Counter(Counter(word1).values())
                == Counter(Counter(word2).values()))


if __name__ == '__main__':
    word1 = "cabbba"
    word2 = "abbccc"
    res = Solution2().close_strings(word1, word2)
    print(res)
