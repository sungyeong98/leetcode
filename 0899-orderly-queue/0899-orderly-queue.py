class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s=list(s)
        result=[]

        while k>0:
            target_word=min(s)
            target_idx=s.index(target_word)

            result.append(target_word)
            s=s[target_idx+1:]+s[:target_idx]
            k-=1

        result+=s
        return ''.join(result)