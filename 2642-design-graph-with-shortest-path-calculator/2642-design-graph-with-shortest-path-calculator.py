class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.graph=defaultdict(list)
        for s,e,w in edges:
            self.graph[s].append((e,w))

    def addEdge(self, edge: List[int]) -> None:
        s,e,w=edge
        self.graph[s].append((e,w))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap=[(0,node1)]
        dis={i:int(1e9) for i in range(self.n)}
        dis[node1]=0

        while heap:
            cur_dis, cur_node=heapq.heappop(heap)

            if cur_node==node2:
                return cur_dis
            
            if cur_dis>dis[cur_node]:
                continue
            
            for next_node, next_dis in self.graph[cur_node]:
                total_dis=cur_dis+next_dis
                if total_dis<dis[next_node]:
                    dis[next_node]=total_dis
                    heapq.heappush(heap,(total_dis,next_node))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)