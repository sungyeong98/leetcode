class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        temp=[]
        prev=0
        for id,t in logs:
            temp.append((id,t-prev))
            prev=t
        return sorted(temp,key=lambda x:(-x[1],x[0]))[0][0]