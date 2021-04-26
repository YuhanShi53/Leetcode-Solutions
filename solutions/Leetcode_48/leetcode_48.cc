#include <algorithm>
#include <vector>

using namespace std;

class Solution1
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        int n = matrix.size();
        for (int i = 0; i < n / 2; ++i)
            for (int j = 0; j < n - n / 2; ++j)
            {
                swap(matrix[i][j], matrix[n - j - 1][i]);
                swap(matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1]);
                swap(matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1]);
            }
    }
};

class Solution2
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        reverse(matrix.begin(), matrix.end());
        for (int i = 0; i != matrix.size(); ++i)
            for (int j = i + 1; j != matrix.size(); ++j)
                swap(matrix[i][j], matrix[j][i]);
    }
};