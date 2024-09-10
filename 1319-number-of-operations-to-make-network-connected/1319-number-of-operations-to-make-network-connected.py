class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent=list(range(n))
        cnt,red=n,0

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            nonlocal cnt,red
            rootx=find(x)
            rooty=find(y)
            if rootx!=rooty:
                parent[rootx]=rooty
                cnt-=1
            else:
                red+=1
        
        for x,y in connections:
            union(x,y)
        if red>=cnt-1:
            return cnt-1
        return -1