#include <algorithm>
#include <vector>

using namespace std;

class Solution1
{
public:
    int minMoves2(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        int median = nums[nums.size() / 2];
        int sum = 0;
        for (int num : nums)
            sum += abs(num - median);
        return sum;
    }
};


class Solution2
{
public:
    int minMoves2(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        int sum = 0, n = nums.size();
        for (int i = 0; i < n / 2; i++)
            sum += nums[n-1-i] - nums[i];
        return sum;
    }
};