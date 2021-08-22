#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution1
{
public:
    int rectangleArea(std::vector<std::vector<int>> &rectangles)
    {
        std::vector<int> xs;
        std::vector<std::vector<int>> ys;
        for (const std::vector<int> &rectangle : rectangles)
        {
            xs.push_back(rectangle[0]);
            xs.push_back(rectangle[2]);
            ys.push_back({rectangle[1], rectangle[0], rectangle[2], 1});
            ys.push_back({rectangle[3], rectangle[0], rectangle[2], -1});
        }
        std::sort(xs.begin(), xs.end());
        std::vector<int>::iterator uniqueEnd = std::unique(xs.begin(), xs.end());
        xs.erase(uniqueEnd, xs.end());
        std::unordered_map<int, int> xIndex;
        for (int i = 0; i < xs.size(); i++)
            xIndex[xs[i]] = i;
        std::vector<int> scanLine(xs.size(), 0);

        std::sort(ys.begin(), ys.end());
        long yy = 0, accumulateX = 0, area = 0;
        for (const std::vector<int> &rectangle : ys)
        {
            int y = rectangle[0], x1 = rectangle[1], x2 = rectangle[2], flag = rectangle[3];
            area += (y - yy) * accumulateX;
            for (int i = xIndex[x1]; i < xIndex[x2]; i++)
                scanLine[i] += flag;
            accumulateX = 0;
            for (int i = 0; i < scanLine.size() - 1; i++)
            {
                if (scanLine[i] > 0)
                    accumulateX += xs[i + 1] - xs[i];
            }
            yy = y;
        }
        return area % (int)(1e9 + 7);
    }
};