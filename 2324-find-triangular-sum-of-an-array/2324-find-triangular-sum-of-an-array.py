class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        #solution1
        '''
        result=[nums]
        while len(result[-1])>1:
            temp=[]
            for i in range(len(result[-1])-1):
                temp.append((result[-1][i]+result[-1][i+1])%10)
            result.append(temp)
        return result[-1][0]
        '''
        n = len(nums)
        choose = 1
        total = 0
        for r in range(n):
            total += nums[r] * choose
            choose = choose * ((n-1)-r) // (r+1)
            
        return total % 10