#include <algorithm>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution1
{
public:
    bool canReorderDoubled(std::vector<int> &arr)
    {
        std::unordered_map<int, int> numCount;
        for (const int x : arr)
            numCount[x]++;
        std::vector<int> keys;
        for (std::pair<const int, int> item : numCount)
            keys.push_back(item.first);
        std::sort(keys.begin(), keys.end(), [](int x, int y){ return abs(x) < abs(y); });
        for (const int x : keys)
        {
            if (numCount[x] > numCount[x * 2])
                return false;
            numCount[x * 2] -= numCount[x];
        }
        return true;
    }
};