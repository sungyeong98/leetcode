class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        nums=list(range(1,n+1))

        def helper(nums):
            if len(nums)<3:
                return nums
            even=nums[::2]
            odd=nums[1::2]
            return helper(even)+helper(odd)
        return helper(nums)