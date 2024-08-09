class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        graph={i:[] for i in range(n)}
        
        for i in range(n):
            for j in range(n):
                if i!=j:
                    dis=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    graph[i].append((dis, j))
        
        min_cost=0
        vistied=[False]*n
        min_heap=[(0,0)]

        while min_heap:
            cost, u = heapq.heappop(min_heap)
            if vistied[u]:
                continue

            vistied[u]=True
            min_cost+=cost

            for edge_cost, v in graph[u]:
                if not vistied[v]:
                    heapq.heappush(min_heap, (edge_cost,v))

        return min_cost