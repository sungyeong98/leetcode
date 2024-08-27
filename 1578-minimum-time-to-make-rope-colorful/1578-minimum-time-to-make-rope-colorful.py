class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result=0
        i,j=0,0
        n=len(neededTime)
        while i<n and j<n:
            cur_cnt=0
            cur_max=0

            while j<n and colors[i]==colors[j]:
                cur_cnt+=neededTime[j]
                cur_max=max(cur_max,neededTime[j])
                j+=1
            result+=cur_cnt-cur_max
            i=j
        return result