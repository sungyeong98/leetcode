class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph=defaultdict(list)
        for (x,y),p in zip(edges,succProb):
            graph[x].append((y,p))
            graph[y].append((x,p))

        result=0
        visited=set()
        visited.add(start)

        def backtrack(cur_node,cur_prob,visited):
            nonlocal result
            if cur_node==end:
                result=max(result,cur_prob)
                return
            
            for next_node, next_prob in graph[cur_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    backtrack(next_node,cur_prob*next_prob if cur_prob!=0 else next_prob, visited)
                    visited.remove(next_node)
        backtrack(start,0,visited)
        return result