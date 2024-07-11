from collections import defaultdict, Counter
from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #solution1
        '''
        if len(nums)==1:
            return 1
        
        n=len(nums)
        temp=defaultdict(int)
        for i in range(1,n+1):
            for j in combinations(nums,i):
                n=reduce(lambda x,y:x|y,list(j))
                temp[n]+=1
        
        return temp[max(temp.keys())]
        '''

        dp=Counter([0])
        for i in nums:
            for k,v in list(dp.items()):
                dp[i|k]+=v
        return dp[max(dp)]