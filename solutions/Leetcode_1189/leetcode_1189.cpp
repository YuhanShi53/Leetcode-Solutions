#include <algorithm>
#include <string>

class Solution1
{
public:
    int maxNumberOfBallons(std::string text)
    {
        int textCount[26] = {};
        for (const char &x : text)
            textCount[x-'a'] += 1;
        return std::min({textCount[1], textCount[0], textCount[11]/2, textCount[14]/2, textCount[13]});
    }
};
