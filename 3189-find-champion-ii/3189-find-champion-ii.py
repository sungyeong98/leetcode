class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        temp = list(range(n))

        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
        
        for i in range(n):
            if i in graph:
                for del_num in graph[i]:
                    if del_num in temp:
                        temp.pop(temp.index(del_num))
        
        if len(temp)>1:
            return -1
        
        return temp[-1]