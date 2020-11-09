""" Leetcode 100 - Same Tree

https://leetcode.com/problems/same-tree/

1. self-implement Complete-Compare: Time: 36ms(30%) Memory: 14MB(21%)
2. self-implement Dynamic-Compare: Time: 36ms(30%) Memory: 14MB(21%)
3. Recursive: Time: 56ms(6%) Memory: 14MB(13%)

"""

from common import TreeNode


class Solution1:
    """ 1. self-implement Complete-Compare """
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        p_values = self.display_tree(p)
        q_values = self.display_tree(q)
        if p_values == q_values:
            return True
        else:
            return False

    def display_tree(self, node):
        queue = [node]
        tree_values = []
        while queue:
            node = queue.pop()
            if node is None:
                tree_values.append('null')
            else:
                tree_values.append(node.val)

                queue.insert(0, node.left)
                queue.insert(0, node.right)

        return tree_values


class Solution2:
    """ 2. self-implement Dynamic-Compare """
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        p_queue = [p]
        q_queue = [q]
        while p_queue and q_queue:
            p_node = p_queue.pop()
            q_node = q_queue.pop()

            if p_node is not None and q_node is not None and p_node.val == q_node.val:
                p_queue.insert(0, p_node.left)
                p_queue.insert(0, p_node.right)
                q_queue.insert(0, q_node.left)
                q_queue.insert(0, q_node.right)
            elif p_node is not None or q_node is not None:
                return False

        if p_queue or q_queue:
            return False
        return True


class Solution3:
    """ 3. Recursive """
    def is_same_tree(self, p, q):
        if p and q:
            return p.val == q.val and self.is_same_tree(
                p.left, q.left) and self.is_same_tree(p.right, q.right)
        return p is q


if __name__ == '__main__':
    p = TreeNode.from_list([1, 2, 'null'])
    q = TreeNode.from_list([1, 2, 3])
    res = Solution3().is_same_tree(p, q)
    print(res)
