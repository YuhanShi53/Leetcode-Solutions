from queue import Queue
from typing import List


class SolutionMINE:
    def longest_ones(self, nums: List[int], k: int) -> int:
        q = Queue()
        longest_len = start = 0
        for i, x in enumerate(nums):
            if x == 0:
                if k > 0:
                    k -= 1
                    q.put(i)
                elif not q.empty():
                    start = q.get() + 1
                    q.put(i)
                else:
                    start = i + 1
            longest_len = max(longest_len, i - start + 1)
        return longest_len
