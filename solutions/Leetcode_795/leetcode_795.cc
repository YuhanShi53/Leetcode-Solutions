#include <vector>

using namespace std;


class Solution1
{
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right)
    {
        int prev = 0, last_invalid = -1, count = 0;
        for (int i = 0; i != nums.size(); ++i)
        {
            if (nums[i] > right)
            {
                prev = 0;
                last_invalid = i;
            }
            else if (left <= nums[i])
                prev = i - last_invalid;
            count += prev;
        }
        return count;
    }
};