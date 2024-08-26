"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        s, li = [], []
        s.append(root)
        if not root:
            return
        while s:
            temp=s.pop()
            li.append(temp.val)
            for i in temp.children:
                s.append(i)
        return li[::-1]