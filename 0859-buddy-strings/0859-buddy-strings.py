class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n=len(s)
        s,g=list(s),list(goal)
        for i in range(n-1):
            for j in range(i+1,n):
                temp=list(s)
                temp[i],temp[j]=temp[j],temp[i]
                if temp==g:
                    return True
        return False