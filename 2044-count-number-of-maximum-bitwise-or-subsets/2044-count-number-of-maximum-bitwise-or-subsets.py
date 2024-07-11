from collections import defaultdict
from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        n=len(nums)
        temp=defaultdict(int)
        for i in range(1,n+1):
            for j in combinations(nums,i):
                n=reduce(lambda x,y:x|y,list(j))
                temp[n]+=1
        
        return temp[max(temp.keys())]