class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n//k <2:
            return False
        if k==1:
            return True
        
        visited = [0]*n
        start, end = 0, 1
        while end<n:
            while end<n and nums[end]>nums[end-1]:
                if end-start+1 ==k:
                    visited[start]=1
                    start+=1
                end+=1
            start=end
            end+=1
        for i in range(n-(2*k)+1):
            if visited[i] and visited[i+k]:
                return True
        return False