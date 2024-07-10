class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if i!='../' and i!='./':
                stack.append(i)
            elif i=='../':
                if len(stack)>0:
                    stack.pop(-1)
        return len(stack)