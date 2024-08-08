class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result=0
        n=len(s)

        a=b=c=-1

        for i in range(n):
            if s[i]=='a':
                a=i
            elif s[i]=='b':
                b=i
            else:
                c=i
            
            if a!=-1 and b!=-1 and c!=-1:
                temp=min(a,b,c)
                result+=temp+1
        return result