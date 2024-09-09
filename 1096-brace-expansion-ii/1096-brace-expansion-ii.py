class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack, result, cur = [], [], []
        for i in range(len(expression)):
            v=expression[i]
            if v.isalpha():
                cur=[c+v for c in cur or ['']]
            elif v=='{':
                stack.append(result)
                stack.append(cur)
                result, cur = [], []
            elif v=='}':
                pre=stack.pop()
                preRes=stack.pop()
                cur=[p+c for c in result+cur for p in pre or ['']]
                result=preRes
            elif v==',':
                result+=cur
                cur=[]
        return sorted(set(result+cur))