""" Leetcode 437 - Path Sum III

https://leetcode.com/problems/path-sum-iii/

1. MINE DFS & Backtracing

"""

from common import TreeNode


class Solution1:
    """ 1. MINE DFS & Backtracing """

    def path_sum(self, root: TreeNode, sum: int) -> int:

        count = 0

        def dfs(node, prev_nums):
            nonlocal count
            if not node:
                return

            prev_nums = prev_nums + [0]
            current_value = node.val
            for i in range(len(prev_nums)):
                prev_nums[i] += current_value
                if prev_nums[i] == sum:
                    count += 1
            dfs(node.left, prev_nums)
            dfs(node.right, prev_nums)

        dfs(root, [])
        return count


if __name__ == '__main__':
    root = TreeNode.from_list([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    sum = 8
    res = Solution1().path_sum(root, sum)
    print(res)
