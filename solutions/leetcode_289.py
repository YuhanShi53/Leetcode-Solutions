""" Leetcode 289 - Game of Life

https://leetcode.com/problems/game-of-life/

"""

from typing import List


class Solution1:
    """ 1. MINE """

    def game_of_life(self, board: List[List[int]]) -> None:
        height, width = len(board), len(board[0])
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, 1),
                      (1, 1), (1, 0), (1, -1), (0, -1))
        for i in range(height):
            for j in range(width):
                neighbour = 0
                for direction in directions:
                    ii, jj = i + direction[0], j + direction[1]
                    if (0 <= ii < height
                            and 0 <= jj < width):
                        neighbour += board[ii][jj] % 2
                if neighbour < 2 or neighbour > 3:
                    board[i][j] = 0 if board[i][j] == 0 else 3
                elif board[i][j] == 0 and neighbour == 2:
                    board[i][j] = 0 if board[i][j] == 0 else 3
                else:
                    board[i][j] = 1 if board[i][j] == 1 else 2
        for i in range(height):
            for j in range(width):
                board[i][j] = 0 if board[i][j] % 3 == 0 else 1


class Solution2:
    """ 2. Bit-Manipulation """

    def game_of_life(self, board):
        height, width = len(board), len(board[0])
        for i in range(height):
            for j in range(width):
                count = 0
                for ii in range(max(0, i-1), min(i+2, height)):
                    for jj in range(max(0, j-1), min(j+2, width)):
                        count += board[ii][jj] & 1
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2
        for i in range(height):
            for j in range(width):
                board[i][j] >>= 1


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution2().game_of_life(board)
    print(board)
