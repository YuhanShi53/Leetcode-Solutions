from collections import Counter
from typing import List

class Solution1:
    def can_reorder_doubled(self, arr: List[int]) -> bool:
        num_count = Counter(arr)
        for x in sorted(num_count.keys(), key=abs):
            if num_count[x] > num_count[2*x]:
                return False
            num_count[2*x] -= num_count[x]
        return True
