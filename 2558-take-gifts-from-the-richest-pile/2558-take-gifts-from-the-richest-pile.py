class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap=[]
        total_gift=0
        for i in gifts:
            heapq.heappush(max_heap,(-i,i))
            total_gift+=i

        while k>0:
            num=heapq.heappop(max_heap)[1]
            fixed_num=int(math.sqrt(num))

            total_gift-=(num-fixed_num)
            heapq.heappush(max_heap,(-fixed_num,fixed_num))

            k-=1
        
        return total_gift