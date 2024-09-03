class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n=min(len(s1),len(s2),len(s3))
        sum_len=len(s1)+len(s2)+len(s3)

        if s1[0]!=s2[0] or s1[0]!=s3[0] or s2[0]!=s3[0]:
            return -1
        
        for i in range(n):
            if s1[i]==s2[i]==s3[i]:
                sum_len-=3
            else:
                break
        return sum_len