class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        result=0
        for i in range(n):
            temp=0
            if nums[i]%2==0 and nums[i]<=threshold:
                temp=1
                for j in range(i+1,n):
                    if nums[j]%2==nums[j-1]%2 or nums[j]>threshold:
                        break
                    temp+=1
            result=max(result,temp)
        return result