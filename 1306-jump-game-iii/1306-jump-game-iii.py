class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        visited=set()
        idx=start
        visited.add(idx)

        def backtrack(idx, temp):
            if arr[idx]==0:
                return True
            
            dis=arr[idx]

            if idx-dis not in temp and 0<=idx-dis<n:
                temp.add(idx-dis)
                if backtrack(idx-dis, temp):
                    return True
                temp.remove(idx-dis)
            
            if idx+dis not in temp and 0<=idx+dis<n:
                temp.add(idx+dis)
                if backtrack(idx+dis,temp):
                    return True
                temp.remove(idx+dis)
            
            return False
        return backtrack(idx,visited)