class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num=list(num)
        ori=num.copy()

        for _ in range(k):
            for i in reversed(range(len(num)-1)):
                if num[i]<num[i+1]:
                    ii=i+1
                    while ii<len(num) and num[i]<num[ii]:
                        ii+=1
                    num[i],num[ii-1]=num[ii-1],num[i]
                    lo,hi=i+1,len(num)-1
                    while lo<hi:
                        num[lo],num[hi]=num[hi],num[lo]
                        lo+=1
                        hi-=1
                    break
        result=0
        for i in range(len(num)):
            ii=i
            while ori[i]!=num[i]:
                result+=1
                ii+=1
                num[i],num[ii]=num[ii],num[i]
        return result