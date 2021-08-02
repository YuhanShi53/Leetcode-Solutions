class Solution1
{
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while ((root->val - p->val) * (root -> val - q->val) > 0)
            root = root->val > p->val ? root->left : root->right;
        return root;
    }
};