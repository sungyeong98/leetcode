# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result=[[-1]*n for _ in range(m)]
        result[0][0], head = head.val, head.next
        x,y,dx,dy,r,c=0,0,0,1,range(m),range(n)
        while head:
            if x+dx in r and y+dy in c and result[x+dx][y+dy]==-1:
                x+=dx
                y+=dy
                result[x][y], head = head.val, head.next
            else:
                dx,dy=dy,-dx
        return result