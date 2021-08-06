#include <vector>


class Solution1
{
public:
    bool stoneGame(std::vector<int>& piles)
    {
        int num_piles = piles.size();
        std::vector<std::vector<int>> dp(num_piles, std::vector<int>(num_piles, 0));
        for (int d = 1; d < num_piles; d++)
            for (int i = 0; i < num_piles - d; i++)
                dp[i][i+d] = std::max(piles[i] - dp[i+1][i+d], piles[i+d] - dp[i][i+d-1]);
        return dp[0][num_piles-1];
    }
};
