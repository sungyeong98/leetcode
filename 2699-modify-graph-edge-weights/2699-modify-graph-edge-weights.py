class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph=[[] for _ in range(n)]
        for s,e,w in edges:
            graph[s].append([e,w])
            graph[e].append([s,w])
        
        def find(source, graph, skip):
            pq=[[0,source]]
            dis=defaultdict(lambda:inf)
            dis[source]=0
            parent={}
            while pq:
                d,node=heappop(pq)
                if d>dis[node]:
                    continue
                for nei,w in graph[node]:
                    if w==-1:
                        if skip:
                            continue
                        w=1
                    
                    d2=d+w
                    if d2<dis[nei]:
                        dis[nei]=d2
                        parent[nei]=node
                        heappush(pq,[d2,nei])
            return dis, parent
        disR,parentR=find(destination, graph, skip=True)
        if disR.get(source,inf)<target:
            return []
        dis,parent=find(source,graph, skip=False)
        if dis[destination]>target:
            return []

        path=[destination]
        while path[-1]!=source:
            path.append(parent[path[-1]])
        path=path[::-1]

        edges={(min(u,v),max(u,v)): w for u,v,w in edges}

        walked=0
        for u,v in zip(path,path[1:]):
            e=(min(u,v),max(u,v))
            if edges[e]==-1:
                edges[e]=max(target-disR.get(v,inf)-walked,1)
                if edges[e]>1:
                    break
            walked+=edges[e]
        for e,w in edges.items():
            if w==-1:
                edges[e]=2*(10**9)
        return [[u,v,w] for (u,v),w in edges.items()]