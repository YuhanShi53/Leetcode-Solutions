from typing import List

class Solution1:
    def build_tree(self, preorder, inorder):
        indices = {x: i for i, x in enumerate(inorder)}

        def build_tree(idx, low, high):
            if low > high:
                return None
            root = TreeNode(preorder[idx])
            mid = indices[root.val]
            root.left = build_tree(idx+1, low, mid-1)
            root.right = build_tree(idx+mid-low+1, mid+1, high)
            return root
        
        return build_tree(0, 0, len(inorder)-1)

class SolutionMINE:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        value = preorder[0]
        root = TreeNode(value)
        idx = inorder.index(value)
        root.left = self.build_tree(preorder[:idx], inorder[:idx])
        root.right = self.build_tree(preorder[idx+1:], inorder[idx+1:])
        return root