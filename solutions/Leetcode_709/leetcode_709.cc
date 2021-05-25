#include <string>

using namespace std;

class Solution1
{
public:
    string toLowerCase(string s)
    {
        for (char &x : s)
            if ('A' <= x && x <= 'Z')
                 x += 32;
        return s;
    }
};