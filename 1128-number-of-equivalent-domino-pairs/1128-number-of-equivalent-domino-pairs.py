class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt=defaultdict(int)
        for i,j in dominoes:
            if i>j:
                i,j=j,i
            cnt[(i,j)]+=1
        result=0
        for i in cnt:
            n=cnt[i]
            result+=(n*(n-1))//2
        return result