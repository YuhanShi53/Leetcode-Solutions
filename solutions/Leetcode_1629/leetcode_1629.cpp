#include <string>
#include <vector>

class Solution1
{
public:
    char slowestKey(std::vector<int> & releaseTimes, std::string keysPressed)
    {
        int longestTime = releaseTimes[0];
        char key = keysPressed[0];
        for (int i = 1; i < releaseTimes.size(); i++)
        {
            int duration = releaseTimes[i] - releaseTimes[i-1];
            if (duration > longestTime || duration == longestTime && keysPressed[i] > key)
            {
                longestTime = duration;
                key = keysPressed[i];
            }
        }
        return key;
    }
};
