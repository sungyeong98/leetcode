class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result=0
        col=list(zip(*mat))
        for idx,sub in enumerate(mat):
            if sum(sub)==1 and sum(col[sub.index(1)])==1:
                result+=1
        return result