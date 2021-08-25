#include <cmath>

class Solution1
{
public:
    bool judgeSquareSum(int c)
    {
        int m = std::sqrt(c), n = 0;
        while (m >= n)
        {
            int diff = c - m * m;
            if (diff == n * n)
                return true;
            if (diff > n * n)
                n++;
            else
                m--;
        }
        return false;
    }
};
