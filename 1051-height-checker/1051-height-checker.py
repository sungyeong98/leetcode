class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp=heights.copy()
        heights.sort()
        result=0
        for i,j in zip(temp,heights):
            if i!=j:
                result+=1
        return result