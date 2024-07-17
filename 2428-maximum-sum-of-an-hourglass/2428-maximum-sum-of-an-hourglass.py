class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        pos=[(0,0),(0,1),(0,2),(1,1),(2,0),(2,1),(2,2)]
        m,n=len(grid),len(grid[0])

        result=0
        for x in range(m-2):
            for y in range(n-2):
                temp=0
                for dx,dy in pos:
                    temp+=grid[x+dx][y+dy]
                
                if result<temp:
                    result=temp
        return result