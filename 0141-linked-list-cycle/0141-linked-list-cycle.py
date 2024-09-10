# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        cur_node=head
        while cur_node:
            if cur_node in visited:
                return True
            visited.add(cur_node)
            cur_node=cur_node.next
        return False