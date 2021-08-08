#include <string>
#include <vector>

class Solution1
{
public:
    int minCut(std::string s)
    {
        std::vector<int> dp;
        for (int x = 0; x <= s.size(); x++)
            dp.push_back(x-1);
        for (int i = 0; i < s.size(); i++)
        {
            // Odd Palindrome
            for (int d = 0; (i+d) < s.size() && (i-d) >= 0 && s[i-d] == s[i+d]; d++)
                dp[i+d+1] = std::min(dp[i+d+1], 1 + dp[i-d]);
            // Even Palindrome
            for (int d = 0; (i+d+1) < s.size() && (i-d) >= 0 && s[i-d] == s[i+d+1]; d++)
                dp[i+d+2] = std::min(dp[i+d+2], 1 + dp[i-d]);
        }
        return dp[s.size()];
    }
};