#include <map>
#include <vector>

using namespace std;

class Solution1
{
public:
    int leastBricks(vector<vector<int>> &wall)
    {
        map<int, int> edge_dict = {{0, 0}};
        int max_count = 0;
        for (vector<int> &row : wall)
        {
            int position = 0;
            for (int i = 0; i != row.size() - 1; ++i)
            {
                position += row[i];
                edge_dict[position]++;
                max_count = max(max_count, edge_dict[position]);
            }
        }
        return wall.size() - max_count;
    }
};