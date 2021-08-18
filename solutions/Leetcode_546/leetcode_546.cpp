#include <algorithm>
#include <vector>

class Solution1
{
private:
    std::vector<std::vector<std::vector<int>>> dp;

    int helper(std::vector<int> &boxes, int left, int right, int numSameLeft)
    {
        if (left > right)
            return 0;
        if (dp[left][right][numSameLeft] > 0)
            return dp[left][right][numSameLeft];
        int leftCopy = left, numSameLeftCopy = numSameLeft;
        while (left + 1 <= right && boxes[left] == boxes[left + 1])
        {
            left++;
            numSameLeft++;
        }
        int ret = (numSameLeft + 1) * (numSameLeft + 1) + helper(boxes, left + 1, right, 0);
        for (int i = left + 1; i <= right; i++)
            if (boxes[left] == boxes[i])
                ret = std::max(ret, helper(boxes, i, right, numSameLeft + 1) + helper(boxes, left + 1, i - 1, 0));
        dp[leftCopy][right][numSameLeftCopy] = ret;
        return ret;
    }

public:
    int removeBoxes(std::vector<int> &boxes)
    {
        int n = boxes.size();
        dp = std::vector<std::vector<std::vector<int>>>(n, std::vector<std::vector<int>>(n, std::vector<int>(n, 0)));
        return helper(boxes, 0, n - 1, 0);
    }
};