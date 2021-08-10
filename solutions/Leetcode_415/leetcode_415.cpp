#include <algorithm>
#include <string>

class Solution1
{
public:
    std::string addStrings(std::string num1, std::string num2)
    {
        int i = num1.size() - 1;
        int j = num2.size() - 1;
        std::string ret = "";
        int addOne = 0;
        while (i >= 0 || j >= 0 || addOne)
        {
            int x1 = i >= 0 ? num1[i] - '0' : 0;
            int x2 = j >= 0 ? num2[j] - '0' : 0;
            i--;
            j--;
            int sum = x1 + x2 + addOne;
            addOne = sum / 10;
            sum %= 10;
            ret.push_back('0' + sum);
        }
        std::reverse(ret.begin(), ret.end());
        return ret;
    }
};