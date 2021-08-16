#include <string>
#include <vector>

class Solution1
{
public:
    std::string minWindow(std::string s, std::string t)
    {
        std::vector<int> charCount(58, 0);
        for (const char x : t)
            charCount[x - 65]++;
        int left = 0, right = 0, head = 0, min_len = INT_MAX, missing = t.size();
        while (right < s.size())
        {
            if (charCount[s[right] - 65] > 0)
                missing--;
            charCount[s[right] - 65]--;
            right++;
            while (missing == 0)
            {
                if (right - left < min_len)
                {
                    head = left;
                    min_len = right - left;
                }
                if (charCount[s[left] - 65] == 0)
                    missing++;
                charCount[s[left] - 65]++;
                left++;
            }
        }
        return min_len == INT_MAX ? "" : s.substr(head, min_len);
    }
};