# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_set, cur = set(), headA
        while cur:
            first_set.add(cur)
            cur=cur.next
        cur=headB
        while cur:
            if cur in first_set:
                return cur
            cur=cur.next
        return None