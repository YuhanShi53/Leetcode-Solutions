#include <vector>

using namespace std;

class Solution1
{
public:
    int stoneGameVII(vector<int> &stones)
    {
        int n = stones.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        vector<int> prev_sum{0};
        for (int x : stones)
            prev_sum.push_back(prev_sum.back() + x);
        return dfs(0, n - 1, dp, prev_sum, stones);
    }

private:
    int dfs(int i, int j, vector<vector<int>> &dp, vector<int> &prev_sum, vector<int> &stones)
    {
        if (i == j)
            return 0;
        if (dp[i][j] == 0)
        {
            int summation = prev_sum[j + 1] - prev_sum[i];
            dp[i][j] = max(summation - stones[i] - dfs(i + 1, j, dp, prev_sum, stones), summation - stones[j] - dfs(i, j - 1, dp, prev_sum, stones));
        }
        return dp[i][j];
    }
};