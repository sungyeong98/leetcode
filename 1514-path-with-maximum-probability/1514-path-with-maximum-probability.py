class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph=defaultdict(list)
        for idx,(x,y) in enumerate(edges):
            graph[x].append((y,idx))
            graph[y].append((x,idx))
        q=deque([start])
        prob=[0.0]*n
        prob[start]=1.0
        while q:
            cur_node=q.popleft()
            for next_node, idx in graph[cur_node]:
                if prob[cur_node]*succProb[idx]>prob[next_node]:
                    prob[next_node]=prob[cur_node]*succProb[idx]
                    q.append(next_node)
        return prob[end]