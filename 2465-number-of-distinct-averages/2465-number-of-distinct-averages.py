class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        score=set()
        while nums:
            left=nums.pop(0)
            right=nums.pop(-1)
            score.add((left+right)/2)
        return len(score)