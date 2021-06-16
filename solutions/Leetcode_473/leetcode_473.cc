#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>

using namespace std;

class Solution1
{
public:
    bool makesquare(vector<int> &matchsticks)
    {
        int sum = accumulate(matchsticks.begin(), matchsticks.end(), 0);
        if (sum % 4)
            return false;
        vector<int> targets(4, sum / 4);
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
        return dfs(matchsticks, targets, 0);
    }

private:
    bool dfs(vector<int> &matchsticks, vector<int> &targets, int idx)
    {
        if (idx == matchsticks.size())
            return true;
        for (int i = 0; i < 4; ++i)
        {
            if (matchsticks[idx] <= targets[i])
            {
                targets[i] -= matchsticks[idx];
                if (dfs(matchsticks, targets, idx + 1))
                    return true;
                targets[i] += matchsticks[idx];
            }
        }
        return false;
    }
};
