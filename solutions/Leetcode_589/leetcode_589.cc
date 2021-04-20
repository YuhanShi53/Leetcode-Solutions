#include <vector>

using namespace std;

class Node
{
public:
    int val;
    vector<Node *> children;

    Node() {}

    Node(int _val)
    {
        val = _val;
    }

    Node(int _val, vector<Node *> _children)
    {
        val = _val;
        children = _children;
    }
};

class Solution1
{
public:
    vector<int> preorder(Node *root)
    {
        vector<int> traversal;
        if (root == nullptr)
            return traversal;
        vector<Node *> stack{root};
        while (!stack.empty())
        {
            Node *node = stack.back();
            traversal.push_back(node->val);
            stack.pop_back();
            for (auto it = node->children.rbegin(); it != node->children.rend(); ++it)
                if (*it != nullptr)
                    stack.push_back(*it);
        }
        return traversal;
    }
};