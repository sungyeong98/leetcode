# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result=0
        def helper(node, val):
            nonlocal result
            if not node:
                return 

            if node.val>=val:
                result+=1
            helper(node.left, max(node.val, val))
            helper(node.right, max(node.val, val))
        helper(root, root.val)
        return result