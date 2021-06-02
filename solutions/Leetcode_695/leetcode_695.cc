#include <stack>
#include <vector>

using namespace std;

class Solution1
{
public:
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int max_area = 0, current = 0, m = grid.size(), n = grid[0].size(), offset[] = {1, 0, -1, 0, 1}, x, y;
        stack<pair<int, int>> s;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j])
                {
                    current = 0;
                    s.push({i, j});
                    grid[i][j] = 0;
                    while (!s.empty())
                    {
                        x = s.top().first;
                        y = s.top().second;
                        s.pop();
                        current++;
                        for (int k = 0; k < 4; k++)
                        {
                            int xx = x + offset[k], yy = y + offset[k + 1];
                            if (xx >= 0 && xx < m && yy >= 0 && yy < n && grid[xx][yy])
                            {    
                                grid[xx][yy] = 0;
                                s.push({xx, yy});
                            }
                        }
                    }
                }
                max_area = max(max_area, current);
            }
        }
        return max_area;
    }
};


class Solution2
{
public:
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int max_area = 0;
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j])
                {
                    max_area = max(max_area, dfs(grid, i, j));
                }
            }
        }
        return max_area;
    }

private:
    int dfs(vector<vector<int>> &grid, int x, int y)
    {
        if (0 <= x && x < grid.size() && 0 <= y && y < grid[0].size() && grid[x][y])
        {
            grid[x][y] = 0;
            return 1 + dfs(grid, x+1, y) + dfs(grid, x, y+1) + dfs(grid, x-1, y) + dfs(grid, x, y-1);
        }
        return 0;
    }
};