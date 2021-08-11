#include <string>

class Solution1
{
public:
    int minFlipsMonoIncr(std::string s)
    {
        int minFlip = 0, numOnes = 0;
        for (const char &x : s)
        {
            if (x == '0')
                minFlip = std::min(minFlip + 1, numOnes);
            else
                numOnes++;
        }
        return minFlip;
    }
};