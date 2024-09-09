class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph=defaultdict(list)
        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)
        result=0

        def dfs(i,prev,people=1):
            nonlocal result
            for x in graph[i]:
                if x==prev:
                    continue
                people+=dfs(x,i)
            result+=(int(ceil(people/seats)) if i else 0)
            return people
        dfs(0,0)
        return result