class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result=0
        n=len(nums)
        for i in range(n):
            prev=nums[i]
            cnt=1
            for j in range(i+1,n):
                if nums[j]>prev:
                    prev=nums[j]
                    cnt+=1
                else:
                    break
            result=max(result,cnt)
        return result