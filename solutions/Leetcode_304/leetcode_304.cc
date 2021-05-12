#include <vector>

using namespace std;

class NumMatrix
{
public:
    NumMatrix(vector<vector<int>> &matrix)
    {
        int num_row = matrix.size();
        int num_col = matrix[0].size();
        sums = vector<vector<int>>(num_row + 1, vector<int>(num_col + 1, 0));
        for (int row = 1; row <= num_row; row++)
            for (int col = 1; col <= num_col; col++)
                sums[row][col] = matrix[row - 1][col - 1] + sums[row][col - 1] + sums[row - 1][col] - sums[row - 1][col - 1];
    }

    int sumRegion(int row1, int col1, int row2, int col2)
    {
        return sums[row2 + 1][col2 + 1] - sums[row2 + 1][col1] - sums[row1][col2 + 1] + sums[row1][col1];
    }

private:
    vector<vector<int>> sums;
};
