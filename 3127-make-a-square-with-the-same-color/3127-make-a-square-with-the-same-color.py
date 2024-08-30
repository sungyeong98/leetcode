class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                temp=[grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
                c=Counter(temp)
                if max(c.values())>=3:
                    return True
        return False