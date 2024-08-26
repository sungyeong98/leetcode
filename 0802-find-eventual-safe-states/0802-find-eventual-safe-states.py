class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        visited=[0]*n
        result=[]

        def isvalid(s,graph, visited):
            if visited[s]==1:
                return True
            if visited[s]==-1:
                return False
            
            visited[s]=-1
            for i in graph[s]:
                if not isvalid(i,graph,visited):
                    return False
            visited[s]=1
            return True

        for i in range(n):
            if isvalid(i, graph, visited):
                result.append(i)
        return result