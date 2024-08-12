class Solution:
    def beautySum(self, s: str) -> int:
        result=0
        n=len(s)

        for i in range(n-1):
            for j in range(i+1,n+1):
                counter=Counter(s[i:j])
                result+=(max(counter.values())-min(counter.values()))

        return result