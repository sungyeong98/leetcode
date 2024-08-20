class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        graph=defaultdict(list)
        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)

        result=0
        for i in range(n-1):
            left=set(graph[i])
            for j in range(i+1,n):
                right=set(graph[j])
                if left|right==set([i,j]):
                    result=max(result,1)
                else:
                    result=max(result,len(left|right))
        return result