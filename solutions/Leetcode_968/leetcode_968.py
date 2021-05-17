class Solution1:
    def min_camera_cover(self, root):
        self._num_camera = 0
        def dfs(node):
            if not node:
                return 2
            left, right = dfs(node.left), dfs(node.right)
            if left == 0 or right == 0:
                self._num_camera += 1
                return 1
            return 2 if left == 1 or right == 1 else 0
        return (dfs(root) == 0) + self._num_camera


class SolutionMINE:
    def min_camera_cover(self, root):
        self._num_camera = 0
        dummy = TreeNode(0, left=root, right=None)
        self.helper(dummy)
        return self._num_camera

    def helper(self, node):
        left = self.helper(node.left) if node.left else 0
        right = self.helper(node.right) if node.right else 0
        if left == 2 or right == 2:
            self._num_camera += 1
        if left == right == 0:
            return 2
        return max(left, right) - 1

