# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0:
            return []
        temp={}

        def helper(n):
            if n in temp:
                return temp[n]
            
            graph=[]
            if n==1:
                graph.append(TreeNode(0))
            else:
                for i in range(1,n-1,2):
                    left=helper(i)
                    right=helper(n-i-1)

                    for l in left:
                        for r in right:
                            graph.append(TreeNode(0,l,r))
            temp[n]=graph
            return graph
        return helper(n)