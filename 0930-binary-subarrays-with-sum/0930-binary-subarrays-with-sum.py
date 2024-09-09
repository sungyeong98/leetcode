class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count={0:1}
        cur_sum, total = 0, 0
        for num in nums:
            cur_sum+=num
            if cur_sum-goal in count:
                total+=count[cur_sum-goal]
            count[cur_sum]=count.get(cur_sum,0)+1
        return total