#include <queue>
#include <vector>

using namespace std;

class Solution1
{
public:
    int furthestBuilding(vector<int> heights, int bricks, int ladders)
    {
        priority_queue<int> heap;
        for (int i = 0; i < heights.size() - 1; i++)
        {
            if (heights[i + 1] - heights[i] > 0)
                heap.push(heights[i] - heights[i + 1]);
            if (heap.size() > ladders)
            {
                bricks += heap.top();
                heap.pop();
            }
            if (bricks < 0)
                return i;
        }
        return heights.size() - 1;
    }
};
