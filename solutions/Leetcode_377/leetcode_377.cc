#include <vector>
#include <unordered_map>

using namespace std;

class Solution1
{
public:
    int combinationSum4(vector<int> &nums, int target)
    {
        vector<unsigned int> combination_count(target + 1);
        combination_count[0] = 1;
        for (int i = 0; i <= target; ++i)
            for (int x : nums)
                if (x <= i)
                    combination_count[i] += combination_count[i - x];
        return combination_count[target];
    }
};

class Solution2
{
private:
    unordered_map<int, int> map;

public:
    int combinationSum4(vector<int> &nums, int target)
    {
        map[0] = 1;
        return helper(nums, target);
    }

    int helper(vector<int> &nums, int target)
    {
        if (map.count(target))
            return map[target];
        long total = 0;
        for (int x : nums)
            if (target - x >= 0)
                total += helper(nums, target - x);
        map[target] = total;
        return total;
    }
};