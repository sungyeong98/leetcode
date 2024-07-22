class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        cnt=1
        while memory1>0 or memory2>0:
            if memory1<cnt and memory2<cnt:
                break

            if memory1>memory2:
                memory1-=cnt
            elif memory2>memory1:
                memory2-=cnt
            else:
                memory1-=cnt
            cnt+=1
        return [cnt,memory1,memory2]