class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        temp=sorted([nums[i:j] for i in range(n) for j in range(i+1,n+1)],key=len)
        for sub in temp:
            num=0
            for i in sub:
                num|=i
            if num>=k:
                return len(sub)
        return -1