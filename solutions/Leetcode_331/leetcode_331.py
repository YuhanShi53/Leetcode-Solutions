class Solution1:
    def is_valid_serialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        count = 1
        for x in preorder:
            if count == 0:
                return False
            count += -1 if x == '#' else 1
        return count == 0
