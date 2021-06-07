from collections import deque
from typing import List


class Solution1:
    def open_lock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        visited = set(deadends)
        minimum_turns = -1
        queue = deque(['0000'])
        while queue:
            minimum_turns += 1
            for _ in range(len(queue)):
                num = queue.popleft()
                if num == target:
                    return minimum_turns
                if num in visited:
                    continue
                visited.add(num)
                for i in range(4):
                    up = num[:i] + str((int(num[i]) + 1) % 10) + num[i+1:]
                    down = num[:i] + str((int(num[i]) - 1) % 10) + num[i+1:]
                    queue.append(up)
                    queue.append(down)
        return -1