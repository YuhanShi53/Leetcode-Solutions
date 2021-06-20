#include <queue>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution1
{
public:
    int swimInWater(vector<vector<int>> &grid)
    {
        unordered_map<int, queue<pair<int, int>>> time;
        time[grid[0][0]].push({0, 0});
        unordered_set<pair<int, int>> visited{{0, 0}};
        int n = grid.size();
        int directions[5]{1, 0, -1, 0, 1};
        for (int t = 0; t < n; ++t)
        {
            while (time.find(t) != time.end() && !time[t].empty())
            {
                int x = time[t].front().first, y = time[t].front().second;
                time[t].pop();
                if (x == n - 1 && y == n - 1)
                    return t;
                for (int i; i < 4; ++i)
                {
                    int xx = x + directions[i], yy = y + directions[i + 1];
                    if (0 <= xx && xx < n && 0 <= yy && yy < n && visited.find(pair<int, int>{xx, yy}) == visited.end())
                    {
                        visited.insert({xx, yy});
                        time[max(grid[xx][yy], t)].push({xx, yy});
                    }
                }
            }
        }
    }
};