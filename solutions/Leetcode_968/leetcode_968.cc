class Solution1
{
public:
    int minCameraCover(TreeNode* root)
    {
        return (dfs(root) == 0 ? 1 : 0) + num_cameras;
    }

private:
    int num_cameras = 0;

    int dfs(TreeNode* node)
    {
        if (node == nullptr)
            return 2;
        int left = dfs(node->left);
        int right = dfs(node->right);
        if (left == 0 || right == 0)
        {
            num_cameras++;
            return 1;
        }
        return left == 1 || right == 1 ? 2 : 0;
    }
};