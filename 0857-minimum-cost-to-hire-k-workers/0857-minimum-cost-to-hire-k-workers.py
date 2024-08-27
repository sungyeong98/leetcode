class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio=sorted([(w/q,q) for w,q in zip(wage,quality)])
        heap=[]
        q_sum,max_ratio=0,0.0
        for i in range(k):
            max_ratio=max(max_ratio, ratio[i][0])
            q_sum+=ratio[i][1]
            heapq.heappush(heap, -ratio[i][1])
        result=max_ratio*q_sum

        for i in range(k,len(quality)):
            max_ratio=max(max_ratio, ratio[i][0])
            q_sum+=ratio[i][1]+heapq.heappop(heap)
            heapq.heappush(heap, -ratio[i][1])
            result=min(result, max_ratio*q_sum)
        return result