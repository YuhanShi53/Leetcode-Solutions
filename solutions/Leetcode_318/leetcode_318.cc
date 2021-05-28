#include <string>
#include <unordered_map>
#include <vector>


using namespace std;

class Solution1
{
public:
    int maxProduct(vector<string> &words)
    {
        unordered_map<int, int> mask_len;
        for (string word : words)
        {
            int mask = 0;
            for (char x : word)
            {
                mask |= 1 << (x - 'a');
            }
            mask_len[mask] = max(mask_len[mask], (int) word.size());
        }
        int max_len = 0;
        for (auto x : mask_len)
            for (auto y : mask_len)
            {
                if (!(x.first & y.first))
                    max_len = max(max_len, x.second * y.second);
            }
        return max_len;
    }
};