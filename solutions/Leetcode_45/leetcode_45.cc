#include <vector>

using namespace std;

class Solution1
{
public:
    int jump(vector<int> nums)
    {
        int n = nums.size(), start = 0, end = 0, thre = 0, step = 0;
        while (thre < n - 1)
        {
            step++;
            while (start <= end)
            {
                thre = max(thre, start + nums[start]);
                if (thre >= n - 1)
                    return step;
                start++;
            }
            if (thre == end)
                break;
            end = thre;
        }
        return n == 1 ? 0 : -1;
    }
};