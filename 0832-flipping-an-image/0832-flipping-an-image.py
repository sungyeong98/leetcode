class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in image:
            i.reverse()
            result.append([0 if _ else 1 for _ in i])
        return result