class Solution:
    def minSwaps(self, s: str) -> int:
        result=0
        for i in s:
            if result>0 and i==']':
                result-=1
            elif i=='[':
                result+=1
        return (result+1)//2