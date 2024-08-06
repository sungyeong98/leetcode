class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            stack=[]
            for i in s:
                if not stack:
                    stack.append(i)
                else:
                    if stack[-1].islower():
                        if i.isupper() and stack[-1]==i.lower():
                            stack.pop()
                        else:
                            stack.append(i)
                    else:
                        if i.islower() and stack[-1]==i.upper():
                            stack.pop()
                        else:
                            stack.append(i)
            if ''.join(stack)==s:
                return s
            s=''.join(stack)