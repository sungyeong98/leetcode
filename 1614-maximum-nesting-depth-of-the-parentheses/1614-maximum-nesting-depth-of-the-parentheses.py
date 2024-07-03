class Solution:
    def maxDepth(self, s: str) -> int:
        result=0
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')':
                n=len(stack)
                if result<n:
                    result=n
                stack.pop(-1)
        return result