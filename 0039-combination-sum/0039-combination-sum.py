class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        c=sorted(candidates)
        result=[]
        visited_set=set()

        def dfs(c,visited,start):
            total=sum(visited)
            if total==target:
                temp=tuple(sorted(visited))
                if temp not in visited_set:
                    result.append(visited[:])
                    visited_set.add(temp)
                return
            elif total>target:
                return
            
            for i in range(start,len(c)):
                visited.append(c[i])
                dfs(c,visited,i)
                visited.pop()
        dfs(c,[],0)
        return result