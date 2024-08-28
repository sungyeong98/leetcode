class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start,end=rounds[0],rounds[-1]
        if end>=start:
            return [i for i in range(start,end+1)]
        else:
            result=[]
            for i in range(n):
                if i+1<=end or i+1>=start:
                    result.append(i+1)
            return sorted(result)