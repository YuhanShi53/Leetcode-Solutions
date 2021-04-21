from typing import List


class Solution1:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        level = triangle[0]
        for i in range(1, len(triangle)):
            temp = triangle[i]
            temp[0] += level[0]
            temp[-1] += level[-1]
            for j in range(1, i):
                temp[j] += min(level[j-1], level[j])
            level = temp
        return min(level)


class Solution2:
    def minimum_total(self, triangle):
        level = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                level[j] = triangle[i][j] + min(level[j], level[j+1])
        return level[0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    ans = Solution2().minimum_total(triangle)
    print(ans)
