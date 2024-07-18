class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        coin=sorted(costs)
        if sum(coin)<=coins:
            return len(coin)
        else:
            while sum(coin)>coins:
                coin.pop()
        return len(coin)