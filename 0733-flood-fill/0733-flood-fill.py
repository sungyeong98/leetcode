class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n=len(image),len(image[0])
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=set()
        target_color=image[sr][sc]
        visited.add((sr,sc))
        stack=[(sr,sc)]
        image[sr][sc]=color
        while stack:
            r,c=stack.pop()

            for dr,dc in dir:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and image[nr][nc]==target_color:
                    image[nr][nc]=color
                    visited.add((nr,nc))
                    stack.append((nr,nc))
        return image