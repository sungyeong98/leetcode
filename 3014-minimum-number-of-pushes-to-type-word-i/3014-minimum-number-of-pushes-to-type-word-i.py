class Solution:
    def minimumPushes(self, word: str) -> int:
        counter=Counter(word)
        cnt=sorted(counter.values(),reverse=True)
        n=len(cnt)
        result=0
        level=1
        for i in range(0,n,8):
            result+=sum(cnt[i:i+8])*level
            level+=1
        return result