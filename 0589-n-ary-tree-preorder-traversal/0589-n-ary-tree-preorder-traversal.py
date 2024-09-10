"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result=[]
        if not root:
            return result
        def preorder(node):
            if node.val>=0:
                result.append(node.val)
            for next_node in node.children:
                preorder(next_node)
        preorder(root)
        return result