#include <algorithm>
#include <vector>


class Solution1
{
public:
    std::vector<std::vector<int>> subsetsWithDup(std::vector<int>& nums)
    {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> subsets{{}};
        int prev_len = 1;
        for (int i = 0; i < nums.size(); i++)
        {
            if (i == 0 || nums[i] != nums[i-1])
                prev_len = subsets.size();
            int current_len = subsets.size();
            for (int j = current_len - prev_len; j < current_len; j++)
            {
                std::vector<int> subset = subsets[j];
                subset.push_back(nums[i]);
                subsets.push_back(subset);
            }
        }
        return subsets;
    }
};
