#include <vector>

using namespace std;

class Solution1
{
public:
    vector<int> constructArray(int n, int k)
    {
        vector<int> array{1};
        int factor = 1;
        for (int i = n - 1; i > 0; --i)
        {
            if (k > 1)
            {
                array.push_back(array[array.size() - 1] + factor * i);
                factor *= -1;
            }
            else
                array.push_back(array[array.size() - 1] + factor);
        }
        return array;
    }
};

class Solution2
{
public:
    vector<int> constructArray(int n, int k)
    {
        vector<int> array;
        for (int i = 1, j = n; i <= j;)
        {
            if (k > 1)
            {
                array.push_back(k-- % 2 ? i++ : j--);
            }
            else
            {
                array.push_back(i++);
            }
        }
        return array;
    }
};