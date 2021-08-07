from typing import List


class Solution1:
    def level_order(self, root) -> List[List[int]]:
        if not root:
            return []
        traversal = []
        queue = [root]
        while queue:
            traversal.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return traversal
