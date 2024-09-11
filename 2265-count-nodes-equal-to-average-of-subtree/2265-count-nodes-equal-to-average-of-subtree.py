# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result=0
        
        def find(node):
            nonlocal result
            if not node:
                return 0,0
            left_sum, left_count=find(node.left)
            right_sum,right_count=find(node.right)

            cur_sum=node.val+left_sum+right_sum
            cur_count=1+left_count+right_count

            if cur_sum//cur_count==node.val:
                result+=1
            return cur_sum,cur_count
        
        find(root)
        return result