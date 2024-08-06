class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        g=sorted(grades)
        cnt=1
        prev=0
        while g:
            if len(g)<cnt:
                return cnt-1
            count=0
            temp=0
            while count<cnt:
                temp+=g.pop(0)
                count+=1
            if temp>prev:
                cnt+=1
            else:
                return cnt-1
        return cnt-1