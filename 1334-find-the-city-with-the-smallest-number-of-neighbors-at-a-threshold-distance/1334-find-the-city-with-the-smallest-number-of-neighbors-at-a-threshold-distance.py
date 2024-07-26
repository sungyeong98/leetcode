class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph={i:[] for i in range(n)}
        for s,e,w in edges:
            if w<=distanceThreshold:
                graph[s].append((e,w))
                graph[e].append((s,w))  

        def find(start):
            min_heap=[(0,start)]
            dist={i:float('inf') for i in range(n)}
            dist[start]=0

            while min_heap:
                d, u = heappop(min_heap)
                if d>dist[u]:
                    continue
                for v,w in graph[u]:
                    if dist[u]+w<dist[v]:
                        dist[v]=dist[u]+w
                        heappush(min_heap, (dist[v],v))
            return dist

        min_num, result=n,-1
        for start in range(n):
            dis=find(start)
            cnt=sum([1 for d in dis.values() if d<=distanceThreshold])
            if cnt<min_num or (cnt==min_num and start>result):
                min_num=cnt
                result=start
        return result