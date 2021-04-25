#include <string>

using namespace std;

class Solution1
{
public:
    int countBinarySubstrings(string s)
    {
        int prev_count = 0, current_count = 1, total = 0;
        for (int i = 1; i != s.size(); ++i)
        {
            if (s[i] == s[i - 1])
                current_count++;
            else
            {
                total += min(prev_count, current_count);
                prev_count = current_count;
                current_count = 1;
            }
        }
        return total + min(prev_count, current_count);
    }
};