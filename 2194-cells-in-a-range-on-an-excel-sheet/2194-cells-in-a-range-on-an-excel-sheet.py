class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s=s.split(':')
        start_n,end_n=int(s[0][1]),int(s[1][1])
        start_s,end_s=ord(s[0][0]),ord(s[1][0])

        result=[]
        for i in range(start_s,end_s+1):
            for j in range(start_n,end_n+1):
                result.append(chr(i)+str(j))
        return result