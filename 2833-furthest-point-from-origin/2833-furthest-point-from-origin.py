class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter=Counter(moves)
        result=0
        if counter['L']>counter['R']:
            result+=(counter['L']-counter['R'])
            result+=counter['_']
        elif counter['R']>counter['L']:
            result+=(counter['R']-counter['L'])
            result+=counter['_']
        else:
            result+=counter['_']
        return result