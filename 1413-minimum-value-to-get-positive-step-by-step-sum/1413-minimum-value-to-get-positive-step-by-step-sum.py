class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        temp=0
        result=0
        for i in nums:
            temp+=i
            result=min(result,temp)
        return abs(result)+1 if result<=0 else 1