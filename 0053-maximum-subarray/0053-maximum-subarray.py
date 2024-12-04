class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, float('-inf')
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            
            if cur_sum < 0:
                cur_sum = 0
        return max_sum