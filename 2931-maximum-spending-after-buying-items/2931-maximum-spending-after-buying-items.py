class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        temp=[j for i in values for j in i]
        temp.sort()
        result=0
        for idx,val in enumerate(temp):
            result+=val*(idx+1)
        return result