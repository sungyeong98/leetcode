class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=Counter(nums)
        for i in n:
            if n[i]%2!=0:
                return False
        return True