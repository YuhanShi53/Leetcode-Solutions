#include <vector>

using namespace std;

class Solution1
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        vector<int> ans{-1, -1};
        int starting = search(nums, target);
        if (!nums.empty() && starting < nums.size() && nums[starting] == target)
        {
            ans[0] = starting;
            ans[1] = search(nums, target + 1) - 1;
        }
        return ans;
    }

private:
    int search(vector<int> &nums, int target)
    {
        int left = 0, right = nums.size();
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};

class Solution2
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        if (nums.empty())
            return {-1, -1};
        return divide_and_search(nums, target, 0, nums.size() - 1);
    }

private:
    vector<int> divide_and_search(vector<int> &nums, int target, int left, int right)
    {
        if (nums[left] == target && target == nums[right])
            return {left, right};
        if (nums[left] <= target && target <= nums[right])
        {
            int mid = left + (right - left) / 2;
            vector<int> l = divide_and_search(nums, target, left, mid);
            vector<int> r = divide_and_search(nums, target, mid + 1, right);
            if (l[0] == -1)
                return r;
            if (r[0] == -1)
                return l;
            return {l[0], r[1]};
        }
        return {-1, -1};
    }
};