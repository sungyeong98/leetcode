class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even=[i for i in nums if i%2==0]
        if len(even)>=2:    return True
        return False