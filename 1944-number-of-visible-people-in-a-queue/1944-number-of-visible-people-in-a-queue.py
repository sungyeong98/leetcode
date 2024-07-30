class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n=len(heights)
        result=[0]*n
        stack=[]

        for i in range(n):
            while stack and heights[i]>heights[stack[-1]]:
                result[stack.pop()]+=1
            if stack:
                result[stack[-1]]+=1
            stack.append(i)
        return result