""" Leetcode 1457 - Pseudo-Palindromic Paths in a Binary Tree

https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

1. Time: O(n) Memory: O(h) (n, h are the number of nodes and height of tree)
2. Time: O(n) Memory: O(h) (n, h are the number of nodes and height of tree)

"""

from collections import defaultdict

from common import TreeNode


class Solution1:
    """ 1. MINE | DFS | HASH """

    def pseudo_palindromic_paths(self, root: TreeNode) -> int:
        count = 0
        nums = defaultdict(int)

        def dfs(node):
            nonlocal count
            nums[node.val] += 1
            if node.left is None and node.right is None:
                odd_num = sum([1 for x in nums.values() if x % 2 > 0])
                if odd_num <= 1:
                    count += 1
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
            nums[node.val] -= 1
        dfs(root)
        return count


class Solution2:
    """ 2. Bit-Manipulation | DFS

    https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/648534/JavaC%2B%2BPython-At-most-one-odd-occurrence

    """

    def pseudo_palindromic_paths(self, root):
        def dfs(node, num_count):
            if node is None:
                return 0
            num_count ^= 1 << (node.val - 1)
            count = dfs(node.left, num_count) + dfs(node.right, num_count)
            if node.left is None and node.right is None:
                if num_count & (num_count - 1) == 0:
                    count += 1
            return count
        return dfs(root, 0)


if __name__ == '__main__':
    list_of_tree = [2, 1, 1, 1, 3, None, None, None, None, None, 1]
    root = TreeNode.from_list(list_of_tree)
    res = Solution2().pseudo_palindromic_paths(root)
    print(res)
