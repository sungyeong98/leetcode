class Solution:
    def getSmallestString(self, s: str) -> str:
        result=[]
        idx,n=0,len(s)
        s=list(s)
        while idx<n-1:
            if int(s[idx])%2==0 and int(s[idx+1])%2==0 and int(s[idx])>int(s[idx+1]):
                result.append(''.join(s[:idx]+s[idx:idx+2][::-1]+s[idx+2:]))
            elif int(s[idx])%2==1 and int(s[idx+1])%2==1 and int(s[idx])>int(s[idx+1]):
                result.append(''.join(s[:idx]+s[idx:idx+2][::-1]+s[idx+2:]))
            idx+=1
        return min(result) if result else ''.join(s)