class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n=len(adjacentPairs)

        temp=defaultdict(list)
        for i,j in adjacentPairs:
            temp[i].append(j)
            temp[j].append(i)

        for num in temp:
            visited=set()
            visited.add(num)
            
            def dfs(cur_num,visited,road):
                road.append(cur_num)
                if len(road)==n+1:
                    return road
                for next_num in temp[cur_num]:
                    if next_num not in visited:
                        visited.add(next_num)
                        result=dfs(next_num, visited, road)
                        if result:
                            return result
                        road.pop()
                        visited.remove(next_num)
                return None
            
            road=dfs(num,visited,[])

            if road:
                return road