class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        info={}
        for k,v in knowledge:
            info[k]=v
        
        result=[]
        stack=[]
        for i in s:
            if i=='(' and stack:
                result.append(''.join(stack))
                stack.clear()
            elif i==')':
                target_key=''.join(stack)
                if target_key in info:
                    result.append(info[target_key])
                    stack.clear()
                else:
                    result.append('?')
                    stack.clear()
            elif i!='(' and i!=')':
                stack.append(i)
        if stack:
            result.append(''.join(stack))
        return ''.join(result)