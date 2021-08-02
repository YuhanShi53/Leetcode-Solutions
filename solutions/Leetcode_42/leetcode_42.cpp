#include <vector>

class Solution1
{
public:
    int trap(std::vector<int> &height)
    {
        int left = 0, right = height.size() - 1, leftMax = 0, rightMax = 0, water = 0;
        while (left < right)
        {
            if (height[left] <= height[right])
            {
                if (height[left] < leftMax)
                    water += leftMax - height[left];
                else
                    leftMax = height[left];
                left++;
            }
            else
            {
                if (height[right] < rightMax)
                    water += rightMax - height[right];
                else
                    rightMax = height[right];
                right--;
            }
        }
        return water;
    }
};
