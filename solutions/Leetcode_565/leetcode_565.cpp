#include <vector>

class Solution1
{
public:
    int arrayNesting(std::vector<int> &nums)
    {
        std::vector<int> visited(nums.size(), 0);
        int maxLength;
        for (int x : nums)
        {
            int length = 0;
            while (!visited[x])
            {
                length++;
                visited[x] = 1;
                x = nums[x];
            }
            maxLength = std::max(maxLength, length);
        }
        return maxLength;
    }
};