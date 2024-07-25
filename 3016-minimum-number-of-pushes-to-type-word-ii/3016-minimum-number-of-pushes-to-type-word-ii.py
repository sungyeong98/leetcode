class Solution:
    def minimumPushes(self, word: str) -> int:
        num=Counter(word)
        num=dict(sorted(num.items(), key=lambda x:-x[1]))
        n,cnt,mul=8,0,1
        result=0
        for s in num:
            result+=num[s]*mul
            cnt+=1
            if cnt==n:
                mul+=1
                cnt=0
        return result