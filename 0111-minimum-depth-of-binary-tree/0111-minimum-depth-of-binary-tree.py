# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)

        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1+right
        if not root.right:
            return 1+left
        return min(left,right)+1