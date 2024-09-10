# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, level = {}, 0
        while head:
            temp[level]=head
            head=head.next
            level+=1
        n=len(temp)//2
        return temp[n]