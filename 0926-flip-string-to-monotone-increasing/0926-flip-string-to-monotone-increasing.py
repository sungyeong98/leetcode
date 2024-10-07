class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt, result = 0, 0
        for d in s:
            if d=='1':
                cnt+=1
            elif cnt:
                cnt-=1
                result+=1
        return result