class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            for j in range(i):
                if j | (j+1) == i:
                    result.append(j)
                    break
                else:
                    result.append(-1)
        return result