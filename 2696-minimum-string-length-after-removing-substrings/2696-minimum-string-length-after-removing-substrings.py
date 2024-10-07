class Solution:
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            stack=[]
            for i in s:
                if i=='B' and stack and stack[-1]=='A':
                    stack.pop()
                elif i=='D' and stack and stack[-1]=='C':
                    stack.pop()
                else:
                    stack.append(i)
            s=''.join(stack)
        return len(s)