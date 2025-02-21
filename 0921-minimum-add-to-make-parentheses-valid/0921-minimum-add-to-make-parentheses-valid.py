class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in list(s):
            if i=='(':
                stack.append(i)
            else:
                if not stack or stack[-1]!='(':
                    stack.append(i)
                else:
                    stack.pop()
        return len(stack)