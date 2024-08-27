class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        result=0
        cnt=0
        while cost:
            if cnt<2:
                result+=cost.pop()
            else:
                cost.pop()
            cnt=(cnt+1)%3
        return result