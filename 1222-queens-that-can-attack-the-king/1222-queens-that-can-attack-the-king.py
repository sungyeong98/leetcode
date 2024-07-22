class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result=[]
        temp=set(tuple(q) for q in queens)

        dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        for dx,dy in dir:
            x,y=king
            while 0<=x+dx<8 and 0<=y+dy<8:
                x+=dx
                y+=dy
                if (x,y) in temp:
                    result.append([x,y])
                    break
        return result