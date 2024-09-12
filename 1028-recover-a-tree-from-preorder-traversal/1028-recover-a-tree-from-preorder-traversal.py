# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root=None
        for val in traversal.split('-'):
            if not root or val=='':
                parent=(parent.right if parent.right else parent.left) if root else (root:=TreeNode(int(val)))
            else:
                parent,_=root, setattr(parent, 'right' if parent.left else 'left', TreeNode(int(val)))
        return root