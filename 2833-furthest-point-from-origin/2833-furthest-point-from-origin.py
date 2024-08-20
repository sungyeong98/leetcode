class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n=len(moves)
        result=0
        def move_point(idx, pos):
            nonlocal result
            if idx==n:
                result=max(result,abs(pos))
                return
            
            if moves[idx]=='L':
                move_point(idx+1, pos-1)
            elif moves[idx]=='R':
                move_point(idx+1, pos+1)
            else:
                move_point(idx+1, pos-1)
                move_point(idx+1, pos+1)
            return
        move_point(0,0)
        return result