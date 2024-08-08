class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dir=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),(0,0)]
        m,n=len(img),len(img[0])
        val_dict=defaultdict(list)
        result=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                temp=[]
                for dx,dy in dir:
                    if 0<=i+dx<m and 0<=j+dy<n:
                        temp.append(img[i+dx][j+dy])
                temp.sort()
                val_dict[tuple(temp)].append((i,j))

        for val in val_dict:
            temp=list(val)
            total_val=int(sum(temp)/len(temp))
            
            for x,y in val_dict[val]:
                result[x][y]=total_val
        
        return result