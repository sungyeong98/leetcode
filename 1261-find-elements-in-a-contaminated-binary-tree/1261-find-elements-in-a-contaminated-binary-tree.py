# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.visited=defaultdict(bool)

        root.val=0
        self.visited[0]=True
        def helper(node):
            if node.left:
                node.left.val=node.val*2+1
                self.visited[node.left.val]=True
                helper(node.left)
            if node.right:
                node.right.val=node.val*2+2
                self.visited[node.right.val]=True
                helper(node.right)
        helper(root)
        self.root=root

    def find(self, target: int) -> bool:
        return True if target in self.visited else False        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)