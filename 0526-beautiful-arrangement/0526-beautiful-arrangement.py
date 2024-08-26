class Solution:
    def countArrangement(self, n: int) -> int:
        result=0
        nums=[i for i in range(1,n+1)]

        def dfs(nums,i):
            nonlocal result
            if i==n+1:
                result+=1
                return
            
            for j, num in enumerate(nums):
                if not (num%i and i%num):
                    dfs(nums[:j]+nums[j+1:], i+1)
        
        dfs(nums,1)
        return result