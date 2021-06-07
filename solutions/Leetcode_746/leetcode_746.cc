#include <vector>

using namespace std;

class Solution1
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        int prev1 = 0, prev2 = 0;
        for (int i = 0; i < cost.size(); i++)
        {
            int tmp = prev2;
            prev2 = cost[i] + min(prev1, prev2);
            prev1 = tmp;
        }
        return min(prev1, prev2);
    }
};