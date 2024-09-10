# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result=0

        def helper(node):
            nonlocal result
            left=helper(node.left) if node.left else 0
            right=helper(node.right) if node.right else 0
            result=max(result,left+right)
            return 1+max(left,right)
        
        helper(root)
        return result