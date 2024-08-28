class Solution:
    def maxPower(self, s: str) -> int:
        s=s+'+'
        stack=[]
        result=0
        for i in s:
            if not stack or stack[-1]==i:
                stack.append(i)
            else:
                result=max(result,len(stack))
                stack=[i]
        return result