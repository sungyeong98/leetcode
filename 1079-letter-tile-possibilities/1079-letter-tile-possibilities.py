from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n=len(tiles)
        result=set()
        for i in range(1,n+1):
            for j in permutations(list(tiles),i):
                result.add(''.join(j))
        return len(result)