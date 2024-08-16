class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0]*n
        for idx,val in enumerate(temperatures):
            if not stack:
                stack.append((idx,val))
            else:
                while stack and stack[-1][1]<val:
                    prev_idx,_=stack.pop()
                    result[prev_idx]=idx-prev_idx
                stack.append((idx,val))
        return result