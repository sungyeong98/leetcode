class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result,n=0,len(satisfaction)
        satisfaction.sort()

        for i in range(n):
            temp, s = 0, satisfaction[i:]
            for j in range(len(s)):
                temp+=(j+1)*s[j]
            if temp>result:
                result=temp
        return result