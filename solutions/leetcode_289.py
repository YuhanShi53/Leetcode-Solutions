# https://leetcode.com/problems/game-of-life/

class Solution():
    def game_of_life(self, board):
        self.board = board
        self.directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), 
        (0, -1), (-1, -1)]
        self.height = len(board)
        self.width = len(board[0])

        for y in range(self.height):
            for x in range(self.width):
                self.decide_life([y, x])

        for y in range(self.height):
            for x in range(self.width):
                self.board[y][x] = self.board[y][x] >> 1

    def decide_life(self, position):
        y = position[0]
        x = position[1]
        num_alive_neighbor = 0
        for direction in self.directions:
            next_y = y + direction[0]
            next_x = x + direction[1]
            if next_y >= 0 and next_y < self.height and next_x >= 0 and \
                next_x < self.width and self.board[next_y][next_x] & 1:
                num_alive_neighbor += 1
        if (self.board[y][x] and num_alive_neighbor == 2) or \
            num_alive_neighbor == 3:
            self.board[y][x] |= 2

if __name__ == "__main__":
    state = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().game_of_life(state)
    print(state)