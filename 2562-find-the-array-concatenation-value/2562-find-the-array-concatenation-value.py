class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result=0
        while nums:
            temp=int(str(nums.pop(0))+str(nums.pop())) if len(nums)>1 else nums.pop()
            result+=temp
        return result