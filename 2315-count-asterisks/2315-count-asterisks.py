class Solution:
    def countAsterisks(self, s: str) -> int:
        result=0
        flag=False
        for i in s:
            if i=='|':
                if flag:
                    flag=False
                else:
                    flag=True
            elif i=='*' and not flag:
                result+=1
        return result