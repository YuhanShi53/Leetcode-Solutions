# include <unordered_map>
# include <vector>

using namespace std;

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder)
    {
        unordered_map<int, int> indices;
        for (int i = 0; i != inorder.size(); i++)
            indices[inorder[i]] = i;
        return buildSubTree(preorder, inorder, indices, 0, 0, inorder.size()-1);
    }

private:
    TreeNode *buildSubTree(vector<int>& preorder, vector<int> &inorder, unordered_map<int, int> &indices, int idx, int low, int high)
    {
        if (low > high)
            return nullptr;
        TreeNode *root = new TreeNode(preorder[idx]);
        int mid = indices[root->val];
        root->left = buildSubTree(preorder, inorder, indices, idx+1, low, mid-1);
        root->right = buildSubTree(preorder, inorder, indices, idx+mid-low+1, mid+1, high);
        return root;
    }
};