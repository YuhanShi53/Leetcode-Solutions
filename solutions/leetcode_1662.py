""" Leetcode 1662 - Check if Two String Arrays are Equivalent

https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

"""

from typing import List


class Solution1:
    """ 1. MINE """

    def array_string_are_equal(
            self, word1: List[str], word2: List[str]) -> bool:
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        return word1 == word2


if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "cb"]
    res = Solution1().array_string_are_equal(word1, word2)
    print(res)
