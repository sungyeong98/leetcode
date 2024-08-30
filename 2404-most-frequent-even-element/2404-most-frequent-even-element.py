class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c=Counter([i for i in nums if i%2==0])
        return sorted(c.keys(),key=lambda x:(-c[x],x))[0] if c else -1