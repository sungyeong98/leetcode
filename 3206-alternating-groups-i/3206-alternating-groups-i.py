class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        result=0
        c=[colors[-1]]+colors+[colors[0]]
        n=len(c)
        for i in range(1,n-1):
            if c[i-1]==c[i+1] and c[i]!=c[i-1]:
                result+=1
        return result