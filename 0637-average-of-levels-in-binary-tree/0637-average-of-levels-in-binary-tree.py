# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:    return []
        temp=defaultdict(list)
        stack=[(root,0)]
        while stack:
            node,level=stack.pop()
            temp[level].append(node.val)
            if node.left:
                stack.append((node.left,level+1))
            if node.right:
                stack.append((node.right,level+1))
        result=[sum(temp[i])/len(temp[i]) for i in range(len(temp))]
        return result