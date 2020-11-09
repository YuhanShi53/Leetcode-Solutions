""" Leetcode 763 - Partition Labels

https://leetcode.com/problems/partition-labels/

1. Two-Pointer & Greedy: Time: O(n) Space: O(1) (n is len(S))

"""


from collections import defaultdict
from typing import List


class Solution1:
    """ 1. Two-Pointer & Greedy """

    def partition_labels(self, S: str) -> List[int]:
        if not S:
            return []
        last = {}
        for i, x in enumerate(S):
            last[x] = i

        left = 0
        right = 0
        lengths = []
        for i, x in enumerate(S):
            right = max(right, last[x])
            if right == i:
                lengths.append(right - left + 1)
                left = right + 1
        return lengths


if __name__ == '__main__':
    s = 'ababcbacadefegdehijhklij'
    res = Solution1().partition_labels(s)
    print(res)
