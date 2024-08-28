class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack)<2:
                stack.append(i)
            else:
                if stack[-1]!=i or stack[-2]!=i:
                    stack.append(i)
        return ''.join(stack)