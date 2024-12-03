class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char!=')' and char!=',':
                stack.append(char)
            elif char == ')':
                exp = []

                while stack and stack[-1]!='(':
                    token = stack.pop()
                    exp.append(True if token=='t' else False)
                
                stack.pop()

                if stack:
                    token = stack.pop()
                    val = exp[0]
                
                    if token == '&':
                        for i in exp:
                            val &= i
                    elif token == '|':
                        for i in exp:
                            val |= i
                    else:
                        val = not val
                
                stack.append('t' if val else 'f')
        return stack[-1]=='t'