#include <algorithm>
#include <string>

using namespace std;

class Solution1
{
    int minPartitions(string n)
    {
        return *max_element(begin(n), end(n)) - '0';
    }
};