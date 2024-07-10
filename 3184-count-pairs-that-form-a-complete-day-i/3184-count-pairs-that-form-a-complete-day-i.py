class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        result,n=0,len(hours)
        for i in range(n-1):
            for j in range(i+1, n):
                if (hours[i]+hours[j])%24==0:
                    result+=1
        return result