#include <sstream>
#include <string>

class Solution1
{
public:
    bool isValidSerialization(std::string preorder)
    {
        int count = 1;
        std::stringstream ss(preorder);
        std::string x;
        while (getline(ss, x, ','))
        {
            if (count == 0)
                return false;
            count += x == "#" ? -1 : 1;
        }
        return count == 0;
    }
};

// Borrow from: <https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78554/C%2B%2B-4ms-solution-O(1)-space-O(n)-time>
class SolutionWithoutSplit
{
public:
    bool isValidSerialization(std::string preorder)
    {
        preorder += ',';
        int count = 1;
        int idx = 0;
        for (int idx = 0; idx < preorder.size(); idx++)
        {
            if (count == 0)
                return false;
            if (preorder[idx] != ',')
                continue;
            count += preorder[idx - 1] == '#' ? -1 : 1;
        }
        return count == 0;
    }
};
