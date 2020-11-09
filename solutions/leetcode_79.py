""" Leetcode 79 - Word Search

https://leetcode.com/problems/word-search/

1. self-implement DFS: Time: 384ms(59%) Memory: 15MB(59%)

"""

from collections import defaultdict
from typing import List


class Solution1:
    """ self-implement DFS """
    def exist(self, board: List[List[str]], word: str) -> bool:
        initial = word[0]
        initial_locs = [(i, j) for i in range(len(board))
                        for j in range(len(board[0]))
                        if board[i][j] == initial]
        visited = defaultdict(int)
        self.row_num = len(board)
        self.col_num = len(board[0])
        self.board = board
        flag = False

        for row, col in initial_locs:
            visited[(row, col)] = 1
            flag = self.dfs(row, col, visited, word[1:])
            visited[(row, col)] = 0
            if flag:
                return flag
        return flag

    def dfs(self, row, col, visited, word):
        if not word:
            return True

        flag = False
        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_row = row + i
            new_col = col + j
            if (0 <= new_row < self.row_num 
                    and 0 <= new_col < self.col_num
                    and visited[(new_row, new_col)] != 1
                    and self.board[new_row][new_col] == word[0]):
                visited[(new_row, new_col)] = 1
                flag = self.dfs(new_row, new_col, visited, word[1:])
                visited[(new_row, new_col)] = 0
                if flag:
                    return flag

        return flag


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    words = 'CCC'
    res = Solution1().exist(board, words)
    print(res)