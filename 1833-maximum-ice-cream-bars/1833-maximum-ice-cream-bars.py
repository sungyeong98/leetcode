class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        coin=deque(sorted(costs))
        result,total_cost=0,0
        while coin and total_cost<=coins:
            cost=coin.popleft()
            if total_cost+cost<=coins:
                result+=1
                total_cost+=cost
        return result