class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph={i:[] for i in range(n)}
        for s,e,w in edges:
            graph[s].append((e,w))
            graph[e].append((s,w))

        result={}
        for node in graph:
            temp=set()
            if result and len(graph[node])>min(result.values()):
                continue

            for s_node,s_wei in graph[node]:
                if s_wei>distanceThreshold:
                    continue
                temp.add(s_node)

                stack=[(s_node,s_wei)]

                while stack:
                    cur_node,cur_wei=stack.pop()

                    for next_node, next_wei in graph[cur_node]:
                        if next_node!=node and next_node not in temp and cur_wei+next_wei<=distanceThreshold:
                            stack.append((next_node,next_wei+cur_wei))
                            temp.add(next_node)

            result[node]=len(temp)
        result=sorted(result.items(), key=lambda x:(x[1],-x[0]))
        return result[0][0]