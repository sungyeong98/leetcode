class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        nodes={i:graph[i] for i in range(len(graph))}
        start, end = 0, len(graph)-1
        
        def dfs(start, end, path=[]):
            path=path+[start]

            if start==end:
                return [path]
            
            temp=[]
            for node in nodes[start]:
                if node not in path:
                    new_paths=dfs(node,end,path)

                    for p in new_paths:
                        temp.append(p)
            
            return temp

        return dfs(start,end)