#include <algorithm>
#include <vector>

using namespace std;

class Solution1
{
public:
    int maxArea(int h, int w, vector<int> &horizontalCuts, vector<int> &verticalCuts)
    {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
        int max_h = max(horizontalCuts[0], h - horizontalCuts.back());
        int max_w = max(verticalCuts[0], w - verticalCuts.back());
        for (int i = 1; i < horizontalCuts.size(); i++)
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1]);
        for (int i = 1; i < verticalCuts.size(); i++)
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1]);
        return (long)max_h * max_w % 1000000007;
    }
};