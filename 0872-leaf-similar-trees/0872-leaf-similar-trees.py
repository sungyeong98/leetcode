# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        temp1,temp2=[],[]
        def chk1(node):
            if not node.left and not node.right:
                temp1.append(node.val)
                return
            if node.left:
                chk1(node.left)
            if node.right:
                chk1(node.right)
        def chk2(node):
            if not node.left and not node.right:
                temp2.append(node.val)
                return
            if node.left:
                chk2(node.left)
            if node.right:
                chk2(node.right)
        chk1(root1)
        chk2(root2)
        return temp1==temp2