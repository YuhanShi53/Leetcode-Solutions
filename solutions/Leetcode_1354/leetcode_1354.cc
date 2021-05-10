#include <numeric>
#include <queue>
#include <vector>

using namespace std;

class Solution1
{
public:
    bool isPossible(vector<int> target)
    {
        long total = accumulate(target.begin(), target.end(), (long)0);
        int max_value;
        priority_queue<int> q(target.begin(), target.end());
        while (true)
        {
            max_value = q.top();
            q.pop();
            total -= max_value;
            if (max_value == 1 || total == 1)
                return true;
            if (max_value <= total || total == 0 || max_value % total == 0)
                return false;
            max_value %= total;
            total += max_value;
            q.push(max_value);
        }
    }
};