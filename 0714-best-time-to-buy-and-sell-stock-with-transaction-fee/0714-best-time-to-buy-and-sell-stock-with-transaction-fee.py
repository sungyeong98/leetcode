class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)

        no_stock=[0]*n
        has_stock=[0]*n

        has_stock[0]=-prices[0]

        for i in range(1,n):
            no_stock[i]=max(no_stock[i-1], has_stock[i-1]+prices[i]-fee)
            has_stock[i]=max(has_stock[i-1], no_stock[i-1]-prices[i])
        
        return no_stock[-1]