import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap=[]
        maxValue=float('-inf')

        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i][0], i, 0))
            maxValue = max(maxValue, nums[i][0])
        
        start,end=0,float('inf')
        while minHeap:
            minValue, r, c = heapq.heappop(minHeap)

            if maxValue-minValue<end-start:
                start,end=minValue,maxValue

            if c+1<len(nums[r]):
                nextValue = nums[r][c+1]
                heapq.heappush(minHeap, (nextValue, r, c+1))
                maxValue = max(maxValue, nextValue)
            else:
                break
        return [start,end]