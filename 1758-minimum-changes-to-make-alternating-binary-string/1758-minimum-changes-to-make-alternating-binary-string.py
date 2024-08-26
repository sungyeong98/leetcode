class Solution:
    def minOperations(self, s: str) -> int:
        left_s,right_s=list(s),list(s)
        n=len(s)
        left,right=0,0

        for i in range(n-1):
            if i==0:
                right_s[i]='0' if right_s[i]=='1' else '1'
                right+=1
            if left_s[i+1]==left_s[i]:
                left+=1
                left_s[i+1]='0' if left_s[i+1]=='1' else '1'
            if right_s[i+1]==right_s[i]:
                right+=1
                right_s[i+1]='0' if right_s[i+1]=='1' else '1'
        
        return min(left, right)