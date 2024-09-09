class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        result=0
        def count():
            nonlocal result
            prev_row=grid[0]
            for row in grid[1:]:
                cur_row=row[::]
                for j in range(1, len(grid[0])-1):
                    if cur_row[j]==0:
                        continue
                    cur_row[j]=min(prev_row[j-1:j+2])
                    result+=cur_row[j]
                    cur_row[j]+=1
                prev_row=cur_row
            return
        count()
        grid=grid[::-1]
        count()
        return result