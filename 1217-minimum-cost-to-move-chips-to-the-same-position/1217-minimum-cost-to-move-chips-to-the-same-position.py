class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        p=dict(sorted(Counter(position).items(),key=lambda x:(-x[1],x[0])))

        num=list(set(position))
        result=[]
        for t in p:
            temp=0
            for i in num:
                if i==t:
                    pass
                if abs(t-i)%2==0:
                    pass
                else:
                    temp+=p[i]
            result.append(temp)
        return min(result)