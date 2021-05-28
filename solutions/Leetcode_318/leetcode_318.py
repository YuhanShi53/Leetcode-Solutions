from typing import List

class Solution1:
    def max_product(self, words: List[str]) -> int:
        mask_len = {}
        for word in words:
            mask = 0
            for x in word:
                mask |= 1 << (ord(x) - 97)
            mask_len[mask] = max(mask_len.get(mask, 0), len(word))
        max_len = 0
        for i in mask_len.keys():
            for j in mask_len.keys():
                if not i & j:
                    max_len = max(max_len, mask_len[i] * mask_len[j])
        return max_len