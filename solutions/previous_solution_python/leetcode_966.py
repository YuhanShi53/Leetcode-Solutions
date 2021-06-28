""" Leetcode 966 - Vowel Spellchecker

https://leetcode.com/problems/vowel-spellchecker/

1. Time: O(max(m, n)) Memory: O(n) (m is length of queries, n is length of wordlist)

"""

from typing import List


class Solution1:
    """ 1. MINE | Hashmap """

    def __init__(self):
        self._vowel = ('a', 'e', 'i', 'o', 'u')

    def spell_checker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def convert(word):
            pattern = ''.join(['_' if x in self._vowel else x for x in word])
            return pattern

        word_dict = {}
        lower_word_dict = {}
        pattern_dict = {}
        for x in wordlist:
            word_dict[x] = True
            lower_word_dict[x.lower()] = lower_word_dict.get(x.lower(), x)
            pattern_dict[convert(x.lower())] = pattern_dict.get(
                convert(x.lower()), x)

        ans = []
        for query in queries:
            if word_dict.get(query, False):
                ans.append(query)
            elif lower_word_dict.get(query.lower(), False):
                ans.append(lower_word_dict[query.lower()])
            elif pattern_dict.get(convert(query.lower()), False):
                ans.append(pattern_dict[convert(query.lower())])
            else:
                ans.append('')
        return ans


if __name__ == '__main__':
    word_list = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "HARE",
               "Hear", "hear", "keti", "keet", "keto"]
    ans = Solution1().spell_checker(word_list, queries)
    print(ans)
