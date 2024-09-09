class Solution:
    def stringHash(self, s: str, k: int) -> str:
        d={chr(i):i-ord('a') for i in range(ord('a'),ord('z')+1)}
        rev_d={i-ord('a'):chr(i) for i in range(ord('a'),ord('z')+1)}

        n=len(s)
        result=''
        for i in range(0,n,k):
            temp=0
            for j in range(i,i+k):
                temp+=d[s[j]]
            result+=rev_d[temp%26]
        return result