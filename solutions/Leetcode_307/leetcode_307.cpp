#include <vector>

using namespace std;

struct SegmentTree
{
    SegmentTree(int s, int e) : start(s), end(e) {}

    int start, end, total = 0;
    SegmentTree *left = nullptr, *right = nullptr;
};

class NumArray1
{
public:
    NumArray1(vector<int> &nums)
    {
        root = create_tree(nums, 0, nums.size()-1);
    }

    void update(int index, int val)
    {
        update_util(root, index, val);
    }

    int sumRange(int left, int right)
    {
        return sum_util(root, left, right);
    }

private:
    SegmentTree *root;

    SegmentTree *create_tree(vector<int> &nums, int start, int end)
    {
        SegmentTree *node = new SegmentTree(start, end);
        if (start == end)
        {
            node->total = nums[start];
            return node;
        }
        int mid = (start + end) / 2;
        node->left = create_tree(nums, start, mid);
        node->right = create_tree(nums, mid + 1, end);
        node->total = node->left->total + node->right->total;
        return node;
    }

    int update_util(SegmentTree *node, int index, int value)
    {
        if (node->start == index && node->end == index)
        {
            node->total = value;
            return node->total;
        }
        int mid = (node->start + node->end) / 2;
        if (index <= mid)
            update_util(node->left, index, value);
        else
            update_util(node->right, index, value);
        node->total = node->left->total + node->right->total;
        return node->total;
    }

    int sum_util(SegmentTree *node, int start, int end)
    {
        if (node->start == start && node->end == end)
            return node->total;
        int mid = (node->start + node->end) / 2;
        if (mid < start)
            return sum_util(node->right, start, end);
        else if (end <= mid)
            return sum_util(node->left, start, end);
        else
            return sum_util(node->left, start, mid) + sum_util(node->right, mid + 1, end);
    }
};


class NumArray2
{
public:
    NumArray2(std::vector<int>& nums)
    {
        _nums = std::vector<int>(nums.size(), 0);
        _bitTree = std::vector<int>(nums.size() + 1, 0);
        _treeLength = nums.size() + 1;
        for (int i = 0; i < nums.size(); i++)
            update(i, nums[i]);
    }

    void update(int index, int val)
    {
        int diff = val - _nums[index];
        _nums[index] = val;
        index++;
        while (index < _treeLength)
        {
            _bitTree[index] += diff;
            index += index & (-index);
        }
    }

    int sumRange(int left, int right)
    {
        return _sumTo(right) - _sumTo(left-1);
    }

private:
    int _sumTo(int index)
    {
        int total = 0;
        index++;
        while (index > 0)
        {
            total += _bitTree[index];
            index -= index & (-index);
        }
        return total;
    }

    std::vector<int> _nums;
    std::vector<int> _bitTree;
    int _treeLength;
};