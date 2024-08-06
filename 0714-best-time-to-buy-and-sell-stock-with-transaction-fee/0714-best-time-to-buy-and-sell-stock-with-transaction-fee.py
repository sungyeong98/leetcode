class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        result=0
        def backtrack(idx,val,flag):
            nonlocal result
            if idx==n-1:
                if val>0:
                    result=max(result,val)
                return
            
            if flag:
                for i in range(idx+1,n):
                    cnt=(prices[i]-prices[idx]-fee)
                    if cnt>0:
                        backtrack(i,val+cnt,False)
            else:
                for i in range(idx,n):
                    backtrack(i,val,True)
        backtrack(0,0,False)
        return result