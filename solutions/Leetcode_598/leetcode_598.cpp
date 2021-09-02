#include <vector>

class Solution1
{
public:
    int maxCount(int m, int n, std::vector<std::vector<int>> &ops)
    {
        if (ops.size() > 0)
        {
            for (const std::vector<int> &op : ops)
            {
                m = std::min(m, op[0]);
                n = std::min(n, op[1]);
            }
        }
        return m * n;
    }
};
