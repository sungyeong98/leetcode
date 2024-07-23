class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        result=original
        while result in nums:
            result*=2
        return result