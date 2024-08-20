class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if len(s1)>len(s2):
            s1,s2=s2,s1
        
        prev=[0]*(len(s2)+1)
        for j in range(1,len(s2)+1):
            prev[j]=prev[j-1]+ord(s2[j-1])
        
        for i in range(1,len(s1)+1):
            cur=[prev[0]+ord(s1[i-1])]
            for j in range(1,len(s2)+1):
                if s1[i-1]==s2[j-1]:
                    cur.append(prev[j-1])
                else:
                    cur.append(min(prev[j]+ord(s1[i-1]), cur[j-1]+ord(s2[j-1])))
            prev=cur
        return prev[-1]