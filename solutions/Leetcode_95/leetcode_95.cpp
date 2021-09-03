#include <vector>

class Solution1
{
public:
    std::vector<TreeNode*> generateTrees(int n)
    {
        return _generateTreesInRange(1, n);
    }

private:
    std::vector<TreeNode*> _generateTreesInRange(int m, int n)
    {
        if (m > n)
           return {nullptr};
        std::vector<TreeNode*> trees;
        for (int x = m; x <= n; x++)
            for (TreeNode* leftTree : _generateTreesInRange(m, x-1))
                for (TreeNode* rightTree : _generateTreesInRange(x+1, n))
                {
                    TreeNode* node = new TreeNode(x);
                    node->left = leftTree;
                    node->right = rightTree;
                    trees.push_back(node);
                }
        return trees;
    }
};
