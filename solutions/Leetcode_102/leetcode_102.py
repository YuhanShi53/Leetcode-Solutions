class Solution1:
    def level_order(self, root):
        if not root:
            return []
        queue = [root]
        traversal = []
        while queue:
            level_values = []
            for i in range(len(queue)):
                node = queue.pop()
                level_values.append(node.val)
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            traversal.append(level_values)
        return traversal
