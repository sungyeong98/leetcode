class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        count=set()
        result=0

        for i in rolls:
            count.add(i)
            if len(count)==k:
                result+=1
                count.clear()
        return result+1