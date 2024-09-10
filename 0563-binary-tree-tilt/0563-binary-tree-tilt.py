# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result=0
        def helper(node):
            nonlocal result
            if not node:
                return 0
            left,right=helper(node.left), helper(node.right)
            result+=abs(left-right)
            return node.val+left+right
        helper(root)
        return result