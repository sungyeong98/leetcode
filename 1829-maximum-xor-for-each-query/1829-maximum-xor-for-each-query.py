class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target=2**maximumBit-1
        num=0
        result=[]
        for i in nums:
            num^=i
            result.append(num^target)
        return result[::-1]