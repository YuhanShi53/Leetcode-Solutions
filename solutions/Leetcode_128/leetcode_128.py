from typing import List


class Solution1:
    def longest_consecutive(self, nums: List[int]) -> int:
        dic = {}
        max_len = 0
        for x in nums:
            if not dic.get(x, False):
                right = dic.get(x+1, 0)
                left = dic.get(x-1, 0)
                length = right + left + 1
                dic[x] = length
                dic[x-left] = length
                dic[x+right] = length
                max_len = max(max_len, length)
        return max_len
