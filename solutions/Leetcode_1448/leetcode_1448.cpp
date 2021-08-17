#include <stack>
#include <utility>

class Solution1
{
public:
    int goodNodes(TreeNode *root)
    {
        int count = 0;
        std::stack<std::pair<TreeNode *, int>> s;
        s.push({root, -10000});
        TreeNode *node;
        int maxValue;
        while (!s.empty())
        {
            std::pair<TreeNode *, int> nodeMaxValue = s.top();
            node = nodeMaxValue.first;
            maxValue = nodeMaxValue.second;
            s.pop();
            if (node != nullptr)
            {
                if (node->val >= maxValue)
                {
                    maxValue = node->val;
                    count++;
                }
                s.push({node->left, maxValue});
                s.push({node->right, maxValue});
            }
        }
        return count;
    }
};

class Solution1Recursion
{
private:
    int count = 0;

    void dfs(TreeNode *node, int maxValue)
    {
        if (node != nullptr)
        {
            if (node->val >= maxValue)
            {
                count++;
                maxValue = node->val;
            }
            dfs(node->left, maxValue);
            dfs(node->right, maxValue);
        }
    }

public:
    int goodNodes(TreeNode *root)
    {
        dfs(root, -10000);
        return count;
    }
};