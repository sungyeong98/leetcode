# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        temp=defaultdict(int)
        def find(node,depth):
            if not node:
                return
            temp[depth]+=node.val
            find(node.left, depth+1)
            find(node.right, depth+1)
        find(root,0)
        return temp[max(temp.keys())]