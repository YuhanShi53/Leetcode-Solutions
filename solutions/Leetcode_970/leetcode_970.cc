#include <unordered_set>
#include <vector>

using namespace std;

class Solution1
{
public:
    vector<int> powerfulIntegers(int x, int y, int bound)
    {
        unordered_set<int> set;
        for (int i = 1; i <= bound; i *= x)
        {
            for (int j = 1; i + j <= bound; j *= y)
            {
                set.insert(i + j);
                if (y == 1)
                    break;
            }
            if (x == 1)
                break;
        }
        return vector<int>(set.begin(), set.end());
    }
};