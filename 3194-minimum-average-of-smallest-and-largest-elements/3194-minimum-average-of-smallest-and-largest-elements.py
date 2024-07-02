class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        result=int(1e9)
        while nums:
            min_num, max_num = min(nums), max(nums)
            val=(min_num+max_num)/2
            if val<result:  result=val
            nums.remove(min_num)
            nums.remove(max_num)
        return result