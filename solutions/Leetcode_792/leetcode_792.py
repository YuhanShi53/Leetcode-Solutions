from collections import defaultdict
from typing import List


class Solution1:
    def num_matching_subseq(self, s, words):
        dic = defaultdict(list)
        for it in map(iter, words):
            dic[next(it)].append(it)
        for x in s:
            for it in dic.pop(x, ()):
                dic[next(it, None)].append(it)
        return len(dic[None])


class SolutionMINE:
    def num_matching_subseq(self, s: str, words: List[str]) -> int:
        num = 0
        dic = defaultdict(list)
        for i, x in enumerate(s):
            dic[ord(x)-97].append(i)
        for word in words:
            idx = [0] * 26
            temp = -1
            flag = True
            for x in word:
                id = ord(x) - 97
                while idx[id] < len(dic[id]) and temp >= dic[id][idx[id]]:
                    idx[id] += 1
                if idx[id] >= len(dic[id]):
                    flag = False
                    break
                temp = dic[id][idx[id]]
            num += flag
        return num
