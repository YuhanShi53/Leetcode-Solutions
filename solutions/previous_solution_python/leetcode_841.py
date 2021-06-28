""" Leetcode 841 - Keys and Rooms

https://leetcode.com/problems/keys-and-rooms/

1. Time: O(n) Memory: O(n) (n is number of rooms)
2. Time: O(n) Memory: O(n) (n is number of rooms)

"""

from typing import List


class Solution1:
    """ 1. MINE | BFS """

    def can_visit_all_rooms(self, rooms: List[List[int]]) -> bool:
        visited = [True] + [False] * (len(rooms) - 1)
        queue = rooms[0]
        while queue:
            key = queue.pop()
            if not visited[key]:
                visited[key] = True
                for x in rooms[key]:
                    if not visited[x]:
                        queue.insert(0, x)
        return all(visited)


class Solution2:
    """ 2. MINE | DFS """

    def can_visit_all_rooms(self, rooms) -> bool:
        visited = [True] + [False] * (len(rooms) - 1)
        queue = rooms[0]
        while queue:
            key = queue.pop()
            if not visited[key]:
                visited[key] = True
                for x in rooms[key]:
                    if not visited[x]:
                        queue.append(x)
        return all(visited)


if __name__ == '__main__':
    rooms = [[1, 2, 3], [2], [3], [1]]
    res = Solution1().can_visit_all_rooms(rooms)
    print(res)
