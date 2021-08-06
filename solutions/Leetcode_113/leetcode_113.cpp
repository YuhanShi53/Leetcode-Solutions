#include <vector>

class Solution1
{
public:
    std::vector<std::vector<int>> pathSum(TreeNode *root, int targetSum)
    {
        if (root == nullptr)
            return {};
        std::vector<int> path{root->val};
        std::vector<std::vector<int>> paths;
        dfs(root, path, targetSum - root->val, paths);
        return paths;
    }

private:
    void dfs(TreeNode *node, const std::vector<int> &path, int pathSum, std::vector<std::vector<int>> &paths)
    {
        if (node->left != nullptr)
        {
            std::vector<int> leftPath = path;
            leftPath.push_back(node->left->val);
            dfs(node->left, leftPath, pathSum - node->left->val, paths);
        }
        if (node->right != nullptr)
        {
            std::vector<int> rightPath = path;
            rightPath.push_back(node->right->val);
            dfs(node->right, rightPath, pathSum - node->right->val, paths);
        }
        if (node->left == nullptr && node->right == nullptr && pathSum == 0)
            paths.push_back(path);
    }
};
