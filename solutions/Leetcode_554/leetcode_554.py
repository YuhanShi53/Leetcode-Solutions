from typing import List


class Solution1:
    def least_bricks(self, wall: List[List[int]]) -> int:
        edge_dict = {0: 0}
        for row in wall:
            position = 0
            for x in row[:-1]:
                position += x
                edge_dict[position] = edge_dict.get(position, 0) + 1
        return len(wall) - max(edge_dict.values())


if __name__ == '__main__':
    wall = [[1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]]
    ans = Solution1().least_bricks(wall)
    print(ans)
