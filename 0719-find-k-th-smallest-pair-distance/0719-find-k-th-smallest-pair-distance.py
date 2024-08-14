class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right=0,nums[-1]-nums[0]

        def count(nums, dis):
            cnt,left=0,0
            for right in range(1,len(nums)):
                while nums[right]-nums[left]>dis:
                    left+=1
                cnt+=right-left
            return cnt

        while left<right:
            mid=(left+right)//2
            if count(nums,mid)<k:
                left=mid+1
            else:
                right=mid
        
        return left