""" Leetcode 623 - Add One Row To Tree

https://leetcode.com/problems/add-one-row-to-tree/

1. Time: O(2^(d-1)) Memory: O(2^(d-1)) (d is given variable)
2. Time: O(2^(d-1)) Memory: O(2^(d-1)) (d is given variable)
3. Time: O(2^(d-1)) Memory: O(2^(d-1)) (d is given variable)

"""

from .common import TreeNode


class Solution1:
    """ 1. MINE | Iteration | BFS """

    def add_one_row(self, root: TreeNode, v: int, d: int) -> TreeNode:
        depth = 1
        if depth == d:
            return TreeNode(v, left=root)
        queue = [root]
        while queue and depth < d - 1:
            num_nodes = len(queue)
            for i in range(num_nodes):
                node = queue.pop()
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            depth += 1
        for node in queue:
            node.left = TreeNode(v, left=node.left)
            node.right = TreeNode(v, right=node.right)
        return root


class Solution2:
    """ 2. Simplified of 1 | Iteration | BFS 

    Borrow from: https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS

    """

    def add_one_row(self, root, v, d):
        dummy = TreeNode(None, root)
        queue = [dummy]
        for i in range(d-1):
            queue = [kid for node in queue
                     for kid in (node.left, node.right) if kid]
        for node in queue:
            node.left = TreeNode(v, left=node.left)
            node.right = TreeNode(v, right=node.right)
        return dummy.left


class Solution3:
    """ 3. Recursion | DFS

    Borrow from: https://leetcode.com/problems/add-one-row-to-tree/discuss/104555/C%2B%2B-Java-10-line-Solution-no-helper

    """

    def add_one_row(self, root, v, d):
        if d == 0:
            return TreeNode(v, right=root)
        elif d == 1:
            return TreeNode(v, left=root)
        if root:
            if d > 2:
                root.left = self.add_one_row(root.left, v, d-1)
                root.right = self.add_one_row(root.right, v, d-1)
            else:
                root.left = self.add_one_row(root.left, v, 1)
                root.right = self.add_one_row(root.right, v, 0)
        return root


if __name__ == '__main__':
    tree_in_list = [4, 2, 6, 3, 1, 5, None]
    root = TreeNode.from_list(tree_in_list)
    v = 1
    d = 2
    res = Solution1().add_one_row(root, v, d)
    pass
