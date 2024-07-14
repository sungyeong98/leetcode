from collections import deque
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        element={}
        f=deque(list(formula))
        level=0
        stack=[]
        while f:
            char=f.popleft()
            cnt=''
            if char.isupper():
                while f and f[0].islower():
                    char+=f.popleft()
            
                while f and f[0].isdigit():
                    cnt+=f.popleft()
                if not cnt:
                    cnt=1
                if char not in element:
                    element[char]={level:int(cnt)}
                else:
                    if level not in element[char]:
                        element[char][level]=int(cnt)
                    else:
                        element[char][level]+=int(cnt)
            elif char=='(':
                level+=1
                stack.append(level)
            elif char==')':
                while f and f[0].isdigit():
                    cnt+=f.popleft()
                if not cnt:
                    cnt=1

                cur_level=stack.pop()
                for ele in element:
                    if cur_level in element[ele]:
                        element[ele][cur_level]*=int(cnt)
                        if cur_level-1 not in element[ele]:
                            element[ele][cur_level-1]=0
                        element[ele][cur_level-1]+=element[ele][cur_level]
                        del element[ele][cur_level]
                                
                level-=1

        result={}
        for ele in element:
            result[ele]=element[ele][min(element[ele])]
        
        result=sorted(result.items(), key=lambda x:(x[0],x[1]))

        answer=''
        for e,n in result:
            answer+=e
            if n>1:
                answer+=str(n)
        return answer