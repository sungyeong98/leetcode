class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s)==1:   return 0
        if 'a' not in s or 'b' not in s:    return 0
        result=int(1e9)
        for i in range(len(s)+1):
            a_cnt=s[:i].count('b')
            b_cnt=s[i:].count('a')

            result=min(result,a_cnt+b_cnt)
        return result