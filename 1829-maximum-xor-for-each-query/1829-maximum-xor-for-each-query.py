class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target=2**maximumBit-1
        result=[]
        while nums:
            n=reduce(lambda x,y:x^y,nums)
            result.append(n^target)
            nums.pop()
        return result