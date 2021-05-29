#include <numeric>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution1
{
public:
    int maximumUniqueSubarray(vector<int> &nums)
    {
        unordered_map<int, int> last_num_index;
        int maximum = 0, current = 0, head = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            int x = nums[i];
            if (last_num_index.count(x) && last_num_index[x] >= head)
            {
                for (int j = head; j <= last_num_index[x]; j++)
                    current -= nums[j];
                head = last_num_index[x] + 1;
            }
            current += x;
            last_num_index[x] = i;
            maximum = max(maximum, current);
        }
        return maximum;
    }
};

class Solution2
{
public:
    int maximumUniqueSubarray(vector<int> &nums)
    {
        unordered_set<int> unique;
        int maximum = 0, current = 0, head = 0;
        for (int tail = 0; tail < nums.size(); tail++)
        {
            while (unique.find(nums[tail]) != unique.end())
            {
                unique.erase(nums[head]);
                current -= nums[head];
                head++;
            }
            unique.insert(nums[tail]);
            current += nums[tail];
            maximum = max(maximum, current);
        }
        return maximum;
    }
};
