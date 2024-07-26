class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if (i%2==0 and nums[i]%2==1 and j%2==1 and nums[j]%2==0)\
                    or (i%2==1 and nums[i]%2==0 and j%2==0 and nums[j]%2==1):
                    nums[i],nums[j]=nums[j],nums[i]
        return nums