class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s=s+'2'
        one,zero=0,0
        stack=[]
        for i in s:
            if not stack or stack[-1]==i:
                stack.append(i)
            else:
                if stack[-1]=='1':
                    one=max(one,len(stack))
                else:
                    zero=max(zero,len(stack))
                stack=[i]
        return True if one>zero else False