class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen=deque([])
        result=[]

        cnt=0
        for i in nums:
            if i!=-1:
                cnt=0
                seen.appendleft(i)
            else:
                cnt+=1
                if len(seen)>=cnt:
                    result.append(seen[cnt-1])
                else:
                    result.append(-1)
        
        return result