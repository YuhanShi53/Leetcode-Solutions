class Solution1:
    def sorted_array_to_bst(self, nums: List[int]) -> TreeNode:
        def build_tree(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = build_tree(left, mid-1)
            root.right = build_tree(mid+1, right)
            return root
        return build_tree(0, len(nums)-1)
