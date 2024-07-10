from collections import deque
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n=len(s)
        nums=deque([i for i in range(0,n+1)])
        result=[]
        for i in s:
            if i=='I':
                result.append(nums.popleft())
            else:
                result.append(nums.pop())
        result.append(nums.pop())
        return result