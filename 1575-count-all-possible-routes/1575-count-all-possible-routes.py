class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod=10**9+7
        @lru_cache(None)
        def helper(n,x):
            if x<0:
                return 0
            result=0
            if n==finish:
                result+=1
            for i in range(len(locations)):
                if i!=n:
                    result+=helper(i, x-abs(locations[n]-locations[i]))
            return result
        
        return helper(start,fuel)%mod