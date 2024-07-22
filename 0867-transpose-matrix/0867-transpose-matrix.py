class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in list(zip(*matrix)):
            result.append(list(i))
        return result