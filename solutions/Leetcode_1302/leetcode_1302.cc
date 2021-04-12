#include <queue>

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
    int deepestLeavesSum(TreeNode* root) {
        int sum = 0;
        queue<TreeNode *> level;
        level.push(root);
        while (level.size())
        {
            sum = 0;
            for (int i = level.size(); i > 0; --i)
            {
                TreeNode* node = level.front();
                level.pop();
                sum += node->val;
                if (node->left) level.push(node->left);
                if (node->right) level.push(node->right);
            }
        }
        return sum;
    }
};