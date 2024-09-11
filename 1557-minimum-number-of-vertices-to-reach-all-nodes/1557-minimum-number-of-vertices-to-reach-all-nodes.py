class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(g,c,visited,result):
            visited[c]=True
            for adj in g[c]:
                if not visited[adj]:
                    dfs(g,adj,visited,result)
                elif adj in result:
                    result.remove(adj)
        g=defaultdict(list)
        for e in edges:
            u,v=e
            g[u].append(v)
        
        result=set()
        visited=[False]*n
        for i in range(n):
            if not visited[i]:
                dfs(g,i,visited,result)
                result.add(i)
        return list(result)