""" Leetcode 621 - Task Scheduler

https://leetcode.com/problems/task-scheduler/

1. Greedy: Time: O(n) Space: O(1)

"""

from collections import defaultdict
from typing import List


class Solution1:
    """ 1. Greedy """

    def least_interval(self, tasks: List[int], n: int) -> int:
        task_frequency = defaultdict(int)
        for task in tasks:
            task_frequency[task] += 1

        max_frequency = 0
        for frequency in task_frequency.values():
            if max_frequency < frequency:
                max_frequency = frequency
                num_of_max_frequency = 1
            elif max_frequency == frequency:
                num_of_max_frequency += 1
        return max((n+1)*(max_frequency-1)+num_of_max_frequency, len(tasks))


if __name__ == "__main__":
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    res = Solution1().least_interval(tasks, n)
    print(res)
