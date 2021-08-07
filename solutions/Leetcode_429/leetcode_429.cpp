#include <queue>
#include <vector>

class Solution1
{
public:
    std::vector<std::vector<int>> levelOrder(Node* root) {
        if (root == nullptr)
            return {};
        std::vector<std::vector<int>> traversal;
        std::queue<Node*> q;
        q.push(root);
        std::vector<int> nums;
        while (!q.empty())
        {
            nums.clear();
            int len_q = q.size();
            for (int i = 0; i < len_q; i++)
            {
                Node* node = q.front();
                q.pop();
                nums.push_back(node->val);
                for (Node* child : node->children)
                    q.push(child);
            }
            traversal.push_back(nums);
        }
        return traversal;
    }
};