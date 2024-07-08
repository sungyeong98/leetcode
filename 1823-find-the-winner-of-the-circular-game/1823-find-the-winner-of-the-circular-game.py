class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        temp={i:i+1 for i in range(1,n+1)}
        temp[n]=1

        start=1
        while sum(1 for value in temp.values() if value!=0)>1:
            cnt, previous=0 if k>1 else -1, 0
            while cnt<k-1:
                previous=start
                start=temp[start]
                cnt+=1
            
            temp[previous]=temp[start]
            temp[start]=0
            start=temp[previous]
        
        for i in temp.keys():
            if temp[i]!=0:
                return i