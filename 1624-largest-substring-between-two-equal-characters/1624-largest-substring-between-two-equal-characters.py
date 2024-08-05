class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        counter=Counter(s)

        num=[i for i in counter.keys() if counter[i]>1]
        result=-1
        for n in num:
            idx=[idx for idx,val in enumerate(s) if val==n]
            result=max(idx[-1]-idx[0]-1,result)

        return result