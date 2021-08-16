#include <vector>

class NumArray
{
public:
    NumArray(std::vector<int> &nums)
    {
        for (int x : nums)
            _range_sums.push_back(_range_sums.back() + x);
    }

    int sumRange(int left, int right)
    {
        return _range_sums[right + 1] - _range_sums[left];
    }

private:
    std::vector<int> _range_sums = {0};
};
