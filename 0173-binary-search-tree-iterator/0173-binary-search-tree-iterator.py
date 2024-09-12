# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        temp=[]
        def helper(node):
            if not node:
                return 
            temp.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        
        self.nums=deque(sorted(temp))

    def next(self) -> int:
        return self.nums.popleft()

    def hasNext(self) -> bool:
        return True if self.nums else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()