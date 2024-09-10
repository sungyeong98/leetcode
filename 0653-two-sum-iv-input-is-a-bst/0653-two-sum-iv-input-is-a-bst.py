# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        temp={}
        def find_val(node):
            if not node:
                return False
            if node.val in temp:
                return True
            temp[k-node.val]=True
            return find_val(node.left) or find_val(node.right)
        return find_val(root)