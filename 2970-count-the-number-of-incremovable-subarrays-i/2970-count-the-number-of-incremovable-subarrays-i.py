class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        result=0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                flag=True
                prev=-1
                for k in range(n):
                    if i<=k<=j:
                        continue
                    else:
                        flag&=prev<nums[k]
                        prev=nums[k]
                result+=int(flag)
        return result