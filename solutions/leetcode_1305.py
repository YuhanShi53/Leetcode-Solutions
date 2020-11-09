""" Leetcode 1305 - All 

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/


"""

from collections import deque
from common import TreeNode
from typing import List


class Solution1:

    def get_all_elements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def traverse(root):
            if root is None:
                return []
            nums = []
            q = deque([root])
            while q:
                node = q.pop()
                nums.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            return nums

        nums1 = traverse(root1)
        nums2 = traverse(root2)

        nums = nums1 + nums2
        nums.sort()
        return nums


if __name__ == '__main__':
    root1 = TreeNode.from_list([])
    root2 = TreeNode.from_list([5, 1, 7, 0, 2])
    res = Solution1().get_all_elements(root1, root2)
    print(res)
