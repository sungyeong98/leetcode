# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        result=None

        while q:
            node=q.popleft()
            result=node.val

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return result