from collections import defaultdict
from typing import List


class Solution1:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        areas = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                x = board[i][j]
                if x != '.':
                    hashed_pos = i // 3 * 3 + j // 3
                    if x in rows[i] or x in cols[j] or x in areas[hashed_pos]:
                        return False
                    rows[i].append(x)
                    cols[j].append(x)
                    areas[hashed_pos].append(x)
        return True
