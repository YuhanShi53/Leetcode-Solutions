#include <unordered_map>
#include <vector>

using namespace std;

class Solution1
{
public:
    int longestConsecutive(vector<int> nums)
    {
        unordered_map<int, int> dic;
        int max_len = 0;
        for (int x : nums)
        {
            if (dic.find(x) == dic.end())
            {
                int right = dic.find(x + 1) == dic.end() ? 0 : dic[x + 1];
                int left = dic.find(x - 1) == dic.end() ? 0 : dic[x - 1];
                int length = right + left + 1;
                dic[x] = length;
                dic[x + right] = length;
                dic[x - left] = length;
                max_len = max(max_len, length);
            }
        }
        return max_len;
    }
};