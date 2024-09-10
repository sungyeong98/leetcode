# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        def chk(node,path):
            next_path=path+str(node.val)
            if not node.left and not node.right:
                result.append(next_path)
                return
            
            if node.left:
                chk(node.left,next_path+'->')
            if node.right:
                chk(node.right,next_path+'->')
        chk(root,'')
        return result