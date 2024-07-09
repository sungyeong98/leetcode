from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        if len(nums)==len(list(set(nums))): return 0

        n=Counter(nums)
        temp=[i for i in n.keys() if n[i]==2]
        if len(temp)==1:   return temp[0]
        result=temp[0]
        for i in range(1,len(temp)):
            result^=temp[i]
        return result