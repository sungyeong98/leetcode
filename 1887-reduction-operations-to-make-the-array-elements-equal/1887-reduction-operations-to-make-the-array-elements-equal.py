class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n=Counter(nums)
        num=list(set(nums))
        result=0

        for i in n:
            temp=[j for j in num if j<i]
            if temp:
                result+=n[i]*len(temp)
        return result