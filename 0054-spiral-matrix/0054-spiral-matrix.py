class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_idx, x, y = 0, 0, 0
        m, n = len(matrix), len(matrix[0])
        result, visited = [], set()

        while len(visited) < m * n :
            if (x, y) not in visited:
                visited.add((x, y))
                result.append(matrix[x][y])
                if len(visited)==m*n:
                    break

            while True:
                dx, dy = dir[dir_idx][0], dir[dir_idx][1]
                nx, ny = x + dx, y + dy

                if 0<=nx<m and 0<=ny<n and (nx, ny) not in visited:
                    x, y = nx, ny
                    break
                
                else:
                    dir_idx = (dir_idx + 1) % 4
            
        return result    