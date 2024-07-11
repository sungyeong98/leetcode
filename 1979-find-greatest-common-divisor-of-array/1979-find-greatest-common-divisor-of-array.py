class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num,max_num=min(nums),max(nums)
        result=[i for i in range(1,min_num+1) if min_num%i==0 and max_num%i==0]
        return max(result)