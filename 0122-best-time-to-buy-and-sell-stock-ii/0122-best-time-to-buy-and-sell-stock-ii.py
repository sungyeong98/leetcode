class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        not_stock=0
        stock=-prices[0]

        for i in range(1,n):
            #주식O -> 존버,  팔기
            stock=max(stock, not_stock-prices[i])
            #주식X ->     존버,       사기
            not_stock=max(not_stock, stock+prices[i])
        
        return not_stock