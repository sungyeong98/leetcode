# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result=0

        def helper(node, min_val, max_val):
            nonlocal result
            if not node:
                result=max(result,max_val-min_val)
                return
            
            helper(node.left, min(min_val, node.val), max(max_val, node.val))
            helper(node.right, min(min_val, node.val), max(max_val, node.val))
        
        helper(root, float('inf'), -1)
        return result