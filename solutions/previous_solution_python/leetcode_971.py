""" Leetcode 971 - Flip Binary Tree To Match Preorder Traversal

https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

1. Time: O(n) Memory: O(n) (n is number of nodes)

"""

from typing import List

from common import TreeNode


class Solution1:
    """ 1. MINE | Tree | DFS """

    def flip_match_voyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stack = [root]
        ans = []
        for i in range(len(voyage)):
            node = stack.pop()
            if node.val != voyage[i]:
                return [-1]
            if node.left and node.left.val != voyage[i+1]:
                ans.append(node.val)
                node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans


if __name__ == '__main__':
    tree_in_list = [1, 2, 3, None, 6, 5, 4]
    voyage = [1, 3, 4, 5, 2, 6]
    root = TreeNode().from_list(tree_in_list)
    ans = Solution1().flip_match_voyage(root, voyage)
    print(ans)
