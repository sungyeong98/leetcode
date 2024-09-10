# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cur_val, cur_cnt, max_cnt, modes = None, 0, 0, []
        def helper(node):
            nonlocal cur_val, cur_cnt, max_cnt, modes
            if not node:
                return
            helper(node.left)
            cur_cnt=cur_cnt+1 if node.val==cur_val else 1
            cur_val=node.val

            if cur_cnt>max_cnt:
                max_cnt=cur_cnt
                modes=[cur_val]
            elif cur_cnt==max_cnt:
                modes.append(cur_val)
            helper(node.right)
        helper(root)
        return modes