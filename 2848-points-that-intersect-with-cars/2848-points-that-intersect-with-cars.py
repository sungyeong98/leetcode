class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        result=[0]
        for s,e in nums:
            if len(result)<e:
                result.extend([0]*(e-len(result)))
            for i in range(s,e+1):
                result[i-1]=1
        return sum(result)