from collections import defaultdict
from typing import List

class Solution1:
    def group_anagrams(self, strs):
        anagrams_dict = defaultdict(list)
        for word in strs:
            anagrams_dict[''.join(sorted(word))].append(word)
        return list(anagrams_dict.values())

class SolutionMINE:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(word):
            key = [0] * 26
            for x in word:
                key[ord(x) - 97] += 1
            return '.'.join(map(str, key))
        
        anagrams_dict = defaultdict(list)
        for word in strs:
            anagrams_dict[hash(word)].append(word)
        return list(anagrams_dict.values())
