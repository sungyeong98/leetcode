class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s=s+' '
        result=[]
        stack=[]
        for idx,val in enumerate(s):
            if not stack or stack[-1][0]==val:
                stack.append((val,idx))
            else:
                if len(stack)>=3:
                    result.append([stack[0][1],stack[-1][1]])
                stack=[(val,idx)]
        return result