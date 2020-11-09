""" Leetcode 967 - 

https://leetcode.com/problems/numbers-with-same-consecutive-differences/


"""

from collections import deque
from typing import List


class Solution1:
    """ 1. SM """

    def num_same_consec_diff(self, N: int, K: int) -> List[int]:
        queue = deque([x for x in range(1, 10)])
        for i in range(N-1):
            temp_len = len(queue)
            while temp_len:
                num = queue.pop()
                last_dig = num % 10
                if last_dig + K < 10:
                    queue.appendleft(num*10+last_dig+K)
                if last_dig - K >= 0:
                    queue.appendleft(num*10+last_dig-K)
                temp_len -= 1
        if N == 1:
            queue.append(0)
        return list(set(queue))


if __name__ == '__main__':
    N = 3
    K = 7
    res = Solution1().num_same_consec_diff(N, K)
    print(res)
