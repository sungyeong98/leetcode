# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        temp=[]
        def helper(node):
            if not node:
                return
            temp.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        temp.sort()
        n=len(temp)
        result=float('inf')
        for i in range(n-1):
            result=min(result,temp[i+1]-temp[i])
        return result