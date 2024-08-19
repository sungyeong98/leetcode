class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap,(-i,i))
        while len(heap)>1:
            x=heapq.heappop(heap)[1]
            y=heapq.heappop(heap)[1]
            if x==y:
                continue
            else:
                heapq.heappush(heap, (-(x-y),x-y))
        return heapq.heappop(heap)[1] if heap else 0