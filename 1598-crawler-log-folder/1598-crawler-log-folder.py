class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #solution1
        '''
        stack=[]
        for i in logs:
            if i!='../' and i!='./':
                stack.append(i)
            elif i=='../':
                if len(stack)>0:
                    stack.pop(-1)
        return len(stack)
        '''
        result=0
        for i in logs:
            if i=='../':
                result-=1 if result>0 else 0
            elif i=='./':
                pass
            else:
                result+=1
        return result