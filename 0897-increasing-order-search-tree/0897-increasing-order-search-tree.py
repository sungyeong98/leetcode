# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, node: TreeNode) -> TreeNode:
        dummy=tail=TreeNode()
        while node is not None:
            if node.left is not None:
                pred=node.left
                while pred.right is not None:
                    pred=pred.right
                pred.right=node
                left,node.left=node.left,None
                node=left
            else:
                tail.right=tail=node
                node=node.right
        return dummy.right