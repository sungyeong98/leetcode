class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid=grid
        self.n=len(grid)
        self.position={grid[i][j]:(i,j) for i in range(self.n) for j in range(self.n)}

    def adjacentSum(self, value: int) -> int:
        i,j=self.position[value]
        adj=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        sum=0
        for x,y in adj:
            if 0<=x<self.n and 0<=y<self.n:
                sum+=self.grid[x][y]
        return sum

    def diagonalSum(self, value: int) -> int:
        if value not in self.position:
            return 0
        i,j=self.position[value]
        dia=[(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
        sum=0
        for x,y in dia:
            if 0<=x<self.n and 0<=y<self.n:
                sum+=self.grid[x][y]
        return sum


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)