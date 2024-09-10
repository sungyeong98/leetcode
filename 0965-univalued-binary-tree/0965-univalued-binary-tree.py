# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        temp=set()
        def chk(node):
            temp.add(node.val)
            if node.left:
                chk(node.left)
            if node.right:
                chk(node.right)
        chk(root)
        return len(temp)==1