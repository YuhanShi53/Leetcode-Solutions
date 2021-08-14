#include <vector>

class Solution1
{
public:
    void setZeros(std::vector<std::vector<int>> &matrix)
    {
        int num_rows = matrix.size();
        int num_cols = matrix[0].size();
        int col_1 = matrix[0][0];
        for (int i = 0; i < num_rows; i++)
        {
            if (matrix[i][0] == 0)
                col_1 = 0;
            for (int j = 1; j < num_cols; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = num_rows - 1; i >= 0; i--)
        {
            for (int j = num_cols - 1; j > 0; j--)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
            matrix[i][0] = col_1 == 0 ? 0 : matrix[i][0];
        }
    }
};
