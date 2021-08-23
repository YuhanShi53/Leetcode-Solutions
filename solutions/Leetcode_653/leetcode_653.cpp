#include <stack>
#include <unordered_set>

class Solution1
{
public:
    bool findTarget(TreeNode* root, int k)
    {
        std::unordered_set<int> set;
        std::stack<TreeNode*> s;
        s.push(root);
        while (!s.empty())
        {
            TreeNode* node = s.top();
            s.pop();
            if (node != nullptr)
            {
                int target = k - node->val;
                if (set.find(target) != set.end())
                    return true;
                set.insert(node->val);
                s.push(node->left);
                s.push(node->right);
            }
        }
        return false;
    }
};


class Solution2
{
TreeNode* _root = nullptr;

public:
    bool findTarget(TreeNode* root, int k)
    {
        if (this->_root == nullptr)
            this->_root = root;
        if (root == nullptr)
            return false;
        return (_dfs(root, k - root->val) || findTarget(root->left, k) || findTarget(root->right, k));
    }

private:
    bool _dfs(TreeNode* node, int target)
    {
        TreeNode* root = this->_root;
        while (root != nullptr)
        {
            if (root->val == target && root != node)
                return true;
            if (root->val > target)
                root = root->left;
            else
                root = root->right;
        }
        return false;
    }
};
