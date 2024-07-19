class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp={}
        for i in range(len(mat)):
            temp[i]=sum(mat[i])
        return list(sorted(temp.keys(), key=lambda x:temp[x]))[:k]