#include <vector>

using namespace std;

class Solution1
{
public:
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
    {
        int row = obstacleGrid.size(), col = obstacleGrid[0].size();
        vector<int> dp(col, 0);
        dp[0] = 1 - obstacleGrid[0][0];
        for (int i = 1; i != col; ++i)
            dp[i] = dp[i - 1] * (1 - obstacleGrid[0][i]);
        for (int i = 1; i != row; ++i)
        {
            dp[0] *= (1 - obstacleGrid[i][0]);
            for (int j = 1; j != col; ++j)
                dp[j] = (dp[j] + dp[j - 1]) * (1 - obstacleGrid[i][j]);
        }
        return dp[col - 1];
    }
};
