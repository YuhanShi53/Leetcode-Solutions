#include <unordered_map>
#include <vector>

class Solution1
{
public:
    std::vector<int> intersect(std::vector<int> &nums1, std::vector<int> &nums2)
    {
        std::unordered_map<int, int> numDict;
        std::vector<int> intersection;
        for (int x : nums1)
            numDict[x]++;
        for (int x : nums2)
        {
            if (numDict.find(x) != numDict.end() && numDict[x] > 0)
            {
                intersection.push_back(x);
                numDict[x]--;
            }
        }
        return intersection;
    }
};
