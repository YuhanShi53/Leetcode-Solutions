#include <string>
#include <vector>

class Solution1
{
public:
    std::string shiftingLetters(std::string s, std::vector<int> &shifts)
    {
        int prevShift = 0;
        std::string shiftedLetters = s;
        for (int i = shifts.size() - 1; i >= 0; i--)
        {
            int totalShift = (prevShift + shifts[i]) % 26;
            prevShift = totalShift;
            shiftedLetters[i] = (shiftedLetters[i] - 'a' + totalShift) % 26 + 'a';
        }
        return shiftedLetters;
    }
};
