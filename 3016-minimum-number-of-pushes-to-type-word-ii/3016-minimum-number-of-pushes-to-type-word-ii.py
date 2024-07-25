class Solution:
    def minimumPushes(self, word: str) -> int:
        num=Counter(word)
        num=dict(sorted(num.items(), key=lambda x:-x[1]))
        n,cnt=7,0
        result=0
        for s in num:
            if cnt<=n:
                result+=num[s]
            else:
                result+=2*num[s]
            cnt+=1
        return result