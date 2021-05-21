#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution1
{
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        if (root == nullptr)
            return {};
        queue<TreeNode *> q;
        q.push(root);
        vector<vector<int>> traversal;
        int num_in_level = 0;
        TreeNode *node;
        while (!q.empty())
        {
            num_in_level = q.size();
            vector<int> level;
            for (int i = 0; i < num_in_level; i++)
            {
                node = q.front();
                q.pop();
                level.push_back(node->val);
                if (node->left != nullptr)
                    q.push(node->left);
                if (node->right != nullptr)
                    q.push(node->right);

            }
            traversal.push_back(level);
        }
        return traversal;
    }
};
