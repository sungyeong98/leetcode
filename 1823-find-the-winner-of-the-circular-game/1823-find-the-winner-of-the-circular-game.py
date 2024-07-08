class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        temp={i:[] for i in range(1,n+1)}
        for i in range(1,n+1):
            left=i-1 if i-1>0 else n
            right=i+1 if i+1<=n else 1
            temp[i].append(left)
            temp[i].append(right)

        start=1
        while True:
            cnt=0
            while cnt<k:
                start=temp[start][1]
                cnt+=1
            
            if start==temp[start][1]:
                return start
            
            prev=temp[start][0]
            temp[temp[prev][0]][1]=start
            temp[start][0]=temp[prev][0]
            temp[prev][0]=temp[prev][1]=0