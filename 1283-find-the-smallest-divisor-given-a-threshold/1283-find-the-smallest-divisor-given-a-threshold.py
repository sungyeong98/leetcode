class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)+1

        def check(m):
            s=0
            for x in nums:
                s+=ceil(x/m)
            return s<=threshold
        
        while left<right:
            mid=(left+right)//2

            if check(mid):
                result=mid
                right=mid
            else:
                left=mid+1
        return result