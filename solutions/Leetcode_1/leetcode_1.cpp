#include <unordered_map>
#include <vector>

class Solution1
{
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target)
    {
        std::unordered_map<int, int> num_idx;
        for (int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];
            if (num_idx.find(diff) != num_idx.end())
                return {i, num_idx[diff]};
            else
                num_idx[nums[i]] = i;
        }
        return {};
    }
};