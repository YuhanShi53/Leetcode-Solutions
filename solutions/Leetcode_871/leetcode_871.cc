#include <queue>
#include <vector>

using namespace std;

class Solution1
{
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations)
    {
        priority_queue<int> q;
        q.push(startFuel);
        int idx = 0, distance = 0;
        int count = -1;
        while (distance < target && !q.empty())
        {
            distance += q.top();
            q.pop();
            count++;
            while (idx < stations.size() && distance >= stations[idx][0])
                q.push(stations[idx++][1]);
        }
        return distance >= target ? count : -1;
    }
};

class Solution2
{
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations)
    {
        vector<long> dp(stations.size() + 1, 0);
        dp[0] = startFuel;
        for (int i = 0; i < stations.size(); i++)
            for (int t = i; t > -1 && dp[t] >= stations[i][0]; t--)
                dp[t + 1] = max(dp[t + 1], dp[t] + stations[i][1]);
        for (int i = 0; i < dp.size(); i++)
            if (dp[i] >= target)
                return i;
        return -1;
    }
};