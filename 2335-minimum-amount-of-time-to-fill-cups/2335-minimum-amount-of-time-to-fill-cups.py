class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap=[-i for i in amount]
        heapify(heap)
        result=0

        while heap[0]!=0:
            e1=heappop(heap)
            e2=heappop(heap)
            if e1!=0:
                e1+=1
            if e2!=0:
                e2+=1
            heappush(heap, e1)
            heappush(heap, e2)

            result+=1
        return result