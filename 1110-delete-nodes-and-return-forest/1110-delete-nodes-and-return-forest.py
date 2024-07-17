# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        temp=set(to_delete)
        result=[]

        def dfs(root,isRoot):
            if not root:
                return None
            
            del_root=root.val in temp
            if isRoot and not del_root:
                result.append(root)
            root.left=dfs(root.left,del_root)
            root.right=dfs(root.right,del_root)
            return None if del_root else root
        dfs(root,True)
        return result