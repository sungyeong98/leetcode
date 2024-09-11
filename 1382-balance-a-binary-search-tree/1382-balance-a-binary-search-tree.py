# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left)+[node.val]+dfs(node.right)

        temp=dfs(root)

        def solution(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(temp[mid])
            root.left, root.right = solution(left, mid-1), solution(mid+1, right)
            return root
        
        return solution(0,len(temp)-1)