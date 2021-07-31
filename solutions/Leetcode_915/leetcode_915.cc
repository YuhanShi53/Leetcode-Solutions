#include <vector>

class Solution1
{
public:
    int partitionDisjoint(std::vector<int>& nums) {
        int left_max = nums[0], global_max = nums[0], partition = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (left_max > nums[i]) {
                partition = i;
                left_max = global_max;
            }
            global_max = std::max(global_max, nums[i]);
        }
        return partition + 1;
    }
};