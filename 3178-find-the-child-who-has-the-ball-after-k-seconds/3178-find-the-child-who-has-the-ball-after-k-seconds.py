class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        temp=list(range(n))
        idx,state=0,True
        while k>0:
            if state and idx<n-1:
                idx+=1
            elif state and idx==n-1:
                idx-=1
                state=False
            elif not state and idx>0:
                idx-=1
            elif not state and idx==0:
                idx+=1
                state=True
            k-=1
        return idx