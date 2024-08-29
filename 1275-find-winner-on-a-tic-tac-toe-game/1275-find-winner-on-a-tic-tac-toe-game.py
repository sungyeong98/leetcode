class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a=sorted([val for idx,val in enumerate(moves) if idx%2==0])
        b=sorted([val for idx,val in enumerate(moves) if idx%2==1])
        
        win_case=[[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]],
                [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
                [[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]]]
        
        for i in combinations(a,3):
            if list(i) in win_case:
                return 'A'
        for i in combinations(b,3):
            if list(i) in win_case:
                return 'B'
        if len(moves)==9:
            return 'Draw'
        return 'Pending'