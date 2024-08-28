class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i in mat:
            n=len(i)
            for j in range(n):
                if i[j]!=i[(j+k)%n]:
                    return False
        return True