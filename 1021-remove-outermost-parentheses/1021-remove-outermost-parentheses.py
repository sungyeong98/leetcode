class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result, cnt = [], 0
        for i in s:
            if i=='(':
                if cnt>0:
                    result.append(i)
                cnt+=1
            elif i==')':
                cnt-=1
                if cnt>0:
                    result.append(i)
        return ''.join(result)