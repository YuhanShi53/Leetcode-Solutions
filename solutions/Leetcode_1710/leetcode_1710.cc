#include <algorithm>
#include <vector>

using namespace std;

class Solution1
{
public:
    int maximumUnits(vector<vector<int>> &boxTypes, int truckSize)
    {
        sort(boxTypes.begin(), boxTypes.end(), [](vector<int> &first, vector<int> &second) {
            return first[1] > second[1];
        });
        int units = 0;
        for (auto box_type : boxTypes)
        {
            int n = min(box_type[0], truckSize);
            truckSize -= n;
            units += n * box_type[1];
            if (truckSize == 0)
                return units;
        }
        return units;
    }
};