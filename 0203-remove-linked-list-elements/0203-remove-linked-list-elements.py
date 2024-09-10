# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result=ListNode(-1)
        result.next=head

        cur_node=result
        while cur_node.next!=None:
            if cur_node.next.val==val:
                cur_node.next=cur_node.next.next
            else:
                cur_node=cur_node.next
        return result.next