# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reversed(a,b,flag):
            if not a or not b:
                return
            if flag:
                a.val, b.val = b.val, a.val
            reversed(a.left, b.right, not flag)
            reversed(a.right, b.left, not flag)
        reversed(root.left, root.right, True)
        return root