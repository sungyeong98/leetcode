class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        result=0
        visited=set()
        for i in range(n):
            if i not in visited:
                if i not in graph:
                    visited.add(i)
                    result+=1
                    continue

                temp, stack = set(), [i]
                temp.add(i)
                while stack:
                    node=stack.pop()
                    for next_node in graph[node]:
                        if next_node not in temp:
                            temp.add(next_node)
                            stack.append(next_node)
                if all(len(graph[i])==len(temp)-1 for i in temp):
                    result+=1
                
                visited.update(temp)
        return result