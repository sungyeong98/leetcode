class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k
        min_val=nums[k]
        result=min_val

        while left>0 or right<len(nums)-1:
            if left==0 or (right<len(nums)-1 and nums[right+1]>nums[left-1]):
                right+=1
            else:
                left-=1
            min_val=min(min_val, nums[left], nums[right])
            result=max(result, min_val*(right-left+1))
        return result