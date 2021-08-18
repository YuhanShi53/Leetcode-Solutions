#include <string>
#include <unordered_map>

class Solution1
{
public:
    int numDecodings(std::string s)
    {
        std::unordered_map<std::string, int> validNums;
        for (int x = 1; x <= 26; x++)
            validNums[std::to_string(x)] = 1;
        int pprev = 1;
        int prev = validNums[s.substr(0, 1)] ? 1 : 0;
        for (int i = 1; i < s.size(); i++)
        {
            int current = validNums[s.substr(i, 1)] * prev + validNums[s.substr(i - 1, 2)] * pprev;
            pprev = prev;
            prev = current;
        }
        return prev;
    }
};

class Solution2
{
public:
    int numDecodings(std::string s)
    {
        int pprev = 1;
        int prev = s[0] == '0' ? 0 : 1;
        for (int i = 1; i < s.size(); i++)
        {
            int current = (s[i] != '0' ? prev : 0) + ((s[i - 1] == '1' || s[i - 1] == '2' && s[i] < '7') ? pprev : 0);
            pprev = prev;
            prev = current;
        }
        return prev;
    }
};
