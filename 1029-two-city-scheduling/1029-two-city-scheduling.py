class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        result=int(1e9)

        def backtrack(a,b,a_cnt,b_cnt,cost):
            nonlocal result
            if not cost:
                result=min(result,a+b)
                return
            
            if a_cnt<n//2 and b_cnt<n//2:
                prices=cost[0]
                backtrack(a+prices[0],b,a_cnt+1,b_cnt,cost[1:])
                backtrack(a,b+prices[1],a_cnt,b_cnt+1,cost[1:])
            
            elif a_cnt<n//2:
                prices=cost[0]
                backtrack(a+prices[0],b,a_cnt+1,b_cnt,cost[1:])
            
            else:
                prices=cost[0]
                backtrack(a,b+prices[1],a_cnt,b_cnt+1,cost[1:])
        
        backtrack(0,0,0,0,costs)
        return result