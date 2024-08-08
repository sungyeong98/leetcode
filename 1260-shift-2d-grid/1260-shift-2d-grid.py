class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        temp=deque([j for i in grid for j in i])
        result=[[0]*n for _ in range(m)]
        cnt=0
        while cnt<k:
            temp.appendleft(temp.pop())
            cnt+=1

        for i in range(m):
            for j in range(n):
                result[i][j]=temp.popleft()
        return result