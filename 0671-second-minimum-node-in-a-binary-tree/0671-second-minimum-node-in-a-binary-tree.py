# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        temp=set()

        def find(node):
            if not node:
                return 
            temp.add(node.val)
            find(node.left)
            find(node.right)
        find(root)
        
        return sorted(list(temp))[1] if len(temp)>1 else -1