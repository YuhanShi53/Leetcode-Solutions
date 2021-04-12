from solutions.common import TreeNode


class Solution1:
    def deepest_leaves_sum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [root]
        while queue:
            count = len(queue)
            summation = 0
            while count > 0:
                node = queue.pop()
                summation += node.val
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
                count -= 1
        return summation


if __name__ == '__main__':
    tree_in_list = [1, 2, 3, 4, 5, None, 6, 7,
                    None, None, None, None, None, None, 8]
    root = TreeNode.from_list(tree_in_list)
    ans = Solution1().deepest_leaves_sum(root)
    print(ans)
