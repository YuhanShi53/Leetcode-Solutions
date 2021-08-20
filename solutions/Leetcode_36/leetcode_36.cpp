#include <vector>

class Solution1
{
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board)
    {
        int rows[9][9] = {0}, cols[9][9] = {0}, areas[9][9] = {0};
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
            {
                if (board[i][j] != '.')
                {
                    int num = board[i][j] - '0' - 1;
                    int k = i / 3 * 3 + j / 3; 
                    if (rows[i][num] || cols[j][num] || areas[k][num]) 
                        return false;
                    rows[i][num] = cols[j][num] = areas[k][num] = 1;
                }
            }
        return true;
    }
};