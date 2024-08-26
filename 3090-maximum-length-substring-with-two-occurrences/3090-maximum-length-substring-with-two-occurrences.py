class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result=0
        n=len(s)
        for i in range(n-1):
            temp={'a':0, 'b':0, 'c':0}
            temp[s[i]]+=1
            for j in range(i+1,n):
                temp[s[j]]+=1
                if max(temp.values())<=2:
                    result=max(result,j-i+1)
        return result