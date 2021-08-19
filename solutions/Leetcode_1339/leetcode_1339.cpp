#include <algorithm>
#include <vector>

class Solution1
{
public:
    int maxProduct(TreeNode *root)
    {
        _dfs(root);
        long ret = 0;
        for (const int x : _subSums)
        {
            ret = std::max(ret, x * (_total - x));
        }
        return ret % (int)(1e9 + 7);
    }

private:
    long _total = 0;
    std::vector<int> _subSums;

    int _dfs(TreeNode *node)
    {
        if (node == nullptr)
            return 0;
        _total += node->val;
        int subSum = node->val + _dfs(node->left) + _dfs(node->right);
        _subSums.push_back(subSum);
        return subSum;
    }
};
