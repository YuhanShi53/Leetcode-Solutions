#include <deque>
#include <queue>
#include <vector>

using namespace std;

class Solution1
{
public:
    int maxResult(vector<int> &nums, int k)
    {
        deque<pair<int, int>> q;
        q.push_back({0, nums[0]});
        int ret = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            while (!q.empty() && q.back().first < (i - k))
                q.pop_back();
            ret = q.back().second + nums[i];
            while (!q.empty() && q.front().second < ret)
                q.pop_front();
            q.push_front({i, ret});
        }
        return ret;
    }
};

class Solition2
{
public:
    int maxResult(vector<int> &nums, int k)
    {
        priority_queue<pair<int, int>> p;
        p.push({nums[0], 0});
        int ret = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            while (!p.empty() && p.top().second < (i - k))
                p.pop();
            ret = p.top().first + nums[i];
            p.push({ret, i});
        }
        return ret;
    }
};