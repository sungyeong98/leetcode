class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result=[nums]
        while len(result[-1])>1:
            temp=[]
            for i in range(len(result[-1])-1):
                temp.append((result[-1][i]+result[-1][i+1])%10)
            result.append(temp)
        return result[-1][0]