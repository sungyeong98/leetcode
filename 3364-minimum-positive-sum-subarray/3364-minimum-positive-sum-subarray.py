class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float('inf')
        for size in range(l, r+1):
            for i in range(len(nums)-size+1):
                temp = sum(nums[i:i+size])
                if temp>0:
                    result = min(result, sum(nums[i:i+size]))
        return result if result!=float('inf') else -1