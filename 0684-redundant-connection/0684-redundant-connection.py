class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(lambda:[])

        def dfs(u,v):
            if u==v:
                return True
            visited.add(u)
            for nei in graph[u]:
                if nei not in visited:
                    if dfs(nei,v):
                        return True
            return False
        
        for u,v in edges:
            visited=set()
            if dfs(u,v):
                return [u,v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        return None