import heapq
from typing import List


class Solution1:
    def is_possible(self, target):
        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)
        while True:
            max_value = -heapq.heappop(target)
            total -= max_value
            if max_value == 1 or total == 1:
                return True
            if max_value <= total or total == 0 or max_value % total == 0:
                return False
            max_value %= total
            total += max_value
            heapq.heappush(target, -max_value)


class SolutionMINE:
    # Time Limit Exceed
    def is_possible(self, target: List[int]) -> bool:
        target = [-x for x in target]
        heapq.heapify(target)
        while target[0] != -1:
            max_value = heapq.heappop(target)
            max_value -= sum(target)
            if max_value >= 0:
                return False
            heapq.heappush(target, max_value)
        return True


if __name__ == '__main__':
    target = [8, 5]
    ans = SolutionMINE().is_possible(target)
    print(ans)
