class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, result = [], []
        for i in s:
            if i=='(':
                stack.append(len(result))
            elif i==')':
                idx=stack.pop()
                result[idx:]=result[idx:][::-1]
            else:
                result.append(i)
        return ''.join(result)