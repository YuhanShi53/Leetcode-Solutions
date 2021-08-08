#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution1
{
public:
    int largestIsland(std::vector<std::vector<int>> &grid)
    {
        int num_rows = grid.size(), num_cols = grid[0].size(), index = 2;
        std::unordered_map<int, int> index_area;
        std::vector<std::pair<int, int>> zeros;
        index_area[0] = 0;
        index_area[1] = 0;
        for (int x = 0; x < num_rows; x++)
        {
            for (int y = 0; y < num_cols; y++)
            {
                if (grid[x][y] == 1)
                {
                    index_area[index] = dfs(grid, x, y, index);
                    index++;
                }
                else if (grid[x][y] == 0)
                {
                    zeros.push_back({x, y});
                }
            }
        }
        int largest_area = 0;
        for (const std::pair<const int, int> &x : index_area)
            largest_area = std::max(largest_area, x.second);
        for (const std::pair<int, int> &coor : zeros)
        {
            std::unordered_set<int> seen_index = {};
            int area = 1;
            for (int i = 0; i < 4; i++)
            {
                if (check(grid, coor.first + directions[i], coor.second + directions[i + 1]))
                {
                    index = grid[coor.first + directions[i]][coor.second + directions[i + 1]];
                    if (index > 1 && seen_index.find(index) == seen_index.end())
                    {
                        seen_index.insert(index);
                        area += index_area[index];
                    }
                }
            }
            largest_area = std::max(largest_area, area);
        }
        return largest_area;
    }

private:
    int directions[5] = {1, 0, -1, 0, 1};

    int dfs(std::vector<std::vector<int>> &grid, int x, int y, int index)
    {
        int area = 0;
        if (check(grid, x, y) && grid[x][y] == 1)
        {
            area++;
            grid[x][y] = index;
            for (int i = 0; i < 4; i++)
            {
                area += dfs(grid, x + directions[i], y + directions[i + 1], index);
            }
        }
        return area;
    }

    bool check(std::vector<std::vector<int>> &grid, int x, int y)
    {
        if (0 <= x && x < grid.size() && 0 <= y && y < grid[0].size())
            return true;
        return false;
    }
};
