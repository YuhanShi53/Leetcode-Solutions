#!/usr/bin/env python
""" Leetcode 222 - Count Complete Tree Node

https://leetcode.com/problems/count-complete-tree-nodes/

Normal: Time： 128ms(7.55%) Memory: 21.3MB(26.34%)
"""

from utils import TreeNode

class Solution1:
    """ self-implement """
    def count_nodes(self, root: TreeNode) -> int:
        stack = [root]
        count = 1
        
        while len(stack) > 0:
            temp = stack.pop()
            if temp.left is not None:
                stack.append(temp.left)
                count += 1
            if temp.right is not None:
                stack.append(temp.right)
                count += 1
                
        return count
    
if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, None]
    root = TreeNode.from_list(list)
    res = Solution1().count_nodes(root)
    print(res)
    
