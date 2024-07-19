class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n=Counter(nums)
        num=sorted(list(set(nums)))
        result=0

        while num:
            nn=num.pop()
            result+=n[nn]*len(num)

        return result