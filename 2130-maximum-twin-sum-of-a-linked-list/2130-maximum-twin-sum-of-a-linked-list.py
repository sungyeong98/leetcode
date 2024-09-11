# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        result=0

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        cur, prev = slow, None

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        while prev:
            result = max(result, head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return result