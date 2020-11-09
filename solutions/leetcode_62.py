""" Leetcode 62 - Unique Paths

https://leetcode.com/problems/unique-paths/

1. self-implement BFS: Time Limit Exceeded
2. self-implement DP: Time: 32ms(57.17%) Memory: 13.8MB(68.02%)

"""


class Solution1:
    """ self-implement BFS """
    def unique_paths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        x, y = 1, 1
        go_down = (1, 0)
        go_right = (0, 1)
        count = 0

        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            print(x, y)
            for dx, dy in [go_down, go_right]:
                if x+dx == n and y+dy == m:
                    count += 1
                elif x+dx <= n and y+dy <= m:
                    stack.insert(0, (x+dx, y+dy))
        return count


class Solution2:
    """ self-implement DP """
    def unique_paths(self, m, n):
        mat = [[1 for i in range(m)] for j in range(n)]
        for x in range(1, n):
            for y in range(1, m):
                mat[x][y] = mat[x-1][y] + mat[x][y-1]
        return mat[n-1][m-1]


if __name__ == '__main__':
    m = 23
    n = 12
    res = Solution2().unique_paths(m, n)
    print(res)
