from typing import List

class Solution1:
    def update_matrix(self, mat: List[List[int]]) -> List[List[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])
        num_ones = num_rows * num_cols
        stack = []
        ret = [[-1] * num_cols for _ in range(num_rows)]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 0:
                    stack.append((i, j))
                    ret[i][j] = 0
            
        step = 1        
        while num_ones:
            temp = []
            while stack:
                x, y = stack.pop()
                num_ones -= 1
                for dx, dy in directions:
                    if (0 <= x + dx < num_rows
                            and 0 <= y + dy < num_cols
                            and ret[x+dx][y+dy] < 0):
                        temp.append((x+dx, y+dy))
                        ret[x+dx][y+dy] = step
            stack = temp
            step += 1
        return ret
