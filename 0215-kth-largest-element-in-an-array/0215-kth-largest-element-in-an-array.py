class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[]
        for i in nums:
            heapq.heappush(max_heap,(-i,i))

        cnt=0
        while cnt<k-1:
            heapq.heappop(max_heap)
            cnt+=1
        return heapq.heappop(max_heap)[1]