class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        user_x,user_y=0,0
        user_distance = abs(target[0]-user_x)+abs(target[1]-user_y)
        for x,y in ghosts:
            distance = abs(target[0]-x) + abs(target[1]-y)
            if user_distance>=distance:
                return False
        return True