class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        #solution1
        '''
        result,n=0,len(satisfaction)
        satisfaction.sort()

        for i in range(n):
            temp, s = 0, satisfaction[i:]
            for j in range(len(s)):
                temp+=(j+1)*s[j]
            if temp>result:
                result=temp
        return result
        '''
        satisfaction.sort(reverse=True)
        cnt, result=0,0
        n=len(satisfaction)
        for i in range(n):
            if cnt+satisfaction[i]>0:
                cnt+=satisfaction[i]
                result+=cnt
            else:
                break
        return result