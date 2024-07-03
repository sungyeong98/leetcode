import heapq
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:    return 0

        heapq.heapify(nums)
        s=heapq.nsmallest(4,nums)
        l=heapq.nlargest(4,nums)
        l.reverse()

        return min(x-y for x,y in zip(l,s))