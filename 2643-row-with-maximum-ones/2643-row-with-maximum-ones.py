class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        temp={i:sum(mat[i]) for i in range(len(mat))}
        return sorted(temp.items(),key=lambda x:-x[1])[0]