class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=list(set(nums))
        n.sort()
        if n[0]==0:
            return len(n)-1
        return len(n)