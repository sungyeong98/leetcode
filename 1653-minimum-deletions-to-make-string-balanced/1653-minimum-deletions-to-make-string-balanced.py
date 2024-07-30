class Solution:
    def minimumDeletions(self, s: str) -> int:
        left,right=0,s.count('a')
        result=left+right

        for i in range(len(s)):
            if s[i]=='a':
                right-=1
            else:
                left+=1
            result=min(result,left+right)
        return result